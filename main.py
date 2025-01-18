# main.py

from mypackage.MSE import mean_squared_error
from mypackage.SMA import simple_moving_average
from mypackage.DMA import double_moving_average
from mypackage.SSA import simple_smoothing_average
from mypackage.SES import single_exponential_smoothing
from mypackage.DES import double_exponential_smoothing
from mypackage.Table import generate_table
from mypackage.plot import plot_time_series
from mypackage.InputData import get_input_data, write_data_to_file

# Read data from file 'data.txt'
def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip().split('\n')  # To make data = ["1","2","3","4"]
            data = [int(value) for value in data]  # Convert to integers , [10, 20, 30]
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    
# Prompt user for input data and save to file using InputData functions
data = get_input_data()  # Get input data from InputData.py
if data:
    write_data_to_file('data.txt', data)  # Write data to data.txt
else:
    print("No data entered. Exiting.")
    exit(1)

# Load data from data.txt
data = read_data_from_file('data.txt')

if data:
    # SMA, SSA, SES calculations
    window_size = 3
    alpha = 0.2

    ssa_values = simple_smoothing_average(data)
    sma_values = simple_moving_average(data, window_size)
    ses_values = single_exponential_smoothing(data, alpha)

    # Calculate MSE using SES values
    mse_value = mean_squared_error(data, ses_values)
    print(f"Mean Squared Error (MSE): {mse_value}")

    # Generate table
    table = generate_table(data, ses_values, sma_values, ssa_values)
    print(table)

    dma_values = double_moving_average(data, window_size)
    des_values = double_exponential_smoothing(data, alpha)

    plot_time_series(data, sma_values, dma_values, ses_values, des_values)
else:
    print("No data to process.")
