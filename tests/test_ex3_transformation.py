import pytest
import pandas as pd
import numpy as np
from exercises.ex3_transformation import (
    calculate_sales_percentages,
    find_above_average_profit_orders,
    rank_sales_by_region
)

@pytest.fixture
def superstore_data():
    return pd.read_csv("data/superstore.csv", encoding='ISO-8859-1')

def test_calculate_sales_percentages(superstore_data):
    result = calculate_sales_percentages(superstore_data)
    
    # Check return type
    assert isinstance(result, pd.Series)
    
    # Check if percentages sum to 100 (allowing for small floating point differences)
    assert np.isclose(result.sum(), 100, rtol=1e-5)
    
    # Check if all values are between 0 and 100
    assert (result >= 0).all()
    assert (result <= 100).all()

def test_find_above_average_profit_orders(superstore_data):
    result = find_above_average_profit_orders(superstore_data)
    
    # Check return type
    assert isinstance(result, pd.DataFrame)
    
    # Check if we have the same columns as input
    assert set(result.columns) == set(superstore_data.columns)
    
    # Check if profits are actually above category average
    category_avgs = superstore_data.groupby('Category')['Profit'].transform('mean')
    assert (result['Profit'] > category_avgs[result.index]).all()

def test_rank_sales_by_region(superstore_data):
    result = rank_sales_by_region(superstore_data)
    
    # Check return type
    assert isinstance(result, pd.Series)
    
    # Check if ranks are within reasonable range
    assert result.min() >= 1
    assert result.max() <= len(superstore_data)
    
    # Check if ranks are unique within regions
    for region in superstore_data['Region'].unique():
        region_ranks = result[superstore_data['Region'] == region]
        assert len(region_ranks) == len(set(region_ranks))