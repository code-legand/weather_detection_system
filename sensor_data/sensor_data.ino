void setup() {
    // put your setup code here, to run once:
    Serial.begin(115200);
}

void loop() {
    // put your main code here, to run repeatedly:
    String device_id = "Device0001";
    int temperature = 85;
    int humidity = 20;
    int rain = 0;
    float pressure = 20.5;

    String data = "{'device_id':" + device_id + ", 'temperature':" + temperature + ", 'humidity':" + humidity + ", 'rain'" + rain + ", 'pressure':" + pressure + "}";
    Serial.println(data);
    delay(1000);
}
