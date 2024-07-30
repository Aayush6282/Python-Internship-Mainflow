# A Simple Billing Software 

  import sqlite3
  import tkinter as tk
  from tkinter import ttk
  from tkinter import messagebox
  from datetime import datetime
  import reportlab.pdfgen.canvas
  import os
  
  def create_and_populate_database():
      conn = sqlite3.connect('billing.db')
      cursor = conn.cursor()
  
      # Create tables with updated names
      cursor.execute('''
      CREATE TABLE IF NOT EXISTS Customer (
          customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          address TEXT
      )''')
  
      cursor.execute('''
      CREATE TABLE IF NOT EXISTS Product (
          product_id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          price REAL NOT NULL
      )''')
  
      cursor.execute('''
      CREATE TABLE IF NOT EXISTS SalesTransaction (
          transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
          customer_id INTEGER,
          product_id INTEGER,
          quantity INTEGER,
          date TEXT,
          discount_id INTEGER,
          FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
          FOREIGN KEY (product_id) REFERENCES Product(product_id),
          FOREIGN KEY (discount_id) REFERENCES Discount(discount_id)
      )''')
  
      cursor.execute('''
      CREATE TABLE IF NOT EXISTS Discount (
          discount_id INTEGER PRIMARY KEY AUTOINCREMENT,
          code TEXT,
          value REAL
      )''')
  
      # Sample data
      products = [
          ('Milk', 1.20), ('Bread', 2.50), ('Eggs', 3.00), ('Butter', 4.50),
          ('Cheese', 5.00), ('Apples', 2.00), ('Oranges', 3.50), ('Rice', 1.80),
          ('Chicken', 7.00), ('Beef', 8.00), ('Pasta', 1.70), ('Tomatoes', 2.20),
          ('Potatoes', 1.50), ('Onions', 1.30), ('Garlic', 0.80), ('Sugar', 1.60),
          ('Flour', 1.90), ('Coffee', 3.20), ('Tea', 2.80), ('Juice', 2.40),
          ('Cereal', 3.50), ('Yogurt', 1.10), ('Ice Cream', 4.00), ('Chicken Breast', 6.50),
          ('Steak', 9.00), ('Fish', 5.50), ('Vegetables', 2.30), ('Fruit', 2.50),
          ('Cookies', 3.00), ('Chocolate', 1.90), ('Soft Drinks', 1.20), ('Water', 0.90),
          ('Beer', 4.20), ('Wine', 6.00), ('Spices', 2.60), ('Oils', 3.00),
          ('Sauces', 2.80), ('Canned Goods', 1.40), ('Frozen Foods', 3.10), ('Snacks', 2.20),
          ('Nuts', 4.00), ('Dairy', 3.30), ('Eggs', 2.50), ('Meat', 5.50)
      ]
  
      cursor.executemany('INSERT INTO Product (name, price) VALUES (?, ?)', products)
  
      # Close connection
      conn.commit()
      conn.close()
  
  def add_customer(name, address):
      conn = sqlite3.connect('billing.db')
      cursor = conn.cursor()
      cursor.execute('INSERT INTO Customer (name, address) VALUES (?, ?)', (name, address))
      conn.commit()
      conn.close()
  
  def add_product(name, price):
      conn = sqlite3.connect('billing.db')
      cursor = conn.cursor()
      cursor.execute('INSERT INTO Product (name, price) VALUES (?, ?)', (name, price))
      conn.commit()
      conn.close()
  
  def add_transaction(customer_id, product_id, quantity, discount_id=None):
      conn = sqlite3.connect('billing.db')
      cursor = conn.cursor()
      cursor.execute('''
      INSERT INTO SalesTransaction (customer_id, product_id, quantity, date, discount_id)
      VALUES (?, ?, ?, ?, ?)
      ''', (customer_id, product_id, quantity, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), discount_id))
      conn.commit()
      conn.close()
  
  def generate_invoice(transaction_id):
      conn = sqlite3.connect('billing.db')
      cursor = conn.cursor()
      cursor.execute('''
      SELECT t.transaction_id, c.name, c.address, t.date, p.name, p.price, t.quantity
      FROM SalesTransaction t
      JOIN Customer c ON t.customer_id = c.customer_id
      JOIN Product p ON t.product_id = p.product_id
      WHERE t.transaction_id = ?
      ''', (transaction_id,))
      transaction = cursor.fetchone()
  
      if not transaction:
          messagebox.showerror("Error", "Transaction not found.")
          return
  
      transaction_id, customer_name, customer_address, date, product_name, product_price, quantity = transaction
  
      total_amount = product_price * quantity
  
      # Generate PDF invoice
      file_path = "invoice.pdf"
      canvas = reportlab.pdfgen.canvas.Canvas(file_path)
      canvas.drawString(100, 750, f"Invoice ID: {transaction_id}")
      canvas.drawString(100, 730, f"Customer: {customer_name}")
      canvas.drawString(100, 710, f"Address: {customer_address}")
      canvas.drawString(100, 690, f"Date: {date}")
      canvas.drawString(100, 670, f"Product: {product_name}")
      canvas.drawString(100, 650, f"Price: ${product_price:.2f}")
      canvas.drawString(100, 630, f"Quantity: {quantity}")
      canvas.drawString(100, 610, f"Total Amount: ${total_amount:.2f}")
  
      canvas.save()
      messagebox.showinfo("Success", f"Invoice generated and saved as {file_path}.")
      conn.close()
  
  def view_transactions():
      conn = sqlite3.connect('billing.db')
      cursor = conn.cursor()
      cursor.execute('''
      SELECT t.transaction_id, c.name, p.name, t.quantity, t.date
      FROM SalesTransaction t
      JOIN Customer c ON t.customer_id = c.customer_id
      JOIN Product p ON t.product_id = p.product_id
      ''')
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
  
  def create_gui():
      root = tk.Tk()
      root.title("Billing Software")
  
      main_frame = ttk.Frame(root, padding=(10, 5))
      main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
  
      # Customer Management
      customer_frame = ttk.Labelframe(main_frame, text="Manage Customers", padding=(10, 5))
      customer_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
  
      tk.Label(customer_frame, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
      customer_name_entry = tk.Entry(customer_frame, width=40)
      customer_name_entry.grid(row=0, column=1, padx=5, pady=5)
  
      tk.Label(customer_frame, text="Address:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
      customer_address_entry = tk.Entry(customer_frame, width=40)
      customer_address_entry.grid(row=1, column=1, padx=5, pady=5)
  
      def add_customer_command():
          name = customer_name_entry.get()
          address = customer_address_entry.get()
          if name:
              add_customer(name, address)
          else:
              messagebox.showerror("Error", "Customer name is required.")
  
      tk.Button(customer_frame, text="Add Customer", command=add_customer_command).grid(row=2, column=1, pady=10)
  
      # Product Management
      product_frame = ttk.Labelframe(main_frame, text="Manage Products", padding=(10, 5))
      product_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
  
      tk.Label(product_frame, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
      product_name_entry = tk.Entry(product_frame, width=40)
      product_name_entry.grid(row=0, column=1, padx=5, pady=5)
  
      tk.Label(product_frame, text="Price:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
      product_price_entry = tk.Entry(product_frame, width=40)
      product_price_entry.grid(row=1, column=1, padx=5, pady=5)
  
      def add_product_command():
          name = product_name_entry.get()
          price = product_price_entry.get()
          if name and price:
              try:
                  price = float(price)
                  add_product(name, price)
              except ValueError:
                  messagebox.showerror("Error", "Price must be a number.")
          else:
              messagebox.showerror("Error", "Product name and price are required.")
  
      tk.Button(product_frame, text="Add Product", command=add_product_command).grid(row=2, column=1, pady=10)
  
      # Transaction Management
      transaction_frame = ttk.Labelframe(main_frame, text="Manage Transactions", padding=(10, 5))
      transaction_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
  
      tk.Label(transaction_frame, text="Customer:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
      customer_combobox = ttk.Combobox(transaction_frame)
      customer_combobox.grid(row=0, column=1, padx=5, pady=5)
  
      tk.Label(transaction_frame, text="Product:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
      product_combobox = ttk.Combobox(transaction_frame)
      product_combobox.grid(row=1, column=1, padx=5, pady=5)
  
      tk.Label(transaction_frame, text="Quantity:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
      quantity_entry = tk.Entry(transaction_frame, width=10)
      quantity_entry.grid(row=2, column=1, padx=5, pady=5)
  
      def add_transaction_command():
          customer_id = customer_combobox.get()
          product_id = product_combobox.get()
          quantity = quantity_entry.get()
          if customer_id and product_id and quantity:
              try:
                  quantity = int(quantity)
                  add_transaction(customer_id, product_id, quantity)
                  messagebox.showinfo("Success", "Transaction added successfully.")
              except ValueError:
                  messagebox.showerror("Error", "Quantity must be a number.")
          else:
              messagebox.showerror("Error", "All fields are required.")
  
      tk.Button(transaction_frame, text="Add Transaction", command=add_transaction_command).grid(row=3, column=1, pady=10)
  
      # Invoice Management
      invoice_frame = ttk.Labelframe(main_frame, text="Generate Invoice", padding=(10, 5))
      invoice_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
  
      tk.Label(invoice_frame, text="Transaction ID:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
      invoice_transaction_id_entry = tk.Entry(invoice_frame, width=20)
      invoice_transaction_id_entry.grid(row=0, column=1, padx=5, pady=5)
  
      def generate_invoice_command():
          transaction_id = invoice_transaction_id_entry.get()
          if transaction_id:
              generate_invoice(transaction_id)
          else:
              messagebox.showerror("Error", "Transaction ID is required.")
  
      tk.Button(invoice_frame, text="Generate Invoice", command=generate_invoice_command).grid(row=1, column=1, pady=10)
  
      # View Transactions
      tk.Button(main_frame, text="View Transactions", command=view_transactions).grid(row=3, column=0, columnspan=2, pady=10)
  
      root.mainloop()
  
  # Create database and GUI
  create_and_populate_database()
  create_gui()
