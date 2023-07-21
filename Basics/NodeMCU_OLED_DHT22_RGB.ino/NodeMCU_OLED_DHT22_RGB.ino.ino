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

#define LED_R D2
#define LED_G D1
#define LED_B D0

Adafruit_SSD1306 display(128, 64, &Wire, -1);

void setup() {
  pinMode(OLED_SDA, OUTPUT);
  pinMode(OLED_SCL, OUTPUT);
  
  Wire.begin(OLED_SDA, OLED_SCL);
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();

  dht.begin();

  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);
}

void loop() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    display.println("Error: Failed to read sensor data!");
  } else {
    display.print("Temperature: ");
    display.print(temperature);
    display.println(" C");
    display.print("Humidity: ");
    display.print(humidity);
    display.println(" %");

    // set LED color based on temperature
    if (temperature < 40) {
      analogWrite(LED_R, 0);
      analogWrite(LED_G, 255);
      analogWrite(LED_B, 0);
    } else if (temperature >= 40 && temperature < 45) {
      analogWrite(LED_R, 0);
      analogWrite(LED_G, 0);
      analogWrite(LED_B, 255);
    } else {
      analogWrite(LED_R, 255);
      analogWrite(LED_G, 0);
      analogWrite(LED_B, 0);
    }
  }

  display.display();
  delay(2000);
}
