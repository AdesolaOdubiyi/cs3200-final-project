# pages/31_Firm_Dashboard.py
# Stratify - Firm Performance Analytics
# Persona: Director / Executive

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
.firm-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
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
            Firm Performance
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Comprehensive view of AUM, fund performance, and risk distribution
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# FETCH DATA
# ============================================
try:
    response = requests.get("http://web-api:4000/performance/firm/summary")
    if response.status_code == 200:
        data = response.json()
    else:
        st.error("Failed to fetch firm data.")
        data = None
except:
    st.error("Backend connection failed. Using mock data.")
    data = None

if data:
    # ============================================
    # TOP LEVEL METRICS
    # ============================================
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(
            f"""
            <div class="firm-card">
                <div style="color:#94a3b8; font-size:0.9rem;">Total AUM</div>
                <div style="font-size:2.5rem; font-weight:bold; color:#22c55e;">${data['total_aum']/1e9:.2f}B</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            f"""
            <div class="firm-card">
                <div style="color:#94a3b8; font-size:0.9rem;">YTD Return</div>
                <div style="font-size:2.5rem; font-weight:bold; color:#3b82f6;">+{data['ytd_return']}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            f"""
            <div class="firm-card">
                <div style="color:#94a3b8; font-size:0.9rem;">Active Strategies</div>
                <div style="font-size:2.5rem; font-weight:bold; color:#f59e0b;">{data['active_strategies']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ============================================
    # FUND PERFORMANCE TABLE
    # ============================================
    st.markdown("### 📊 Fund Performance")
    
    df_funds = pd.DataFrame(data['funds'])
    
    # Format AUM
    df_funds['aum'] = df_funds['aum'].apply(lambda x: f"${x/1e6:.1f}M")
    df_funds['return'] = df_funds['return'].apply(lambda x: f"{x}%")
    
    st.dataframe(
        df_funds,
        use_container_width=True,
        hide_index=True,
        column_config={
            "name": "Fund Name",
            "aum": "Assets Under Management",
            "return": "YTD Return",
            "risk": "Risk Profile"
        }
    )
    
    # ============================================
    # VISUALIZATION
    # ============================================
    st.markdown("### 🥧 AUM Distribution")
    
    fig = px.pie(data['funds'], values='aum', names='name', hole=0.4, template="plotly_dark")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    
    col_viz, _ = st.columns([2, 1])
    with col_viz:
        st.plotly_chart(fig, use_container_width=True)

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Director Home"):
    st.switch_page("pages/30_Director_Home.py")
