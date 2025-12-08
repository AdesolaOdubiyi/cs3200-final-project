"""
This page was renamed to `03_Geopolitical_Intel_Home.py` to be clearer.
"""

import streamlit as st

st.set_page_config(page_title="Geopolitical Intelligence - Renamed", layout="wide")

st.markdown(
    """
    ## Page Renamed

    This page has been renamed to **`03_Geopolitical_Intel_Home.py`** and added to the sidebar as **Geopolitical Intelligence**.

    If you navigated here by filename, please use the sidebar link instead.
    """,
    unsafe_allow_html=True,
)

if st.button("Go to Geopolitical Intelligence"):
    st.experimental_set_query_params()
    st.experimental_rerun()