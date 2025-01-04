from mypackage.MSE import mean_squared_error
from mypackage.SMA import simple_moving_average
from mypackage.SMA import double_moving_average
from mypackage.SSA import simple_smoothing_average
from mypackage.SES import single_exponential_smoothing
from mypackage.SES import double_exponential_smoothing
from mypackage.Table import generate_table
from mypackage.plot import plot_time_series

# Sample data
data = [112, 118, 132, 129, 121, 135, 148, 148, 136, 119, 104]

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