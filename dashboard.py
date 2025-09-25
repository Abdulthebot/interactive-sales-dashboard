import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
# This must be the first Streamlit command in your script.
st.set_page_config(
    page_title="Interactive Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- DATA LOADING AND CACHING ---
# Using st.cache_data is a best practice to prevent reloading data on every interaction.
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    return df

try:
    df = load_data('sales_data.csv')
except FileNotFoundError:
    st.error("The data file 'sales_data.csv' was not found. Please run `generate_sales_data.py` first.")
    st.stop()


# --- SIDEBAR FOR FILTERS ---
st.sidebar.header("Dashboard Filters")

# Region Filter
region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

# Product Category Filter
category = st.sidebar.multiselect(
    "Select Product Category",
    options=df["Product Category"].unique(),
    default=df["Product Category"].unique()
)

# Date Range Filter
min_date = df["OrderDate"].min()
max_date = df["OrderDate"].max()
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# --- FILTERING THE DATAFRAME BASED ON USER INPUT ---
# Note: st.date_input returns a tuple of datetime.date objects, need to convert to datetime64
start_date = pd.to_datetime(date_range[0])
end_date = pd.to_datetime(date_range[1])

df_selection = df.query(
    "Region == @region & `Product Category` == @category & OrderDate >= @start_date & OrderDate <= @end_date"
)

if df_selection.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# --- MAIN PAGE LAYOUT ---
st.title("📊 Interactive Sales Dashboard")
st.markdown("---")

# Key Performance Indicators (KPIs)
total_sales = int(df_selection["Sales"].sum())
total_units_sold = int(df_selection["Units Sold"].sum())
average_sale_value = round(df_selection["Sales"].mean(), 2)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Sales", value=f"${total_sales:,}")
with col2:
    st.metric(label="Total Units Sold", value=f"{total_units_sold:,}")
with col3:
    st.metric(label="Average Sale Value", value=f"${average_sale_value:,}")

st.markdown("---")

# --- CHARTS ---

# Sales by Product Category (Bar Chart)
sales_by_category = df_selection.groupby("Product Category")["Sales"].sum().sort_values(ascending=False)
fig_sales_by_category = px.bar(
    sales_by_category,
    x=sales_by_category.values,
    y=sales_by_category.index,
    orientation="h",
    title="<b>Sales by Product Category</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_category),
    template="plotly_white"
)
fig_sales_by_category.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# Sales by Region (Pie Chart)
sales_by_region = df_selection.groupby("Region")["Sales"].sum()
fig_sales_by_region = px.pie(
    values=sales_by_region.values,
    names=sales_by_region.index,
    title="<b>Sales by Region</b>",
    hole=0.4
)

# Use columns to display charts side-by-side
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_sales_by_category, use_container_width=True)
right_column.plotly_chart(fig_sales_by_region, use_container_width=True)

# Sales Over Time (Line Chart)
df_selection_time = df_selection.set_index("OrderDate").resample('M').sum()
fig_sales_over_time = px.line(
    df_selection_time,
    x=df_selection_time.index,
    y="Sales",
    title="<b>Sales Over Time</b>"
)

st.plotly_chart(fig_sales_over_time, use_container_width=True)
