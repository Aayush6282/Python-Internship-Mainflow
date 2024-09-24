import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from reportlab.pdfgen import canvas
import os
import matplotlib.pyplot as plt

# Database setup
def create_and_populate_database():
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT,
                        role TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
                        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        address TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Product (
                        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        stock INTEGER DEFAULT 0)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS SalesTransaction (
                        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        date TEXT,
                        discount_id INTEGER,
                        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
                        FOREIGN KEY (product_id) REFERENCES Product(product_id),
                        FOREIGN KEY (discount_id) REFERENCES Discount(discount_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Discount (
                        discount_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        code TEXT,
                        value REAL)''')

    # Sample data
    products = [
        ('Milk', 1.20, 100), ('Bread', 2.50, 50), ('Eggs', 3.00, 200),
        ('Butter', 4.50, 150), ('Cheese', 5.00, 80)
    ]
    cursor.executemany('INSERT INTO Product (name, price, stock) VALUES (?, ?, ?)', products)

    # Sample user for authentication
    cursor.execute('INSERT OR IGNORE INTO User (username, password, role) VALUES (?, ?, ?)', ('admin', 'admin123', 'admin'))

    conn.commit()
    conn.close()

# User authentication
def authenticate_user(username, password):
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT role FROM User WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user[0] if user else None

# Function to create new user
def create_user(username, password, role):
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO User (username, password, role) VALUES (?, ?, ?)', (username, password, role))
    conn.commit()
    conn.close()

# Add customer
def add_customer(name, address):
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Customer (name, address) VALUES (?, ?)', (name, address))
    conn.commit()
    conn.close()

# Add product
def add_product(name, price, stock):
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Product (name, price, stock) VALUES (?, ?, ?)', (name, price, stock))
    conn.commit()
    conn.close()

# Add transaction
def add_transaction(customer_id, product_id, quantity, discount_id=None):
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO SalesTransaction (customer_id, product_id, quantity, date, discount_id) VALUES (?, ?, ?, ?, ?)', 
                   (customer_id, product_id, quantity, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), discount_id))
    conn.commit()

    # Update stock
    cursor.execute('UPDATE Product SET stock = stock - ? WHERE product_id = ?', (quantity, product_id))
    conn.commit()
    conn.close()

# Generate invoice
def generate_invoice(transaction_id):
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT t.transaction_id, c.name, c.address, t.date, p.name, p.price, t.quantity
                      FROM SalesTransaction t
                      JOIN Customer c ON t.customer_id = c.customer_id
                      JOIN Product p ON t.product_id = p.product_id
                      WHERE t.transaction_id = ?''', (transaction_id,))
    transaction = cursor.fetchone()

    if not transaction:
        messagebox.showerror("Error", "Transaction not found.")
        return

    transaction_id, customer_name, customer_address, date, product_name, product_price, quantity = transaction
    total_amount = product_price * quantity

    # Generate PDF invoice
    file_path = "invoice.pdf"
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, f"Invoice ID: {transaction_id}")
    c.drawString(100, 730, f"Customer: {customer_name}")
    c.drawString(100, 710, f"Address: {customer_address}")
    c.drawString(100, 690, f"Date: {date}")
    c.drawString(100, 670, f"Product: {product_name}")
    c.drawString(100, 650, f"Price: ${product_price:.2f}")
    c.drawString(100, 630, f"Quantity: {quantity}")
    c.drawString(100, 610, f"Total Amount: ${total_amount:.2f}")

    c.save()
    messagebox.showinfo("Success", f"Invoice generated and saved as {file_path}.")
    conn.close()

