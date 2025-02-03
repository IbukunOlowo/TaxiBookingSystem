from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DatabaseConnection import Database



class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700")
        self.root.title("Taxi Booking System")
        self.current_frame = None
        self.show_customer_window()
       

    def clear_frame(self):
        """Clears the current frame."""
        if self.current_frame:
            self.current_frame.destroy()

    def show_customer_window(self):
        """Displays the customer login window."""
        self.clear_frame()
        self.current_frame = Frame(self.root, width=500, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        title_label = Label(
            self.current_frame,
            text="Customer Page",
            font=('Arial', 40, 'bold'),
            fg='blue',
            bg='grey'
        )
        title_label.pack()

        

        username_label = Label(
            self.current_frame,
            text="Username:",
            font=('Arial', 20, 'bold'),
            fg='blue',
            bg='grey'
        )
        username_label.place(x=10, y=50)

        self.username_entry = Entry(self.current_frame, font=('Arial', 20))
        self.username_entry.place(x=150, y=50)

        password_label = Label(
            self.current_frame,
            text="Password:",
            font=('Arial', 20, 'bold'),
            fg='blue',
            bg='grey'
        )
        password_label.place(x=10, y=100)

        self.password_entry = Entry(self.current_frame, font=('Arial', 20), show="*")
        self.password_entry.place(x=150, y=100)

        login_button = Button(
            self.current_frame,
            text="Login",
            font=('Arial', 20, 'bold'),
            command=self.validate_login
        )
        login_button.place(x=150, y=200)

        register_button = Button(
            self.current_frame,
            text="Register",
            font=('Arial', 20, 'bold'),
            command=self.show_registration_window
        )
        register_button.place(x=150, y=260)

    def validate_login(self):

        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        
        db = Database()
        user = db.login(username = entered_username, password = entered_password)

        if user:
            customer_id = user[0]
            self.customer_id = customer_id
            self.show_customer_home_page()
        else:
            messagebox.showerror("Login failed", "Invalid username or password")

    def show_registration_window(self):
        """Displays the customer registration window."""
        self.clear_frame()
        self.current_frame = Frame(self.root, width=500, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        title_label = Label(
            self.current_frame,
            text="Customer Registration",
            font=('Arial', 40, 'bold'),
            fg='blue',
            bg='grey'
        )
        title_label.pack()

        self.entries = {}

        fields = {
            "first_name:" : "First Name:",
            "last_name:" : "Last Name:",
            "phone_no:" : "Phone No:",
            "username:" : "Username:",
            "password:" : "Password:",
            "address:" : "Address:",
            "email:" : "Email:"
            
        }

        #labels = ["First Name:", "Last Name:", "Phone No:", "Username:", "Password:"]
        for i, (key,text) in enumerate(fields.items()):
            label = Label(
                self.current_frame,
                text=text,
                font=('Arial', 20, 'bold'),
                fg='blue',
                bg='grey'
            )
            label.place(x=10, y=100 + i * 50)

            entry = Entry(self.current_frame, font=('Arial', 20))
            entry.place(x=200, y=100 + i * 50)

            self.entries[key] = entry

        register_button = Button(
            self.current_frame,
            text="Register",
            font=('Arial', 20, 'bold'),
            command=self.collect_registration_data
        )
        register_button.place(x=150, y=600)

        back_button = Button(
            self.current_frame,
            text="Back to login page",
            font=('Arial', 20, 'bold'),
            command=self.show_customer_window
        )
        back_button.place(x=500, y=600)

    def collect_registration_data(self):
        data = {key: entry.get() for key, entry in self.entries.items()}

        try:
            db = Database()
            db.register_customer(
                username= data.get('username:'),
                password= data.get('password:'),
                firstName= data.get('first_name:'),
                lastName= data.get('last_name:'),
                phoneNo= data.get('phone_no:'),
                address= data.get('address:'),
                email= data.get('email:')
            )
            messagebox.showinfo("Notice!!","Customer has been registered successfully")
        except Exception as e:
            messagebox.showerror("Notice!!", "Customer has not been registered ")

    def show_customer_home_page(self):
        """Displays the customer home page."""
        self.clear_frame()
        self.current_frame = Frame(self.root, width=500, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        title_label = Label(
            self.current_frame,
            text="HOME",
            font=('Arial', 40, 'bold'),
            fg='yellow',
            bg='grey'
        )
        title_label.pack()

        intro_label1 = Label(
            self.current_frame,
            text="Running Late?",
            font=('Arial', 20),
            fg='yellow',
            bg='grey'
        )
        intro_label1.place(x=150, y=150)

        intro_label2 = Label(
            self.current_frame,
            text="Book a taxi right now - easy and comfortable.",
            font=('Arial', 20),
            fg='yellow',
            bg='grey'
        )
        intro_label2.place(x=50, y=200)

        menu_options = ["HOME", "BOOKING", "PROFILE", "HISTORY", "CHANGE PASSWORD"]
        clicked = StringVar(value="Menu")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)

        logout_button = Button(
            self.current_frame,
            text='Logout',
            font=('Arial', 20, 'bold'),
            command=self.show_customer_window
        )
        
        logout_button.place(x=500, y=400)

    def page_picker(self,choice):
        if choice == "BOOKING":
            self.clear_frame()
            self.show_customer_booking_page()
        elif choice == "HOME":
            self.clear_frame()
            self.show_customer_home_page()
        elif choice == "PROFILE":
            self.clear_frame()
            self.show_profile_page()
        elif choice == "HISTORY":
            self.clear_frame()
            self.show_history_page()
        elif choice == "CHANGE PASSWORD":
            self.clear_frame()
            self.show_changePassword_page()





    def show_customer_booking_page(self):
        self.clear_frame()
        self.current_frame = Frame(self.root, width=700, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        title_label = Label(
            self.current_frame,
            text="Booking",
            font=('Arial', 40, 'bold'),
            fg='yellow',
            bg='grey'
        )
        title_label.pack()

        menu_options = ["HOME", "BOOKING", "PROFILE", "HISTORY", "CHANGE PASSWORD"]
        clicked = StringVar(value="Menu")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)

        self.entries = {}

        fields = {
            "pickup_address" : "Pickup Address:",
            "dropoff_address" : "Drop-off Address:",
            "pickup_time" : "Pickup Time:",
            "date" : "Date:"
        }


        #labels = ["Pickup Address :", "Drop-off Address:", "Pickup Time ", "Pickup Date:"]
        for i, (key,text) in enumerate(fields.items()):
            label = Label(
                self.current_frame,
                text=text,
                font=('Arial', 20, 'bold'),
                fg='yellow',
                bg='grey'
            )
            label.place(x=10, y=100 + i * 50)

            entry = Entry(self.current_frame, font=('Arial', 20))
            entry.place(x=200, y=100 + i * 50)

            self.entries[key] = entry

        self.Request_button = Button(
            self.current_frame,
            text='Request Booking', 
            command= self.make_booking
        )
        self.Request_button.place(x=150,y=350)
        self.Request_button.config(font=('Arial',20,'bold'))


        self.clear_button = Button(
            self.current_frame,
            text='CLEAR', 
            #command= self.open_driver_page
        )
        self.clear_button.place(x=150,y=400)
        self.clear_button.config(font=('Arial',20,'bold'))

        self.Update_button = Button(
            self.current_frame,
            text='Update Booking', 
            #command= self.open_driver_page
        )
        self.Update_button.place(x=370,y=350)
        self.Update_button.config(font=('Arial',20,'bold'))


        self.cancel_button = Button(
            self.current_frame,
            text='Cancel Booking', 
            #command= self.open_driver_page
        )
        self.cancel_button.place(x=370,y=400)
        self.cancel_button.config(font=('Arial',20,'bold'))


        self.table = ttk.Treeview(self.current_frame, columns= ('Booking_ID', 'Customer_ID','Driver_ID','Pick Address', 'Drop Address', 'Time', 'Date','Car Type'), show= 'headings')

        self.table.column("Booking_ID", width= 80)
        self.table.column("Customer_ID", width= 80)
        self.table.column("Driver_ID", width= 80)
        self.table.column("Pick Address", width= 160)
        self.table.column("Drop Address", width= 160)
        self.table.column("Time", width= 80)
        self.table.column("Date", width= 80)
        self.table.column("Car Type", width= 80)


        self.table.heading('Booking_ID', text='Booking_ID')
        self.table.heading('Customer_ID', text='Customer_ID')
        self.table.heading('Driver_ID', text='Driver_ID')
        self.table.heading('Pick Address', text='Pick Address')
        self.table.heading('Drop Address', text='Drop Address')
        self.table.heading('Time', text='Time')
        self.table.heading('Date', text='Date')
        self.table.heading('Car Type', text='Car Type')
        self.table.place(x=500, y = 100)

        self.populate_booking_treeview(customer_id= self.customer_id)

    def populate_booking_treeview(self, customer_id):
        for item in self.table.get_children():
            self.table.delete(item)


        db = Database()
        records = db.fetch_bookings_bycustomer(customer_id)


        for record in records:
            self.table.insert("","end", values = record)




    def make_booking(self):
        data = {key: entry.get() for key, entry in self.entries.items()}
        pick_up_add = data.get('pickup_address')
        drop_off_add = data.get('dropoff_address')
        time = data.get('pickup_time')
        date = data.get('date')

        try:
            db = Database()
            db.new_booking(
                customer_id = self.customer_id,
                pick_up_add= pick_up_add,
                drop_off_add= drop_off_add,
                time= time,
                date= date,
            )
            messagebox.showinfo("Notice!!","Booking has been made successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Booking was not made. Please try again. Error: {e}")


    
    def show_profile_page(self):
        self.clear_frame()
        self.current_frame = Frame(self.root, width=700, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        title_label = Label(
            self.current_frame,
            text="Edit Profile",
            font=('Arial', 40, 'bold'),
            fg='yellow',
            bg='grey'
        )
        title_label.pack()

        menu_options = ["HOME", "BOOKING", "PROFILE", "HISTORY", "CHANGE PASSWORD"]
        clicked = StringVar(value="Menu")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)

        self.entries = {}

        fields = {
        "first_name:": {"label": "First Name:", "x": 10, "y": 100},
        "last_name:": {"label": "Last Name:", "x": 10, "y": 150},
        "phone_no:": {"label": "Phone No:", "x": 10, "y": 200},
        "username:": {"label": "Username:", "x": 10, "y": 250},
        "address:": {"label": "Address:", "x": 500, "y": 100},
        "email:": {"label": "Email:", "x": 500, "y": 150},
    }

        #labels = ["First Name :", "Last Name:", "Phone No ", "Username:"]
        for key, field in fields.items():
            label = Label(
                self.current_frame,
                text=field["label"],
                font=('Arial', 20, 'bold'),
                fg='yellow',
                bg='grey'
            )
            label.place(x=field["x"], y=field["y"])

            entry = Entry(self.current_frame, font=('Arial', 20))
            #entry.place(x=200, y=100 + i * 50)



            entry = Entry(self.current_frame, font=('Arial', 20))
            entry.place(x=field["x"] + 200, y=field["y"])

            self.entries[key] = entry

        self.confirm_button = Button(
            self.current_frame,
            text='Confirm Edit', 
            command= lambda: self.confirm_profile_edit(self.customer_id)
            )
        self.confirm_button.place(x=370,y=350)
        self.confirm_button.config(font=('Arial',20,'bold'))


    def confirm_profile_edit(self,user_id):
        updated_data = {key: entry.get() for key, entry in self.entries.items()}

        try:
            db = Database()  
            db.update_customer_profile(
                user_id=self.customer_id,
                firstName=updated_data["first_name:"],
                lastName=updated_data["last_name:"],
                phoneNo=updated_data["phone_no:"],
                address=updated_data["address:"],
                email=updated_data["email:"]
            )
            messagebox.showinfo("Success", "Profile updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Profile update failed: {e}")


    def show_history_page(self):
        self.clear_frame()
        self.current_frame = Frame(self.root, width=700, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        title_label = Label(
            self.current_frame,
            text="History Page",
            font=('Arial', 40, 'bold'),
            fg='yellow',
            bg='grey'
        )
        title_label.pack()

        menu_options = ["HOME", "BOOKING", "PROFILE", "HISTORY", "CHANGE PASSWORD"]
        clicked = StringVar(value="Menu")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)



        self.historyTable = ttk.Treeview(self.current_frame, columns= ('Booking_ID', 'Customer_ID','Driver_ID','Pick Address', 'Drop Address', 'Time', 'Date','Car Type'), show= 'headings')

        self.historyTable.column("Booking_ID", width= 80)
        self.historyTable.column("Customer_ID", width= 80)
        self.historyTable.column("Driver_ID", width= 80)
        self.historyTable.column("Pick Address", width= 160)
        self.historyTable.column("Drop Address", width= 160)
        self.historyTable.column("Time", width= 80)
        self.historyTable.column("Date", width= 80)
        self.historyTable.column("Car Type", width= 80)


        self.historyTable.heading('Booking_ID', text='Booking_ID')
        self.historyTable.heading('Customer_ID', text='Customer_ID')
        self.historyTable.heading('Driver_ID', text='Driver_ID')
        self.historyTable.heading('Pick Address', text='Pick Address')
        self.historyTable.heading('Drop Address', text='Drop Address')
        self.historyTable.heading('Time', text='Time')
        self.historyTable.heading('Date', text='Date')
        self.historyTable.heading('Car Type', text='Car Type')
        self.historyTable.place(x=10, y = 150)

        self.populate_history_treeview(customer_id= self.customer_id)

    def populate_history_treeview(self, customer_id):
        for item in self.historyTable.get_children():
            self.historyTable.delete(item)


        db = Database()
        records = db.fetch_bookings_bycustomer(customer_id)


        for record in records:
            self.historyTable.insert("","end", values = record)

    def show_changePassword_page(self):
        self.clear_frame()
        self.current_frame = Frame(self.root, width=700, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)

        title_label = Label(
            self.current_frame,
            text="Change Password Page",
            font=('Arial', 40, 'bold'),
            fg='yellow',
            bg='grey'
        )
        title_label.pack()

        menu_options = ["HOME", "BOOKING", "PROFILE", "HISTORY", "CHANGE PASSWORD"]
        clicked = StringVar(value="Menu")
        menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
        menu_bar.config(font=('Arial', 16), pady=20)
        menu_bar.place(x=10, y=10)

        

        intro_label = Label(
            self.current_frame,
            text="Proceed below to change password",
            font=('Arial', 20),
            fg='yellow',
            bg='grey'
        )
        intro_label.place(x=150, y=70)

        self.entries = {}

        fields = {
        "old_password": {"label": "Old Password:", "y": 200},
        "new_password": {"label": "New Password:", "y": 250}
        }

        #labels = ["Old Password ", "New Password"]
        for key, field in fields.items():
            label = Label(
                self.current_frame,
                text=field["label"],
                font=('Arial', 20, 'bold'),
                fg='yellow',
                bg='grey'
            )
            label.place(x=10, y=field["y"])

            entry = Entry(self.current_frame, font=('Arial', 20))
            entry.place(x=200, y=field["y"])

            self.entries[key] = entry


            self.changePassword_button = Button(
            self.current_frame,
            text='Change Password', 
            command= self.change_password
            )


        self.changePassword_button.place(x=370,y=350)
        self.changePassword_button.config(font=('Arial',20,'bold'))

    #def register(self):

    def change_password(self):
    
        #old_password = self.entries.get["old_password"].get()
        new_password = self.entries["new_password"].get()

        try:
        
            db = Database()  
            db.update_password(self.customer_id, new_password)
            messagebox.showinfo("Success", "Password changed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to change password: {e}")
        

    





if __name__ == "__main__":
    root = Tk()
    app = CustomerWindow(root)
    root.mainloop()
