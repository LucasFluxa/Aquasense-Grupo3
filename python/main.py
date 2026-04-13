import serial
import threading
import time
import cv2
from flask import Flask, render_template, Response, jsonify
from datetime import datetime
import collections

app = Flask(__name__)

# ── Configuración ─────────────────────────────────────────────
SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
CAMERA_INDEX = 0

# ── Estado global ─────────────────────────────────────────────
estado = {
    "temperatura": None,
    "alerta_temp": False,
    "movimiento": False,
    "historial": collections.deque(maxlen=50)
}

TEMP_MIN = 24.0
TEMP_MAX = 28.0

# ── Lector de temperatura (con reconexión automática) ─────────
def leer_temperatura():
    while True:
        try:
            ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
            print(f"[Serial] Conectado en {SERIAL_PORT}")
            while True:
                linea = ser.readline().decode("utf-8").strip()
                if linea:
                    try:
                        temp = float(linea)
                        if temp == -127.0:          # DS18B20 desconectado
                            continue
                        estado["temperatura"] = temp
                        estado["alerta_temp"] = temp < TEMP_MIN or temp > TEMP_MAX
                        estado["historial"].append({
                            "hora": datetime.now().strftime("%H:%M:%S"),
                            "temp": temp
                        })
                    except ValueError:
                        pass
        except Exception as e:
            print(f"[Serial] Error: {e} — reintentando en 5s")
            time.sleep(5)

# ── Cámara con detección de movimiento ────────────────────────
def generar_video():
    camara = cv2.VideoCapture(CAMERA_INDEX)   # inicialización local (fix race condition)
    
    if not camara.isOpened():
        print(f"[Cámara] No se pudo abrir el índice {CAMERA_INDEX}")
        return

    frame_anterior = None                      # variable local (fix thread-safety)

    try:
        while True:
            ok, frame = camara.read()
            if not ok:
                print("[Cámara] No se pudo leer frame")
                break

            gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gris = cv2.GaussianBlur(gris, (21, 21), 0)

            if frame_anterior is None:
                frame_anterior = gris
                continue

            diff = cv2.absdiff(frame_anterior, gris)
            thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
            pixeles_movimiento = cv2.countNonZero(thresh)

            estado["movimiento"] = pixeles_movimiento > 500

            color = (0, 0, 255) if estado["movimiento"] else (0, 255, 0)
            texto = "Movimiento detectado" if estado["movimiento"] else "Sin movimiento"
            cv2.putText(frame, texto, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            frame_anterior = gris

            _, buffer = cv2.imencode(".jpg", frame)
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" +   # fix \\r\\n → \r\n
                   buffer.tobytes() + b"\r\n")
    finally:
        camara.release()   # libera la cámara si el generador termina

# ── Rutas Flask ───────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video")
def video():
    return Response(generar_video(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/datos")
def datos():
    return jsonify({
        "temperatura": estado["temperatura"],
        "alerta_temp": estado["alerta_temp"],
        "movimiento": estado["movimiento"],
        "historial": list(estado["historial"])
    })

# ── Inicio ────────────────────────────────────────────────────
if __name__ == "__main__":
    hilo_temp = threading.Thread(target=leer_temperatura, daemon=True)
    hilo_temp.start()
    app.run(host="0.0.0.0", port=5000, debug=False)