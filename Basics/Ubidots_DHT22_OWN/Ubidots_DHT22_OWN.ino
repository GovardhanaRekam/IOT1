/****************************************
 * Include Libraries
 ****************************************/
#include "UbidotsESPMQTT.h"
#include<DHT.h>

/****************************************
 * Define Constants
 ****************************************/
#define DHTPIN D3
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
 
#define TOKEN "BBFF-AgVi1B9tCKlbNUScLctZNFKENsOT7O" // Your Ubidots TOKEN
#define WIFINAME "vivo 1916" //Your SSID
#define WIFIPASS "0123456789" // Your Wifi Pass

Ubidots client(TOKEN);

/****************************************
 * Auxiliar Functions
 ****************************************/

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i=0;i<length;i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

/****************************************
 * Main Functions
 ****************************************/

void setup() {
  dht.begin();
  delay(1000);
  // put your setup code here, to run once:
  //client.ubidotsSetBroker("industrial.api.ubidots.com"); // Sets the broker properly for the industrial account
  client.setDebug(true); // Pass a true or false bool value to activate debug messages
  Serial.begin(115200);
  client.wifiConnection(WIFINAME, WIFIPASS);
  client.begin(callback);
  }

void loop() {
  // put your main code here, to run repeatedly:
  if(!client.connected()){
      client.reconnect();
      }
  
  float Temperature = dht.readTemperature();
  float Humidity = dht.readHumidity();
    client.add("temperature", Temperature);
    client.add("Humidity", Humidity);
  client.ubidotsPublish("Thermometer");
  client.loop();
  delay(5000);
}
