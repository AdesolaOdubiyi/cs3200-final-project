# pages/02_Map_Demo.py
# Stratify - Geospatial Analytics
# Persona: Political Strategy Advisor / Supply Chain Analyst

import sys
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

sys.path.append("..")
from stratify_theme import apply_stratify_theme
from modules.nav import SideBarLinks

apply_stratify_theme()
SideBarLinks()
# STYLES

st.markdown(
    """
<style>
.map-card {
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
# HEADER

st.markdown(
    """
    <div style="padding: 1.5rem 0 1rem 0;">
        <h1 style="font-size: 2.5rem; color: #f59e0b; margin-bottom: 0.25rem;">
            Geospatial Analytics
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Supply chain monitoring and asset distribution visualization
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)
# MAP CONTROLS

c1, c2 = st.columns([1, 3])

with c1:
    st.markdown('<div class="map-card">', unsafe_allow_html=True)
    st.markdown("### ⚙️ Layer Controls")
    
    show_assets = st.checkbox("Show Asset Locations", value=True)
    show_routes = st.checkbox("Show Supply Routes", value=True)
    show_risk = st.checkbox("Show Risk Zones", value=False)
    
    st.markdown("#### Filter by Region")
    st.multiselect("Regions", ["North America", "Europe", "APAC"], default=["North America", "Europe"])
    
    if st.button("Update Map View", type="primary"):
        show_stratify_loader(duration=1.5, message="Rendering Layers...", style="simultaneous")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown("### 🌍 Global Asset Distribution")
    
    # Mock Data
    # 1. Asset Locations (Scatterplot)
    assets_df = pd.DataFrame({
        "lat": np.random.normal(37.76, 10, 50),
        "lon": np.random.normal(-90, 20, 50),
        "value": np.random.randint(10, 100, 50)
    })
    
    # 2. Supply Routes (Arc)
    routes_df = pd.DataFrame({
        "start_lat": [37.77, 40.71, 51.50],
        "start_lon": [-122.41, -74.00, -0.12],
        "end_lat": [35.68, 48.85, 1.35],
        "end_lon": [139.69, 2.35, 103.81],
        "volume": [100, 50, 80]
    })
    
    layers = []
    
    if show_assets:
        layers.append(pdk.Layer(
            "ScatterplotLayer",
            data=assets_df,
            get_position=["lon", "lat"],
            get_color=[59, 130, 246, 160],
            get_radius="value * 1000",
            pickable=True,
        ))
        
    if show_routes:
        layers.append(pdk.Layer(
            "ArcLayer",
            data=routes_df,
            get_source_position=["start_lon", "start_lat"],
            get_target_position=["end_lon", "end_lat"],
            get_source_color=[34, 197, 94, 160],
            get_target_color=[239, 68, 68, 160],
            get_width=5,
        ))

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=pdk.ViewState(
            latitude=30,
            longitude=-40,
            zoom=1.5,
            pitch=0,
        ),
        layers=layers,
    ))
# FOOTER

st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Dashboard"):
    st.switch_page("Home.py")
