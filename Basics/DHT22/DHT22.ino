#include<DHT.h>
#define Type DHT22
int sensePin = D3;
DHT HT(sensePin,Type);
float humidity;
float tempF;
float tempC;
int setTime=500;
void setup() {
 Serial.begin(9600);
 HT.begin();
 delay(setTime);
}
void loop() {
  humidity = HT.readHumidity();
  tempC = HT.readTemperature();
  tempF = HT.readTemperature();
  Serial.print("humidity");
  Serial.print(humidity);
  Serial.print("\t temperature C=");
  Serial.print(tempC);
  Serial.print("temp F = ");
  Serial.println(tempF);
  delay(1000);
  
}
