import pandas as pd
import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.footer import render_footer

# Load Data
qs = load_data()

# Set page configuration
st.set_page_config(page_title="Scores Overview")
st.title("QS World University Scores 2025")

score_options = {
    "Academic_Reputation_Score": "Academic Reputation",
    "Employer_Reputation_Score": "Employer Reputation",
    "Faculty_Student_Score": "Faculty-Student Ratio",
    "Citations_per_Faculty_Score": "Citations per Faculty",
    "International_Faculty_Score": "International Faculty",
    "International_Students_Score": "International Students",
    "International_Research_Network_Score": "International Research Network",
    "Employment_Outcomes_Score": "Employment Outcomes",
    "Sustainability_Score": "Sustainability",
    "Overall_Score": "Overall Score"
}

# Select score
score_key = st.selectbox(
    "Choose Score Indicator",
    options = list(score_options.keys()),
    format_func=lambda x: score_options[x]
)
# Use slider to choose how many universities to display
n = st.slider(
    "Select number of universities to display",
    min_value=5,
    max_value=100,
    value=10,  # default value
    step=5
)

filtered_score = qs.dropna(subset=[score_key]).sort_values(by=score_key, ascending=False).head(n)

# Plot
fig = px.bar(
    filtered_score,
    x=score_key,
    y="Institution_Name",
    orientation="h",
    title=f"Top {n} Universities by {score_options[score_key]} in QS World University Rankings 2025",
    color=score_key,
    color_continuous_scale=px.colors.sequential.Viridis
)

fig.update_layout(
    yaxis=dict(autorange="reversed"),  # Reverse y-axis to show top universities at the top
    xaxis_title=score_options[score_key],
    yaxis_title="Institution",
    margin=dict(t=60, l=100, r=20, b=20),
)

# display
st.plotly_chart(fig, use_container_width=True)
st.dataframe(filtered_score[["RANK_2025", "Institution_Name", score_key]].reset_index(drop=True),use_container_width=True)

# Footer
render_footer()