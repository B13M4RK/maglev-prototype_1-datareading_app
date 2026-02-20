from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.geometry('600x350')

def submit():
  my_label.configure(text=f'Hello {my_entry.get()}')
  my_entry.delete(0, END)
  my_entry.configure(state="disabled")
  
my_label = customtkinter.CTkLabel(root, 
  text="", 
  font=("Helvetica", 24),
  )
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root,
  placeholder_text="Enter Your Name",
  height=50,
  width=200,
  font=("Helvetica", 18),
  corner_radius=20
  )
my_entry.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
my_button.pack(pady=10)





root.mainloop()