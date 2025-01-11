#DMA.py
from mypackage.SMA import simple_moving_average

def double_moving_average(data, window_size):
    """
    Calculate Double Moving Average (DMA).
    Args:
        data (list): List of numerical values.
        window_size (int): Number of data points to include in the average.
    Returns:
        list: DMA values.
    """
    if window_size > len(data):
        raise ValueError("Window size must be less than or equal to the length of the data.")

    first_ma = simple_moving_average(data, window_size)
    second_ma = simple_moving_average(first_ma, window_size)
    
    return second_ma