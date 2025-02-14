//uses SPI commands
#include <SPI.h>

//setting the commands to send to the RE to words I can type
const int none = 0x00;
const int position = 0x10;
const int zero = 0x70;
int x = 0;
int re = 0;
int de = 0;
int de2 = 0;
int z = 0;
int p1 = 0;
int p2 = 0;
int t = 0;
int x1 = 0;
int x2 = 0;
int x3 = 0;
int x4 = 0;
int b1 = 0;
int b2 = 0;
int b3 = 0;
int b4 = 0;

//pin decloration
#define DATAOUT 11 //COPI
#define DATAIN  12 //CIPO
#define SPICLOCK  13//sck
#define TEMP1 7//ss
#define TEMP2 6
#define PRESSURE 5
#define ROTARY 4

void setup() {
  // put your setup code here, to run once:

  // Settings for serial communication
  Serial.begin(115200);
  Serial.setTimeout(1);

  // Settings for SPI
  SPI.begin();
  // Pins shared for SPI communication
  pinMode (DATAOUT, OUTPUT);
  pinMode (DATAIN, INPUT);
  pinMode (SPICLOCK, OUTPUT);
  // Individual sesor select pins
  pinMode (TEMP1, OUTPUT);
  pinMode (PRESSURE, OUTPUT);
  pinMode (TEMP2, OUTPUT);
  pinMode (ROTARY, OUTPUT);
  digitalWrite(TEMP1, HIGH);
  digitalWrite(PRESSURE, HIGH);
  digitalWrite(ROTARY, HIGH);
  digitalWrite(TEMP2, HIGH);
  SPI.beginTransaction(SPISettings(750000, MSBFIRST, SPI_MODE0));
}

void loop() {
  // put your main code here, to run repeatedly:
  x = Serial.readString().toInt();


  while(x != 1){ // reads from the serial port and looks for a 1
    x = Serial.readString().toInt();
  }

  // Sends the command to the rotary encoder asking for the position data
  digitalWrite(ROTARY, LOW);
  re = SPI.transfer(position);
  digitalWrite(ROTARY, HIGH);

  

  while(re != 0x10){ //This loop reads the output from the rotary encoder and waits until it returns 0x10
    digitalWrite(ROTARY, LOW);
    re = SPI.transfer(none);
    digitalWrite(ROTARY, HIGH);

    
  }

  //Gathers the position data from the rotary encoder
  delayMicroseconds(20);
  digitalWrite(ROTARY, LOW);
  de = SPI.transfer(none);
  digitalWrite(ROTARY, HIGH);
  delayMicroseconds(20);
  
  digitalWrite(ROTARY, LOW);
  de2 = SPI.transfer(none);
  digitalWrite(ROTARY, HIGH);
  delayMicroseconds(20);
  
  
  //reads the pressure data in 4 separate parts
  digitalWrite(PRESSURE, LOW);
  p1 = SPI.transfer(none);
  p2 = SPI.transfer(none);
  t = SPI.transfer(none);
  t = SPI.transfer(none);
  digitalWrite(PRESSURE, HIGH);

  //reads the temperature data, four bytes from each sensor
  digitalWrite(TEMP1, LOW);
  x1 = SPI.transfer(none);
  x2 = SPI.transfer(none);
  x3 = SPI.transfer(none);
  x4 = SPI.transfer(none);
  digitalWrite(TEMP1, HIGH);
  digitalWrite(TEMP2, LOW);
  b1 = SPI.transfer(none);
  b2 = SPI.transfer(none);
  b3 = SPI.transfer(none);
  b4 = SPI.transfer(none);
  digitalWrite(TEMP2, HIGH);

  //Sends the data I collected over serial
  Serial.print('%');
  Serial.print(millis(),HEX);
  Serial.print(',');
  Serial.print(de,HEX);
  Serial.print(',');
  Serial.print(de2,HEX);
  Serial.print(',');
  Serial.print(p1,HEX);
  Serial.print(',');
  Serial.print(p2,HEX);
  Serial.print(',');
  Serial.print(x1,HEX);
  Serial.print(',');
  Serial.print(x2,HEX);
  Serial.print(',');
  Serial.print(b1,HEX);
  Serial.print(',');
  Serial.print(b2,HEX);
  Serial.println(',');
}

