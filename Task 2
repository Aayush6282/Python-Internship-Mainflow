import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import requests
import plotly.express as px
from sklearn.linear_model import LinearRegression

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Data Analysis Tool")
        self.df = pd.DataFrame()
        self.conn = None

        # Create GUI buttons
        self.load_button = tk.Button(root, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=5)

        self.filter_button = tk.Button(root, text="Filter Data", command=self.filter_data, state=tk.DISABLED)
        self.filter_button.pack(pady=5)

        self.sort_button = tk.Button(root, text="Sort Data", command=self.sort_data, state=tk.DISABLED)
        self.sort_button.pack(pady=5)

        self.group_button = tk.Button(root, text="Group Data", command=self.group_data, state=tk.DISABLED)
        self.group_button.pack(pady=5)

        self.visualize_button = tk.Button(root, text="Visualize Data", command=self.visualize_data, state=tk.DISABLED)
        self.visualize_button.pack(pady=5)

        self.api_button = tk.Button(root, text="Fetch Weather Data", command=self.fetch_weather_data)
        self.api_button.pack(pady=5)

        self.ml_button = tk.Button(root, text="Run Regression Analysis", command=self.perform_regression, state=tk.DISABLED)
        self.ml_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Data", command=self.save_data, state=tk.DISABLED)
        self.save_button.pack(pady=5)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.df.fillna('', inplace=True)
                self.filter_button.config(state=tk.NORMAL)
                self.sort_button.config(state=tk.NORMAL)
                self.group_button.config(state=tk.NORMAL)
                self.visualize_button.config(state=tk.NORMAL)
                self.ml_button.config(state=tk.NORMAL)
                self.save_button.config(state=tk.NORMAL)
                messagebox.showinfo("Success", "CSV file loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading CSV file: {e}")

    def filter_data(self):
        filter_column = simpledialog.askstring("Filter", "Enter column to filter by:")
        filter_value = simpledialog.askstring("Filter", f"Enter value to filter by in {filter_column}:")
        if filter_column in self.df.columns:
            self.df = self.df[self.df[filter_column] == filter_value]
            messagebox.showinfo("Filtered Data", f"Filtered data contains {len(self.df)} records.")
        else:
            messagebox.showerror("Error", "Column not found!")

    def sort_data(self):
        sort_column = simpledialog.askstring("Sort", "Enter column to sort by:")
        sort_order = simpledialog.askstring("Sort", "Enter sort order (asc/desc):")
        if sort_column in self.df.columns:
            ascending = sort_order.lower() == 'asc'
            self.df = self.df.sort_values(by=sort_column, ascending=ascending)
            messagebox.showinfo("Sorted Data", "Data sorted successfully!")
        else:
            messagebox.showerror("Error", "Column not found!")

    def group_data(self):
        group_column = simpledialog.askstring("Group", "Enter column to group by:")
        agg_column = simpledialog.askstring("Group", "Enter column for aggregation:")
        if group_column in self.df.columns and agg_column in self.df.columns:
            self.df = self.df.groupby(group_column)[agg_column].mean().reset_index()
            messagebox.showinfo("Grouped Data", f"Grouped data with {len(self.df)} groups.")
        else:
            messagebox.showerror("Error", "Column not found!")

    def visualize_data(self):
        column_to_plot = simpledialog.askstring("Visualize", "Enter column to visualize:")
        if column_to_plot in self.df.columns:
            fig = px.bar(self.df, x=column_to_plot, y=self.df.columns[1], title=f'{column_to_plot} Distribution')
            fig.show()
        else:
            messagebox.showerror("Error", "Column not found!")

    def fetch_weather_data(self):
        city = simpledialog.askstring("Weather Data", "Enter the city name:")
        if city:
            api_key = "YOUR_API_KEY"  # Replace with your actual API key from openweathermap.org
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
                weather_desc = data['weather'][0]['description']
                messagebox.showinfo("Weather Data", f"Temperature: {temp:.2f}°C\nCondition: {weather_desc}")
            else:
                messagebox.showerror("Error", "City not found or API request failed.")

    def perform_regression(self):
        feature_col = simpledialog.askstring("Regression", "Enter the feature column (e.g., Age):")
        target_col = simpledialog.askstring("Regression", "Enter the target column (e.g., Salary):")
        
        if feature_col in self.df.columns and target_col in self.df.columns:
            model = LinearRegression()
            X = self.df[[feature_col]].dropna()
            y = self.df[target_col].dropna()
            model.fit(X, y)
            messagebox.showinfo("Regression Analysis", f"Coefficient: {model.coef_[0]}\nIntercept: {model.intercept_}")
        else:
            messagebox.showerror("Error", "Columns not found or data insufficient for regression.")

    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", f"Data saved to {file_path} successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
