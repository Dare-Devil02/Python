from tkinter import PanedWindow

char= input("Press any key: ")
if char.isalpha():
    print("Thee user has entered a alphabet")
if char.isdigit():
    print("The user has entered a digit")
if char.isspace():
    print("the user has entered a white space")