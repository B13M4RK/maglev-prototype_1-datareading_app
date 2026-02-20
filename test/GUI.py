import customtkinter



# FUNCTIONS
def click_button():
  my_label.configure(text=my_button.cget("text"))



# window
app = customtkinter.CTk()
app.geometry("400x150")

# button
my_button = customtkinter.CTkButton(app, text="click me", command=click_button)
my_button.pack(pady=50)

# label
my_label = customtkinter.CTkLabel(app, text="")
my_label.pack(pady=20)




# mainloop
app.mainloop()

