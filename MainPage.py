from tkinter import *
from CustomerPage import CustomerWindow
from AdminPage import adminWindow
from DriverPage import DriverWindow


class MainWindow():
    def __init__(self,root):

        self.root = root
        self.root.geometry("700x600")
        self.root.title("Taxi Booking System")
        self.current_frame = None
        self.show_main_window()




    def clear_frame(self):
        """Clears the current frame."""
        if self.current_frame:
            self.current_frame.destroy()



    def show_main_window(self):
        self.current_frame =Frame(root, width=500, height=500, bg="grey")
        self.current_frame.pack(fill="both", expand=1)


        titleLabel = Label(
            self.current_frame,
            text="Welcome to Taxi Booking System",
            font=('Arial',40 ,'bold'),
            fg='blue',
            bg= 'grey'
        )
        titleLabel.pack()

        self.usertypeLabel = Label(
            self.current_frame,
            text="Select User Type",
            font=('Arial',40 ,'bold'),
            fg='blue',
            bg= 'grey'
        )
        self.usertypeLabel.place(x=100,y=100)

        self.custButton = Button(
            self.current_frame,
            text='Customer', 
            command= self.open_customer_page
        )
        self.custButton.place(x=200,y=200)
        self.custButton.config(font=('Arial',40,'bold'))

        self.adminButton = Button(
            self.current_frame,
            text='Admin', 
            command= self.open_admin_page
        )
        self.adminButton.config(font=('Arial',40,'bold'))
        #adminButton.config(bg='#77e349')
        self.adminButton.place(x=200,y=300)


        self.driverButton = Button(
            self.current_frame,
            text='Driver', 
            command= self.open_driver_page
        )
        self.driverButton.place(x=200,y=400)
        self.driverButton.config(font=('Arial',40,'bold'))


    def open_customer_page(self):
        self.clear_frame()
        CustomerWindow(self.root)


    def open_admin_page(self):
        self.clear_frame()
        adminWindow(self.root)
 

    def open_driver_page(self):
        self.clear_frame()
        DriverWindow(self.root)




   
  
if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()