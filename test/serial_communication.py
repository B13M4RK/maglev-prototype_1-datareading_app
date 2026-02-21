# Library for serial communication
import serial

# Configure the serial port
ser = serial.Serial(
  port='COM4',
  baudrate=9600,
  timeout=2,
)

try:
  while True:
    # Read a line ending with a newline character
    data = ser.readline().decode('utf-8').rstrip()
    print(f"Data: {data}")
except KeyboardInterrupt:
  # end program with ctrl+c
  print("Exiting")
finally:
  # Close serial port (to be able to upload next time without closing serial port manually)
  ser.close()