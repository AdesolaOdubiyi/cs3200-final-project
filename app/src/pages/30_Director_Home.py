# pages/30_Director_Home.py
# Stratify - Executive Overview & Strategy
# Persona: Sarah Martinez (Director of Portfolio Strategy)

import sys
import streamlit as st
import pandas as pd
import requests

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="Director Dashboard - Stratify",
    page_icon=None,
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
.exec-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
}

.exec-val {
    font-size: 2.5rem;
    font-weight: 800;
    font-family: 'Inter', sans-serif;
    margin: 0.5rem 0;
    background: -webkit-linear-gradient(45deg, #fff, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.drift-alert {
    padding: 1rem;
    background: rgba(245, 158, 11, 0.1);
    border: 1px solid #f59e0b;
    border-radius: 8px;
    margin-bottom: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
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
        <h1 style="font-size: 2.5rem; color: #e2e8f0; margin-bottom: 0.25rem;">
            Executive Overview
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Firm-wide performance, risk, and strategy alignment
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# FETCH DATA
# ============================================
summary_data = {}
alerts_data = []
activity_data = {}

try:
    summary_res = requests.get("http://web-api:4000/director/summary")
    if summary_res.status_code == 200:
        summary_data = summary_res.json()
        
    alerts_res = requests.get("http://web-api:4000/director/alerts")
    if alerts_res.status_code == 200:
        alerts_data = alerts_res.json()
        
    activity_res = requests.get("http://web-api:4000/director/activity")
    if activity_res.status_code == 200:
        activity_data = activity_res.json()
except:
    st.error("Backend connection failed. Using mock data.")
    # Fallback defaults
    summary_data = {"total_aum": 0, "ytd_growth": 0, "firm_alpha": 0, "active_strategies": 0, "drift_flags": 0}
    alerts_data = []
    activity_data = {"backtests_run": 0, "new_models": 0, "research_notes": 0}

# ============================================
# FIRM-WIDE METRICS
# ============================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f"""
        <div class="exec-card">
            <div style="color:#94a3b8; text-transform:uppercase; letter-spacing:1px;">Total AUM</div>
            <div class="exec-val">${summary_data.get('total_aum', 0)/1e9:.2f} Billion</div>
            <div style="color:#22c55e;">▲ {summary_data.get('ytd_growth', 0)}% YTD</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f"""
        <div class="exec-card">
            <div style="color:#94a3b8; text-transform:uppercase; letter-spacing:1px;">Firm-Wide Alpha</div>
            <div class="exec-val">+{summary_data.get('firm_alpha', 0)}%</div>
            <div style="color:#64748b;">vs Aggregate Benchmark</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f"""
        <div class="exec-card">
            <div style="color:#94a3b8; text-transform:uppercase; letter-spacing:1px;">Active Strategies</div>
            <div class="exec-val">{summary_data.get('active_strategies', 0)}</div>
            <div style="color:#f59e0b;">{summary_data.get('drift_flags', 0)} Flagged for Drift</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# STRATEGY DRIFT & ALERTS
# ============================================
col_main, col_side = st.columns([2, 1])

with col_main:
    st.markdown("### Performance vs Benchmark (Aggregated)")
    # Mock Chart (Frontend only for now as it's viz)
    chart_data = pd.DataFrame(
        {
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "Firm": [100, 105, 103, 108, 112, 115],
            "Benchmark": [100, 102, 101, 104, 106, 108],
        }
    )
    st.line_chart(chart_data.set_index("Month"), color=["#3b82f6", "#64748b"])
    
    st.markdown("### Analyst Activity")
    st.markdown(
        f"""
        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:1rem;">
            <div style="background:#1e293b; padding:1rem; border-radius:8px;">
                <div style="color:#94a3b8; font-size:0.8rem;">Backtests Run (Week)</div>
                <div style="font-size:1.5rem; font-weight:bold;">{activity_data.get('backtests_run', 0)}</div>
            </div>
            <div style="background:#1e293b; padding:1rem; border-radius:8px;">
                <div style="color:#94a3b8; font-size:0.8rem;">New Models Created</div>
                <div style="font-size:1.5rem; font-weight:bold;">{activity_data.get('new_models', 0)}</div>
            </div>
            <div style="background:#1e293b; padding:1rem; border-radius:8px;">
                <div style="color:#94a3b8; font-size:0.8rem;">Research Notes</div>
                <div style="font-size:1.5rem; font-weight:bold;">{activity_data.get('research_notes', 0)}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_side:
    st.markdown("### Strategy Drift Alerts")
    
    for alert in alerts_data:
        color = "#ef4444" if alert['severity'] == "high" else "#f59e0b"
        bg_style = f"background:rgba(239,68,68,0.1); border-color:#ef4444;" if alert['severity'] == "high" else ""
        
        st.markdown(
            f"""
            <div class="drift-alert" style="{bg_style}">
                <div>
                    <strong style="color:{color};">{alert['fund']}</strong><br>
                    <span style="font-size:0.8rem; color:#cbd5e1;">{alert['issue']}</span>
                </div>
                <button style="background:{color}; border:none; color:black; padding:0.25rem 0.5rem; border-radius:4px; font-size:0.8rem; cursor:pointer;">{alert['action']}</button>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("### Market Intelligence")
    st.info("Fed meeting minutes released: Hawkish tone implies rate volatility.")
    st.info("Tech sector rotation observed in last 48h.")

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("View Detailed Risk Report"):
    show_stratify_loader(duration=1, message="Loading Risk Dashboard...")
    st.switch_page("pages/02_Risk_Dashboard.py")
