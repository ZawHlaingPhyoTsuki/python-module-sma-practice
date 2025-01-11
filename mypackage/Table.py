#Table.py
import pandas as pd

def generate_table(data, ses_values, sma_values, ssa_values):
    """
    Generate a table of SES, SMA, and SSA results, including errors.
    Args:
        data (list): Actual data points.
        ses_values (list): Smoothed SES values.
        sma_values (list): SMA values.
        ssa_values (list): SSA values.
    Returns:
        pd.DataFrame: A DataFrame containing the results.
    """
    ses_errors = [d - s for d, s in zip(data, ses_values)]
    ses_squared_errors = [e ** 2 for e in ses_errors]

    table = pd.DataFrame({
        "Data": data,
        "SES": ses_values + [None] * (len(data) - len(ses_values)),  # Padding for alignment
        "SMA": [None] * (len(data) - len(sma_values)) + sma_values,  # Padding for alignment
        "SSA": ssa_values,
        "SES Error": ses_errors + [None] * (len(data) - len(ses_errors)),
        "SES Squared Error": ses_squared_errors + [None] * (len(data) - len(ses_squared_errors)),
    })
    
    # Summary statistics
    sse = sum(ses_squared_errors)
    
    print(f"Sum of Squared Errors (SSE): {sse}")
    
    return table