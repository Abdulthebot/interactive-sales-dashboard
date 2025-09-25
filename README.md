# Interactive Sales Dashboard with Streamlit

This project is a fully interactive sales dashboard built with Streamlit. It provides a user-friendly interface for non-technical users to explore and analyze sales data, empowering them to derive actionable insights through dynamic visualizations.


*(After running the app, take a screenshot and replace this text with the image.)*

## The Business Problem
Business leaders and sales managers need a quick, intuitive way to understand performance across different regions, product categories, and time periods. This dashboard replaces static reports with a live, filterable tool for real-time decision-making.

## Features
- **Interactive Filtering:** Filter data by Region, Product Category, and a specific Date Range.
- **KPI Metrics:** At-a-glance view of Total Sales, Total Units Sold, and Average Sale Value based on selected filters.
- **Dynamic Charts:** All charts are built with Plotly and update instantly based on user selections.
  - Sales by Product Category (Bar Chart)
  - Sales by Region (Pie Chart)
  - Sales Over Time (Line Chart)

## How to Run

### 1. Prerequisites
- Python 3.8+
- Pip

### 2. Installation & Execution
```bash
# Clone this repository
git clone [https://github.com/YOUR_USERNAME/interactive-sales-dashboard.git](https://github.com/YOUR_USERNAME/interactive-sales-dashboard.git)
cd interactive-sales-dashboard

# Install dependencies
pip install -r requirements.txt

# Step 1: Generate the synthetic dataset
python generate_sales_data.py

# Step 2: Run the Streamlit application
streamlit run dashboard.py
```
Your browser will open a new tab with the running application.

## Architect's Notes
- **Streamlit for Speed:** Streamlit was chosen as the framework to enable rapid development of a beautiful, functional data application without needing to write any HTML, CSS, or JavaScript.
- **Plotly for Interactivity:** Plotly Express was used for all visualizations to provide a modern, interactive user experience with features like hover-tooltips, zooming, and panning right out of the box.
- **Performance with Caching:** The core data loading function is decorated with `@st.cache_data`. This is a key Streamlit feature that caches the dataset in memory, ensuring that the application is fast and responsive, as the data is not re-read from disk every time a filter is changed.
