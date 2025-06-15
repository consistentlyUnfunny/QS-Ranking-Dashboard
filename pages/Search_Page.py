import pandas as pd
import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.footer import render_footer

# Load Data
qs = load_data()
st.set_page_config(page_title="University Search")
st.title("University Search")

# Search bar
query = st.text_input("Enter university name or keyword", "") # Second argument is default value

# Filter data based on query
results = qs[qs["Institution_Name"].str.contains(query, case=False, na=False)] # Case insensitive comparison and force NaN to be non matching, exlude empty entries from result instead of throwing errors

# If results found
if not results.empty:
    selected = st.selectbox("Select a university", results["Institution_Name"].tolist())
    uni_data = results[results["Institution_Name"] == selected].iloc[0] # Select first row of the data frame, so if there are multiple rows with the same name, we only get one
    st.subheader(f"Details for {uni_data['Institution_Name']}")

    st.markdown(f"""
    - **Rank 2025**: {uni_data['RANK_2025']}
    - **Rank 2024**: {uni_data['RANK_2024']}
    - **Change in Rank**: {uni_data.get('RANK_CHANGED', 'N/A')}
    - **Overall Score**: {uni_data['Overall_Score']}
    - **Location**: {uni_data['Location']} ({uni_data['Region']})
    - **Size**: {uni_data['SIZE']}
    """)

     # Display a table of scores
    st.markdown("### 📊 Key Metrics")
    metrics = {
        "Academic Reputation": uni_data["Academic_Reputation_Score"],
        "Employer Reputation": uni_data["Employer_Reputation_Score"],
        "Faculty-Student Ratio": uni_data["Faculty_Student_Score"],
        "Citations per Faculty": uni_data["Citations_per_Faculty_Score"],
        "International Faculty": uni_data["International_Faculty_Score"],
        "International Students": uni_data["International_Students_Score"],
        "International Research Network": uni_data["International_Research_Network_Score"],
        "Employment Outcomes": uni_data["Employment_Outcomes_Score"],
        "Sustainability": uni_data["Sustainability_Score"],
    }

    st.dataframe(pd.DataFrame(metrics.items(), columns=["Metric", "Score"]), use_container_width=True)

else:
    if query: # query not empty but no results found
        st.warning("No universities found matching your query. Please try a different keyword.")
# Footer
render_footer()