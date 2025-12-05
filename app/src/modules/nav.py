# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


def SideBarLinks(show_home=False):
    """
    Global Sidebar Navigation
    """
    # Logo
    st.sidebar.image("assets/logo_clean.png", width=180)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    # Home
    # Home
    st.sidebar.page_link("Home.py", label="Home")

    # Dashboards
    st.sidebar.markdown("### Dashboards")
    st.sidebar.page_link("pages/10_Analyst_Home.py", label="Analyst Workspace")
    st.sidebar.page_link("pages/00_Data_Analyst_Home.py", label="Data Analyst Workspace")
    st.sidebar.page_link("pages/30_Director_Home.py", label="Director Overview")
    st.sidebar.page_link("pages/02_Risk_Dashboard.py", label="Risk Intelligence")
    st.sidebar.page_link("pages/01_Backtest_Dashboard.py", label="Backtest Engine")

    # Analytics & Tools
    st.sidebar.markdown("### Analytics & Tools")
    st.sidebar.page_link("pages/11_Prediction.py", label="AI Forecasting")
    st.sidebar.page_link("pages/21_ML_Model_Mgmt.py", label="ML Model Registry")
    st.sidebar.page_link("pages/01_World_Bank_Viz.py", label="Global Macro Data")
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Geospatial Analytics")
    st.sidebar.page_link("pages/13_Classification.py", label="Asset Classification")

    # Management
    st.sidebar.markdown("### System & Admin")
    st.sidebar.page_link("pages/20_Admin_Home.py", label="Admin Console")
    st.sidebar.page_link("pages/21_System_Management.py", label="System Operations")
    st.sidebar.page_link("pages/12_API_Test.py", label="API Diagnostics")

    # Resources
    st.sidebar.markdown("### Resources")
    st.sidebar.page_link("pages/30_About.py", label="About Stratify")
    
    # Logout
    st.sidebar.markdown("---")
    if st.session_state.get("authenticated", False):
        if st.sidebar.button("Logout", type="secondary"):
            st.session_state["authenticated"] = False
            st.session_state["role"] = None
            st.switch_page("Home.py")
