"""app/src/pages/00_Pol_Strat_Home.py
Light-weight redirect notice — page was renamed to `03_Geopolitical_Intel_Home.py`.
This file remains to help users who open the old filename directly.
"""

import sys
import streamlit as st

sys.path.append("..")
from modules.nav import SideBarLinks
from stratify_theme import apply_stratify_theme

st.set_page_config(page_title="Geopolitical Intelligence - Renamed", page_icon="🧭", layout="wide")

apply_stratify_theme()
SideBarLinks()

st.markdown(
    """
    ## Page Renamed

    This page has been renamed to **`03_Geopolitical_Intel_Home.py`** and added to the sidebar as **Geopolitical Intelligence**.

    If you navigated here by filename, please use the sidebar link instead.
    """,
    unsafe_allow_html=True,
)

if st.button("Go to Geopolitical Intelligence"):
    # Use Streamlit navigation to switch to the new page
    st.switch_page("pages/03_Geopolitical_Intel_Home.py")