#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2  // Pin DATA del DS18B20

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  
  // Manda la temperatura al lado Linux por serial
  Serial.println(tempC);
  
  delay(2000); // Cada 2 segundos
}