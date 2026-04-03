# PROY-2026-GRUPO-3

Repositorio del grupo 3 para el proyecto del ramo *Proyecto Inicial (IWG400)* – 2026.

## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol USM      |
| ----------------- | -------------- | ------------------------ | ------------ |
| Lucas Fluxá       | @LucasFluxa    | lfluxa@usm.cl            | 202630017-k  |
| Bruno Olguín      | @Bruno-Olguin  | bolguinc@usm.cl          | 202630028-5  |
| Domingo Vargas    | @Domingo-07    | jvargascar@usm.cl        | 202630026-9  |
| Daniel Guerra     | @user          | user@usm.cl              | 2026xxxxx-x  |

---

## 📝 Descripción breve del proyecto

<<<<<<< HEAD
**AquaSense** es un sistema inteligente de monitoreo de acuarios que combina sensores físicos, visión por computadora y una interfaz web local. El sistema mide en tiempo real la temperatura, pH y turbidez del agua, y utiliza una cámara para trackear el comportamiento de los peces, detectando signos de estrés o anomalías. Todo el procesamiento ocurre directamente en el Arduino UNO Q, sin depender de servidores externos.
=======
> *Aquí va una descripción general del proyecto, incluyendo su propósito, contexto dentro del curso y motivación.*
>>>>>>> parent of d3d8190 (Update README.md)

---

## 🎯 Objetivos

- **Objetivo general:**
  - Desarrollar un sistema de monitoreo inteligente de acuarios que permita detectar condiciones adversas del agua y comportamiento anómalo de los peces en tiempo real.

- **Objetivos específicos:**
  - Medir temperatura, pH y turbidez del agua mediante sensores conectados al Arduino UNO Q.
  - Implementar tracking de movimiento de peces mediante cámara USB y visión por computadora corriendo localmente en el UNO Q.
  - Desarrollar un dashboard web hosteado en el propio Arduino UNO Q accesible desde cualquier dispositivo en la misma red.
  - Generar alertas automáticas cuando algún parámetro salga del rango ideal para las especies registradas.
  - Permitir al usuario registrar las especies de peces de su acuario y consultar su compatibilidad y temperatura ideal.

---

## 🧩 Alcance del proyecto

**Dentro del alcance:**
- Monitoreo en tiempo real de temperatura, pH y turbidez
- Tracking de movimiento de peces con detección de comportamiento anómalo
- Dashboard web local con historial de datos
- Base de datos de especies de peces con parámetros ideales y compatibilidad
- Alertas cuando los parámetros salen del rango óptimo

**Fuera del alcance:**
- Control automatizado de equipos del acuario (calefactor, filtro, etc.)

---

## 🛠️ Tecnologías y herramientas utilizadas

- **Lenguaje(s) de programación:**
  - Python (dashboard web)
  - C++ / Arduino Sketch (control en tiempo real del STM32U585)

- **Microcontroladores:**
  - Arduino UNO Q (Qualcomm Dragonwing QRB2210 + STM32U585)

- **Sensores:**
  - DS18B20 — temperatura del agua (sumergible, OneWire)
  - pH-4502C — pH del agua (analógico, con placa de acondicionamiento)
  - TSD-10 — turbidez del agua (analógico)
  - Webcam USB — tracking de movimiento de peces (V4L2 / OpenCV)

---

## 🗂️ Estructura del repositorio

> *Por definir*

---

## 🚀 Instrucciones de Instalación y Uso

> *Por definir*

---

## 📐 Diseño del Sistema

![Diagrama de Conexiones](./assets/diagrama_conexiones.png)

*El STM32U585 lee los sensores de temperatura, pH y turbidez y los envía al Qualcomm via comunicación interna. El Qualcomm corre Python con OpenCV para el tracking de la cámara y Flask para el dashboard web.*

---

## 📅 Cronograma de trabajo

[Carta Gantt](https://google.com)

---

## 📚 Bibliografía

- [Arduino UNO Q — Documentación oficial](https://docs.arduino.cc/hardware/uno-q/)


---

## 📌 Notas adicionales

> - El sensor de pH requiere calibración inicial con soluciones buffer pH 4.0 y pH 7.0, y recalibración.
> - La cámara USB se conecta al puerto USB-C del UNO Q mediante adaptador USB-A a USB-C.
> - Para la demo final se presentará un acuario real con peces.
