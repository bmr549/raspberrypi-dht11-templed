import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

DHT_PIN = 4
RED_LED = 11
BLUE_LED = 13
SENSOR = Adafruit_DHT.DHT11

GPIO.setup(RED_LED, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(BLUE_LED, GPIO.OUT, initial = GPIO.LOW)

humidity, temperature = Adafruit_DHT.read_retry(SENSOR, DHT_PIN)
print(temperature)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, DHT_PIN)
    print(temperature)
    print(humidity)
    if temperature > 24:
        GPIO.output(RED_LED, GPIO.HIGH)
    else if temperature < 20:
        GPIO.output(BLUE_LED, GPIO.HIGH)