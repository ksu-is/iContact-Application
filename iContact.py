from tkinter import *
import tkinter as tk
import controller

class iContact(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, NewContact, ContactGroups):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky=N+S+E+W)

            self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Landing Page!")
        label.pack()

        button = tk.Button(self, height=5, width=20, text="New Contact", command=lambda: controller.show_frame(NewContact))
        button.pack()

        button2 = tk.Button(self, height=5, width=20, text="Contact Groups", command=lambda: controller.show_frame(ContactGroups))
        button2.pack()


class NewContact(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Create a New Contact")
        label.pack()

        

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two", command=lambda: controller.show_frame(ContactGroups))
        button2.pack()


class ContactGroups(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!")
        label.pack()

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(NewContact))
        button2.pack()


app = iContact()
app.geometry("600x800")
app.mainloop()
