#include <LiquidCrystal.h> // Biblioteca visor
#include <Servo.h> // Biblioteca Micro servo


#define pinPIR 0

//Variáveis
const int trigPin = 8;
const int echoPin = 9;
bool som;
int LED8 = 8;
LiquidCrystal lcd(2,3,4,5,6,7); // config Visor
long duration;
int distance;

Servo myServo;

void setup() {
  //Config
  Serial.begin(9600);
  //Teste
  pinMode(LED8, OUTPUT);  // liga led test

    
  //Visor lcd
  lcd.begin(16,2);
  


  //Micro servo e sensor de distancia
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 
  myServo.attach(10);
  
}

void loop() {
  bool valorPIR = digitalRead(pinPIR); // Sensor de presença
  int LDR = analogRead(A0); // sensor de luz
  
  //Serial.println(LDR);

  //Sensor de luz
  if (LDR > 400){
    digitalWrite(LED8, HIGH);
  }

  else{
    digitalWrite(LED8, LOW);
  }
  
  //Micro servo e sensor de distancia
  for(int i=15;i<=165;i++){  
  myServo.write(i);
  delay(30);
  distance = calculateDistance();
    //Serial.println(i);
  lcd.clear();
  lcd.print("Distancia: ");
  lcd.print(distance);
  Serial.print(distance);

  
  }

  
  for(int i=165; i>15;i--){  
  myServo.write(i);
  delay(30);
  distance = calculateDistance();
    //Serial.println(i);
  lcd.clear();
  lcd.print("Distancia: ");
  lcd.print(distance);
  Serial.print(distance);
  }
}


//Micro servo e sensor de distancia
int calculateDistance(){ 
  
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(5);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); // Reads the echoPin, returns the sound wave travel time in microseconds
  distance= duration*0.034/2;
  return distance;

  
}
