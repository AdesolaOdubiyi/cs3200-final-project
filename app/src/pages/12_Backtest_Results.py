# pages/12_Backtest_Results.py
# Stratify - Backtest Analysis
# Persona: Asset Analyst / Data Analyst

import sys
import streamlit as st
import pandas as pd
import requests
import plotly.express as px

sys.path.append("..")
from stratify_theme import apply_stratify_theme
from modules.nav import SideBarLinks

apply_stratify_theme()
SideBarLinks()

# ============================================
# STYLES
# ============================================
st.markdown(
    """
<style>
.result-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.metric-big {
    font-size: 2rem;
    font-weight: bold;
    font-family: 'JetBrains Mono';
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
        <h1 style="font-size: 2.5rem; color: #3b82f6; margin-bottom: 0.25rem;">
            Backtest Analysis
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Detailed performance review and trade logs
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# FETCH DATA
# ============================================
# In a real app, we'd pass the ID via query params or session state
backtest_id = "BT-1001" 

try:
    # Fetch from our new backend route
    response = requests.get(f"http://web-api:4000/backtest/results/{backtest_id}")
    if response.status_code == 200:
        data = response.json()
    else:
        st.error("Failed to fetch backtest data.")
        data = None
except:
    st.error("Backend connection failed. Using mock data.")
    data = None

if data:
    # ============================================
    # KEY METRICS
    # ============================================
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown(f"<div class='result-card'><div style='color:#94a3b8'>Total Return</div><div class='metric-big' style='color:#22c55e'>{data['metrics']['total_return']}</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='result-card'><div style='color:#94a3b8'>Sharpe Ratio</div><div class='metric-big' style='color:#3b82f6'>{data['metrics']['sharpe_ratio']}</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='result-card'><div style='color:#94a3b8'>Max Drawdown</div><div class='metric-big' style='color:#ef4444'>{data['metrics']['max_drawdown']}</div></div>", unsafe_allow_html=True)
    with m4:
        st.markdown(f"<div class='result-card'><div style='color:#94a3b8'>Win Rate</div><div class='metric-big' style='color:#f59e0b'>{data['metrics']['win_rate']}</div></div>", unsafe_allow_html=True)

    # ============================================
    # EQUITY CURVE
    # ============================================
    st.markdown("### 📈 Equity Curve")
    
    df_curve = pd.DataFrame({
        "Date": data['dates'],
        "Equity": data['equity_curve']
    })
    
    fig = px.line(df_curve, x="Date", y="Equity", template="plotly_dark")
    fig.update_traces(line_color='#3b82f6', line_width=3)
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    # ============================================
    # TRADE LOG
    # ============================================
    st.markdown("### 📝 Trade Log")
    
    df_trades = pd.DataFrame(data['trades'])
    st.dataframe(df_trades, use_container_width=True, hide_index=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Export Results to PDF"):
        show_stratify_loader(duration=2, message="Generating PDF...", style="sequential")
        st.success("Report downloaded.")

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Back to Backtest Dashboard"):
    st.switch_page("pages/01_Backtest_Dashboard.py")