# View transactions
def view_transactions():
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT t.transaction_id, c.name, p.name, t.quantity, t.date
                      FROM SalesTransaction t
                      JOIN Customer c ON t.customer_id = c.customer_id
                      JOIN Product p ON t.product_id = p.product_id''')
    transactions = cursor.fetchall()
    conn.close()

    transaction_window = tk.Toplevel()
    transaction_window.title("View Transactions")

    columns = ("transaction_id", "customer", "product", "quantity", "date")
    tree = ttk.Treeview(transaction_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col.capitalize())
    tree.pack(expand=True, fill=tk.BOTH)

    for transaction in transactions:
        tree.insert("", tk.END, values=transaction)

# Search for customers
def search_customers(name):
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customer WHERE name LIKE ?', ('%' + name + '%',))
    customers = cursor.fetchall()
    conn.close()
    return customers

# Generate Sales Report
def generate_sales_report():
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT p.name, SUM(t.quantity) AS total_quantity, SUM(t.quantity * p.price) AS total_sales
                      FROM SalesTransaction t
                      JOIN Product p ON t.product_id = p.product_id
                      GROUP BY p.name''')
    report = cursor.fetchall()
    conn.close()

    plt.bar([x[0] for x in report], [x[1] for x in report])
    plt.title('Total Sales Quantity')
    plt.xlabel('Product')
    plt.ylabel('Quantity Sold')
    plt.show()

# Create GUI
def create_gui():
    root = tk.Tk()
    root.title("Billing Software")

    main_frame = ttk.Frame(root, padding=(10, 5))
    main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # User Authentication Frame
    auth_frame = ttk.Labelframe(main_frame, text="User Login", padding=(10, 5))
    auth_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    tk.Label(auth_frame, text="Username:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    username_entry = tk.Entry(auth_frame, width=20)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(auth_frame, text="Password:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    password_entry = tk.Entry(auth_frame, show="*", width=20)
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    def login_command():
        username = username_entry.get()
        password = password_entry.get()
        role = authenticate_user(username, password)
        if role:
            messagebox.showinfo("Success", f"Welcome {role}!")
            auth_frame.grid_remove()  # Hide auth frame
            create_main_interface()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    tk.Button(auth_frame, text="Login", command=login_command).grid(row=2, column=1, pady=10)

    def create_main_interface():
        # Create a new frame for main interface
        main_interface_frame = ttk.Labelframe(main_frame, text="Main Interface", padding=(10, 5))
        main_interface_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Add customer
        tk.Label(main_interface_frame, text="Customer Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        customer_name_entry = tk.Entry(main_interface_frame, width=20)
        customer_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(main_interface_frame, text="Customer Address:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        customer_address_entry = tk.Entry(main_interface_frame, width=20)
        customer_address_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(main_interface_frame, text="Add Customer", command=lambda: add_customer(customer_name_entry.get(), customer_address_entry.get())).grid(row=2, column=1, pady=10)

        # Add product
        tk.Label(main_interface_frame, text="Product Name:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        product_name_entry = tk.Entry(main_interface_frame, width=20)
        product_name_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(main_interface_frame, text="Product Price:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        product_price_entry = tk.Entry(main_interface_frame, width=20)
        product_price_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(main_interface_frame, text="Product Stock:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        product_stock_entry = tk.Entry(main_interface_frame, width=20)
        product_stock_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Button(main_interface_frame, text="Add Product", command=lambda: add_product(product_name_entry.get(), float(product_price_entry.get()), int(product_stock_entry.get()))).grid(row=6, column=1, pady=10)

        # Add transaction
        tk.Label(main_interface_frame, text="Customer ID:").grid(row=7, column=0, sticky="w", padx=5, pady=5)
        customer_id_entry = tk.Entry(main_interface_frame, width=20)
        customer_id_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(main_interface_frame, text="Product ID:").grid(row=8, column=0, sticky="w", padx=5, pady=5)
        product_id_entry = tk.Entry(main_interface_frame, width=20)
        product_id_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(main_interface_frame, text="Quantity:").grid(row=9, column=0, sticky="w", padx=5, pady=5)
        quantity_entry = tk.Entry(main_interface_frame, width=20)
        quantity_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Button(main_interface_frame, text="Add Transaction", command=lambda: add_transaction(int(customer_id_entry.get()), int(product_id_entry.get()), int(quantity_entry.get()))).grid(row=10, column=1, pady=10)

        # View transactions
        tk.Button(main_interface_frame, text="View Transactions", command=view_transactions).grid(row=11, column=1, pady=10)

        # Generate Sales Report
        tk.Button(main_interface_frame, text="Generate Sales Report", command=generate_sales_report).grid(row=12, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_and_populate_database()
    create_gui()
