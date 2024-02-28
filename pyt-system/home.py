import tkinter as tk
import customtkinter as ctk
import subprocess

def button1_command():
     root.withdraw()
     subprocess.run(["python3", "Employee.py"], check=True)

def button2_command():
    root.withdraw()
    subprocess.run(["python3", "master.py"], check=True)

def button3_command():
    root.withdraw()
    subprocess.run(["python3", "Bc.py"], check=True)

def button4_command():
    root.withdraw()
    subprocess.run(["python3", "ph.py"], check=True)


def button5_command():
    root.withdraw()
    subprocess.run(["python3", "Contract.py"], check=True)


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.title("Button Page")
root.geometry("600x600")  

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill='both', expand=True)

button1 = ctk.CTkButton(master=frame, text="العاملين", command=button1_command, height=90, width=300)
button1.pack(pady=12, padx=10)

button2 = ctk.CTkButton(master=frame, text="ماجستير", command=button2_command, height=90, width=300)
button2.pack(pady=12, padx=10)

button3 = ctk.CTkButton(master=frame, text="بكالوريس", command=button3_command, height=90, width=300)
button3.pack(pady=12, padx=10)

button4 = ctk.CTkButton(master=frame, text="دكتوراه", command=button4_command, height=90, width=300)
button4.pack(pady=12, padx=10)

button5 = ctk.CTkButton(master=frame, text="متعاونين", command=button5_command, height=90, width=300)
button5.pack(pady=12, padx=10)

root.mainloop()
