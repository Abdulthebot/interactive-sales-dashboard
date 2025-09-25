import pandas as pd
import numpy as np

def generate_data(num_rows=1000):
    """Generates a synthetic sales dataset and saves it to a CSV file."""
    
    # Generate date range
    dates = pd.to_datetime(pd.date_range(start='2023-01-01', end='2024-12-31', periods=num_rows))
    
    # Define product categories and regions
    product_categories = ['Electronics', 'Apparel', 'Home Goods', 'Beauty', 'Toys']
    regions = ['North', 'South', 'East', 'West']
    
    # Create the DataFrame
    df = pd.DataFrame({
        'OrderID': range(1001, 1001 + num_rows),
        'OrderDate': dates,
        'Product Category': np.random.choice(product_categories, num_rows),
        'Region': np.random.choice(regions, num_rows),
        'Units Sold': np.random.randint(1, 10, num_rows),
        'Sales': np.round(np.random.uniform(20.0, 500.0, num_rows), 2)
    })
    
    df.to_csv('sales_data.csv', index=False)
    print(f"Synthetic sales data 'sales_data.csv' with {num_rows} rows created successfully.")

if __name__ == '__main__':
    generate_data()
