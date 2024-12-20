import tkinter
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

window = tkinter.Tk()
window.title("Login")
window.minsize(width=1000, height=1000)
window.config(padx=20, pady=20)


def read_config(file_path):
    """
    Reads the configuration file for email credentials.

    Parameters:
        file_path (str): Path to the configuration file.

    Returns:
        dict: A dictionary containing sender_email and app_password.
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    return {
        "sender_email": config.get("Email", "sender_email"),
        "app_password": config.get("Email", "app_password")
    }


def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using Gmail's SMTP server.

    Parameters:
        sender_email (str): The email address of the sender.
        sender_password (str): The password or App Password for the sender's Gmail account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.

    Returns:
        str: Success or error message.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        return "Email sent successfully!"
    except Exception as e:
        return f"Error: {e}"


# Setting the function for the send button
def Send():
    # Setting the if and else statements to answer the iniquitous and giving an error when someone deos not answer
    # the survey.
    if first_name_entry.get() and last_name_entry.get() and password_entry.get():
        messagebox.showinfo(message="Thank you for answering the survey")
    else:
        messagebox.showerror(message="You did not answer the survey!")

    #  Making frist and last name to be a string value.
    if first_name_entry.get().isalpha() and last_name_entry.get().isalpha():
        messagebox.showinfo(message="Valid First and Last_name:...")
    else:
        messagebox.showerror(message="Invalid name Frist_name and Last_name:....")
    # Read configuration
    config = read_config("config.ini")
    sender = config["sender_email"]
    password = config["app_password"]
    sender = sender
    password = password
    recipient = gmail_entry.get()
    subject = "Test Email"
    body = "i love u -emre."

    result = send_email(sender, password, recipient, subject, body)
    print(result)


# Setting the show password
def show_password():
    # This if statement is used for hiding password
    if password_entry.cget('show') == '*':  # get is used for getting the value of password entry
        password_entry.config(show='')
        # Putting text on hide_button
        hide_button.config(text='Hide Password')
    # Now we are doing else statement for showing the password
    else:
        password_entry.config(show='*')
        hide_button.config(text="Show password")


# Setting_Button
def Reset():
    # Clear all text in the first entry field
    first_name_entry.delete(0, 'end')
    # Clear all text in the second entry field
    last_name_entry.delete(0, 'end')
    # Clear all text in the password field
    password_entry.delete(0, 'end')
    # Clear all text in the Gmail field
    gmail_entry.delete(0, 'end')


# Setting the title
login_label = tkinter.Label(font=("Roboto", 35), text="Login", bg="black", fg="white")
login_label.pack(pady=20)

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

# Setting the gmail label
gmail_label = tkinter.Label(window, font=("Playwrite England SemiJoined", 12), text="What is your gmail address",
                            bg='black', fg='white')
gmail_label.pack(pady=10)

# Setting the gmail entry
gmail_entry = tkinter.Entry(window, font=("Playwrite England SemiJoined", 12), bg="gold", fg="black")
gmail_entry.pack()

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

# Making a rest button that way it can reset the survey
rest_button = tkinter.Button(font=("Bona Nova SC", 12), text="Rest Survey", bg='black', fg="white", command=Reset)
rest_button.pack(pady=10)

window.mainloop()
