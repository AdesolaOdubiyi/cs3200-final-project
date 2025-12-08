# pages/11_Portfolio_Manager.py
# Stratify - Portfolio Management & Trade Execution
# Persona: Jonathan Chen (Asset Management Analyst)

import sys
import streamlit as st
import pandas as pd
from datetime import datetime

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402
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
.card { background: var(--bg-light); border: 1px solid var(--bg-border); border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.04); }

.action-btn > button { width: 100%; background-color: var(--primary) !important; color: white !important; border: 1px solid var(--primary-dark) !important; border-radius: 8px; padding: 0.5rem; transition: all 0.2s; }
.action-btn > button:hover { background-color: var(--primary-dark) !important; transform: translateY(-1px); }

.secondary-btn > button { width: 100%; background-color: transparent !important; color: var(--text-tertiary) !important; border: 1px solid var(--bg-border) !important; border-radius: 8px; }
.secondary-btn > button:hover { border-color: var(--text-secondary) !important; color: white !important; }

.table-header { background: var(--bg-white); padding: 0.75rem; border-radius: 8px 8px 0 0; border-bottom: 1px solid var(--bg-border); font-weight: 600; color: var(--text-secondary); }
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
        <h1 style="font-size: 2.5rem; color: var(--primary); margin-bottom: 0.25rem;">Portfolio Manager</h1>
        <p style="font-size: 1rem; color: var(--text-tertiary); margin: 0;">Manage model portfolios, execute trades, and track positions</p>
    </div>
    <hr style="border-color: var(--bg-border); margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# MAIN CONTENT
# ============================================

# Tabs for different workflows
tab1, tab2, tab3 = st.tabs(["Active Portfolios", "Trade Execution", "Create New Model"])

# --- TAB 1: ACTIVE PORTFOLIOS ---
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📈 Current Holdings")
        
        # Mock Data
        data = {
            "Symbol": ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"],
            "Position": [1500, 800, 400, 600, 1200],
            "Avg Price": [175.50, 320.10, 450.00, 135.20, 145.80],
            "Market Value": ["$263,250", "$256,080", "$180,000", "$81,120", "$174,960"],
            "Unrealized P/L": ["+12.5%", "+8.2%", "+24.1%", "-2.3%", "+5.6%"]
        }
        df = pd.DataFrame(data)
        
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Unrealized P/L": st.column_config.TextColumn(
                    "Unrealized P/L",
                    help="Profit/Loss",
                    validate="^[-+]?[0-9]*\.?[0-9]+%$"
                )
            }
        )
        
        st.markdown("### 📝 Position Notes")
        with st.expander("View/Edit Notes for AAPL"):
            st.text_area("Analyst Notes", "Strong Q3 earnings expected. Maintaining overweight position despite tech sector volatility. Watch for supply chain updates.", height=100)
            st.button("Save Note", key="save_note")

    with col2:
        st.markdown("### 📊 Allocation")
        st.markdown(
            """
            <div class="card">
                <h4 style="color:var(--text-secondary); font-size:0.9rem; text-transform:uppercase;">Total AUM</h4>
                <h2 style="color:var(--success); font-family:var(--font-mono);">$955,410</h2>
                <div style="height:10px; background:var(--bg-border); border-radius:5px; margin-top:1rem; overflow:hidden;">
                    <div style="width:45%; height:100%; background:var(--primary); float:left;"></div>
                    <div style="width:30%; height:100%; background:var(--success); float:left;"></div>
                    <div style="width:15%; height:100%; background:var(--warning); float:left;"></div>
                    <div style="width:10%; height:100%; background:var(--text-tertiary); float:left;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; margin-top:0.5rem; font-size:0.8rem; color:var(--text-secondary);">
                    <span>Tech (45%)</span>
                    <span>Fin (30%)</span>
                    <span>Enr (15%)</span>
                    <span>Cash (10%)</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("### ⚠️ Alerts")
        st.info("GOOGL approaching stop-loss limit ($130.00)")
        st.warning("Tech sector exposure > 40% (Policy Limit)")

# --- TAB 2: TRADE EXECUTION ---
with tab2:
    st.markdown("### ⚡ Execute Simulated Trade")
    
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Order Ticket")
        
        ticker = st.text_input("Ticker Symbol", placeholder="e.g. TSLA")
        side = st.selectbox("Side", ["Buy", "Sell"])
        quantity = st.number_input("Quantity", min_value=1, value=100)
        order_type = st.selectbox("Order Type", ["Market", "Limit", "Stop"])
        
        if order_type in ["Limit", "Stop"]:
            price = st.number_input("Price", min_value=0.01, format="%.2f")
        
        st.markdown('<div class="action-btn">', unsafe_allow_html=True)
        if st.button("Submit Order"):
            if not ticker:
                st.error("Please enter a ticker symbol.")
            else:
                show_stratify_loader(duration=2, message="Routing Order...", style="sequential")
                st.success(f"✅ Order Executed: {side} {quantity} {ticker} @ {order_type}")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Recent Activity")
        st.markdown(
            """
            <div style="font-size:0.9rem;">
                <div style="padding:0.5rem 0; border-bottom:1px solid var(--bg-border); display:flex; justify-content:space-between;">
                    <span style="color:var(--success);">BUY AAPL</span>
                    <span style="color:var(--text-secondary);">100 @ MKT</span>
                    <span style="color:var(--text-tertiary);">10:30 AM</span>
                </div>
                <div style="padding:0.5rem 0; border-bottom:1px solid var(--bg-border); display:flex; justify-content:space-between;">
                    <span style="color:var(--error);">SELL NFLX</span>
                    <span style="color:var(--text-secondary);">50 @ 420.50</span>
                    <span style="color:var(--text-tertiary);">09:45 AM</span>
                </div>
                <div style="padding:0.5rem 0; border-bottom:1px solid var(--bg-border); display:flex; justify-content:space-between;">
                    <span style="color:var(--success);">BUY MSFT</span>
                    <span style="color:var(--text-secondary);">200 @ MKT</span>
                    <span style="color:var(--text-tertiary);">Yesterday</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 3: CREATE NEW MODEL ---
with tab3:
    st.markdown("### 🆕 Create Model Portfolio")
    
    with st.form("new_portfolio_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            p_name = st.text_input("Portfolio Name", placeholder="e.g. Q3 Growth Strategy")
            p_capital = st.number_input("Initial Capital ($)", value=1000000)
        with col_b:
            p_benchmark = st.selectbox("Benchmark", ["S&P 500", "NASDAQ 100", "Russell 2000"])
            p_desc = st.text_area("Strategy Description", placeholder="Describe the investment thesis...")
            
        submitted = st.form_submit_button("Create Portfolio")
        if submitted:
            if p_name:
                show_stratify_loader(duration=1.5, message="Creating Portfolio...")
                st.success(f"✅ Portfolio '{p_name}' created successfully!")
            else:
                st.error("Please enter a portfolio name.")

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
col_back, _, _ = st.columns([1, 2, 1])
with col_back:
    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
    if st.button("← Back to Analyst Dashboard"):
        st.switch_page("pages/10_Analyst_Home.py")
    st.markdown('</div>', unsafe_allow_html=True)
