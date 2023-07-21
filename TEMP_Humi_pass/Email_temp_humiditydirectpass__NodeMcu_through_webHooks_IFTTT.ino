#include <ESP8266WiFi.h>
#include <ThingSpeak.h> 
#include <DHT.h>
#define DHTPIN D7 //pin where the DHT22 is connected
DHT dht(DHTPIN, DHT22);

const char* ssid = "pw:-12345678";
const char* password = "12345678";
const char* host = "maker.ifttt.com";

WiFiClient client; 
unsigned long counterChannelNumber = 2117778;                // motor channel/Led
const char * myCounterReadAPIKey = "0R2ANBOSEKLQ7ZAZ";
const int FieldNumber1 = 1;
//---------------------//
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define OLED_ADDR   0x3C
#define OLED_SDA    D5
#define OLED_SCL    D6
Adafruit_SSD1306 display(128, 64, &Wire, -1);
void setup() {
    Serial.begin(9600);
    //-------//
     pinMode(OLED_SDA, OUTPUT);
  pinMode(OLED_SCL, OUTPUT);
    
  Wire.begin(OLED_SDA, OLED_SCL);
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();
  //----//
    pinMode(2,OUTPUT);
    dht.begin();
    delay(100);
    Serial.println("Email from Node Mcu");
    delay(100);
    Serial.print("Connecting to ");
    Serial.println(ssid);
    
    WiFi.begin(ssid, password);
    
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
  
    Serial.println("");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());  
    ThingSpeak.begin(client);
            



}

void loop() {  
      
      
           WiFiClient client; 
           const int httpPort = 80;  
            if (!client.connect(host, httpPort)) {  
                  Serial.println("connection failed");  
            return;} 
        
                    delay(8000);
          float h = dht.readHumidity();
          delay(1000);// Reading Temperature form DHT sensor
          float t = dht.readTemperature();
          delay(100);
          String T="TEMPERATURE:"+(String)t;
           Serial.println(T);
           delay(1500);
           String H="Humidity:"+(String)h;
           Serial.println(H);
           delay(150);
          if (isnan(h) || isnan(t))
         {
  Serial.println("Failed to read from DHT sensor!");
    return;
    }
    //-------//
   display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
 display.print("Temp:");
  display.setCursor(0,15);
  display.print(t);
  display.println("C");
  display.setCursor(0,30);
  display.print("Hum:          ");
  display.setCursor(0,45);
  display.print(h);
  display.println("%");

  display.display();
  delay(2000);
    //-------//
    int A = ThingSpeak.readLongField(counterChannelNumber, FieldNumber1, myCounterReadAPIKey);
    digitalWrite(2,A);
    if(A==1){
      Serial.println("Fan was rotating");
      delay(2000);
    }
          if(t>23&&h>30){
           delay(1000);
           //------//
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
 display.print("Temperature high turn on fan");
  display.setCursor(0,45);
  display.print("with mit");
  display.println(" app");
 // display.setCursor(0,30);
 /* display.print("Hum:          ");
  display.setCursor(0,45);
  display.print(humidity);
  display.println("%");
*/
  display.display();
  delay(2000);
           
           //------//
               /*     String url1 = "/trigger/TEMP_HUMI/with/key/gs3n-eDFtAEB7JXK7LpZ-RW7EzXPZYxOn8h2ib8ZjGG?value1="+(String)t;
                    delay(100);
                    url1+="&value2="+(String)h; 
                    delay(120);
          
                    Serial.print("Requesting URL: ");
                    Serial.println(url1);
                 
                     client.print(String("GET ") + url1 + " HTTP/1.1\r\n" + 
                                    "Host: " + host + "\r\n" +   
                                           "Connection: close\r\n\r\n");  
                       delay(5000);   */
                 /*      //...........................................................................//
                    String url2 = "/trigger/TEMP_HUMI_C/with/key/f6XiUTJijWto_XZammvo1_9mnHsjHOU45YdYnlxv_D2?value1="+(String)t;
                    delay(100);
                    url2+="&value2="+(String)h; 
                    delay(120);
          
                    Serial.print("Requesting URL: ");
                    Serial.println(url2);
                 
                     client.print(String("GET ") + url2 + " HTTP/1.1\r\n" + 
                                    "Host: " + host + "\r\n" +   
                                           "Connection: close\r\n\r\n");  */ 
              //....................................................................//
              delay(1000);
              String url3 = "/trigger/TEMP_HUMI_M/with/key/gs3n-eDFtAEB7JXK7LpZ-RW7EzXPZYxOn8h2ib8ZjGG?value1="+(String)t;
                    delay(1000);
                    url3+="&value2="+(String)h; 
                    delay(120);
          
                    Serial.print("Requesting URL: ");
                    Serial.println(url3);
                 
                     client.print(String("GET ") + url3 + " HTTP/1.1\r\n" + 
                                    "Host: " + host + "\r\n" +   
                                           "Connection: close\r\n\r\n");
                
          
          delay(1000);
          }
      
}
