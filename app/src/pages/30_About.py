# pages/30_About.py
# Stratify - About Page

import sys
import streamlit as st

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="About - Stratify",
    page_icon="ℹ️",
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
.tech-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    transition: transform 0.2s;
}
.tech-card:hover {
    transform: translateY(-5px);
    border-color: #3b82f6;
}

.tech-icon {
    font-size: 2.5rem;
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
    <div style="text-align: center; padding: 3rem 0;">
        <h1 style="font-size: 3.5rem; font-weight: 800; background: -webkit-linear-gradient(45deg, #3b82f6, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            STRATIFY
        </h1>
        <p style="font-size: 1.2rem; color: #94a3b8; max-width: 600px; margin: 0 auto;">
            Next-generation portfolio management and analytics platform for the modern financial era.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================
# PROJECT INFO
# ============================================
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("### 🎯 Project Goal")
    st.markdown(
        """
        Stratify was built for the **Data and Software in International Government and Politics Dialogue 2025** course.
        
        It demonstrates a full-stack data application architecture, integrating:
        - **Role-Based Access Control (RBAC)** for diverse personas.
        - **Real-time Analytics** for financial decision making.
        - **AI/ML Integration** for predictive modeling.
        - **Modern UI/UX** principles for complex data visualization.
        """
    )

with c2:
    st.markdown("### 👥 Personas Supported")
    st.markdown(
        """
        - **Jonathan Chen**: Asset Analyst (Portfolio Mgmt, Backtesting)
        - **Noah Harrison**: Data Analyst (ML Models, Risk Analysis)
        - **Sarah Martinez**: Director (Strategy, Firm Oversight)
        - **Rajesh Singh**: Administrator (System Health, User Mgmt)
        """
    )

# ============================================
# TECH STACK
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>🛠️ Technology Stack</h3>", unsafe_allow_html=True)

tc1, tc2, tc3, tc4 = st.columns(4)

with tc1:
    st.markdown(
        """
        <div class="tech-card">
            <div class="tech-icon">🐍</div>
            <div style="font-weight:bold; font-size:1.1rem;">Python</div>
            <div style="color:#94a3b8; font-size:0.9rem;">Core Logic</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with tc2:
    st.markdown(
        """
        <div class="tech-card">
            <div class="tech-icon">👑</div>
            <div style="font-weight:bold; font-size:1.1rem;">Streamlit</div>
            <div style="color:#94a3b8; font-size:0.9rem;">Frontend UI</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with tc3:
    st.markdown(
        """
        <div class="tech-card">
            <div class="tech-icon">🌶️</div>
            <div style="font-weight:bold; font-size:1.1rem;">Flask</div>
            <div style="color:#94a3b8; font-size:0.9rem;">Backend API</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with tc4:
    st.markdown(
        """
        <div class="tech-card">
            <div class="tech-icon">🐳</div>
            <div style="font-weight:bold; font-size:1.1rem;">Docker</div>
            <div style="color:#94a3b8; font-size:0.9rem;">Containerization</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
c_foot = st.columns([1, 1, 1])
with c_foot[1]:
    if st.button("Return to Home", type="primary", use_container_width=True):
        st.switch_page("Home.py")
