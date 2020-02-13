const unsigned int TRIG_PIN1=9;
const unsigned int ECHO_PIN1=10;
const unsigned int TRIG_PIN2=5;
const unsigned int ECHO_PIN2=6;
const unsigned int BAUD_RATE=9600;

void setup() {
  pinMode(TRIG_PIN1, OUTPUT);
  pinMode(ECHO_PIN1, INPUT);

  pinMode(TRIG_PIN2, OUTPUT);
  pinMode(ECHO_PIN2, INPUT);
  Serial.begin(BAUD_RATE);
}

void loop() {
   digitalWrite(TRIG_PIN1, LOW);
   delayMicroseconds(2);
   digitalWrite(TRIG_PIN1, HIGH);
   delayMicroseconds(10);
   digitalWrite(TRIG_PIN1, LOW);
   
   unsigned long duration= pulseIn(ECHO_PIN1, HIGH);
   int distance= duration/29/2;
   if(duration==0){
   Serial.println("Warning: no pulse from sensor 1");
   } 
   else{
   Serial.println("Proximity/1");
   Serial.println(distance);
   }
   
   delay(38);

  digitalWrite(TRIG_PIN2, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN2, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN2, LOW);

  duration= pulseIn(ECHO_PIN2, HIGH);
  distance= duration/29/2;
  if(duration==0){
    Serial.println("Warning: no pulse from sensor 2");
  } 
  else{
    Serial.println("Proximity/2");
    Serial.println(distance);
  }
  delay(38);



}



