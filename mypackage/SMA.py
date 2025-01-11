#SMA.py
def simple_moving_average(data, window_size):
    """
    Calculate Simple Moving Average (SMA).
    Args:
        data (list): List of numerical values.
        window_size (int): Number of data points to include in the average.
    Returns:
        list: SMA values (length will be len(data) - window_size + 1).
    """
    if window_size > len(data):
        raise ValueError("Window size must be less than or equal to the length of the data.")
    
    sma_values = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        sma_values.append(sum(window) / window_size)
    
    return sma_values

