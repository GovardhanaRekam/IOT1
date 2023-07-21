#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_ADDR   0x3C
#define OLED_SDA    D5
#define OLED_SCL    D6

Adafruit_SSD1306 display(128, 64, &Wire, -1);

void setup() {
  pinMode(OLED_SDA, OUTPUT);
  pinMode(OLED_SCL, OUTPUT);
  
  Wire.begin(OLED_SDA, OLED_SCL);
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();
}

void loop() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("Hello,Innovators");
  display.setCursor(0,20);
  display.println("Let's Engage in");
  display.setTextSize(2);
  display.setCursor(0,40);
  display.println("Astronics");
  display.display();
  delay(1000);
}
