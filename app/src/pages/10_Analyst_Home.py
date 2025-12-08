# pages/10_Analyst_Home.py
# Stratify - Asset Management Analyst Home Dashboard
# Clean dark-mode version with minimal navigation UI


import sys
import streamlit as st


sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402


st.set_page_config(
   page_title="Analyst Dashboard - Stratify",
   page_icon=None,
   layout="wide"
)

from modules.nav import SideBarLinks
from stratify_theme import apply_stratify_theme

apply_stratify_theme()
SideBarLinks()
# GLOBAL DARK THEME + CARD STYLING

st.markdown("""
<style>
/* ==================== METRIC CARDS ==================== */
.metric-card {
   padding: 1.5rem;
   background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
   border: 1px solid #334155;
   border-radius: 12px;
   box-shadow: 0 4px 6px rgba(0,0,0,0.3);
   transition: all 0.3s ease;
}


.metric-card:hover {
   border-color: #3b82f6;
   box-shadow: 0 8px 16px rgba(59,130,246,0.2);
   transform: translateY(-2px);
}


.metric-label {
   color: #64748b;
   font-size: 0.85rem;
   font-weight: 600;
   text-transform: uppercase;
}


.metric-value {
   font-size: 2rem;
   font-weight: 700;
   font-family: "JetBrains Mono", monospace;
}


.metric-subtext {
   color: #94a3b8;
   font-size: 0.85rem;
   margin-top: 0.5rem;
}


/* Colored dots */
.metric-dot {
   width: 10px;
   height: 10px;
   border-radius: 999px;
   margin-right: 8px;
}
.dot-blue { background-color: #3b82f6; }
.dot-green { background-color: #22c55e; }
.dot-orange { background-color: #fb923c; }
.dot-purple { background-color: #a855f7; }


/* ==================== EMPTY STATE ==================== */
.empty-state {
   padding: 2rem;
   background: #1e293b;
   border: 2px dashed #475569;
   border-radius: 8px;
   text-align: center;
}
.empty-state h4 {
   color: #cbd5e1;
}
.empty-state p {
   color: #94a3b8;
}


/* ==================== NAVIGATION BUTTONS ==================== */
.nav-dark-btn > button {
   width: 100% !important;
   height: 50px !important;
   background-color: #1e293b !important;
   color: #e2e8f0 !important;
   border: 1px solid #334155 !important;
   border-radius: 10px !important;
   font-size: 1rem !important;
   transition: all 0.2s ease;
}
.nav-dark-btn > button:hover {
   background-color: #334155 !important;
   border-color: #3b82f6 !important;
   color: #ffffff !important;
}


/* Footer */
.stratify-footer {
   text-align: center;
   padding: 2rem 0;
   color: #64748b;
   font-size: 0.85rem;
   border-top: 1px solid #334155;
   margin-top: 2rem;
}
.stratify-footer-subtext {
   font-size: 0.75rem;
   color: #475569;
}
</style>
""", unsafe_allow_html=True)
# HEADER

def render_header():
   st.markdown("""
       <div style="text-align:center; padding: 2rem 0 1rem 0;">
           <h1 style="font-size:2.5rem; color:#60a5fa;">Analyst Dashboard</h1>
           <p style="font-size:1.1rem; color:#94a3b8;">
               Welcome back, Jonathan Chen | Asset Management Analyst
           </p>
       </div>
   """, unsafe_allow_html=True)
   st.markdown("---")
# METRICS

def render_key_metrics():
   st.markdown("### Portfolio Overview")
   col1, col2, col3, col4 = st.columns(4)


   with col1:
       st.markdown("""
           <div class="metric-card">
               <div style="display:flex;align-items:center;">
                   <div class="metric-dot dot-blue"></div>
                   <span class="metric-label">Active Portfolios</span>
               </div>
               <div class="metric-value" style="color:#3b82f6;">--</div>
               <div class="metric-subtext">Currently managing</div>
           </div>
       """, unsafe_allow_html=True)


   with col2:
       st.markdown("""
           <div class="metric-card">
               <div style="display:flex;align-items:center;">
                   <div class="metric-dot dot-green"></div>
                   <span class="metric-label">Total Positions</span>
               </div>
               <div class="metric-value" style="color:#22c55e;">--</div>
               <div class="metric-subtext">Across portfolios</div>
           </div>
       """, unsafe_allow_html=True)


   with col3:
       st.markdown("""
           <div class="metric-card">
               <div style="display:flex;align-items:center;">
                   <div class="metric-dot dot-orange"></div>
                   <span class="metric-label">Best Performer</span>
               </div>
               <div class="metric-value" style="color:#f59e0b;">--</div>
               <div class="metric-subtext">YTD return</div>
           </div>
       """, unsafe_allow_html=True)


   with col4:
       st.markdown("""
           <div class="metric-card">
               <div style="display:flex;align-items:center;">
                   <div class="metric-dot dot-purple"></div>
                   <span class="metric-label">Watchlist Items</span>
               </div>
               <div class="metric-value" style="color:#a855f7;">--</div>
               <div class="metric-subtext">Stocks monitored</div>
           </div>
       """, unsafe_allow_html=True)


   st.write("")
