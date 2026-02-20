import customtkinter



# FUNCTIONS
def click_button():
  my_label.configure(text=my_button.cget("text"))



# window
app = customtkinter.CTk()
app.geometry("1920x1080")

# button
my_button = customtkinter.CTkButton(app, 
  text="click me", 
  command=click_button,
  height=100,
  width=200,
  font=("Helvetica", 25),
  text_color="black",
  fg_color="red",
  hover_color="green",
  corner_radius=50,
  bg_color="white",
  border_width=10,
  border_color="yellow")
my_button.pack(pady=50)

# label
my_label = customtkinter.CTkLabel(app, text="")
my_label.pack(pady=20)




# mainloop
app.mainloop()

