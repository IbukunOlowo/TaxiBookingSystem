from tkinter import *


def RegistrationWindow():
    
    root = Tk()


    root.geometry("700x450")
    root.title("Taxi Booking System")

    registration_page_frame =Frame(root, width=500, height=500, bg="green")
    registration_page_frame.pack(fill="both", expand=1)


    titleLabel = Label(root,text="Customer Registration",font=('Arial',40 ,'bold'),fg='blue')
    titleLabel.pack()

    firstnameLabel = Label(registration_page_frame,text="First Name :",font=('Arial',20 ,'bold'),fg='blue')
    firstnameLabel.place(x=10,y=100)

    firstNameEntry = Entry()
    firstNameEntry.config(font=('Arial',20))
    firstNameEntry.place(x=130,y=100)

    lastNameLabel = Label(registration_page_frame,text="Last Name :",font=('Arial',20 ,'bold'),fg='blue')
    lastNameLabel.place(x=10,y=150)

    lastNameEntry = Entry()
    lastNameEntry.config(font=('Arial',20))
    lastNameEntry.place(x=130,y=150)

    phoneNoLabel = Label(registration_page_frame,text="Phone no:",font=('Arial',20 ,'bold'),fg='blue')
    phoneNoLabel.place(x=10,y=200)

    phoneNoEntry = Entry()
    phoneNoEntry.config(font=('Arial',20))
    phoneNoEntry.place(x=130,y=200)


    usernameLabel = Label(registration_page_frame,text="Username :",font=('Arial',20 ,'bold'),fg='blue')
    usernameLabel.place(x=10,y=250)

    usernameEntry = Entry()
    usernameEntry.config(font=('Arial',20))
    usernameEntry.place(x=130,y=250)

    passwordLabel = Label(registration_page_frame,text="Password :",font=('Arial',20 ,'bold'),fg='blue')
    passwordLabel.place(x=10,y=300)

    passwordEntry = Entry()
    passwordEntry.config(font=('Arial',20))
    passwordEntry.place(x=130,y=300)


    registerButton = Button(registration_page_frame,text='Register')
    registerButton.place(x=150,y=400)
    registerButton.config(font=('Arial',20,'bold'))






    root.mainloop()