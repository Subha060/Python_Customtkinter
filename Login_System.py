# This is a simple login system using customtkinter
import customtkinter
from tkinter import messagebox

def login():
    email = email_input.get()
    password = password_input.get()
    print(email, password)
    file = open("details.txt", "a")
    file.write("Email: " + email + "\n" + "Password: " + password + "\n" + "\n")
    file.close()
    if email == "" and password == "":
        messagebox.showerror('login', 'Error')
    else:
        messagebox.showinfo('Login', 'Successful')

    email_input.delete(0, 'end')
    password_input.delete(0, 'end')


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.title("Login System")
# root.iconbitmap("secure_login_icon_150316.ico")
root.minsize(300, 350)
root.maxsize(300, 350)
# root.config(background= "#1a1919")

frame1 = customtkinter.CTkFrame(master=root, width=300, height=50, corner_radius=15, fg_color="#1a1919")
frame1.pack(padx=5, pady=(10, 5))
frame2 = customtkinter.CTkFrame(master=root, width=200, height=50, corner_radius=15, fg_color="#1a1919")
frame2.pack(pady=10, padx=4)

login_text = customtkinter.CTkLabel(master=frame1, text="Login System", text_color="#b8f0f2", font=("Algerian", 25))
login_text.pack(pady=(10, 12), padx=17)

username_label = customtkinter.CTkLabel(master=frame2, text="Username", font=("Baskerville Old Face", 15))
username_label.pack(pady=(10, 0), padx=(0, 100))
email_input = customtkinter.CTkEntry(master=frame2, width=170, placeholder_text="Enter Username",
                                     font=("Baskerville Old Face", 15))
email_input.pack(pady=(0, 15), padx=24)

password_label = customtkinter.CTkLabel(master=frame2, text="Password", font=("Baskerville Old Face", 15))
password_label.pack(pady=(2, 2), padx=(0, 100))
password_input = customtkinter.CTkEntry(master=frame2, width=170, placeholder_text="Enter Password", show="*",
                                        font=("Baskerville Old Face", 15))
password_input.pack(pady=(0, 17), padx=24)

checkbox = customtkinter.CTkCheckBox(master=frame2, text="Remember Me", font=("Baskerville Old Face", 16))
checkbox.pack(pady=0, padx=(23, 60))

button = customtkinter.CTkButton(master=frame2, width=170, text="Submit", corner_radius=12,
                                 font=("Baskerville Old Face", 20), command=login)
button.pack(pady=(12, 20), padx=20)

root.mainloop()
