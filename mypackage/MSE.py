#MSE.py
def mean_squared_error(actual, predicted):
    """
    Calculate Mean Squared Error (MSE).
    Args:
        actual (list): Actual data points.
        predicted (list): Predicted data points.
    Returns:
        float: MSE value.
    """
    errors = [(a - p) ** 2 for a, p in zip(actual, predicted)]
    return sum(errors) / len(errors)