# serial communication
import serial
import time

serialcomm = serial.Serial('COM4', 9600)
serialcomm.timeout = 2


# While running the programm
while True:
  # print to terminal the light intensity
    print("light intensity: ", serialcomm.readline().decode('ascii'))