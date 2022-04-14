void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  Serial.begin(9600);
  Serial.println("Arduino is ready");
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    int inc = Serial.read();
    if (inc == 1) {
      digitalWrite(4, HIGH);
    } else {
      digitalWrite(4, LOW);
    }
    delay(500);
  }
}
