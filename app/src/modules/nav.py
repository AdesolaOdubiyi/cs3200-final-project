# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


def SideBarLinks(show_home=False):
    """
    Global Sidebar Navigation
    """
    # Logo
    st.sidebar.image("assets/Stratify Logo.png", width=180)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    # Home
    # Home
    st.sidebar.page_link("Home.py", label="Home")

    # Dashboards
    st.sidebar.markdown("### Dashboards")
    st.sidebar.page_link("pages/10_Analyst_Home.py", label="Analyst Dashboard")
    st.sidebar.page_link(
        "pages/00_Data_Analyst_Home.py", label="Data Analyst Workspace"
    )
    st.sidebar.page_link(
        "pages/03_Geopolitical_Intel_Home.py", label="Geopolitical Intelligence"
    )
    st.sidebar.page_link("pages/30_Director_Home.py", label="Director Overview")
    st.sidebar.page_link("pages/02_Risk_Dashboard.py", label="Risk Intelligence")
    st.sidebar.page_link("pages/01_Backtest_Dashboard.py", label="Backtest Dashboard")
    st.sidebar.page_link("pages/11_Portfolio_Manager.py", label="Portfolio Manager")
    st.sidebar.page_link("pages/31_Firm_Dashboard.py", label="Firm Dashboard")

    # Analytics & Tools
    st.sidebar.markdown("### Analytics & Tools")
    st.sidebar.page_link("pages/01_Global_Macro_Data.py", label="Global Macro Data")

    # Management
    st.sidebar.markdown("### System & Admin")
    st.sidebar.page_link("pages/21_System_Management.py", label="System Operations")

    # Logout
    st.sidebar.markdown("---")
    if st.session_state.get("authenticated", False):
        if st.sidebar.button("Logout", type="secondary"):
            st.session_state["authenticated"] = False
            st.session_state["role"] = None
            st.switch_page("Home.py")
