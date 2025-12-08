# pages/02_Risk_Dashboard.py
# Stratify - Risk Intelligence & Exposure Monitoring
# Personas: Noah Harrison (Data Analyst), Sarah Martinez (Director)

import sys
import pandas as pd
import streamlit as st

sys.path.append("..")

from stratify_loader import show_stratify_loader  # noqa: E402
from modules.nav import SideBarLinks
from stratify_theme import apply_stratify_theme, get_color


# ------------------------------------------------------------------------------
# PAGE CONFIG & THEME
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Risk Dashboard - Stratify",
    page_icon="🛡️",
    layout="wide",
)

apply_stratify_theme()
SideBarLinks()


# ------------------------------------------------------------------------------
# CUSTOM STYLES
# ------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .metric-box {
        background: var(--bg-light);
        border: 1px solid var(--bg-border);
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
    }

    .metric-val {
        font-size: 2rem;
        font-weight: 700;
        font-family: var(--font-mono);
        margin: 0.5rem 0;
        color: var(--text-primary);
    }

    .metric-lbl {
        color: var(--text-tertiary);
        font-size: 0.85rem;
        text-transform: uppercase;
    }

    .risk-card {
        background: var(--bg-light);
        border: 1px solid var(--bg-border);
        border-radius: 12px;
        padding: 1.5rem;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------------------
st.markdown(
    """
    <div style="padding: 1.5rem 0 1rem 0;">
        <h1 style="font-size: 2.5rem; margin-bottom: 0.25rem;">
            Risk Intelligence
        </h1>
        <p style="font-size: 1rem; color: var(--text-tertiary); margin: 0;">
            Firm-wide exposure monitoring and stress testing
        </p>
    </div>
    <hr style="border-color: var(--bg-border); margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------------------------
# KEY RISK METRICS
# ------------------------------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="metric-box">
            <div class="metric-lbl">Value at Risk (95%)</div>
            <div class="metric-val" style="color: var(--error);">$42.5K</div>
            <div style="color: var(--text-tertiary); font-size:0.8rem;">Daily VaR</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="metric-box">
            <div class="metric-lbl">Portfolio Beta</div>
            <div class="metric-val" style="color: var(--primary);">1.15</div>
            <div style="color: var(--text-tertiary); font-size:0.8rem;">vs S&P 500</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="metric-box">
            <div class="metric-lbl">Sharpe Ratio</div>
            <div class="metric-val" style="color: var(--success);">1.84</div>
            <div style="color: var(--text-tertiary); font-size:0.8rem;">Risk-Adjusted Return</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        """
        <div class="metric-box">
            <div class="metric-lbl">Max Drawdown</div>
            <div class="metric-val" style="color: var(--warning);">-12.4%</div>
            <div style="color: var(--text-tertiary); font-size:0.8rem;">Trailing 12M</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# EXPOSURE ANALYSIS
# ------------------------------------------------------------------------------
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown('<div class="risk-card">', unsafe_allow_html=True)
    st.markdown("### 🗺️ Sector Exposure Heatmap")

    # Mock exposure data (replace with real portfolio exposures)
    sectors = ["Tech", "Finance", "Energy", "Healthcare", "Consumer"]
    exposure = [45, 30, 15, 5, 5]

    chart_data = pd.DataFrame(
        {
            "Sector": sectors,
            "Exposure (%)": exposure,
        }
    )

    st.bar_chart(
        chart_data.set_index("Sector"),
        color=get_color("primary"),
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="risk-card">', unsafe_allow_html=True)
    st.markdown("### ⚠️ Concentration Alerts")

    st.markdown(
        """
        <div style="margin-top:1rem;">
            <div style="padding:0.75rem; background:rgba(239,68,68,0.08); border-left:4px solid var(--error); margin-bottom:0.5rem; border-radius:4px;">
                <strong style="color:var(--error);">High Tech Exposure</strong><br>
                <span style="font-size:0.85rem; color:var(--text-secondary);">
                    Portfolio A exceeds 40% limit (Current: 45%)
                </span>
            </div>

            <div style="padding:0.75rem; background:rgba(245,158,11,0.08); border-left:4px solid var(--warning); margin-bottom:0.5rem; border-radius:4px;">
                <strong style="color:var(--warning);">Correlation Spike</strong><br>
                <span style="font-size:0.85rem; color:var(--text-secondary);">
                    Tech &amp; Crypto correlation &gt; 0.85
                </span>
            </div>

            <div style="padding:0.75rem; background:rgba(59,130,246,0.08); border-left:4px solid var(--primary); border-radius:4px;">
                <strong style="color:var(--primary);">Liquidity Watch</strong><br>
                <span style="font-size:0.85rem; color:var(--text-secondary);">
                    Small cap positions &lt; 2 days volume
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# STRESS TESTING
# ------------------------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🌪️ Scenario Stress Testing")

with st.expander("Run Stress Test Scenario", expanded=True):
    sc_col1, sc_col2 = st.columns([3, 1])

    with sc_col1:
        scenario = st.selectbox(
            "Select Market Scenario",
            [
                "2008 Financial Crisis (-50%)",
                "Tech Bubble Burst (-30% Tech)",
                "Interest Rate Hike (+200bps)",
                "Oil Price Shock (+50%)",
            ],
        )

    with sc_col2:
        st.write("")
        st.write("")
        if st.button("Simulate Impact", use_container_width=True, type="primary"):
            show_stratify_loader(
                duration=2,
                message="Running Monte Carlo Simulation...",
                style="cascade",
            )
            st.error("Estimated Portfolio Impact: -18.4% ($175,800 Loss)")


# ------------------------------------------------------------------------------
# FOOTER NAVIGATION
# ------------------------------------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

f_col1, f_col2 = st.columns(2)

with f_col1:
    if st.button("← Back to Analyst Home"):
        st.switch_page("pages/10_Analyst_Home.py")

with f_col2:
    if st.button("Go to Director Dashboard →"):
        st.switch_page("pages/30_Director_Home.py")