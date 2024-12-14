import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analysis Tool")
        self.df = pd.DataFrame()
        self.conn = None

        # Create buttons for file loading, processing, and saving
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
                self.save_button.config(state=tk.NORMAL)
                messagebox.showinfo("Success", "CSV file loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading CSV file: {e}")

    def filter_data(self):
        filter_column = simpledialog.askstring("Filter", "Enter column to filter by:")
        filter_value = simpledialog.askstring("Filter", f"Enter value to filter by in {filter_column}:")
        if filter_column in self.df.columns:
            filtered_df = self.df[self.df[filter_column] == filter_value]
            messagebox.showinfo("Filtered Data", f"Filtered data contains {len(filtered_df)} records.")
            self.df = filtered_df
        else:
            messagebox.showerror("Error", "Column not found!")

    def sort_data(self):
        sort_column = simpledialog.askstring("Sort", "Enter column to sort by:")
        sort_order = simpledialog.askstring("Sort", "Enter sort order (asc/desc):")
        if sort_column in self.df.columns:
            ascending = sort_order.lower() == 'asc'
            sorted_df = self.df.sort_values(by=sort_column, ascending=ascending)
            self.df = sorted_df
            messagebox.showinfo("Sorted Data", "Data sorted successfully!")
        else:
            messagebox.showerror("Error", "Column not found!")

    def group_data(self):
        group_column = simpledialog.askstring("Group", "Enter column to group by:")
        agg_column = simpledialog.askstring("Group", "Enter column to aggregate:")
        if group_column in self.df.columns and agg_column in self.df.columns:
            grouped_df = self.df.groupby(group_column)[agg_column].mean().reset_index()
            messagebox.showinfo("Grouped Data", f"Grouped data with {len(grouped_df)} groups.")
            self.df = grouped_df
        else:
            messagebox.showerror("Error", "Column not found!")

    def visualize_data(self):
        column_to_plot = simpledialog.askstring("Visualize", "Enter column to visualize:")
        if column_to_plot in self.df.columns:
            plt.figure(figsize=(10, 6))
            self.df[column_to_plot].value_counts().plot(kind='bar')
            plt.title(f'Distribution of {column_to_plot}')
            plt.xlabel(column_to_plot)
            plt.ylabel('Frequency')
            plt.show()
        else:
            messagebox.showerror("Error", "Column not found!")

    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", f"Data saved to {file_path} successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
