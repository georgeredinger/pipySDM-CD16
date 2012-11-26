import RPi.GPIO as GPIO
import time
# Set up the GPIO channels  GPIO22,23,24
HIGH = GPIO.HIGH
LOW  = GPIO.LOW

C1 = 22 #data
C2 = 23 #clock
C3 = 24 #enable

SDMCD16ADDRESS =  int('11111111',2)
FILL = int('0000000000000000',2)

#def setup_GPIO():
GPIO.setmode(GPIO.BCM)
GPIO.setup(C1, GPIO.OUT)
GPIO.setup(C2, GPIO.OUT)
GPIO.setup(C3, GPIO.OUT)
GPIO.output(C1, GPIO.LOW)
GPIO.output(C2, GPIO.LOW)
GPIO.output(C3, GPIO.LOW)

def clock_a_bit(bit):
  if bit == 1:
    state = HIGH
  else:
    state = LOW
  GPIO.output(C1,state)
  GPIO.output(C2,HIGH)
  GPIO.output(C2,LOW)

def clock_a_byte(byte):
  b = byte
  for i in xrange(8):
    clock_a_bit(b & 1)
    b = b >> 1
 
def clock_a_word(word):
  w = word
  for i in xrange(16):
    clock_a_bit(w & 1)
    w = w >> 1

def latch_SDM():
  GPIO.output(C3,GPIO.LOW)
  GPIO.output(C3,GPIO.HIGH)

def enable_SDM():
  GPIO.output(C2,GPIO.HIGH)
  GPIO.output(C3,GPIO.HIGH)

def disable_SDM():
  GPIO.output(C2,GPIO.LOW)
  GPIO.output(C3,GPIO.LOW)


while True:
  enable_SDM()
  clock_a_byte(SDMCD16ADDRESS)
  clock_a_word(FILL)
  latch_SDM()
  disable_SDM()
  time.sleep(1)



