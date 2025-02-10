# Import tkinter for the GUI, random for generating the password and pyperclip for copying the password to the clipboard
import tkinter
import random
import pyperclip

# Initialize the window
root = tkinter.Tk()
root.geometry("400x300")
root.title("Password Generator")

# List of characters
chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*1234567890"
pass_stringvar = tkinter.StringVar(root)

# Password generation function
def generate_password():
    try:
        length = int(passlen_input.get())
        if length > 20:
            pass_stringvar.set("Length too big")
        else:
            pass_str = ""
            for i in range(length):
                pass_str += random.choice(chars)
            pass_stringvar.set(pass_str)
    except Exception:
        pass_stringvar.set("Length is not a number")

def copy_pass():
    pyperclip.copy(pass_stringvar.get())

# Widgets
# Welcome text
welcome = tkinter.Label(root, text="Welcome to Password Generator!", font=("Arial", 19))
# Password length hint(it's not possible to add hint to a tkinter Entry, so I will display a label)
passlen_hint = tkinter.Label(root, text="Enter password length(maximum 20 characters):")
# Password length input
passlen_input = tkinter.Entry(root)
# Generate button
generate_button = tkinter.Button(root, text="Generate", command=generate_password)
# The password will be displayed in a read-only Entry so that it can be copied
password_label = tkinter.Label(root, textvariable=pass_stringvar)
# Button to copy password to clipboard
copy_button = tkinter.Button(root, text="Copy to clipboard", command=copy_pass)


# Place the widgets
welcome.place(x=10, y=0)
passlen_hint.place(x=100, y=50)
passlen_input.place(x=100, y=70)
generate_button.place(x=250, y=65)
password_label.place(x=100, y=100)
copy_button.place(x=250, y=100)

# Main loop
root.mainloop()
