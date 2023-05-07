#include <Adafruit_I2CDevice.h>
#include <Adafruit_BMP085.h>
#include <DHT.h>
#define dhtPin 2
#define rainPin A10
#define dhtType DHT11

DHT dht(dhtPin, dhtType);
Adafruit_BMP085 bmp;

int temperature;
int humidity;
int rain;
float pressure;
String device_id = "Device0001";


void setup() {
    // put your setup code here, to run once:
  pinMode(dhtPin, INPUT);
    pinMode(rainPin, INPUT);
    
    Serial.begin(115200);
    dht.begin();
    bmp.begin();
}

void loop() {
    // put your main code here, to run repeatedly:
    temperature =  int((9 / 5.0) * dht.readTemperature()  + 32);
    humidity = int(dht.readHumidity());
    rain = map(analogRead(rainPin), 0, 1023, 100, 0);
    pressure = bmp.readPressure() * 0.0002953;

    String data = "{'device_id':" + device_id + ", 'temperature':" + temperature + ", 'humidity':" + humidity + ", 'rain'" + rain + ", 'pressure':" + pressure + "}";
    Serial.println(data);
    delay(1000);
}
