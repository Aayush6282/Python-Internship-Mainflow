import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch exchange rates from an API
def fetch_exchange_rates():
    try:
        # URL of the exchange rate API
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        return data['rates']
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch exchange rates: {e}")
        return None

# Function to convert USD to selected currency
def convert_currency():
    try:
        usd_amount = float(entry_usd.get())
        selected_currency = variable.get()
        conversion_rate = exchange_rates[selected_currency]
        converted_amount = usd_amount * conversion_rate
        label_result.config(text=f"{usd_amount:.2f} USD = {converted_amount:.2f} {selected_currency}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")
    except KeyError:
        messagebox.showerror("Error", "Failed to fetch the conversion rate")

# Fetch exchange rates at the start of the program
exchange_rates = fetch_exchange_rates()

# Check if exchange rates were fetched successfully
if exchange_rates:
    # Get the list of available currencies
    currency_options = list(exchange_rates.keys())

    # Create the main window
    root = tk.Tk()
    root.title("USD Currency Converter")

    # Create and place the widgets
    label_usd = tk.Label(root, text="Amount in USD:")
    label_usd.grid(row=0, column=0, padx=10, pady=10)

    entry_usd = tk.Entry(root)
    entry_usd.grid(row=0, column=1, padx=10, pady=10)

    label_currency = tk.Label(root, text="Convert to:")
    label_currency.grid(row=1, column=0, padx=10, pady=10)

    variable = tk.StringVar(root)
    variable.set(currency_options[0])  # Set default currency

    dropdown_currency = tk.OptionMenu(root, variable, *currency_options)
    dropdown_currency.grid(row=1, column=1, padx=10, pady=10)

    button_convert = tk.Button(root, text="Convert", command=convert_currency)
    button_convert.grid(row=2, column=0, columnspan=2, pady=20)

    label_result = tk.Label(root, text="")
    label_result.grid(row=3, column=0, columnspan=2, pady=10)

    # Start the main event loop
    root.mainloop()
else:
    messagebox.showerror("Error", "Unable to start the application without exchange rates.")
