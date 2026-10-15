import tkinter as tk
from tkinter import messagebox
from password_generator import password_generator
import pyperclip
from tkinter import ttk

def show_alert():
    messagebox.showinfo("Password Manager","Password Saved!")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = password_generator()
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_name_entry.get()
    if website != "" or website.strip() != "":
        email = email_username_entry.get()
        if email != "" or email.strip() != "":
            password = password_entry.get()
            if password != "" or password.strip() != "":
                is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs this correct?")
                if is_ok:
                    with open("my_passwords.txt", "a") as output_file:
                        line = f"{website} | {email} | {password}\n"
                        output_file.write(line)
                    website_name_entry.delete(0, 'end')
                    password_entry.delete(0, 'end')
                    website_name_entry.focus()
                    show_alert()
            else:
                messagebox.showinfo("Password Manager","Password can't be empty!")
                password_entry.focus()
        else:
            messagebox.showinfo("Password Manager","Email can't be empty!")
            email_username_entry.focus()
    else:
        messagebox.showinfo("Password Manager","Website can't be empty!")
        website_name_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window_width = 500
window_height = 400
# 1. Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# 2. Find the center point coordinates
center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# 3. Apply the geometry string
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
tomato_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(row=0, column=1)

website_name_label = tk.Label(text="Website:")
website_name_label.grid(row=1, column=0)
website_name_entry = tk.Entry(width=35)
website_name_entry.focus()
website_name_entry.grid(row=1, column=1, columnspan=2, sticky='EW')

email_username_label = tk.Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
email_username_entry = tk.Entry(width=35)
email_username_entry.insert(0,"triciamiller2025@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2, sticky='EW')

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky='EW', padx=(0, 5))
generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=30, command=save_to_file)
add_button.grid(row=4, column=1,columnspan=2, sticky='EW')





window.mainloop()