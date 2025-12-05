# pages/00_Data_Analyst_Home.py
# Stratify - Data Analysis & Reporting
# Persona: Noah Harrison (Data Analyst)

import sys
import streamlit as st
import pandas as pd
import numpy as np

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="Data Analyst Workspace - Stratify",
    page_icon="📉",
    layout="wide",
)

from modules.nav import SideBarLinks
from stratify_theme import apply_stratify_theme

apply_stratify_theme()
SideBarLinks()

# ============================================
# STYLES
# ============================================
st.markdown(
    """
<style>
.data-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.report-item {
    padding: 1rem;
    border-bottom: 1px solid #334155;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.report-item:last-child {
    border-bottom: none;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================
# HEADER
# ============================================
st.markdown(
    """
    <div style="padding: 1.5rem 0 1rem 0;">
        <h1 style="font-size: 2.5rem; color: #a855f7; margin-bottom: 0.25rem;">
            Data Analyst Workspace
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Advanced analytics, reporting, and data management
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# WORKSPACE TABS
# ============================================
tab1, tab2, tab3 = st.tabs(["Market Analysis", "Report Generation", "Data Management"])

# --- TAB 1: MARKET ANALYSIS ---
with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### Comparative Analysis")
        
        # Mock Data for Chart
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["Portfolio A", "Portfolio B", "Benchmark"]
        )
        st.line_chart(chart_data)
        
    with col2:
        st.markdown("### Analysis Tools")
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.selectbox("Select Dataset", ["Global Equities 2024", "Commodities Futures", "Crypto Spot"])
        st.multiselect("Metrics", ["Returns", "Volatility", "Sharpe", "Sortino"], default=["Returns", "Sharpe"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Run Analysis", use_container_width=True):
            show_stratify_loader(duration=2, message="Processing Data...", style="cascade")
            st.success("Analysis Complete")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: REPORT GENERATION ---
with tab2:
    st.markdown("### Automated Reporting")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.markdown("#### Generate New Report")
        
        r_type = st.selectbox("Report Type", ["Monthly Performance", "Risk Attribution", "Sector Exposure", "Client Summary"])
        r_format = st.radio("Format", ["PDF", "CSV", "Excel"], horizontal=True)
        
        if st.button("Generate & Download", type="primary"):
            show_stratify_loader(duration=2.5, message="Compiling Report...", style="sequential")
            st.success(f" {r_type} generated successfully ({r_format})")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.markdown("#### Recent Reports")
        
        reports = [
            {"name": "Q3_Performance_Review.pdf", "date": "Oct 24, 2024", "size": "2.4 MB"},
            {"name": "Tech_Sector_Deep_Dive.csv", "date": "Oct 22, 2024", "size": "450 KB"},
            {"name": "Weekly_Risk_Summary.xlsx", "date": "Oct 20, 2024", "size": "1.1 MB"},
        ]
        
        for r in reports:
            st.markdown(
                f"""
                <div class="report-item">
                    <div>
                        <div style="color:#e2e8f0; font-weight:bold;">{r['name']}</div>
                        <div style="color:#64748b; font-size:0.8rem;">{r['date']} • {r['size']}</div>
                    </div>
                    <button style="background:none; border:1px solid #334155; color:#3b82f6; border-radius:4px; padding:0.25rem 0.5rem; cursor:pointer;">⬇</button>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: DATA MANAGEMENT ---
with tab3:
    st.markdown("### Data Pipeline Status")
    
    st.info("ℹConnected to Snowflake Data Warehouse (Read-Only)")
    
    d1, d2, d3 = st.columns(3)
    with d1:
        st.metric("Rows Processed (Today)", "1.2M", "+15%")
    with d2:
        st.metric("API Calls", "45.2K", "-2%")
    with d3:
        st.metric("Data Quality Score", "98.5%", "+0.2%")
        
    st.markdown("### Export Data")
    with st.expander("Custom Data Export"):
        st.text_area("SQL Query", "SELECT * FROM market_data WHERE symbol = 'AAPL' AND date > '2023-01-01'")
        if st.button("Execute & Export"):
            show_stratify_loader(duration=1.5, message="Fetching Data...")
            st.warning("Export limited to 10,000 rows in preview mode.")

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Main Menu"):
    st.switch_page("Home.py")
