import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Streamlit automatically show sidebar in pages
st.set_page_config(page_title="QS Dashboard")
st.title("QS Dashboard")
st.info("""
This dashboard visualizes the **QS World University Rankings 2025**, covering over **1,500 institutions** from **105 countries**.  
It offers insights into global university performance based on key indicators such as:

- Academic and employer reputation
- Research impact and faculty-student ratio
- Internationalization and sustainability
- Graduate employment outcomes

Use the sidebar to explore ranking trends, regional distributions, and detailed metrics for each university.
""")


from utils.data_loader import load_data
# Load Dataset
qs = load_data()

# Display top 10 universities of 2025
st.subheader("Top 10 Universities in QS World University Rankings 2025")
top10 = qs.sort_values(by='RANK_2025_NUM').head(10)
# Plot the top 10 universities
# Create figure
fig = go.Figure()

ranks = list(range(1, 11))
fig.add_trace(go.Bar(
    y=ranks,
    x=[1] * 10,
    text=top10["Institution_Name"],
    orientation='h',
    textposition='inside',
    marker_color=px.colors.qualitative.Plotly,  # 10 distinct colors
    hovertext=top10["Institution_Name"],
    hoverinfo='text',
    showlegend=False
))


# Update layout
fig.update_layout(
    title="🎓 Top 10 Universities in 2025",
    yaxis=dict(
        tickmode='array',
        tickvals=ranks,
        ticktext=ranks,
        autorange='reversed'
    ),
    xaxis=dict(
        visible=False
    ),
    height=600,
    margin=dict(l=40, r=40, t=60, b=40)
)

st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False, 'scrollZoom': False, 'staticPlot': True})   


from utils.footer import render_footer
# Display footer
render_footer()


