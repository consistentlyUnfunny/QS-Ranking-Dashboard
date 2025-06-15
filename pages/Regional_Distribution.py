import pandas as pd
import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
# Load Dataset
qs = load_data()

st.set_page_config(page_title="Regional Distribution")
st.title("Regional Distribution of Universities in QS Rankings 2025")

# Aggregate data by region
region_count = qs["Region"].value_counts().reset_index() 
# reset index converts series into data frame, after columns are reset it became data with index and region
region_count.columns = ["Region", "Count"] # Rename columns

# Plot donut chart
fig = px.pie(
    region_count, # Data Frame
    values = "Count", # Columns from the dataframe to use
    names = "Region",
    title = "Universities by Region",
    hole = 0.4,  # Creates a donut chart
    color_discrete_sequence=px.colors.qualitative.Set3
)

# Traces = the individual slices of the pie chart
fig.update_traces(
    textposition='inside',  # Position text inside the slices
    textinfo='percent+label'  # Show percentage and label
)

# Overall layout adjustments
fig.update_layout(
    margin=dict(t=50, b=20, l=20, r=20),  # Adjust margins
    title_x=0.5,  # Center the title
    legend=dict(title="Region"),  # Remove legend title
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

from utils.footer import render_footer
# Display footer
render_footer()