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
# STYLES (use theme variables from stratify_theme)
# ============================================
st.markdown(
    """
<style>
/* Use CSS variables defined by stratify_theme for consistent branding */
.data-card {
    background: var(--bg-light);
    border: 1px solid var(--bg-border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.report-item {
    padding: 1rem;
    border-bottom: 1px solid var(--bg-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.report-item:last-child {
    border-bottom: none;
}

.report-name {
    color: var(--text-primary);
    font-weight: 700;
}
.report-meta {
    color: var(--text-secondary);
    font-size: 0.85rem;
}

.page-hero h1 {
    font-family: var(--font-main);
    font-size: 2.5rem;
    color: var(--primary-dark);
    margin-bottom: 0.25rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
.page-hero p {
    color: var(--text-tertiary);
    margin: 0;
    font-size: 1rem;
}

.download-btn {
    background: transparent;
    border: 1px solid var(--bg-border);
    color: var(--primary);
    border-radius: 6px;
    padding: 0.25rem 0.5rem;
}

@media (max-width: 768px) {
    .page-hero h1 { font-size: 2rem; }
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
    <div class="page-hero" style="padding: 1.5rem 0 1rem 0;">
        <h1>Data Analyst Workspace</h1>
        <p>Advanced analytics, reporting, and data management</p>
    </div>
    <hr style="border-color: var(--bg-border); margin-bottom: 2rem;">
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
        with st.container():
            st.markdown("#### Generate New Report")

            r_type = st.selectbox("Report Type", ["Monthly Performance", "Risk Attribution", "Sector Exposure", "Client Summary"])
            r_format = st.radio("Format", ["PDF", "CSV", "Excel"], horizontal=True)

            if st.button("Generate & Download", type="primary"):
                show_stratify_loader(duration=2.5, message="Compiling Report...", style="sequential")
                st.success(f" {r_type} generated successfully ({r_format})")
        with c2:
            with st.container():
                st.markdown("#### Recent Reports")

                from pathlib import Path

                assets_dir = Path(__file__).resolve().parent.parent / "assets"

                reports = [
                    {"name": "Q3_Performance_Review.pdf", "date": "Oct 24, 2024", "size": "2.4 MB"},
                    {"name": "Tech_Sector_Deep_Dive.csv", "date": "Oct 22, 2024", "size": "450 KB"},
                    {"name": "Weekly_Risk_Summary.xlsx", "date": "Oct 20, 2024", "size": "1.1 MB"},
                ]

                for r in reports:
                    left_col, right_col = st.columns([0.82, 0.18])

                    with left_col:
                        st.markdown(f"<div class='report-name'>{r['name']}</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='report-meta'>{r['date']} • {r['size']}</div>", unsafe_allow_html=True)

                    with right_col:
                        file_path = assets_dir / r['name']
                        if file_path.exists():
                            data = file_path.read_bytes()
                            st.download_button(label="⬇", data=data, file_name=r['name'], use_container_width=True)
                        else:
                            if st.button("⬇", key=f"coming_{r['name']}"):
                                st.info("Download coming soon — backend report storage not configured.")
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
        # Backend not yet available for exports — show disabled button and WIP message
        st.markdown(
            """
            <div style="margin-top:0.6rem;">
                <button disabled style="background:#334155;color:var(--text-secondary);border-radius:6px;padding:8px 16px;border:none;cursor:not-allowed">Execute & Export</button>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.info("Backend - working in progress")

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Main Menu"):
    st.switch_page("Home.py")
