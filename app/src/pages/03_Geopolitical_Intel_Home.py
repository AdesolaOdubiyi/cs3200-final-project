# pages/03_Geopolitical_Intel_Home.py
# Stratify - Geopolitical Intelligence & Risk
# Persona: Political Strategy Advisor / Director

import sys
import pandas as pd
import streamlit as st

sys.path.append("..")

from stratify_theme import apply_stratify_theme
from modules.nav import SideBarLinks
from stratify_loader import show_stratify_loader


# ------------------------------------------------------------------------------
# PAGE CONFIG & THEME
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Geopolitical Intelligence - Stratify",
    page_icon="🌐",
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
    .geo-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    .risk-level-high {
        color: #ef4444;
        font-weight: bold;
        text-transform: uppercase;
    }

    .risk-level-med {
        color: #f59e0b;
        font-weight: bold;
        text-transform: uppercase;
    }

    .risk-level-low {
        color: #22c55e;
        font-weight: bold;
        text-transform: uppercase;
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
        <h1 style="font-size: 2.5rem; color: #38bdf8; margin-bottom: 0.25rem;">
            Geopolitical Intelligence
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Geopolitical risk monitoring and market impact analysis
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------------------------
# WORLD MAP VISUALIZATION (Placeholder)
# ------------------------------------------------------------------------------
st.markdown("### 🗺️ Geopolitical Risk Map")

map_data = pd.DataFrame(
    {
        "lat": [37.77, 51.50, 35.68, 1.35, 40.71, 48.85, 55.75, 25.20],
        "lon": [-122.41, -0.12, 139.69, 103.81, -74.00, 2.35, 37.61, 55.27],
        "risk_score": [10, 20, 15, 5, 12, 18, 85, 45],
    }
)

st.map(
    map_data,
    latitude="lat",
    longitude="lon",
    size="risk_score",
    color="risk_score",
    zoom=1,
)


# ------------------------------------------------------------------------------
# INTELLIGENCE FEED & REGIONAL RISK INDEX
# ------------------------------------------------------------------------------
c1, c2 = st.columns([2, 1])

with c1:
    st.markdown("### 📡 Live Intelligence Feed")

    events = [
        {
            "region": "Eastern Europe",
            "event": "Energy supply chain disruption reported",
            "impact": "High",
            "sector": "Energy",
        },
        {
            "region": "South East Asia",
            "event": "Trade agreement negotiations stalled",
            "impact": "Medium",
            "sector": "Manufacturing",
        },
        {
            "region": "North America",
            "event": "New fiscal policy announcement expected",
            "impact": "Low",
            "sector": "Finance",
        },
    ]

    for e in events:
        risk_class = (
            "risk-level-high"
            if e["impact"] == "High"
            else "risk-level-med"
            if e["impact"] == "Medium"
            else "risk-level-low"
        )

        st.markdown(
            f"""
            <div class="geo-card">
                <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
                    <span style="color:#94a3b8; font-size:0.9rem;">{e['region']}</span>
                    <span class="{risk_class}">{e['impact']} Impact</span>
                </div>
                <div style="font-size:1.1rem; font-weight:bold; margin-bottom:0.5rem;">
                    {e['event']}
                </div>
                <div style="display:inline-block; background:#334155; padding:0.2rem 0.6rem; border-radius:12px; font-size:0.8rem; color:#e2e8f0;">
                    Affected Sector: {e['sector']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with c2:
    st.markdown("### 📊 Regional Risk Index")

    risk_data = pd.DataFrame(
        {
            "Region": ["North America", "Europe", "Asia Pacific", "MENA", "LatAm"],
            "Risk Score": [12, 24, 35, 68, 42],
        }
    )

    st.dataframe(
        risk_data,
        column_config={
            "Risk Score": st.column_config.ProgressColumn(
                "Risk Score",
                help="0-100 Risk Index",
                format="%d",
                min_value=0,
                max_value=100,
            ),
        },
        hide_index=True,
        use_container_width=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Download Full Report", use_container_width=True):
        show_stratify_loader(
            duration=2,
            message="Generating PDF Report...",
            style="sequential",
        )
        st.success("Report downloaded successfully")


# ------------------------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("← Return to Dashboard"):
    st.switch_page("Home.py")