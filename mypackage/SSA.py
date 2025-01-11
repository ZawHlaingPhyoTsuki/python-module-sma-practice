#SSA.py
def simple_smoothing_average(data):
    """
    Calculate Simple Smoothing Average (SSA).
    Args:
        data (list): List of numerical values.
    Returns:
        list: SSA values.
    """
    if len(data) == 0:
        raise ValueError("Data cannot be empty.")
    
    ssa_values = [data[0]]  # Start with the first value
    for t in range(1, len(data)):
        average = sum(data[:t + 1]) / (t + 1)  # Average up to the current point
        ssa_values.append(average)
    
    return ssa_values