import RPi.GPIO as GPIO
import time
# Set up the GPIO channels  GPIO22,23,24


C1 = 22
C2 = 23
C3 = 24
SDMCD16ADDRESS =  int('101010101',2)
FILL = int('1000000000000000',2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(C1, GPIO.OUT)
GPIO.setup(C2, GPIO.OUT)
GPIO.setup(C3, GPIO.OUT)

def clock_a_bit(bit):
  GPIO.output(C1,bit)
  GPIO.output(C2,True)
  GPIO.output(C2,False)

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

def enable_SDM():
  GPIO.output(C2, True)
  GPIO.output(C3, True)

def latch_SDM():
  GPIO.output(C3,False)
  GPIO.output(C3,True)
  GPIO.output(C3,False)
  GPIO.output(C2,False)
  GPIO.output(C1,False)

enable_SDM
clock_a_byte(SDMCD16ADDRESS)
clock_a_word(FILL)
latch_SDM