# QUICK ACTIONS

def render_quick_actions():
   st.markdown("### Quick Actions")
   col1, col2, col3, col4 = st.columns(4)


   with col1:
       if st.button("Create New Portfolio", use_container_width=True):
           show_stratify_loader(duration=1)
           st.switch_page("pages/11_Portfolio_Manager.py")


   with col2:
       if st.button("Run Backtest", use_container_width=True):
           show_stratify_loader(duration=1.2)
           st.switch_page("pages/01_Backtest_Dashboard.py")


   with col3:
       if st.button("Manage Watchlist", use_container_width=True):
           show_stratify_loader(duration=1)
           # Placeholder for watchlist management
           st.toast("Watchlist Management Coming Soon")


   with col4:
       if st.button("View All Portfolios", use_container_width=True):
           show_stratify_loader(duration=1)
           st.switch_page("pages/11_Portfolio_Manager.py")


   st.markdown("---")
# EMPTY STATE

def render_empty_state(title):
   st.markdown(f"""
       <div class="empty-state">
           <h4>{title}</h4>
       </div>
   """, unsafe_allow_html=True)
# PORTFOLIOS / BACKTESTS / WATCHLIST

def render_portfolios_section():
   st.markdown("### My Portfolios")
   render_empty_state("No portfolios yet")
   st.write("")


def render_backtests_section():
   st.markdown("### Recent Backtests")
   render_empty_state("No backtests yet")
   st.write("")


def render_watchlist_section():
   st.markdown("### My Watchlist")
   render_empty_state("Your watchlist is empty")
   st.markdown("---")
# CLEAN MINIMAL NAVIGATION BUTTONS

def render_navigation_section():
   st.markdown("### Navigate to Other Dashboards")
   st.write("")


   col1, col2, col3 = st.columns(3)


   with col1:
       st.markdown('<div class="nav-dark-btn">', unsafe_allow_html=True)
       if st.button("Go to Backtest Dashboard", use_container_width=True, key="nav_backtest"):
           show_stratify_loader(duration=1)
           st.switch_page("pages/01_Backtest_Dashboard.py")
       st.markdown('</div>', unsafe_allow_html=True)


   with col2:
       st.markdown('<div class="nav-dark-btn">', unsafe_allow_html=True)
       if st.button("Go to Risk Dashboard", use_container_width=True, key="nav_risk"):
           show_stratify_loader(duration=1)
           st.switch_page("pages/02_Risk_Dashboard.py")
       st.markdown('</div>', unsafe_allow_html=True)


   with col3:
       st.markdown('<div class="nav-dark-btn">', unsafe_allow_html=True)
       if st.button("Go to Portfolio Manager", use_container_width=True, key="nav_portfolio"):
           show_stratify_loader(duration=1)
           st.switch_page("pages/11_Portfolio_Manager.py")
       st.markdown('</div>', unsafe_allow_html=True)


   st.markdown("---")
# HELP + FOOTER

def render_help_section():
   with st.expander("Getting Started Guide"):
       st.markdown("""
           - Create model portfolios 
           - Run backtests 
           - Track watchlists 
           - Compare benchmark performance 
       """)


def render_footer():
   st.markdown("""
       <div class="stratify-footer">
           Stratify Portfolio Intelligence Platform<br>
           <span class="stratify-footer-subtext">
               Test strategies with zero financial risk • Data-driven confidence
           </span>
       </div>
   """, unsafe_allow_html=True)
# PAGE RENDER ORDER

render_header()
render_key_metrics()
render_quick_actions()
render_portfolios_section()
render_backtests_section()
render_watchlist_section()
render_navigation_section()
render_help_section()
render_footer()
