from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import customtkinter
from PIL import Image
import pyperclip
import json

#Setting up the GUI

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

image = Image.open('padlock.png')
image = customtkinter.CTkImage(light_image=image, dark_image=image, size=(200,200))


#############################################################################################################
# Declaring frame composition
#############################################################################################################

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #Generating Password

        def generate_password():
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            password_letters = [choice(letters) for _ in range(randint(8, 10))]
            password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
            password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

            password_list = password_letters + password_symbols + password_numbers
            shuffle(password_list)

            password = "".join(password_list)
            password_entry.insert(0, password)
            pyperclip.copy(password)

        #Saving Passwprd

        def save():

            website = website_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            new_data = {
                website: {
                    "email": email,
                    "password": password,
                }
            }

            if len(website) == 0 or len(password) == 0 or len(email) == 0:
                messagebox.showinfo(title="Error", message="Empty fields detected.")
            else:
                try:
                    with open("data.json", "r") as data_file:
                        #Reading current data
                        data = json.load(data_file)
                
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)    
                
                else:
                    #Updating with new data
                    data.update(new_data)
                    with open("data.json", "w") as data_file:
                        #Saving updated data
                        json.dump(data, data_file, indent=4)
            
                finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


        #Finding a password

        def find_password():
            website = website_entry.get()
            try:
                with open("data.json") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                messagebox.showinfo(title="Error", message="No Data File Found.")
            else:
                if website in data:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                else:
                    messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

        # add widgets onto the frame, for example:
        #Labels

        image_label = customtkinter.CTkLabel(master=self, text='', image=image, width=200)
        image_label.grid(row=0, column=1)

        website_label = customtkinter.CTkLabel(master=self, text="Website:", width=130, anchor='e')
        website_label.grid(row=1, column=0, padx=10)

        email_label = customtkinter.CTkLabel(master=self, text="Email/Username:", width=130, anchor='e')
        email_label.grid(row=2, column=0, padx=10)

        password_label = customtkinter.CTkLabel(master=self, text="Password:", width=130, anchor='e')
        password_label.grid(row=3, column=0, padx=10)

        #Entries

        website_entry = customtkinter.CTkEntry(master=self, width=250)
        website_entry.grid(row=1, column=1, pady=5)

        email_entry = customtkinter.CTkEntry(master=self, width=390, placeholder_text="email@email.com")
        email_entry.grid(row=2, column=1, columnspan=2, pady=5)

        password_entry = customtkinter.CTkEntry(master=self, width=250)
        password_entry.grid(row=3, column=1, pady=5)

        # Buttons

        search_button = customtkinter.CTkButton(master=self, text="Search", width=130, command=find_password)
        search_button.grid(row=1, column=2, padx=10)

        generate_password_button = customtkinter.CTkButton(master=self, text="Generate Password", width=130, command=generate_password)
        generate_password_button.grid(row=3, column=2, padx=10)

        add_button = customtkinter.CTkButton(master=self, text="Add", width=400, command=save)
        add_button.grid(row=4, column=1, columnspan=2, pady=5)


#############################################################################################################
# Declaring window itself
#############################################################################################################


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=5, pady=5)
        self.geometry('620x400')
        self.minsize(620,400)
        self.grid_rowconfigure(index=[0], weight=1)
        self.grid_columnconfigure(index=[0], weight=1)

        self.main_frame = MyFrame(master=self, fg_color='transparent')
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)


window = Window()
window.mainloop()