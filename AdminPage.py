from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DatabaseConnection import Database


class adminWindow:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700")
        self.root.title("Taxi Booking System")
        self.current_frame = None
        self.show_admin_window()


    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()


    def show_admin_window(self):
        self.clear_frame()
        self.current_frame =Frame(self.root, width=1300, height=700, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

    

        titleLabel = Label(
            self.current_frame,
            text="Admin Page",
            font=('Arial',40 ,'bold'),
            fg='blue'
        )
        titleLabel.pack()

        
        usernameLabel = Label(
            self.current_frame,
            text="Username :",
            font=('Arial',20 ,'bold'),
            fg='blue'
    )
        usernameLabel.place(x=10,y=50)

        self.usernameEntry = Entry(self.current_frame)
        self.usernameEntry.config(font=('Arial',20))
        self.usernameEntry.place(x=130,y=50)

        passwordLabel = Label(
            self.current_frame,
            text="Password :",
            font=('Arial',20 ,'bold'),
            fg='blue'
        )
        passwordLabel.place(x=10,y=100)

        self.passwordEntry = Entry(self.current_frame, show="*")
        self.passwordEntry.config(font=('Arial',20))
        self.passwordEntry.place(x=130,y=100)




        loginButton = Button(
            self.current_frame,
            text='Login', 
            command= self.validate_login
        )
        loginButton.place(x=150,y=250)
        loginButton.config(font=('Arial',20,'bold'))



    def validate_login(self):

        entered_username = self.usernameEntry.get()
        entered_password = self.passwordEntry.get()
        
        db = Database()
        user = db.admin_login(username = entered_username, password = entered_password)
        if user:
            admin_id = user[0]
            self.admin_id = admin_id
            self.show_dashboard()
        else:
            messagebox.showerror("Login failed", "Invalid username or password")


    def page_picker(self,choice):
        if choice == "CUSTOMERS":
            self.clear_frame()
            self.show_customers()
        elif choice == "HOME":
            self.clear_frame()
            self.show_dashboard()
        elif choice == "DRIVERS":
            self.clear_frame()
            self.show_drivers()
        elif choice == "HISTORY":
            self.clear_frame()
            self.show_history()



    def show_dashboard(self):
        """Show a simple Admin Dashboard."""
        self.clear_frame()
        self.current_frame = Frame(self.root, width=1300, height=700, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        menu_options = ["HOME","CUSTOMERS", "BOOKINGS", "DRIVERS", "HISTORY"]
        clicked = StringVar(value="HOME")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)


        titleLabel = Label(
            self.current_frame, 
            text="Admin Dashboard", 
            font=('Arial', 40, 'bold'), 
            fg='blue', 
            bg='grey'
        )
        titleLabel.pack()

        assign_driver_Label = Label(
            self.current_frame, 
            text="Assign Driver :", 
            font=('Arial', 15, 'bold'), 
            fg='blue', 
            bg='grey'
        )
        assign_driver_Label.place(x=10, y= 150)

        driver = []
        self.assign_driver_entry = ttk.Combobox(self.current_frame, values= driver)
        self.assign_driver_entry.place(x= 10, y= 200)


        self.admintable = ttk.Treeview(self.current_frame, columns= ('B:ID', 'Customer_ID','Driver_ID','Pick Address', 'Drop Address', 'Time', 'Date','Car Type'), show= 'headings')


        self.admintable.column("B:ID", width= 80)
        self.admintable.column("Customer_ID", width= 80)
        self.admintable.column("Driver_ID", width= 80)
        self.admintable.column("Pick Address", width= 160)
        self.admintable.column("Drop Address", width= 160)
        self.admintable.column("Time", width= 80)
        self.admintable.column("Date", width= 80)
        self.admintable.column("Car Type", width= 80)

        self.admintable.heading('B:ID', text='B:ID')
        self.admintable.heading('Customer_ID', text='Customer_ID')
        self.admintable.heading('Driver_ID', text='Driver_ID')
        self.admintable.heading('Pick Address', text='Pick Address')
        self.admintable.heading('Drop Address', text='Drop Address')
        self.admintable.heading('Time', text='Time')
        self.admintable.heading('Date', text='Date')
        self.admintable.heading('Car Type', text='Car Type')

        self.admintable.place(x=250, y = 100)
        self.populate_adminDashboard_treeview()

        # Back Button
        backButton = Button(
            self.current_frame, 
            text='Logout', 
            font=('Arial', 20, 'bold'), 
            command=self.show_admin_window
        )
        backButton.place(x=200, y=450)

        assign_driver_button = Button(
            self.current_frame, 
            text="Assign Driver", 
            font=('Arial', 20, 'bold'), 
            #fg='white', 
            bg='yellow'
        )
        assign_driver_button.place(x= 300, y= 400)

        cancel_booking__button = Button(
            self.current_frame, 
            text="Cancel Booking", 
            font=('Arial', 20, 'bold'), 
            #fg='white', 
            bg='yellow'
        )
        cancel_booking__button.place(x= 470, y= 400)

    def populate_adminDashboard_treeview(self):
        for item in self.admintable.get_children():
            self.admintable.delete(item)


        db = Database()
        records = db.fetch_all_bookings()


        for record in records:
            self.admintable.insert("","end", values = record)


    def show_customers(self):
        self.clear_frame()
        self.current_frame = Frame(self.root, width=1000, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        menu_options = ["HOME","CUSTOMERS", "BOOKINGS", "DRIVERS", "HISTORY"]
        clicked = StringVar(value="HOME")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)


        titleLabel = Label(
            self.current_frame, 
            text="All Customers", 
            font=('Arial', 40, 'bold'), 
            fg='yellow', 
            bg='grey'
        )
        titleLabel.pack()

        self.customerTable = ttk.Treeview(self.current_frame, columns= ('User ID','Username', 'Password', 'First Name', 'Last Name', 'Phone No', 'Address', 'Email'), show= 'headings')

        self.customerTable.column("User ID", width= 80)
        self.customerTable.column("Username", width= 160)
        self.customerTable.column("Password", width= 160)
        self.customerTable.column("First Name", width= 80)
        self.customerTable.column("Last Name", width= 160)
        self.customerTable.column("Phone No", width= 160)
        self.customerTable.column("Address", width= 160)
        self.customerTable.column("Email", width= 160)
        

        self.customerTable.heading('User ID', text='User ID')
        self.customerTable.heading('Username', text='Username')
        self.customerTable.heading('Password', text='Password')
        self.customerTable.heading('First Name', text='First Name')
        self.customerTable.heading('Last Name', text='Last Name')
        self.customerTable.heading('Phone No', text='Phone No')
        self.customerTable.heading('Address', text='Address')
        self.customerTable.heading('Email', text='Email')
        self.customerTable.place(x=10, y = 100)

        self.populate_customers_treeview()

    def populate_customers_treeview(self):
        for item in self.customerTable.get_children():
            self.customerTable.delete(item)


        db = Database()
        records = db.fetch_customer()


        for record in records:
            self.customerTable.insert("","end", values = record)

    

    def show_drivers(self):
        self.clear_frame()
        self.current_frame = Frame(self.root, width=1000, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        menu_options = ["HOME","CUSTOMERS", "BOOKINGS", "DRIVERS", "HISTORY"]
        clicked = StringVar(value="HOME")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)

        titleLabel = Label(
            self.current_frame, 
            text="All Drivers", 
            font=('Arial', 40, 'bold'), 
            fg='yellow', 
            bg='grey'
        )
        titleLabel.pack()

        self.driverTable = ttk.Treeview(self.current_frame, columns= ('Driver ID', 'username', 'password', 'First Name', 'Last Name', 'Phone No', 'Car Type'), show= 'headings')

        self.driverTable.column("Driver ID", width= 80)
        self.driverTable.column("username", width= 80)
        self.driverTable.column("password", width= 80)
        self.driverTable.column("First Name", width= 80)
        self.driverTable.column("Last Name", width= 160)
        self.driverTable.column("Phone No", width= 160)
        self.driverTable.column("Car Type", width= 80)
        
        self.driverTable.heading('Driver ID', text='Driver ID')
        self.driverTable.heading('username', text='username')
        self.driverTable.heading('password', text='password')
        self.driverTable.heading('First Name', text='First Name')
        self.driverTable.heading('Last Name', text='Last Name')
        self.driverTable.heading('Phone No', text='Phone No')
        self.driverTable.heading('Car Type', text='Car Type')
        self.driverTable.place(x=10, y = 100)
        self.populate_drivers_treeview()

    def populate_drivers_treeview(self):
        for item in self.driverTable.get_children():
            self.driverTable.delete(item)


        db = Database()
        records = db.fetch_drivers()


        for record in records:
            self.driverTable.insert("","end", values = record)



    def show_history(self):
        self.clear_frame()
        self.current_frame = Frame(self.root, width=1000, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        menu_options = ["HOME","CUSTOMERS", "BOOKINGS", "DRIVERS", "HISTORY"]
        clicked = StringVar(value="HOME")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)

        titleLabel = Label(
            self.current_frame, 
            text="All Previous bookings", 
            font=('Arial', 40, 'bold'), 
            fg='yellow', 
            bg='grey'
        )
        titleLabel.pack()

        
        self.previous_bookings_table = ttk.Treeview(self.current_frame, columns= ('Booking_ID', 'Customer_ID','Driver_ID','Pick Address', 'Drop Address', 'Time', 'Date','Car Type'), show= 'headings')

        self.previous_bookings_table.column("Booking_ID", width= 80)
        self.previous_bookings_table.column("Customer_ID", width= 80)
        self.previous_bookings_table.column("Driver_ID", width= 80)
        self.previous_bookings_table.column("Pick Address", width= 160)
        self.previous_bookings_table.column("Drop Address", width= 160)
        self.previous_bookings_table.column("Time", width= 80)
        self.previous_bookings_table.column("Date", width= 80)
        self.previous_bookings_table.column("Car Type", width= 80)


        self.previous_bookings_table.heading('Booking_ID', text='Booking_ID')
        self.previous_bookings_table.heading('Customer_ID', text='Customer_ID')
        self.previous_bookings_table.heading('Driver_ID', text='Driver_ID')
        self.previous_bookings_table.heading('Pick Address', text='Pick Address')
        self.previous_bookings_table.heading('Drop Address', text='Drop Address')
        self.previous_bookings_table.heading('Time', text='Time')
        self.previous_bookings_table.heading('Date', text='Date')
        self.previous_bookings_table.heading('Car Type', text='Car Type')
        self.previous_bookings_table.place(x=10, y = 100)


    def populate_previousBookings_treeview(self):
        for item in self.previous_bookings_table.get_children():
            self.previous_bookings_table.delete(item)


        db = Database()
        records = db.fetch_all_bookings()


        for record in records:
            self.previous_bookings_table.insert("","end", values = record)




# Main Application Loop
if __name__ == "__main__":
    root = Tk()
    app = adminWindow(root)
    root.mainloop()
    



    #root.mainloop()





#adminWindow()

