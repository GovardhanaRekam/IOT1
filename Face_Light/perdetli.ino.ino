int ledPin = D2; // GPIO number where you connected your LED

void setup() {
  // Start the serial communication
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT); // Initialize the ledPin as an output
}

void loop() {
  if (Serial.available() > 0) { // check if data received
    char data = Serial.read(); // read the incoming byte
    if (data == '1') { // if '1' received
     // digitalWrite(ledPin, LOW); // turn the LED on (LOW is the voltage level)
      //delay(10000); // wait for 5 seconds
      digitalWrite(ledPin, HIGH);
      Serial.println("Light is ON");// turn the LED off by making the voltage HIGH
    }
    else if(data=='0'){
     digitalWrite(ledPin, LOW);
       Serial.println("Light is off");
      
      
      
      }
  }
}
