import streamlit as st
import logging
from stratify_theme import apply_stratify_theme
from stratify_loader import show_stratify_loader
from modules.nav import SideBarLinks

# Set up logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Page Config
st.set_page_config(
    page_title="Stratify",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Theme
apply_stratify_theme()

# Initialize Session State
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Sidebar
SideBarLinks(show_home=True)

# CUSTOM CSS FOR HOME
st.markdown("""
<style>
    /* Hero Specific Styling */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 4rem 0;
        text-align: center;
    }
    
    .hero-title {
        font-size: 5rem;
        font-weight: 800;
        letter-spacing: -0.05em;
        background: linear-gradient(135deg, #fff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #94a3b8 !important;
        max-width: 600px;
        line-height: 1.6;
        font-weight: 300;
    }
    
    .role-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 2rem;
        transition: all 0.3s ease;
        height: 100%;
        backdrop-filter: blur(10px);
    }
    
    .role-card:hover {
        border-color: #3b82f6;
        transform: translateY(-5px);
        box-shadow: 0 10px 30px -10px rgba(59, 130, 246, 0.3);
    }
    
    .role-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #e2e8f0 !important;
    }
    
    .role-desc {
        font-size: 0.9rem;
        color: #64748b !important;
        margin-bottom: 1.5rem;
    }
    
    .stat-box {
        text-align: center;
        padding: 1rem;
        border-right: 1px solid #334155;
    }
    .stat-box:last-child {
        border-right: none;
    }
    
    .stat-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #3b82f6 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .stat-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #64748b !important;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
st.image("assets/logo_clean.png", width=140)
st.markdown("""
    <div class="hero-title">STRATIFY</div>
    <div class="hero-subtitle">
        Institutional-grade portfolio intelligence and risk management platform. 
        Engineered for the modern financial era.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# KEY METRICS
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-value">$4.2B</div>
        <div class="stat-label">Assets Under Management</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-value">12ms</div>
        <div class="stat-label">Execution Latency</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-value">99.9%</div>
        <div class="stat-label">System Uptime</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-value">24/7</div>
        <div class="stat-label">Global Coverage</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# ACCESS PORTAL
st.markdown("### Select Workspace")
st.markdown("<div style='color:#64748b; margin-bottom:2rem;'>Choose a role to enter the platform environment.</div>", unsafe_allow_html=True)

r1, r2, r3, r4 = st.columns(4)

with r1:
    st.markdown("""
    <div class="role-card">
        <div class="role-title">Asset Analyst</div>
        <div class="role-desc">Portfolio construction, backtesting, and performance attribution.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Enter as Analyst", use_container_width=True):
        show_stratify_loader(duration=1)
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'analyst'
        st.switch_page('pages/10_Analyst_Home.py')

with r2:
    st.markdown("""
    <div class="role-card">
        <div class="role-title">Data Scientist</div>
        <div class="role-desc">Machine learning model development and predictive analytics.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Enter as Data Sci", use_container_width=True):
        show_stratify_loader(duration=1)
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'data_analyst'
        st.switch_page('pages/00_Data_Analyst_Home.py')

with r3:
    st.markdown("""
    <div class="role-card">
        <div class="role-title">Director</div>
        <div class="role-desc">Executive oversight, firm-wide risk, and strategic planning.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Enter as Director", use_container_width=True):
        show_stratify_loader(duration=1)
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'director'
        st.switch_page('pages/30_Director_Home.py')

with r4:
    st.markdown("""
    <div class="role-card">
        <div class="role-title">Administrator</div>
        <div class="role-desc">System configuration, user management, and infrastructure.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Enter as Admin", use_container_width=True):
        show_stratify_loader(duration=1)
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'administrator'
        st.switch_page('pages/20_Admin_Home.py')

# FOOTER
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #475569; font-size: 0.8rem; border-top: 1px solid #1e293b; padding-top: 2rem;">
        STRATIFY PLATFORM v2.5.0 • INSTITUTIONAL EDITION<br>
        SECURE CONNECTION • ENCRYPTED
    </div>
""", unsafe_allow_html=True)
