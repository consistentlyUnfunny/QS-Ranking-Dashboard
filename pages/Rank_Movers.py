import pandas as pd
import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
# Load Dataset
qs = load_data()

st.title("Rank Movers in QS World University Rankings 2025")

# Prepare data for rank movers
ranked = qs.dropna(subset=["RANK_CHANGED"]).sort_values(by="RANK_CHANGED", ascending=False)
top_gainers = ranked.head(10)
top_losers = ranked.tail(10)

# Plot (Gainers)
fig_gainers = px.bar(
    top_gainers,
    x="RANK_CHANGED",
    y="Institution_Name",
    orientation="h",
    title="Top 10 Ranking Gainers",
    color="RANK_CHANGED",
    color_continuous_scale="Greens",
)

fig_gainers.update_layout(
    yaxis=dict(autorange="reversed"),  # Top to bottom
    xaxis_title="Ranks Gained",
    yaxis_title="Institution",
    margin=dict(t=60, l=100, r=20, b=20)
)

# Plot (losers)
fig_losers = px.bar(
    top_losers,
    x = 'RANK_CHANGED',
    y = "Institution_Name",
    orientation = "h",
    title = "Top 10 Ranking Losers",
    color = "RANK_CHANGED",
    color_continuous_scale = px.colors.sequential.Reds[::-1]  # Reversed Reds
)

fig_losers.update_layout(
    xaxis_title = "Ranks Lost",
    yaxis_title = "Institution",
    margin = dict(t = 60, l = 100, r = 20, b = 20)
)

st.plotly_chart(fig_gainers, use_container_width=True)
st.plotly_chart(fig_losers, use_container_width=True)



# Footer
from utils.footer import render_footer
render_footer()