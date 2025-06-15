import pandas as pd
import streamlit as st
import plotly.express as px
from utils.data_loader import load_data
from utils.footer import render_footer

# Load Data
qs = load_data()
st.set_page_config(page_title="Rankings Overview")
st.title("QS World University Rankings Overview 2025")

# Use slider to choose how many universities to display
n = st.slider(
    "Select number of universities to display",
    min_value = 5,
    max_value = 100,
    value= 10, # default value
    step = 5
)

# Filter top n universities
top_universities = qs.sort_values(by='RANK_2025_NUM').head(n)

# Plot
fig = px.bar(
    top_universities,
    x="Overall_Score",
    y="Institution_Name",
    orientation="h",
    title=f"Top {n} Universities in QS World University Rankings 2025",
    color="Overall_Score",
    color_continuous_scale=px.colors.sequential.Viridis,
    text="Overall_Score"
)

fig.update_layout(
    yaxis = dict(autorange="reversed"),  # Reverse y-axis to show top universities at the top
    xaxis_title="Overall Score",
    yaxis_title="Institution",
    margin=dict(t=60, l=100, r=20, b=20),
)

st.plotly_chart(fig, use_container_width=True)
st.dataframe(top_universities[["RANK_2025", "Institution_Name", "Overall_Score"]].reset_index(drop=True))

# Footer
render_footer()