# pages/10_USAID_Worker_Home.py
# Stratify - ESG & Impact Investing
# Persona: Impact Analyst / USAID Worker

import sys
import streamlit as st
import pandas as pd

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="ESG & Impact - Stratify",
    page_icon="🌱",
    layout="wide",
)

from modules.nav import SideBarLinks
from stratify_theme import apply_stratify_theme

apply_stratify_theme()
SideBarLinks()
# STYLES

st.markdown(
    """
<style>
.esg-card { background: var(--bg-light); border: 1px solid var(--bg-border); border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; text-align: center; }
.esg-score { font-size: 2.5rem; font-weight: 800; color: var(--success); margin: 0.5rem 0; }
.esg-subtext { color: var(--text-tertiary); }
</style>
""",
    unsafe_allow_html=True,
)
# HEADER

st.markdown(
    """
    <div style="padding: 1.5rem 0 1rem 0;">
        <h1 style="font-size: 2.5rem; color: var(--success); margin-bottom: 0.25rem;">ESG & Impact</h1>
        <p style="font-size: 1rem; color: var(--text-tertiary); margin: 0;">Environmental, Social, and Governance performance tracking</p>
    </div>
    <hr style="border-color: var(--bg-border); margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)
# ESG OVERVIEW

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="esg-card">
            <div style="color:var(--text-tertiary); text-transform:uppercase;">Environmental Score</div>
            <div class="esg-score">84</div>
            <div style="color:var(--success);">Top 10% of Peers</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="esg-card">
            <div style="color:var(--text-tertiary); text-transform:uppercase;">Social Score</div>
            <div class="esg-score" style="color:var(--warning);">62</div>
            <div style="color:var(--warning);">Average Performance</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="esg-card">
            <div style="color:var(--text-tertiary); text-transform:uppercase;">Governance Score</div>
            <div class="esg-score" style="color:var(--primary);">91</div>
            <div style="color:var(--primary);">Industry Leader</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
# IMPACT PORTFOLIO

st.markdown("### 🌍 Impact Portfolio Holdings")

df = pd.DataFrame({
    "Organization": ["Green Energy Corp", "Water For All", "EduTech Global", "Sustainable Agri"],
    "Sector": ["Renewables", "Utilities", "Education", "Agriculture"],
    "Impact Metric": ["1.2M Tons CO2 Saved", "500K People Served", "2M Students Reached", "10K Farmers Supported"],
    "ESG Rating": ["AAA", "AA", "A", "AA+"]
})

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
# ACTIONS

st.markdown("<br>", unsafe_allow_html=True)
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### 📋 NGO Directory")
    st.info("Access the global database of verified NGOs and impact funds.")
    if st.button("Browse Directory"):
        show_stratify_loader(duration=1, message="Loading Directory...")
        # In a real app, this would link to pages/14_NGO_Directory.py
        st.success("Directory Loaded (Demo)")

with col_b:
    st.markdown("### ➕ Add New Impact Fund")
    st.info("Submit a new organization for ESG screening and verification.")
    if st.button("Submit New Fund"):
        show_stratify_loader(duration=1, message="Opening Form...")
        # In a real app, this would link to pages/15_Add_NGO.py
        st.success("Form Opened (Demo)")
# FOOTER

st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Dashboard"):
    st.switch_page("Home.py")