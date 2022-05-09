#include <ArduinoJson.h>;
#include "BluetoothSerial.h"
  
BluetoothSerial SerialBT;
DynamicJsonDocument doc(1024);

const int leftButton = 0;
const int rightButton = 35;


int leftValue = 0;
int rightValue = 0;

void setup() {
  Serial.begin(115200);
  pinMode(leftButton,INPUT_PULLUP);
  pinMode(rightButton,INPUT_PULLUP);
  SerialBT.begin("ESP32test");
  delay(1000);
}

void loop() {
  leftValue = analogRead(leftButton);
  rightValue = analogRead(rightButton);
  doc["leftValue"] = leftValue;
  doc["rightValue"] = rightValue;
  serializeJson(doc, Serial);
  Serial.println();
  SerialBT.println();
  delay(1000);
  }
