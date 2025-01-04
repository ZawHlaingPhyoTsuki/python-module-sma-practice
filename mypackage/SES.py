#ses.py
def single_exponential_smoothing(data, alpha=0.2):
    """
    Perform Single Exponential Smoothing (SES).
    Args:
        data (list): List of numerical values.
        alpha (float): Smoothing factor (0 < alpha ≤ 1).
    Returns:
        list: Smoothed values.
    """
    smoothed = [data[0]]  # First value is same as data
    for t in range(1, len(data)):
        smoothed_value = alpha * data[t] + (1 - alpha) * smoothed[-1]
        smoothed.append(smoothed_value)
    return smoothed

def double_exponential_smoothing(data, alpha=0.2, beta=0.2):
    """
    Perform Double Exponential Smoothing (DES).
    Args:
        data (list): List of numerical values.
        alpha (float): Smoothing factor for level.
        beta (float): Smoothing factor for trend.
    Returns:
        list: Smoothed values.
    """
    if len(data) == 0:
        raise ValueError("Data cannot be empty.")

    level = data[0]
    trend = data[1] - data[0]
    smoothed = [level]

    for t in range(1, len(data)):
        last_level = level
        level = alpha * data[t] + (1 - alpha) * (level + trend)
        trend = beta * (level - last_level) + (1 - beta) * trend
        smoothed.append(level)

    return smoothed