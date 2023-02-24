String command;
bool isOpen = false;
bool didPress = false;
bool botonIsPressed = false;
// bool isOpen = true;
const int vueltas = 59 * 200;
const int velocidad = 400;  // microsegundos

// Variables will change:
int sensor1State;            // the current reading from the input pin
int lastSensor1State = LOW;  // the previous reading from the input pin

// Variables will change:
int buttonState;            // the current reading from the input pin
int lastButtonState = LOW;  // the previous reading from the input pin
int boton;
bool byButton = false;

unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 500;   // the debounce time; increase if the output flickers
unsigned long botonDebounceTime = 0;

#define SENSOR_ABAJO 7
#define SENSOR_ARRIBA 8

void setup() {
  Serial.begin(9600);

  pinMode(10, OUTPUT);           // relaySensor
  pinMode(2, OUTPUT);            // DIR
  pinMode(3, OUTPUT);            // STEP
  pinMode(4, OUTPUT);            // ENABLE
  pinMode(SENSOR_ABAJO, INPUT);  // SENSOR ABAJO
  pinMode(SENSOR_ARRIBA, INPUT);
  pinMode(9, INPUT);  // BOTON
  digitalWrite(4, HIGH);
  digitalWrite(2, HIGH);
  digitalWrite(10, LOW);
}

void loop() {
  command = "";
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();
    if (command.equals("CERRAR") and (isOpen == true)) {
      Serial.println("CERRADO");
      cerrarBox(false);
    }
    if (command.equals("ABRIR") and (isOpen == false)) {
      Serial.println("ABIERTO");
      delay(500);
      abrirBox();
    }
  }

  int boton = digitalRead(9);
  leerBoton(boton);
//  Serial.println(boton);
  delay(100);
  lastButtonState = boton;

  while (isOpen == true) {
    int reading = digitalRead(SENSOR_ABAJO);
//    Serial.println("Sensor de abajo:" + String(reading));

    boton = digitalRead(9);
    leerBoton(boton);
    delay(100);
    lastButtonState = boton;

    if (reading == LOW) {
      lastDebounceTime = millis();  // reset the debouncing timer
    }
    if ((millis() - lastDebounceTime) > debounceDelay) {
      checkearQueEsteHIGH15Segundos();
      delay(1000);
    }

    //lastSensor1State = reading;
  }
}

void abrirBox() {
  digitalWrite(10, HIGH);  //prender relay de sensor

  isOpen = true;
  digitalWrite(4, LOW);  // ENABLE IS ACTIVE LOW
  digitalWrite(2, LOW);

  delay(500);
  for (int i = 0; i <= vueltas; i++) {
    digitalWrite(3, LOW);
    delayMicroseconds(velocidad);
    digitalWrite(3, HIGH);
    delayMicroseconds(velocidad);
  }
}

void cerrarBox(bool byButton) {
  // Serial.println("ENTRO A CERRARBOX");
  bool didStop = false;
  digitalWrite(4, LOW);  // ENABLE IS ACTIVE LOW
  digitalWrite(2, HIGH);
  delay(1000);
  //  Serial.println("Empezamos a cerrar");
  for (int i = 0; i <= vueltas - 50; i++) {
    if (byButton == false) {
      // Serial.println("Se cerro sin boton");
      didStop = checkearSiLOW();
      if (didStop == true) {
        abrirOnStop(i);
        break;
      }
    }

    digitalWrite(3, HIGH);
    delayMicroseconds(velocidad);
    digitalWrite(3, LOW);
    delayMicroseconds(velocidad);
  }
  if (didStop == false) {
    delay(1000);
    digitalWrite(4, HIGH);  // DISABLE STEPPER
    digitalWrite(10, LOW);  // DISABLE AREA SENSOR
    isOpen = false;
    delay(500);
    sensor1State = 0;            
    lastSensor1State = 0; 
  }
}

void checkearQueEsteHIGH15Segundos() {
  unsigned long startMillis = millis();

  while (millis() - startMillis < 15000) {
    int readingAbajo = digitalRead(SENSOR_ABAJO);
    int readingArriba = digitalRead(SENSOR_ARRIBA);
    delay(100);
//    Serial.println("timer: " + String(millis() - startMillis));
    if ((readingAbajo == LOW) or (readingArriba == LOW)) {

      startMillis = millis();
    }
  }
  cerrarBox(false);
}

void abrirOnStop(int iteraciones) {
  delay(1000);
  digitalWrite(2, LOW);
  for (int i = 0; i <= iteraciones; i++) {
    digitalWrite(3, LOW);
    delayMicroseconds(velocidad);
    digitalWrite(3, HIGH);
    delayMicroseconds(velocidad);
  }
  isOpen = true;
}
bool checkearSiLOW() {
  int readingAbajo = digitalRead(SENSOR_ABAJO);
  int readingArriba = digitalRead(SENSOR_ARRIBA);

  int i = 0;
  int iteraciones = 3;
  while (((readingAbajo == LOW) or (readingArriba == LOW)) and (i < iteraciones)) {
    readingAbajo = digitalRead(SENSOR_ABAJO);
    readingArriba = digitalRead(SENSOR_ARRIBA);
    i++;
  }
  if (i == iteraciones) {
    sensor1State = LOW;
    return true;
  }
  return false;
}

void leerBoton(int boton) {

  // If the switch changed, due to noise or pressing:
  if (boton != lastButtonState) {
    // reset the debouncing timer
    botonDebounceTime = millis();
  }

  if ((millis() - botonDebounceTime) > debounceDelay) {
    if (boton != buttonState) {
      buttonState = boton;

      if (buttonState == HIGH) {
        // Serial.println("SE PRESIONO EL BOTON: " + String(boton));

        if (isOpen == true) {
          cerrarBox(true);
          // Serial.println("ENTRO A CERRAR");
        } else {
          // Serial.println("ENTRO A ABRIR");
          abrirBox();
        }
      }
    }
  }
}
