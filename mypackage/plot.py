#plot.py
import matplotlib.pyplot as plt

def plot_time_series(data, sma_values, dma_values, ses_values, des_values):
    """
    Plot time series data with SMA, DMA, SES, and DES.
    Args:
        data (list): Actual data points.
        sma_values (list): Simple Moving Average values.
        dma_values (list): Double Moving Average values.
        ses_values (list): Single Exponential Smoothing values.
        des_values (list): Double Exponential Smoothing values.
    """
    plt.figure(figsize=(12, 6))

    # Plot actual data
    plt.plot(data, label='Actual Data', marker='o')

    # Plot SMA
    plt.plot(range(len(data) - len(sma_values), len(data)), sma_values, label='SMA', linestyle='--')

    # Plot DMA
    plt.plot(range(len(data) - len(dma_values), len(data)), dma_values, label='DMA', linestyle='--')

    # Plot SES
    plt.plot(ses_values, label='SES', linestyle='-.')

    # Plot DES
    plt.plot(des_values, label='DES', linestyle=':')

    plt.title('Time Series Data with SMA, DMA, SES, and DES')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.show()