from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry('700x450')

def game():
  if check_var.get() == "on":
    my_label.configure(text="You Clicked play")
  else:
    my_label.configure(text="You Haven't checked the box")

def clear():
  my_check.deselect()
  
  

check_var = customtkinter.StringVar(value="off")
my_check = customtkinter.CTkCheckBox(root,
  text="would you like to play a game?",
  variable=check_var,
  onvalue="on",
  offvalue="off",
  checkbox_width=50,
  checkbox_height=50,
  font=('Helvetica', 18),
  corner_radius=10
  
)
my_check.pack(pady=40)

my_button = customtkinter.CTkButton(root,
  text="Submit",
  command=game)
my_button.pack(pady=20)

clear_button = customtkinter.CTkButton(root,
  text="Clear",
  command=clear)
clear_button.pack(pady=10)

toggle_button = customtkinter.CTkButton(root,
  text="toggle",
  command=my_check.toggle)
toggle_button.pack(pady=10)

select_button = customtkinter.CTkButton(root,
  text="select",
  command=my_check.select)
select_button.pack(pady=10)
 

my_label = customtkinter.CTkLabel(root,
  text="")
my_label.pack(pady=20)




root.mainloop()