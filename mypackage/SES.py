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
