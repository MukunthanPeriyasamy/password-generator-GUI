#password generator mechanism


from tkinter import *

#Creating Windows
windows = Tk()
windows.title("Password Generator")
windows.config(pady=50, padx=100)
logo_image = PhotoImage(file="logo.png")
windows.iconphoto(True, logo_image)

#Creating Canvas
canvas = Canvas(width=200, height=200)
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(row=0, column=1)

#creating Labels
letters = Label(text="No of Letters: ")
letters.grid(row=1, column=0)
numbers = Label(text="No of Numbers: ")
numbers.grid(row=2, column=0)
symbol = Label(text="No of Symbol: ")
symbol.grid(row=3, column=0)

#creating Entry fields
no_of_letters = Entry(width=35)
no_of_letters.grid(row=1, column=1)
no_of_numbers = Entry(width=35)
no_of_numbers.grid(row=2, column=1)
no_of_symbol = Entry(width=35)
no_of_symbol.grid(row=3, column=1)

new_password = Label(text="Your password")
new_password.grid(row=4, column=1)

import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = []
    for letter in range(int(no_of_letters.get())):
        random_letter = random.choice(letters)
        password.append(random_letter)
    for symbol in range(int(no_of_symbol.get())):
        random_symbol = random.choice(symbols)
        password.append(random_symbol)
    for number in range(int(no_of_numbers.get())):
        random_number = random.choice(numbers)
        password.append(random_number)
    random.shuffle(password)

    add_password = ""
    for char in password:
        add_password += char
    new_password.config(text=f"Your password: {add_password}")


#generate button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0)
windows.mainloop()
