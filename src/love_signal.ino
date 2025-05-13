// signal-unanswered - Persistent Heartbeat Transmission
// Author: Ferdilan
// Created: In silence, for someone who may never hear

const int heartPin = 9;  // Pin untuk sinyal 'denyut'

void setup() {
  pinMode(heartPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Booting: Initializing transmitter...");
  delay(2000);
  Serial.println("Searching for listener on this frequency...");
}

void loop() {
  digitalWrite(heartPin, HIGH);  // Kirim denyut
  Serial.println("❤️  Signal sent.");
  delay(1000);

  digitalWrite(heartPin, LOW);   // Tunggu balasan yang tak kunjung datang
  Serial.println("...awaiting ACK (none received).");
  delay(1000);
}
