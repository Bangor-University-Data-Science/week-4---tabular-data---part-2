import pytest
import pandas as pd
from exercises.ex2_filtering import (
    get_high_sales_regions,
    get_profitable_categories,
    get_large_segments
)

@pytest.fixture
def superstore_data():
    return pd.read_csv("data/superstore.csv", encoding='ISO-8859-1')

def test_get_high_sales_regions(superstore_data):
    result = get_high_sales_regions(superstore_data, threshold=100000)
    
    # Check return type
    assert isinstance(result, pd.Series)
    
    # Check if Region is index
    assert result.index.name == 'Region'
    
    # Check if values meet threshold
    assert (result > 100000).all()

def test_get_profitable_categories(superstore_data):
    result = get_profitable_categories(superstore_data)
    
    # Check return type
    assert isinstance(result, pd.Series)
    
    # Check if Category is index
    assert result.index.name == 'Category'
    
    # Check if values are positive
    assert (result > 0).all()

def test_get_large_segments(superstore_data):
    result = get_large_segments(superstore_data, min_orders=1000)
    
    # Check return type
    assert isinstance(result, pd.Series)
    
    # Check if Segment is index
    assert result.index.name == 'Segment'
    
    # Check if values meet minimum
    assert (result > 1000).all()