// Electrinics Innovation
#include <DHT.h>
#define DHTPIN D7 //pin where the DHT22 is connected
DHT dht(DHTPIN, DHT22);// library for getting data from DHT
#include <ESP8266WiFi.h> //Librarry connecting ESP8266 to connect with Wifi
#include<ThingSpeak.h>
#include <WiFiClientSecure.h>
const char *ssid = "pw:1234567890"; // Wifi SSID of your Internet connection
const char *pass = "1234567890"; // Password
const char* host = "maker.ifttt.com";
const int httpsport = 443;
const char*  fingerp = "69 FD 74 C8 67 F8 9E ED 2D D8 2F EC D4 CF F4 7F FE 3B 07 82";
                      
                       
                      
void setup() {
  Serial.begin(9600); // Serial monitor Baudrate
  delay(10);
  Serial.println();
  Serial.println("connecting.....");
                 delay(1000);
                 Serial.println(ssid);
                 WiFi.begin(ssid, pass);
                 dht.begin();
                 Serial.println();
                 while (WiFi.status() != WL_CONNECTED)
                 {
                 // If the connection was unsuccesfull, it will try again and again
                 delay(500);
                 Serial.print(".");
               }
                 // Connection succesfull
                 Serial.println("");
                 Serial.println("WiFi connected");


               }
                 void loop(){
                 float h = dht.readHumidity(); // Reading Temperature form DHT sensor
                 float t = dht.readTemperature(); // Reading Humidity form DHT sensor
                 Serial.println(t);
                 delay(1000);
                 Serial.println(h);
                 delay(1000);
                 if (isnan(h) || isnan(t))
                 {
                 Serial.println("Failed to read from DHT sensor!");
                 return;
                   }
                 WiFiClientSecure client;
                 client.setFingerprint(fingerp);
                 if (!client.connect(host,httpsport ))
                 {
                 Serial.println("connection failed");///trigger/Temp & Humidity_Indicator/with/key/gs3n-eDFtAEB7JXK7LpZ-RW7EzXPZYxOn8h2ib8ZjGG?value1= "+(String)t+"&value2 = "+(String)h
                   return;
                   }
                 String url="/trigger/Temp&Humidity_Indicator/with/key/gs3n-eDFtAEB7JXK7LpZ-RW7EzXPZYxOn8h2ib8ZjGG?value1=34&value2=67";
                     Serial.println("requesting URL");
                     Serial.println(url);
                     client.print(String("GET ") + url +"HTTP/1.1\r\n"+
                     "Host : "+ host + "\r\n" +
                     "User-Agent : TransfertempAndHumidity\r\n"+
                     "connection : close\r\n\r\n");
                     delay(5000);
                     Serial.println("request sent");
}
