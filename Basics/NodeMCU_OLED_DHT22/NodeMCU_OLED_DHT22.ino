#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHT.h>

#define OLED_ADDR   0x3C
#define OLED_SDA    D5
#define OLED_SCL    D6

#define DHTPIN D3
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

Adafruit_SSD1306 display(128, 64, &Wire, -1);

void setup() {
  pinMode(OLED_SDA, OUTPUT);
  pinMode(OLED_SCL, OUTPUT);
  
  Wire.begin(OLED_SDA, OLED_SCL);
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();

  dht.begin();
  delay(1000);
}

void loop() {
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  display.print("Temp:");
  display.setCursor(0,15);
  display.print(temperature);
  display.println("C");
  display.setCursor(0,30);
  display.print("Hum:          ");
  display.setCursor(0,45);
  display.print(humidity);
  display.println("%");

  display.display();
  delay(2000);
}
