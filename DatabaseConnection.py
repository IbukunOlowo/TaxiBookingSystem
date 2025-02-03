#from tkinter.tix import LabelFrame
import sqlite3
from tkinter import *



class Database:
    def __init__(self, db_name="tbs.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def connect(self):
       
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        
        if self.connection:
            self.connection.close()
        self.connection = None
        self.cursor = None

    def create_tables(self):
        try:
            self.connect()  

            query = """CREATE TABLE IF NOT EXISTS customers(
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT,
                        firstName TEXT,
                        lastName TEXT,
                        phoneNO INTEGER,
                        address TEXT,
                        email VARCHAR(50)
                    )"""
            query2 = """CREATE TABLE IF NOT EXISTS bookings(
                        booking_id INTEGER PRIMARY KEY,
                        customer_id INTEGER,
                        driver_id INTEGER,
                        pick_up_add TEXT,
                        drop_off_add TEXT,
                        date TEXT,
                        time TEXT,
                        car_type TEXT,
                        FOREIGN KEY (customer_id) REFERENCES customers (user_id)
                    )"""
            query3 = """CREATE TABLE IF NOT EXISTS drivers(
                        driver_id INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        phone_no INTEGER,
                        car_type TEXT)"""
            query4 = """CREATE TABLE IF NOT EXISTS admin(
                        admin_id INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT)"""
            
            self.cursor.execute(query)
            self.cursor.execute(query2)
            self.cursor.execute(query3)
            self.cursor.execute(query4)
            self.connection.commit()
        
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            raise
        
        finally:
            self.close()  

    def register_customer(self, username, password, firstName, lastName, phoneNo, address, email):
        try:
            self.connect()  
            query = """INSERT INTO customers(username, password, firstName, lastName, phoneNO, address, email)
                        VALUES(?, ?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(query, (username, password, firstName, lastName, phoneNo, address, email))
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error registering customer: {e}")
            raise

        finally:
            self.close()  

    def register_admin(self, username, password):
        try:
            self.connect()  
            query = """INSERT INTO admin(username, password) VALUES(?, ?)"""
            self.cursor.execute(query, (username, password))
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error registering admin: {e}")
            raise

        finally:
            self.close()  

    def fetch_customer(self):
        try:
            self.connect()  
            query = "SELECT * FROM customers"
            self.cursor.execute(query)
            customers = self.cursor.fetchall()
            return customers

        except sqlite3.Error as e:
            print(f"Error fetching customers: {e}")
            raise

        finally:
            self.close()  

    def fetch_bookings_bycustomer(self, customer_id):
        try:
            self.connect()  
            query = "SELECT * FROM bookings WHERE customer_id = ?"
            self.cursor.execute(query, (customer_id,))
            bookings = self.cursor.fetchall()
            return bookings

        except sqlite3.Error as e:
            print(f"Error fetching bookings: {e}")
            raise

        finally:
            self.close()  

    def fetch_bookings_bydriver(self, driver_id):
        try:
            self.connect()  
            query = "SELECT * FROM bookings WHERE driver_id = ?"
            self.cursor.execute(query, (driver_id,))
            bookings = self.cursor.fetchall()
            return bookings

        except sqlite3.Error as e:
            print(f"Error fetching bookings: {e}")
            raise

        finally:
            self.close()  

    def update_driver_profile(self, driver_id, first_name, last_name, phone_no, car_type):
        try:
            self.connect()  
            query = """UPDATE drivers SET first_name = ?, last_name = ?, phone_no = ?, car_type = ?
                       WHERE driver_id = ?"""
            self.cursor.execute(query, (first_name, last_name, phone_no, car_type,driver_id))
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error updating customer profile: {e}")
            raise

        finally:
            self.close()  

    def update_customer_profile(self, user_id, firstName, lastName, phoneNo, address, email):
        try:
            self.connect()  
            query = """UPDATE customers SET firstName = ?, lastName = ?, phoneNo = ?, address = ?, email = ?
                       WHERE user_id = ?"""
            self.cursor.execute(query, (firstName, lastName, phoneNo, address, email, user_id))
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error updating customer profile: {e}")
            raise

        finally:
            self.close()  

    def update_password(self, user_id, password):
        try:
            self.connect()  
            query = """UPDATE customers SET password = ? WHERE user_id = ?"""
            self.cursor.execute(query, (password, user_id))
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error updating password: {e}")
            raise

        finally:
            self.close() 

    def login(self, username, password):
        try:
            self.connect()  
            query = "SELECT * FROM customers WHERE username = ? AND password = ?"
            self.cursor.execute(query, (username, password))
            user = self.cursor.fetchone()
            return user

        except sqlite3.Error as e:
            print(f"Error during login: {e}")
            raise

        finally:
            self.close() 
    def admin_login(self, username, password):
        try:
            self.connect()  
            query = "SELECT * FROM admin WHERE username = ? AND password = ?"
            self.cursor.execute(query, (username, password))
            user = self.cursor.fetchone()
            return user

        except sqlite3.Error as e:
            print(f"Error during admin login: {e}")
            raise

        finally:
            self.close()  

    def driver_login(self, username, password):
        try:
            self.connect()  # Open a connection
            query = "SELECT * FROM drivers WHERE username = ? AND password = ?"
            self.cursor.execute(query, (username, password))
            user = self.cursor.fetchone()
            return user

        except sqlite3.Error as e:
            print(f"Error during driver login: {e}")
            raise

        finally:
            self.close()  

    def fetch_drivers(self):
        try:
            self.connect()  
            query = "SELECT * FROM drivers"
            self.cursor.execute(query)
            drivers = self.cursor.fetchall()
            return drivers

        except sqlite3.Error as e:
            print(f"Error fetching drivers: {e}")
            raise

        finally:
            self.close() 

    def fetch_all_bookings(self):
        try:
            self.connect() 
            query = "SELECT * FROM bookings"
            self.cursor.execute(query)
            bookings = self.cursor.fetchall()
            return bookings

        except sqlite3.Error as e:
            print(f"Error fetching all bookings: {e}")
            raise

        finally:
            self.close() 

    def assign_driver(self, driver_id, car_type, customer_id):
        try:
            self.connect()  # Open a connection
            query = "UPDATE bookings SET driver_id = ?, car_type = ? WHERE customer_id = ?"
            self.cursor.execute(query, (driver_id, car_type, customer_id))
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error assigning driver: {e}")
            raise

        finally:
            self.close() 

    def new_booking(self, customer_id, pick_up_add, drop_off_add, time, date):
        try:
            self.connect() 
            query = """INSERT INTO bookings (customer_id, pick_up_add, drop_off_add, time, date)
                    VALUES (?, ?, ?, ?, ?)"""
            self.cursor.execute(query, (customer_id, pick_up_add, drop_off_add, time, date))
            self.connection.commit()  

        except sqlite3.Error as e:
            print(f"Error creating new booking: {e}")
            raise  

        finally:
            self.close()  