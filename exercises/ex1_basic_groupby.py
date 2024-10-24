import pandas as pd

def load_data():
    """Load the Superstore dataset."""
    return pd.read_csv("data/superstore.csv", encoding='ISO-8859-1')

def calculate_shipping_stats(df):
    """
    Exercise 1.1: Calculate average shipping cost and total sales by Ship Mode.
    
    Args:
        df: pandas DataFrame containing the Superstore data
    
    Returns:
        pandas DataFrame with Ship Mode as index and columns ['avg_shipping_cost', 'total_sales']
    """
    # Your code here
    
    pass

def calculate_category_stats(df):
    """
    Exercise 1.2: Calculate number of orders and total profit by Category.
    
    Args:
        df: pandas DataFrame containing the Superstore data
    
    Returns:
        pandas DataFrame with Category as index and columns ['order_count', 'total_profit']
    """
    # Your code here
    
    pass

def calculate_region_discount(df):
    """
    Exercise 1.3: Calculate average discount by Region.
    
    Args:
        df: pandas DataFrame containing the Superstore data
    
    Returns:
        pandas Series with Region as index and average discount as values
    """
    # Your code here
    
    pass