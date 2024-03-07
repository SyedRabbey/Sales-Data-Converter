import csv
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class SalesDataConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Data Converter")
        self.root.geometry("300x200")
        self.root.configure(bg="#e2ed11")

        self.label = tk.Label(self.root, text="Sales Data Converter", bg="#1a8517", font=("Arial", 14))
        self.label.pack(pady=10)

        self.open_button = tk.Button(self.root, text="Open File", command=self.open_file, bg="#1a8517")
        self.open_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_program, bg="#FF3300")
        self.quit_button.pack(pady=5)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            sales_data = self.read_csv(file_path)
            if sales_data:
                self.save_json(sales_data)
                messagebox.showinfo("Success", "Data converted and saved to transaction_data.json")

    def read_csv(self, file_path):
        sales_data = []
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            for row in reader:
                cleaned_row = [field.strip('"') for field in row]
                sales_data.append(dict(zip(header, cleaned_row)))
        return sales_data

    def save_json(self, data):
        with open("transaction_data.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def quit_program(self):
        self.root.quit()

def open_additional_window():
    additional_window = tk.Toplevel()
    additional_window.title("Additional Window")
    additional_window.geometry("200x100")
    additional_window.configure(bg="#FFFF99")

    label = tk.Label(additional_window, text="This is an additional window", bg="#FFFF99")
    label.pack(pady=10)

    close_button = tk.Button(additional_window, text="Close", command=additional_window.destroy, bg="#FF3300")
    close_button.pack(pady=5)

def main():
    root = tk.Tk()
    app = SalesDataConverter(root)

    additional_window_button = tk.Button(root, text="Additional Window", command=open_additional_window, bg="#1a8517")
    additional_window_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
