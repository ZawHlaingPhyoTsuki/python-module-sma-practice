import tkinter as tk
from tkinter import filedialog, messagebox
from mypackage.MSE import mean_squared_error
from mypackage.SMA import simple_moving_average
from mypackage.DMA import double_moving_average
from mypackage.SSA import simple_smoothing_average
from mypackage.SES import single_exponential_smoothing
from mypackage.DES import double_exponential_smoothing
from mypackage.Table import generate_table
from mypackage.plot import plot_time_series
from mypackage.InputData import get_input_data, write_data_to_file

# Function to read data from file
def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip().split('\n')
            data = [int(value) for value in data]
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", f"{filename} not found.")
        return []

# Function to handle data processing
def process_data():
    try:
        # Read input data from entry box
        data = [int(x) for x in input_data_entry.get().split(',')]

        # Save data to file
        write_data_to_file('data.txt', data)

        # Perform calculations
        window_size = 3
        alpha = 0.2

        ssa_values = simple_smoothing_average(data)
        sma_values = simple_moving_average(data, window_size)
        ses_values = single_exponential_smoothing(data, alpha)
        dma_values = double_moving_average(data, window_size)
        des_values = double_exponential_smoothing(data, alpha)
        mse_value = mean_squared_error(data, ses_values)

        # Generate table
        table = generate_table(data, ses_values, sma_values, ssa_values)

        # Display results
        results_text.delete('1.0', tk.END)
        results_text.insert(tk.END, f"Mean Squared Error (MSE): {mse_value}\n\n")
        results_text.insert(tk.END, table)

        # Plot time series
        plot_time_series(data, sma_values, dma_values, ses_values, des_values)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid comma-separated integers.")

# Function to load data from file
def load_data():
    filename = filedialog.askopenfilename(title="Select Data File", filetypes=[("Text Files", "*.txt")])
    if filename:
        data = read_data_from_file(filename)
        if data:
            input_data_entry.delete(0, tk.END)
            input_data_entry.insert(0, ','.join(map(str, data)))

# Create main GUI window
root = tk.Tk()
root.title("Time Series Analysis Tool")

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter Data (comma-separated):")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_data_entry = tk.Entry(input_frame, width=50)
input_data_entry.grid(row=0, column=1, padx=5, pady=5)

load_button = tk.Button(input_frame, text="Load from File", command=load_data)
load_button.grid(row=0, column=2, padx=5, pady=5)

# Process Button
process_button = tk.Button(root, text="Process Data", command=process_data, bg="lightblue")
process_button.pack(pady=10)

# Results Frame
results_frame = tk.Frame(root)
results_frame.pack(pady=10)

results_label = tk.Label(results_frame, text="Results:")
results_label.pack(anchor="w")

results_text = tk.Text(results_frame, width=80, height=20)
results_text.pack()

# Start the GUI loop
root.mainloop()
