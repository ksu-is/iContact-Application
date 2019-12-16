from tkinter import *
import tkinter as tk


# This is the root class
class iContact(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # This creates the capability for switching between windows
        for F in (HomePage, NewContact, ContactGroups):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(HomePage)

    # This method is used by the buttons in the page classes to call classes
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# This is the class for the landing page
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Status Bar at the Bottom of the Window
        self.status_bar = tk.Label(self, text="© iContact 2019 ", relief=tk.SUNKEN, bd=1)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Label creates a title at the top of the page
        label = tk.Label(self, text="Home Page", bg="light goldenrod", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)

        # Creates the Buttons that switch Frames
        button = tk.Button(self, height=5, width=20, text="New Contact",
                           command=lambda: controller.show_frame(NewContact))
        button.pack(pady=50)

        button2 = tk.Button(self, height=5, width=20, text="Contact List",
                            command=lambda: controller.show_frame(ContactGroups))
        button2.pack(pady=5)


# This is the class for the New Contact page where users can create a Contact
class NewContact(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Status Bar at the Bottom of the Window
        self.status_bar = tk.Label(self, text="© iContact 2019 ", relief=tk.SUNKEN, bd=1)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Label creates a title at the top of the page
        label = tk.Label(self, text="Create a New Contact", bg="light goldenrod", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)

        # Creates the Full Name Entry Box
        name = tk.Label(self, text='Full Name:')
        name.pack(pady=2, padx=10)
        name_box = tk.Entry(self)
        name_box.pack()
        name_box.focus_set()

        # Creates the Email Entry Box
        email = tk.Label(self, text='Email:')
        email.pack(pady=2, padx=10)
        email_box = tk.Entry(self)
        email_box.pack()

        # Creates the Phone Number Entry Box
        phone = tk.Label(self, text='Phone Number:')
        phone.pack(pady=2, padx=10)
        phone_box = tk.Entry(self)
        phone_box.pack()

        # Creates the Group Entry Box
        group = tk.Label(self, text='Group:')
        group.pack(pady=2, padx=10)
        group_box = tk.Entry(self)
        group_box.pack()

        # Creates the Submit Button
        subm_btn = tk.Button(self, text="SUBMIT", bg="white", fg='black', font=("Helvetica", 16))
        subm_btn.pack(pady=25)

        # Creates the Buttons that switch Frames
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Contact List", command=lambda: controller.show_frame(ContactGroups))
        button2.pack()


# This is the class used to view the list of contacts
class ContactGroups(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Status Bar at the Bottom of the Window
        self.status_bar = tk.Label(self, text="© iContact 2019 ", relief=tk.SUNKEN, bd=1)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Label creates a title at the top of the page
        label = tk.Label(self, text="Contact List", bg="light goldenrod", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)

        # Initializes the ListBox created by the MkListBox Method
        self.MkListBox()

        # Creates the Buttons that switch Frames
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="New Contact", command=lambda: controller.show_frame(NewContact))
        button2.pack()

    # Method Creates a Listbox on the left side of the screen
    def MkListBox(self):
        lbx_names = tk.Listbox(self, width=20)
        lbx_names.pack(fill=Y, side=LEFT)
        lbx_names.focus_set()


# This creates variable 'app' and initializes the root class
app = iContact()
# This adjusts the window size on all Apps
app.geometry("300x450")
# This allows for the app to run on local machines
app.mainloop()
