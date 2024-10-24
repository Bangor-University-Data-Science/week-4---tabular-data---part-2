import pandas as pd

def get_high_sales_regions(df, threshold=100000):
    """
    Exercise 2.1: Find regions with total sales above the threshold.
    
    Args:
        df: pandas DataFrame containing the Superstore data
        threshold: minimum total sales amount (default: 100000)
    
    Returns:
        pandas Series with Region as index and total sales as values,
        containing only regions above the threshold
    """
    # Your code here
    
    pass

def get_profitable_categories(df):
    """
    Exercise 2.2: Find categories with positive average profit.
    
    Args:
        df: pandas DataFrame containing the Superstore data
    
    Returns:
        pandas Series with Category as index and average profit as values,
        containing only categories with positive average profit
    """
    # Your code here
    
    pass

def get_large_segments(df, min_orders=1000):
    """
    Exercise 2.3: Find customer segments with more than min_orders orders.
    
    Args:
        df: pandas DataFrame containing the Superstore data
        min_orders: minimum number of orders required (default: 1000)
    
    Returns:
        pandas Series with Segment as index and order count as values,
        containing only segments with more than min_orders orders
    """
    # Your code here
   
    pass
