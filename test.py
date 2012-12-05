import RPi.GPIO as GPIO
import time
import string,types
# Set up the GPIO channels  GPIO22,23,24
HIGH = GPIO.HIGH
LOW  = GPIO.LOW

C1 = 22 #data
C2 = 23 #clock
C3 = 24 #enable

SDMCD16ADDRESS =  int('33',4)
FILL = int('1000000000000001',2)

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
  time.sleep(0.001)
  GPIO.output(C2,HIGH)
  time.sleep(0.001)
  GPIO.output(C2,LOW)
  time.sleep(0.001)

def clock_a_byte(byte):
  b = byte
  for i in xrange(9):
    clock_a_bit(b & 1)
    b = b >> 1

def clock_a_nyble(nyble):
  n = nyble
  for i in xrange(5):
    clock_a_bit(n & 1)
    n = n >> 1
 
def clock_a_word(word):
  w = word
  for i in xrange(16):
    clock_a_bit(w & 1)
    w = w >> 1

def latch_SDM():
  time.sleep(.001)
  GPIO.output(C2,GPIO.HIGH)
  time.sleep(0.001)
  GPIO.output(C3,GPIO.LOW)
  time.sleep(0.001)
  GPIO.output(C3,GPIO.HIGH)
  time.sleep(0.001)

def enable_SDM():
  GPIO.output(C2,GPIO.HIGH)
  GPIO.output(C3,GPIO.HIGH)
  time.sleep(0.001)

def disable_SDM():
  GPIO.output(C2,GPIO.LOW)
  GPIO.output(C3,GPIO.LOW)


def itoa (n, base = 2,digits=16):
    if type (n) != types.IntType:
        raise TypeError, 'First arg should be an integer'
    if (type (base) != types.IntType) or (base <= 1):
        raise TypeError, 'Second arg should be an integer greater than 1'
    output = []
    pos_n = abs (n)
    while pos_n:
        lowest_digit = pos_n % base
        output.append (str (lowest_digit))
        pos_n = (pos_n - lowest_digit) / base
    output.reverse ()
    if n < 0:
        output.insert (0, '-')
    return string.join (output, '')

def set_SDMCD16(address,bits):
    print  itoa(bits).format(16).zfill(16)
    disable_SDM()
    enable_SDM()
    clock_a_byte(int(address))
    time.sleep(.01)
    clock_a_word(int(bits))
    latch_SDM()
    time.sleep(.01)

def address_blast():
  for i in xrange(16):
    print i,
    set_SDMCD16(i,int(0))


while True:
  #bits=raw_input('bits to set: ')
  bits = int('1100000000000011',2)
  set_SDMCD16(0,bits)
  time.sleep(1)
  set_SDMCD16(0, int('0000000000000000',2))
  time.sleep(1)
 # disable_SDM()

address_blast()

