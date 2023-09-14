#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Servo.h>
#include <DHT.h>
const char* ssid = "pw:-123456789";
const char* password = "123456789";

const char* serverName = "http://api.thingspeak.com/update";
String apiKey = "C7QLG8IFLF1QA4S6";



WiFiClient client;

Servo myServo;
int dhtPin = D7;
int servoPin = D4;  // Pin where the servo is connected
int ledPin = D6;    // Pin where the LED is connected
#define DHTTYPE DHT22
DHT dht(dhtPin, DHTTYPE);
int waterCount = 0;
unsigned long actionEndTime = 0;
const unsigned long actionDuration = 10000;  // 10 seconds
unsigned long previousMillis = 0;
const long interval = 12 * 60 * 60 * 1000; // 12 hours

void setup() {
    Serial.begin(9600);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
    
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
    
    myServo.attach(servoPin);
    myServo.write(0);  // Assume 0 is the closed position of the servo
    dht.begin();    
}

void loop() {
    if (millis() < actionEndTime) {
        // Lighting up the LED and opening the door for 10 seconds after a "1" is received
        digitalWrite(ledPin, HIGH); 
        myServo.write(90);  // Assume 90 is the open position of the servo
        
        return;  // Skip the rest of the loop
    } else {
        // Turn off the LED and close the door after the action time has ended
        digitalWrite(ledPin, LOW);
        myServo.write(0);
    }
   float humidity = dht.readHumidity();
    delay(4000);
    float tempC = dht.readTemperature();

    Serial.print("Humidity: ");
    Serial.println(humidity);
    Serial.print("Temperature: ");
    Serial.println(tempC);

    if (!isnan(humidity) && !isnan(tempC)) {
        if (humidity > 40.0) { 
            waterCount++;
            previousMillis = millis();
            
            if (waterCount <= 3) {
                if (client.connect("api.thingspeak.com", 80)) {
                  String dataStr = "Temp: " + String(tempC) + "C, Humidity: " + String(humidity) + "Message: Time to water the plant"; 
                  dataStr.replace(" ", "%20");  // URL encode spaces                                     
                    String postStr = apiKey;
                    postStr += "&field3=";                   
                    postStr += dataStr;
                    postStr += "\r\n\r\n";
    
                    client.print("POST /update HTTP/1.1\n");
                    client.print("Host: api.thingspeak.com\n");
                    client.print("Connection: close\n");
                    client.print("X-THINGSPEAKAPIKEY: " + apiKey + "\n");
                    client.print("Content-Type: application/x-www-form-urlencoded\n");
                    client.print("Content-Length: ");
                    client.print(postStr.length());
                    client.print("\n\n");
                    client.print(postStr);

                    // New debugging lines to check the HTTP response
                    while (client.connected()) {
                        String line = client.readStringUntil('\n');
                        if (line == "\r") {
                            break;
                        }
                    }
                    String response = client.readString();
                    Serial.print("ThingSpeak response: ");
                    Serial.println(response);

                    delay(2000);                
                } else {
                    Serial.println("Failed to connect to ThingSpeak");
                }
                client.stop();
            }
        }
    }      
    delay(2000);  



    

    if (Serial.available()) {
        String data = Serial.readString();

        // Check if we received a "1" from the Python script
        data.trim();
        if (data == "1") {
            actionEndTime = millis() + actionDuration;
        }
    }
    delay(1000);
}
/*
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Servo.h>
#include <DHT.h>

const char* ssid = "pw:-123456789";
const char* password = "123456789";

Servo myServo; 
int dhtPin = D7;
int servoPin = D5;
int ledPin = D6;

#define DHTTYPE DHT22
DHT dht(dhtPin, DHTTYPE);

unsigned long actionEndTime = 0;
const unsigned long actionDuration = 10000;  // 10 seconds

void setup() {
    Serial.begin(9600);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    
    Serial.println("Connected to WiFi");

    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
    myServo.attach(servoPin);
    myServo.write(0);
    dht.begin();
}

void loop() {
    if (millis() < actionEndTime) {
        digitalWrite(ledPin, HIGH);
        myServo.write(90);  // Open the door
        delay(1000);  // We can afford a 1-second delay here since we're in the middle of the action
        return;  // Skip the rest of the loop
    } else {
        digitalWrite(ledPin, LOW);
        myServo.write(0);  // Close the door
    }

    float humidity = dht.readHumidity();
    delay(4000);
    float tempC = dht.readTemperature();

    Serial.print("Humidity: ");
    Serial.println(humidity);
    Serial.print("Temperature: ");
    Serial.println(tempC);

    if (!isnan(humidity) && !isnan(tempC)) {
        if (humidity < 40.0) { 
            // Your water logic goes here if you still need it
        }
    }      
    delay(2000);

    if(Serial.available()) {
        delay(2000); 
        String data = Serial.readString();

        if (data.trim() == "1") {
            actionEndTime = millis() + actionDuration;
        }
    }
    delay(1000);
}




*/

