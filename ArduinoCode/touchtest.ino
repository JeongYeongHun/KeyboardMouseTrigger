void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  digitalWrite(4,LOW);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  pinMode(4,INPUT);
  delay(1);
  pinMode(4,OUTPUT);
  delay(1);
  Serial.print("1");
}
