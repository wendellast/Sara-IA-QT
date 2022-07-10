#include <LiquidCrystal.h> // Biblioteca visor
#include <Servo.h> // Biblioteca Micro servo
#include "DHT.h"


#define pinPIR A3
#define DHTPIN A2
#define DHTTYPE DHT11


//Variáveis
const int trigPin = 8; // vs e mic
const int echoPin = 9;
bool som;

int LED13 = 13; // Vermelho
int LED14 = 18; // Amarelo
int LED15 = 19; // Azul

int buzzer = 11;
int smoke = A1;
int sensorGas = 500;

//Visor e micro servo
LiquidCrystal lcd(2,3,4,5,6,7); // config Visor
long duration;
int distance;

Servo myServo;


//Temperatura
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  //Config
  Serial.begin(9600);
  pinMode(LED13, OUTPUT);  // liga led test

  //Sensor de som
  pinMode(12, INPUT);


  // Sensor de presensa
  pinMode(pinPIR, INPUT);

  //Visor lcd
  lcd.begin(16,2);
  
  //DHT11 Temperatura
  dht.begin();


  //Micro servo e sensor de distancia
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 
  myServo.attach(10);

  //Buzzer e sensor de gas
  pinMode(buzzer, OUTPUT);
  pinMode(smoke, INPUT);
  
}

void loop() {
  bool valorPIR = digitalRead(pinPIR); // Sensor de presença
  int LDR = analogRead(A0); // sensor de luz
  int analogSensor = analogRead(smoke);  // Sensor de gâs
  float h = dht.readHumidity(); // Umidade
  float t = dht.readTemperature(); // Temperatura


  // sensor de som
  som = digitalRead(12);
  if (!som){
    digitalWrite(LED15, HIGH);
    
  }
  else{
    digitalWrite(LED15, LOW);
  }

  //Serial.println(som);
  //delay(100);


 
  //Serial.println(LDR);

  //Sensor de luz
  if (LDR > 400){
    digitalWrite(LED14, LOW);
  }

  else{
    digitalWrite(LED14, HIGH);
  }

  Serial.println(analogSensor);


  //Sensor de presença
  if (valorPIR) {
    digitalWrite(LED14, HIGH);
  }

  else {
    digitalWrite(LED14, LOW);
  }



  
  //Sensor de gâs e buzzer
  if (analogSensor > sensorGas){
    digitalWrite(buzzer, HIGH);
    digitalWrite(LED13, HIGH);
    delay(100);
    digitalWrite(LED13, LOW);
    digitalWrite(buzzer, LOW);
    digitalWrite(LED13, HIGH);
  }

  else{
    digitalWrite(buzzer, LOW);
    digitalWrite(LED13, LOW);
  }

  //Temperatura e Umidade

  //Serial.print("Umidade: ");
  //Serial.print(h);
  //Serial.print(" Temperatura: ");
  //Serial.println(t);

  //delay(1000);
  

  
  //Micro servo e sensor de distancia
  for(int i=15;i<=165;i++){  
  myServo.write(i);
  delay(30);
  distance = calculateDistance();
    //Serial.println(i);
  lcd.clear();
  lcd.print("Distancia: ");
  lcd.print(distance);
  //Serial.print(distance);

  
  }

  
  for(int i=165; i>15;i--){  
  myServo.write(i);
  delay(30);
  distance = calculateDistance();
    //Serial.println(i);
  lcd.clear();
  lcd.print("Distancia: ");
  lcd.print(distance);
  //Serial.print(distance);
  
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
