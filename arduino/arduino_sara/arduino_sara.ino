#include <LiquidCrystal.h> // Biblioteca visor
#include <Servo.h> // Biblioteca Micro servo
#include <Firmata.h>
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
int LED15 = 19; // verde

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


int lastLine = 1;

void stringDataCallback(char *stringData){
   if ( lastLine ) {
     lastLine = 0;
     lcd.clear();
   } else {
     lastLine = 1;
     lcd.setCursor(0,1);
   }
   lcd.print(stringData);
}


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
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();  
  
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
  int h = dht.readHumidity(); // Umidade
  int t = dht.readTemperature(); // Temperatura
  while (Firmata.available() ) {
    lcd.clear();
    Firmata.processInput();
  }
 
  
  lcd.setCursor(0,1);
  lcd.print("Tp: ");
  lcd.print(t);
  lcd.print("C");
  lcd.print(" Umd: ");
  lcd.print(h);
  
 
    //Sensor de luz
  int LDR = analogRead(A0); // sensor de luz
  if (LDR >= 400){
    digitalWrite(LED14, LOW);
  }


  else{
    digitalWrite(LED14, HIGH);
  }
  
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



  //Serial.println(analogSensor);


  //Sensor de presença
  bool valorPIR = digitalRead(pinPIR); // Sensor de presença
  if (valorPIR){
    digitalWrite(LED13, HIGH);
    digitalWrite(buzzer, HIGH);


  }

   
  //Sensor de gâs e buzzer
  int analogSensor = analogRead(smoke);  // Sensor de gâs
  if (analogSensor > sensorGas){
    
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
  while (Firmata.available() ) {
    lcd.clear();
    Firmata.processInput();
  }
    //Serial.println(i);
  //lcd.clear();
  //lcd.print("Distancia: ");
  //lcd.print(distance);
  //Serial.print(distance);
   
  
  lcd.setCursor(0,1);
  lcd.print("Tp: ");
  lcd.print(t);
  lcd.print("C");
  lcd.print(" Umd: ");
  lcd.print(h);
  
  
  int LDR = analogRead(A0); // sensor de luz
  if (LDR >= 400){
    digitalWrite(LED14, LOW);
  }


  else{
    digitalWrite(LED14, HIGH);
  }
  
  // sensor de som
  som = digitalRead(12);
  if (!som){
    digitalWrite(LED15, HIGH);
    
  }
  else{
    digitalWrite(LED15, LOW);
  }


  //Sensor de presença
  bool valorPIR = digitalRead(pinPIR); // Sensor de presença
  if (valorPIR){
    digitalWrite(LED13, HIGH);
    digitalWrite(buzzer, HIGH);

  }

  
  //Sensor de gâs e buzzer
  int analogSensor = analogRead(smoke);  // Sensor de gâs
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



  
  }

  
  for(int i=165; i>15;i--){  
  myServo.write(i);
  delay(30);
  distance = calculateDistance();
   
  
  while (Firmata.available() ) {
    lcd.clear();
    Firmata.processInput();
  }
   //Serial.println(i);
  lcd.clear();
  lcd.print("Distancia: ");
  lcd.print(distance);
  lcd.print(" Cm");

  lcd.setCursor(0,1);
  lcd.print("Tp: ");
  lcd.print(t);
  lcd.print("C");
  lcd.print(" Umd: ");
  lcd.print(h);
  
  //Serial.print(distance);
  int LDR = analogRead(A0); // sensor de luz
  if (LDR >= 400){
    digitalWrite(LED14, LOW);
  }


  else{
    digitalWrite(LED14, HIGH);
  }
  
  // sensor de som
  som = digitalRead(12);
  if (!som){
    digitalWrite(LED15, HIGH);
    
  }
  else{
    digitalWrite(LED15, LOW);
  }


  //Sensor de presença
  bool valorPIR = digitalRead(pinPIR); // Sensor de presença
  if (valorPIR){
    digitalWrite(LED13, HIGH);
    digitalWrite(buzzer, HIGH);
 
  }

  
  //Sensor de gâs e buzzer
  int analogSensor = analogRead(smoke);  // Sensor de gâs
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

  

  
  }
  
  


  //Monitor
  Serial.print("Luz: ");
  Serial.println(LDR  );
  Serial.print("Som: ");
  Serial.println(som  );
  Serial.print("Presença: ");
  Serial.println(valorPIR);
  Serial.print("Gâs: ");
  Serial.println(analogSensor);
  Serial.print("Umidade: ");
  Serial.println(h);
  Serial.print("Temperatura: ");
  Serial.println(t);

 
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
