import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.title("Login System")
root.minsize(300,150)
root.maxsize(500,350)

frame1 = customtkinter.CTkFrame(master=root,width=200,height=50, corner_radius= 15,)
frame1.pack(pady= 5, padx= 4)
frame2 = customtkinter.CTkFrame(master=root,width=200,height=50,corner_radius=15)
frame2.pack(pady= 25, padx= 4)

label1 = customtkinter.CTkLabel(master=frame1,text="Login System",font=("Sans serif",30),text_color="green")
label1.pack(pady= 5, padx= 4)

username = customtkinter.CTkEntry(master=frame2,placeholder_text="Username")
username.pack(pady= 15, padx= 24)
password = customtkinter.CTkEntry(master=frame2,placeholder_text="Password",show= "*")
password.pack(pady= 15, padx= 24)

checkbox = customtkinter.CTkCheckBox(master=frame2,text="Remember Me")
checkbox.pack(pady= 20, padx= 10)

button = customtkinter.CTkButton(master=frame2,text="Submit")
button.pack(pady= 10, padx= 20)


root.mainloop()