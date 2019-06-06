#include <string.h>
String str;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  str = Serial.readString();
  Serial.println(str);
}
