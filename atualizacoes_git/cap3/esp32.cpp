# ESP32 Code (C++)
#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "SEU_SSID";
const char* password = "SUA_SENHA";
const char* serverName = "http://seu-servidor/api/sensores";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  dht.begin();
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int soilMoisture = analogRead(34);
  float rainfall = analogRead(35) / 1023.0;

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String json = "{\"soil_moisture\":" + String(soilMoisture) + ",\"rainfall\":" + String(rainfall) + ",\"temperature\":" + String(temperature) + ",\"humidity\":" + String(humidity) + "}";

    int httpResponseCode = http.POST(json);
    Serial.println(httpResponseCode);
    http.end();
  }
  delay(5000);
}
