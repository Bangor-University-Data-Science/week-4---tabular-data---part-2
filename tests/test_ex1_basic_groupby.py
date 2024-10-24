import pytest
import pandas as pd
import numpy as np
from exercises.ex1_basic_groupby import (
    load_data,
    calculate_shipping_stats,
    calculate_category_stats,
    calculate_region_discount
)

@pytest.fixture
def superstore_data():
    return load_data()

def test_calculate_shipping_stats(superstore_data):
    result = calculate_shipping_stats(superstore_data)
    
    # Check return type
    assert isinstance(result, pd.DataFrame)
    
    # Check columns
    assert set(result.columns) == {'avg_shipping_cost', 'total_sales'}
    
    # Check if Ship Mode is index
    assert result.index.name == 'Ship Mode'
    
    # Check if values are reasonable
    assert (result['avg_shipping_cost'] >= 0).all()
    assert (result['total_sales'] >= 0).all()

def test_calculate_category_stats(superstore_data):
    result = calculate_category_stats(superstore_data)
    
    # Check return type
    assert isinstance(result, pd.DataFrame)
    
    # Check columns
    assert set(result.columns) == {'order_count', 'total_profit'}
    
    # Check if Category is index
    assert result.index.name == 'Category'
    
    # Check if values are reasonable
    assert (result['order_count'] >= 0).all()
    assert result['total_profit'].notna().all()

def test_calculate_region_discount(superstore_data):
    result = calculate_region_discount(superstore_data)
    
    # Check return type
    assert isinstance(result, pd.Series)
    
    # Check if Region is index
    assert result.index.name == 'Region'
    
    # Check if values are reasonable
    assert (result >= 0).all()
    assert (result <= 1).all()  # Assuming discount is in decimal form