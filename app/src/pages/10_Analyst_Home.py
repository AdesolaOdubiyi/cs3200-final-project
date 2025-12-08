# pages/10_Analyst_Home.py
# Stratify - Asset Management Analyst Home Dashboard
# Clean dark-mode version with minimal navigation UI

import sys

import streamlit as st

sys.path.append("..")

from stratify_loader import show_stratify_loader  # noqa: E402
from modules.nav import SideBarLinks
from stratify_theme import apply_stratify_theme


# ------------------------------------------------------------------------------
# PAGE CONFIG & THEME
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Analyst Dashboard - Stratify",
    page_icon="📊",
    layout="wide",
)

apply_stratify_theme()
SideBarLinks()


# ------------------------------------------------------------------------------
# GLOBAL DARK THEME + CARD STYLING
# ------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* ==================== METRIC CARDS ==================== */
    .metric-card {
        padding: 1.5rem;
        background: linear-gradient(135deg, var(--bg-light) 0%, var(--bg-white) 100%);
        border: 1px solid var(--bg-border);
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }

    .metric-card:hover {
        border-color: var(--primary);
        box-shadow: 0 8px 16px rgba(59,130,246,0.08);
        transform: translateY(-2px);
    }

    .metric-label {
        color: var(--text-secondary);
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        font-family: var(--font-mono);
    }

    .metric-subtext {
        color: var(--text-tertiary);
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
    .dot-blue { background-color: var(--primary); }
    .dot-green { background-color: var(--success); }
    .dot-orange { background-color: var(--warning); }
    .dot-purple { background-color: #a855f7; }

    /* ==================== EMPTY STATE ==================== */
    .empty-state {
        padding: 2rem;
        background: var(--bg-light);
        border: 2px dashed var(--bg-border);
        border-radius: 8px;
        text-align: center;
    }

    .empty-state h4 {
        color: var(--text-primary);
    }

    .empty-state p {
        color: var(--text-tertiary);
    }

    /* ==================== NAVIGATION BUTTONS ==================== */
    .nav-dark-btn > button {
        width: 100% !important;
        height: 50px !important;
        background-color: transparent !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--bg-border) !important;
        border-radius: 10px !important;
        font-size: 1rem !important;
        transition: all 0.2s ease;
    }

    .nav-dark-btn > button:hover {
        background-color: rgba(59,130,246,0.06) !important;
        border-color: var(--primary) !important;
        color: #ffffff !important;
    }

    /* Footer */
    .stratify-footer {
        text-align: center;
        padding: 2rem 0;
        color: var(--text-secondary);
        font-size: 0.85rem;
        border-top: 1px solid var(--bg-border);
        margin-top: 2rem;
    }

    .stratify-footer-subtext {
        font-size: 0.75rem;
        color: var(--bg-medium);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------------------
def render_header() -> None:
    st.markdown(
        """
        <div style="text-align:center; padding: 2rem 0 1rem 0;">
            <h1 style="font-size:2.5rem; color:var(--primary);">Analyst Dashboard</h1>
            <p style="font-size:1.1rem; color:var(--text-tertiary);">
                Welcome back, Jonathan Chen | Asset Management Analyst
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")


# ------------------------------------------------------------------------------
# KEY METRICS
# ------------------------------------------------------------------------------
def render_key_metrics() -> None:
    st.markdown("### Portfolio Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <div style="display:flex;align-items:center;">
                    <div class="metric-dot dot-blue"></div>
                    <span class="metric-label">Active Portfolios</span>
                </div>
                <div class="metric-value" style="color:#3b82f6;">--</div>
                <div class="metric-subtext">Currently managing</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <div style="display:flex;align-items:center;">
                    <div class="metric-dot dot-green"></div>
                    <span class="metric-label">Total Positions</span>
                </div>
                <div class="metric-value" style="color:#22c55e;">--</div>
                <div class="metric-subtext">Across portfolios</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <div style="display:flex;align-items:center;">
                    <div class="metric-dot dot-orange"></div>
                    <span class="metric-label">Best Performer</span>
                </div>
                <div class="metric-value" style="color:#f59e0b;">--</div>
                <div class="metric-subtext">YTD return</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="metric-card">
                <div style="display:flex;align-items:center;">
                    <div class="metric-dot dot-purple"></div>
                    <span class="metric-label">Watchlist Items</span>
                </div>
                <div class="metric-value" style="color:#a855f7;">--</div>
                <div class="metric-subtext">Stocks monitored</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")


# ------------------------------------------------------------------------------
# QUICK ACTIONS
# ------------------------------------------------------------------------------
def render_quick_actions() -> None:
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
            st.toast("Watchlist Management Coming Soon")

    with col4:
        if st.button("View All Portfolios", use_container_width=True):
            show_stratify_loader(duration=1)
            st.switch_page("pages/11_Portfolio_Manager.py")

    st.markdown("---")


# ------------------------------------------------------------------------------
# EMPTY STATE HELPER
# ------------------------------------------------------------------------------
def render_empty_state(title: str) -> None:
    st.markdown(
        f"""
        <div class="empty-state">
            <h4>{title}</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------------------
# PORTFOLIOS / BACKTESTS / WATCHLIST
# ------------------------------------------------------------------------------
def render_portfolios_section() -> None:
    st.markdown("### My Portfolios")
    render_empty_state("No portfolios yet")
    st.write("")


def render_backtests_section() -> None:
    st.markdown("### Recent Backtests")
    render_empty_state("No backtests yet")
    st.write("")


def render_watchlist_section() -> None:
    st.markdown("### My Watchlist")
    render_empty_state("Your watchlist is empty")
    st.markdown("---")


# ------------------------------------------------------------------------------
# CLEAN MINIMAL NAVIGATION BUTTONS
# ------------------------------------------------------------------------------
def render_navigation_section() -> None:
    st.markdown("### Navigate to Other Dashboards")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="nav-dark-btn">', unsafe_allow_html=True)
        if st.button(
            "Go to Backtest Dashboard",
            use_container_width=True,
            key="nav_backtest",
        ):
            show_stratify_loader(duration=1)
            st.switch_page("pages/01_Backtest_Dashboard.py")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="nav-dark-btn">', unsafe_allow_html=True)
        if st.button(
            "Go to Risk Dashboard",
            use_container_width=True,
            key="nav_risk",
        ):
            show_stratify_loader(duration=1)
            st.switch_page("pages/02_Risk_Dashboard.py")
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="nav-dark-btn">', unsafe_allow_html=True)
        if st.button(
            "Go to Portfolio Manager",
            use_container_width=True,
            key="nav_portfolio",
        ):
            show_stratify_loader(duration=1)
            st.switch_page("pages/11_Portfolio_Manager.py")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")


# ------------------------------------------------------------------------------
# HELP + FOOTER
# ------------------------------------------------------------------------------
def render_help_section() -> None:
    with st.expander("Getting Started Guide"):
        st.markdown(
            """
            - Create model portfolios  
            - Run backtests  
            - Track watchlists  
            - Compare benchmark performance  
            """
        )


def render_footer() -> None:
    st.markdown(
        """
        <div class="stratify-footer">
            Stratify Portfolio Intelligence Platform<br>
            <span class="stratify-footer-subtext">
                Test strategies with zero financial risk • Data-driven confidence
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------------------
# PAGE RENDER ORDER
# ------------------------------------------------------------------------------
render_header()
render_key_metrics()
render_quick_actions()
render_portfolios_section()
render_backtests_section()
render_watchlist_section()
render_navigation_section()
render_help_section()
render_footer()