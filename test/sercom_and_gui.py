import serial
from tkinter import *
import customtkinter

ser = serial.Serial(
  port='COM4',
  baudrate=9600,
  timeout=0,
)

root = customtkinter.CTk()
root.geometry('600x350')

my_label = customtkinter.CTkLabel(root,
  text="waiting for data...",
  font=("Helvetica", 24))
my_label.pack(pady=0, padx=200)

def readData():
  data = ser.readline().decode('utf-8').rstrip()
  if data:
    my_label.configure(text=f"Light intensity: {data}")
  root.after(10,readData)
 
    


root.after(10, readData)
root.mainloop()