#include <core.h>
int j;
void setup() { 
  pinMode(2,INPUT);
  j = analogRead(2);
  printf("{\"pH\": %.2f,\"value\": %.2f}\n",j*5.0/4096.0*3.5,j*5.0/4096.0*3.5);
} 

void loop() {
  
}
