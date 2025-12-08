# pages/01_Global_Macro_Data.py
# Stratify - Global Macro Data
# Persona: Economic Research / Analyst

import sys
import streamlit as st
import pandas as pd
import plotly.express as px

sys.path.append("..")
from stratify_theme import apply_stratify_theme
from modules.nav import SideBarLinks
from stratify_loader import show_stratify_loader

apply_stratify_theme()
SideBarLinks()

# ============================================
# STYLES
# ============================================
st.markdown(
    """
<style>
.macro-card {
    background: var(--bg-light);
    border: 1px solid var(--bg-border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.page-center {
    max-width: 1600px;
    margin: 0 auto;
    padding: 0 2rem;
}

/* Reduce top spacing of header */
.page-hero { padding-top: 0.6rem; padding-bottom: 0.4rem; }
.page-hero hr { margin-top: 0.25rem; margin-bottom: 1rem; border-color: var(--bg-border); }

/* Streamlit slider (rc-slider) styling for legibility */
[data-testid="stSlider"] .rc-slider-rail { height: 12px !important; background: rgba(255,255,255,0.06) !important; }
[data-testid="stSlider"] .rc-slider-track { height: 12px !important; background: linear-gradient(to right, var(--primary), var(--primary-dark)) !important; }
[data-testid="stSlider"] .rc-slider-handle { width: 16px !important; height: 16px !important; margin-top: -2px !important; border: 2px solid #ffffff !important; background: var(--primary-light) !important; }
[data-testid="stSlider"] .rc-slider-step { height: 12px !important; }

/* Plotly captions / annotations — force white */
.plotly-graph-div .main-svg { color: #fff !important; }

</style>
""",
    unsafe_allow_html=True,
)

# ============================================
# HEADER
# ============================================
st.markdown(
    """
    <div class="page-center page-hero">
        <h1 style="font-size: 2.5rem; color: var(--primary-dark); margin-bottom: 0.25rem; font-family:var(--font-main); text-transform:uppercase; letter-spacing:0.03em;">Global Macro Data</h1>
        <p style="font-size: 1rem; color: var(--text-tertiary); margin: 0; font-family:var(--font-main);">Economic indicators and development metrics (World Bank)</p>
        <hr>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================
# DATA SELECTOR
# ============================================
with st.container():
    # Center the selector horizontally using the page-center wrapper
    st.markdown('<div class="page-center">', unsafe_allow_html=True)
    st.markdown("### 🔍 Indicator Selection")

    col1, col2 = st.columns([2, 1])
    with col1:
        indicator = st.selectbox(
            "Select Economic Indicator",
            ["GDP (Current US$)", "Inflation, consumer prices (annual %)", "Population, total", "CO2 emissions (metric tons per capita)"],
            index=0,
        )
    with col2:
        # Replace the year slider with a compact dropdown to avoid vertical crowding
        years = list(range(1960, 2024))[::-1]  # show recent years first
        default_year = 2022
        try:
            default_index = years.index(default_year)
        except ValueError:
            default_index = 0
        year = st.selectbox("Select Year", years, index=default_index)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Fetch Data", type="primary"):
        # Ideally call World Bank API here; demo uses mocked data for speed
        show_stratify_loader(duration=2, message="Querying World Bank API...", style="sequential")
        st.session_state['wb_data_fetched'] = True
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# VISUALIZATION
# ============================================
if st.session_state.get('wb_data_fetched'):
    st.markdown("### 📊 Global Trends")

    # Demo/mock data for charts
    data = {
        "Country": ["United States", "China", "Japan", "Germany", "India", "United Kingdom", "France", "Brazil"],
        "Value": [25.46, 17.96, 4.23, 4.07, 3.38, 3.07, 2.78, 1.92],
        "Region": ["North America", "East Asia", "East Asia", "Europe", "South Asia", "Europe", "Europe", "Latin America"],
    }
    df = pd.DataFrame(data)

    # Give the chart more horizontal room (wider main column)
    c1, c2 = st.columns([4, 1])
    with c1:
        fig = px.bar(
            df,
            x="Country",
            y="Value",
            color="Region",
            title=f"{indicator} - Top Economies ({year})",
            template="plotly_dark",
            color_discrete_sequence=px.colors.qualitative.Bold,
        )
        # Improve legibility: white fonts, visible axis lines, angled x-ticks
        fig.update_traces(marker_line_color='rgba(255,255,255,0.12)', marker_line_width=1)
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#ffffff"),
            # Make the title text explicitly visible (keep default placement)
            title_font=dict(size=18, color="#ffffff", family="Inter, Arial, sans-serif"),
            xaxis=dict(
                tickangle=-45,
                tickfont=dict(color="#ffffff", size=11),
                showline=True,
                linecolor='rgba(255,255,255,0.18)',
                linewidth=1
            ),
            yaxis=dict(
                tickfont=dict(color="#ffffff", size=11),
                showline=True,
                linecolor='rgba(255,255,255,0.18)',
                linewidth=1,
                gridcolor='rgba(255,255,255,0.03)'
            ),
            legend=dict(font=dict(color="#ffffff")),
            margin=dict(l=40, r=20, t=90, b=120),
        )
        fig.update_traces(hoverlabel=dict(font_color="#000000"))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Use a plain container for insights to avoid the rounded empty card overlay
        with st.container():
            st.markdown("#### Key Insights")
            st.info("US and China account for >40% of global GDP.")
            st.info("Emerging markets showing ~2x growth rate vs developed economies.")
            st.markdown("#### Regional Breakdown")
            st.dataframe(df.groupby("Region")["Value"].sum().reset_index(), hide_index=True)

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Dashboard"):
    st.switch_page("Home.py")
