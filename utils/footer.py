import streamlit as st

def render_footer():
    st.markdown("---", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; padding-top: 10px; font-size: 0.9em; color: grey;'>
            © 2025 QS University Rankings Dashboard • By <strong>consistentlyUnfunny</strong> • Dataset from Melissa Monfared (Kaggle)
        </div>
        """,
        unsafe_allow_html=True
    )

