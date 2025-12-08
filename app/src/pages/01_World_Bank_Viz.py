# pages/01_World_Bank_Viz.py
# Stratify - Global Macro Data
# Persona: Political Strategy Advisor / Director

"""
This file was renamed to `01_Global_Macro_Data.py` for clarity. The working page is now
available at `pages/01_Global_Macro_Data.py` and linked in the sidebar as "Global Macro Data".

Left for discovery: remove this file or keep as redirect placeholder.
"""

import streamlit as st

st.set_page_config(page_title="Global Macro Data - Renamed", layout="wide")

st.markdown(
    """
    ## Page Renamed

    This page moved to **`pages/01_Global_Macro_Data.py`** and is linked in the sidebar.
    """,
    unsafe_allow_html=True,
)

if st.button("Go to Global Macro Data"):
    st.experimental_set_query_params()
    st.experimental_rerun()
