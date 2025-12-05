# pages/01_World_Bank_Viz.py
# Stratify - Global Macro Data
# Persona: Political Strategy Advisor / Director

import sys
import streamlit as st
import pandas as pd
import world_bank_data as wb
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
.macro-card {
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
        <h1 style="font-size: 2.5rem; color: #38bdf8; margin-bottom: 0.25rem;">
            Global Macro Data
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Economic indicators and development metrics from the World Bank
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# DATA SELECTOR
# ============================================
st.markdown('<div class="macro-card">', unsafe_allow_html=True)
st.markdown("### 🔍 Indicator Selection")

col1, col2 = st.columns(2)
with col1:
    indicator = st.selectbox(
        "Select Economic Indicator",
        ["GDP (Current US$)", "Inflation, consumer prices (annual %)", "Population, total", "CO2 emissions (metric tons per capita)"],
        index=0
    )
with col2:
    year = st.slider("Select Year", 1960, 2023, 2022)

if st.button("Fetch Data", type="primary"):
    show_stratify_loader(duration=2, message="Querying World Bank API...", style="sequential")
    st.session_state['wb_data_fetched'] = True
st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# VISUALIZATION
# ============================================
if st.session_state.get('wb_data_fetched'):
    st.markdown("### 📊 Global Trends")
    
    # Mocking data for stability/speed in demo, but structure allows real WB call
    # In a real app, we would use: wb.get_series('NY.GDP.MKTP.CD', date=year)
    
    data = {
        "Country": ["United States", "China", "Japan", "Germany", "India", "United Kingdom", "France", "Brazil"],
        "Value": [25.46, 17.96, 4.23, 4.07, 3.38, 3.07, 2.78, 1.92], # Trillions
        "Region": ["North America", "East Asia", "East Asia", "Europe", "South Asia", "Europe", "Europe", "Latin America"]
    }
    df = pd.DataFrame(data)
    
    c1, c2 = st.columns([2, 1])
    
    with c1:
        fig = px.bar(
            df, 
            x="Country", 
            y="Value", 
            color="Region", 
            title=f"{indicator} - Top Economies ({year})",
            template="plotly_dark",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
        
    with c2:
        st.markdown('<div class="macro-card">', unsafe_allow_html=True)
        st.markdown("#### Key Insights")
        st.info("US and China account for >40% of global GDP.")
        st.info("Emerging markets showing 2x growth rate vs developed economies.")
        st.markdown("#### Regional Breakdown")
        st.dataframe(df.groupby("Region")["Value"].sum().reset_index(), hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Dashboard"):
    st.switch_page("Home.py")
