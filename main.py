# Setting the models
import tkinter
from tkinter import messagebox

# Setting the screen
window = tkinter.Tk()
window.title("Survey")
window.minsize(width=1000, height=1000)
window.config(padx=20, pady=20)


# Setting the function for the send button
def Send():
    # Setting the if and else statements to answer the iniquitous and giving an error when someone deos not answer
    # the survey.
    if first_name_entry.get() and last_name_entry.get() and password_entry.get():
        messagebox.showinfo(message="Thank you for answering the survey")
    else:
        messagebox.showerror(message="You did not answer the survey!")

    # Password
    try:
        user_input = password_entry.get()
        # Try to convert the input to a number (float or int)
        float(user_input)
        # Shows a message
        messagebox.showinfo(message=":)")

    # If it is not a number which a user puts it will go to show error
    except ValueError:
        # If the input is str, show an error message
        messagebox.showerror(message="You did not write a number for the password!. :(")


# Setting the show password
def show_password():
    # This if statement is used for hiding password
    if password_entry.cget('show') == '*':  # get is used for gettign the value of password entry
        password_entry.config(show='')
        # Putting text on hide_button
        hide_button.config(text='Hide Password')

    # Now we are doing else statement for showing the password
    else:
        password_entry.config(show='*')
        hide_button.config(text="Show password")


# Setting the title
Survey_label = tkinter.Label(font=("Roboto", 35), text="Survey", bg="black", fg="white")
Survey_label.pack(pady=20)

# Setting the label for the first name and the entry for the first name.
first_name_label = tkinter.Label(font=("Playfair Display", 12), text="First name", bg="black", fg="white")
first_name_label.pack(pady=5)

first_name_entry = tkinter.Entry(font=("Kablammo", 12), bg="gold", fg="black")
first_name_entry.pack(pady=5)

# Setting the label and the entry for the last name
last_name_label = tkinter.Label(font=("Bona Nova SC", 12), text="Last name", bg="black", fg="white")
last_name_label.pack(pady=5)
last_name_entry = tkinter.Entry(font=("Oxygen", 12), bg="gold", fg="black")
last_name_entry.pack()

# Setting the label and the entry for the Password
password_label = tkinter.Label(font=("Playwrite England SemiJoined", 12), text="Password", bg="black", fg="white")
password_label.pack(pady=5)
# created hide password
password_entry = tkinter.Entry(window, show='*', font=("PT Sans", 12), bg="gold", fg="black")
password_entry.pack(pady=5)

# creating a button for password visibility
hide_button = tkinter.Button(window, text="show password", command=show_password)
hide_button.pack(pady=3)
# Setting up the send button
send_button = tkinter.Button(font=("Bona Nova SC", 12), text="Send", bg="black", fg="white", command=Send)
send_button.pack()

window.mainloop()
