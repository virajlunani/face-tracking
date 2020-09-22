int pin = 9;


void setup() {
  // put your setup code here, to run once:
  pinMode(pin,OUTPUT);
  Serial.begin(9600);
}

void loop() {
// put your main code here, to run repeatedly:
  digitalWrite(pin, HIGH);
  delayMicroseconds(1500);
  digitalWrite(pin, LOW);
  delay(20);
}
