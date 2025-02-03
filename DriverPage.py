from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DatabaseConnection import Database


class DriverWindow:
    def __init__(self, root):
      self.root = root
      self.root.geometry("1000x500")
      self.root.title("Taxi Booking System")
      self.current_frame = None
      self.show_driver_window()


    def clear_frame(self):
         if self.current_frame:
            self.current_frame.destroy()


    def show_driver_window(self):
         self.clear_frame()
         self.current_frame =Frame(self.root, width=1000, height=500, bg="grey")
         self.current_frame.pack(fill="both", expand=1)

         titleLabel = Label(
            self.current_frame,
            text="Driver Page",
            font=('Arial',40 ,'bold'),
            fg='blue',
            bg= 'grey'
         )
         titleLabel.pack()

         driver_id_label = Label(
            self.current_frame,
            text="Username :",
            font=('Arial',20 ,'bold'),
            fg='blue',
            bg= 'grey'
         )
         driver_id_label.place(x=10,y=50)

         self.driver_username_entry = Entry(self.current_frame)
         self.driver_username_entry.config(font=('Arial',20))
         self.driver_username_entry.place(x=130,y=50)

         passwordLabel = Label(
          self.current_frame,
            text="Password :",
            font=('Arial',20 ,'bold'),
            fg='blue',
            bg= 'grey'
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

         entered_username = self.driver_username_entry.get()
         entered_password = self.passwordEntry.get()
        
         db = Database()
         user = db.driver_login(username = entered_username, password = entered_password)

         if user:
            driver_id = user[0]
            self.driver_id = driver_id
            self.show_dashboard()
         else:
            messagebox.showerror("Login failed", "Invalid username or password")



    def page_picker(self,choice):
      if choice == "HOME":
            self.clear_frame()
            self.show_dashboard()
      elif choice == "PROFILE":
            self.clear_frame()
            self.show_profile()
      elif choice == "HISTORY":
            self.clear_frame()
            self.show_history()




    



    def show_dashboard(self):
         """Displays the Driver Dashboard."""
         self.clear_frame()
         self.current_frame = Frame(self.root, width=1000, height=500, bg="grey")
         self.current_frame.pack(fill="both", expand=1)

        # Dashboard Title
         title_label = Label(
            self.current_frame,
            text="Driver Dashboard",
            font=('Arial', 40, 'bold'),
            fg='white',
            bg='blue'
         )
         title_label.pack()

         menu_options = ["HOME","PROFILE", "HISTORY"]
         clicked = StringVar(value="HOME")
         menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
         menu_bar.config(font=('Arial', 16), pady=20)
         menu_bar.place(x=10, y=10)


         intro_label = Label(
            self.current_frame,
            text="Assigned Customer :",
            font=('Arial', 10),
            fg='white',
            bg='grey'
         )
         intro_label.place(x= 20, y=100)

         intro_label2 = Label(
            self.current_frame,
            text="Name :",
            font=('Arial', 15),
            fg='white',
            bg='grey'
         )
         intro_label2.place(x= 20, y=150)

         intro_label3 = Label(
            self.current_frame,
            text="Email :",
            font=('Arial', 15),
            fg='white',
            bg='grey'
         )
         intro_label3.place(x= 20, y=200)

         intro_label4 = Label(
            self.current_frame,
            text="Phone Number :",
            font=('Arial', 15),
            fg='white',
            bg='grey'
         )
         intro_label4.place(x= 500, y=150)

       
         logout_button = Button(
               self.current_frame,
               text='Logout',
               font=('Arial', 20, 'bold'),
               command=self.show_driver_window
         )
         logout_button.place(x=500, y=400)


    def show_profile(self):
         """Displays the Driver Dashboard."""
         self.clear_frame()
         self.current_frame = Frame(self.root, width=1000, height=500, bg="grey")
         self.current_frame.pack(fill="both", expand=1)

        # Dashboard Title
         title_label = Label(
            self.current_frame,
            text="Edit Profile",
            font=('Arial', 40, 'bold'),
            fg='white',
            bg='grey'
         )
         title_label.pack()

         menu_options = ["HOME","PROFILE", "HISTORY"]
         clicked = StringVar(value="HOME")
         menu_bar = OptionMenu(self.current_frame, clicked, *menu_options,command= self.page_picker)
         menu_bar.config(font=('Arial', 16), pady=20)
         menu_bar.place(x=10, y=10)


         self.entries = {}

         fields = {
         "first_name:": {"label": "First Name:", "x": 10, "y": 100},
         "last_name:": {"label": "Last Name:", "x": 10, "y": 150},
         "phone_no:": {"label": "Phone No:", "x": 10, "y": 200},
         "Car Type:": {"label": "Car Type:", "x": 10, "y": 250},
         }


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
            



            entry = Entry(self.current_frame, font=('Arial', 20))
            entry.place(x=field["x"] + 200, y=field["y"])

            self.entries[key] = entry

         self.confirm_button = Button(
            self.current_frame,
            text='Confirm Edit', 
            command= lambda: self.confirm_profile_edit(self.driver_id)
            )
         self.confirm_button.place(x=370,y=350)
         self.confirm_button.config(font=('Arial',20,'bold'))


    def confirm_profile_edit(self,driver_id):
        updated_data = {key: entry.get() for key, entry in self.entries.items()}

        try:
            db = Database()  
            db.update_driver_profile(
                driver_id=self.driver_id,
                first_name=updated_data["first_name:"],
                last_name=updated_data["last_name:"],
                phone_no=updated_data["phone_no:"],
                car_type=updated_data["Car Type:"]
            )
            messagebox.showinfo("Success", "Profile updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Profile update failed: {e}")


    def show_history(self):
         """Displays the Driver Dashboard."""
         self.clear_frame()
         self.current_frame = Frame(self.root, width=1000, height=500, bg="grey")
         self.current_frame.pack(fill="both", expand=1)

        # Dashboard Title
         title_label = Label(
            self.current_frame,
            text="Previous Bookings",
            font=('Arial', 40, 'bold'),
            fg='white',
            bg='grey'
         )
         title_label.pack()

         menu_options = ["HOME","PROFILE", "HISTORY"]
         clicked = StringVar(value="HOME")
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
         self.populate_history_treeview(customer_id= self.driver_id)

    def populate_history_treeview(self, driver_id):
        for item in self.historyTable.get_children():
            self.historyTable.delete(item)


        db = Database()
        records = db.fetch_bookings_bydriver(driver_id)


        for record in records:
            self.historyTable.insert("","end", values = record)
   


# Main Application Loop
if __name__ == "__main__":
    root = Tk()
    app = DriverWindow(root)
    root.mainloop()
    