# Setting the models
import numbers
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
    # Setting the if else stament for password colum
    if( password_entry.get):
        password_entry.get =(1,2,3,)
        messagebox.showinfo(message=":)")
    else:
        password_entry.get = "STR"
        messagebox.showerror(message="You do not write a number for password")


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

password_entry = tkinter.Entry(font=("PT Sans", 12), bg="gold", fg="black")
password_entry.pack(pady=5)

# Setting up the send button
send_button = tkinter.Button(font=("Bona Nova SC", 12), text="Send", bg="black", fg="white", command=Send)
send_button.pack()

window.mainloop()
