# import tkinter as tk
# from tkinter import ttk

# def on_button_click():
#     label.config(text="Button Clicked")

# root = tk.Tk()
# root.title("Modern Buttons")
# root.configure(background="#202020")

# # Create a style for the ttk buttons
# style = ttk.Style()
# style.configure("TButton", padding=20, relief="flat", background="#202020", foreground="white")

# # Create a ttk button
# button = ttk.Button(root, text="Modern Button", command=on_button_click)
# button.pack(pady=10)

# # Create a label to display a message
# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk
# from ttkthemes import ThemedTk

# root = ThemedTk(theme='equilux')
# root.title("Modern Window")

# # Create a themed style
# # style = ThemedStyle(root)
# # style.set_theme("equilux")  # You can choose a different theme here

# # Create widgets with the themed style
# button = tk.Button(root, text="Styled Button")
# button.pack(pady=10)

# label = tk.Label(root, text="Styled Label")
# label.pack()

# entry = tk.Entry(root)
# entry.pack()

# root.mainloop()

# from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
# from ttkthemes import ThemedTk

# window = ThemedTk(theme="arc")
# ttk.Button(window, text="Quit", command=window.destroy).pack()
# window.mainloop()

# import customtkinter

# customtkinter.set_appearance_mode('dark')
# customtkinter.set_default_color_theme('dark-blue')

import customtkinter

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text='text')
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()

