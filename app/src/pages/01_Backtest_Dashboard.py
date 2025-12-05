# pages/01_Backtest_Dashboard.py
# Stratify - Backtest Dashboard for Strategy Simulation


import sys
from datetime import datetime, timedelta


import streamlit as st


sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402


st.set_page_config(
   page_title="Backtest Dashboard - Stratify",
   page_icon="🎯",
   layout="wide",
)

from modules.nav import SideBarLinks
from stratify_theme import apply_stratify_theme

apply_stratify_theme()
SideBarLinks()


# ============================================
# GLOBAL DARK THEME + COMPONENT STYLES
# ============================================


st.markdown(
   """
<style>
/* Config + results cards */
.config-card {
   padding: 1.5rem;
   background: #1e293b;
   border: 1px solid #334155;
   border-radius: 12px;
   margin-bottom: 1rem;
}


.results-card {
   padding: 2rem;
   background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
   border: 1px solid #334155;
   border-radius: 12px;
   box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}


/* Metric grid */
.metric-row {
   display: grid;
   grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
   gap: 1rem;
   margin: 1rem 0;
}


.metric-item {
   padding: 1rem;
   background: #0f172a;
   border: 1px solid #334155;
   border-radius: 8px;
   text-align: center;
}


.metric-label {
   color: #94a3b8;
   font-size: 0.85rem;
   text-transform: uppercase;
   letter-spacing: 0.05em;
   margin-bottom: 0.5rem;
}


.metric-value {
   font-size: 1.75rem;
   font-weight: 700;
   font-family: "JetBrains Mono", monospace;
   color: #3b82f6;
}


/* Empty state */
.empty-state {
   padding: 2.5rem 2rem;
   background: #1e293b;
   border: 2px dashed #475569;
   border-radius: 8px;
   text-align: center;
}
.empty-state h3, .empty-state h4 {
   color: #cbd5e1;
   margin-bottom: 0.75rem;
}
.empty-state p {
   color: #94a3b8;
   margin: 0.25rem 0;
}


/* Dark buttons (wrapper-based) */
.primary-dark-btn > button {
   width: 100% !important;
   height: 50px !important;
   background-color: #2563eb !important;
   color: #e2e8f0 !important;
   border: 1px solid #3b82f6 !important;
   border-radius: 10px !important;
   font-size: 1rem !important;
   font-weight: 600 !important;
   transition: all 0.2s ease;
}
.primary-dark-btn > button:hover {
   background-color: #1d4ed8 !important;
   border-color: #60a5fa !important;
}


.dark-btn > button {
   width: 100% !important;
   height: 46px !important;
   background-color: #1e293b !important;
   color: #e2e8f0 !important;
   border: 1px solid #334155 !important;
   border-radius: 10px !important;
   font-size: 0.95rem !important;
   transition: all 0.2s ease;
}
.dark-btn > button:hover {
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
   margin-top: 0.5rem;
}
</style>
""",
   unsafe_allow_html=True,
)


# ============================================
# HEADER
# ============================================




def render_header() -> None:
   st.markdown(
       """
       <div style="padding: 1.5rem 0 1rem 0;">
           <h1 style="font-size: 2.5rem; color: #60a5fa; margin-bottom: 0.25rem;">
               Backtest Dashboard
           </h1>
           <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
               Test investment strategies against historical market data
           </p>
       </div>
       """,
       unsafe_allow_html=True,
   )
   st.markdown("---")




# ============================================
# CONFIGURATION SECTION
# ============================================




def render_configuration():
   st.markdown("### Configuration")


   config_col1, config_col2 = st.columns([2, 1])


   # Portfolio selection
   with config_col1:
       st.markdown('<div class="config-card">', unsafe_allow_html=True)


       st.markdown(
           "<p style='font-weight:600; font-size:0.95rem; margin-bottom:0.5rem;'>Select Portfolio</p>",
           unsafe_allow_html=True,
       )


       portfolio_options = ["No portfolios available"]  # TODO: replace with DB query
       selected_portfolio = st.selectbox(
           "Choose a portfolio to backtest:",
           options=portfolio_options,
           index=0,
           label_visibility="collapsed",
       )


       if selected_portfolio == "No portfolios available":
           st.warning(
               "⚠️ No portfolios found. Create a portfolio first from the Analyst Dashboard.",
               icon="⚠️",
           )


       st.markdown("</div>", unsafe_allow_html=True)


   # Benchmark selection
   with config_col2:
       st.markdown('<div class="config-card">', unsafe_allow_html=True)


       st.markdown(
           "<p style='font-weight:600; font-size:0.95rem; margin-bottom:0.5rem;'>Benchmark</p>",
           unsafe_allow_html=True,
       )


       benchmark_options = ["S&P 500", "NASDAQ Composite", "Dow Jones", "Russell 2000"]
       selected_benchmark = st.selectbox(
           "Compare against:",
           options=benchmark_options,
           index=0,
           label_visibility="collapsed",
       )


       st.markdown("</div>", unsafe_allow_html=True)


   # Date range (no extra card wrapper – removes the “empty container”)
   st.markdown("#### Backtest Period")


   date_col1, date_col2 = st.columns(2)
   today = datetime.now().date()


   with date_col1:
       start_date = st.date_input(
           "Start Date",
           value=today - timedelta(days=365),
           max_value=today,
       )


   with date_col2:
       end_date = st.date_input(
           "End Date",
           value=today,
           max_value=today,
       )


   date_error = None
   days_diff = None
   if start_date and end_date:
       if start_date > end_date:
           date_error = "Start date cannot be after end date."
           st.error("❌ Start date must be earlier than or equal to end date.")
       else:
           days_diff = (end_date - start_date).days
           st.caption(
               f"📊 Backtest period: {days_diff} days (~{days_diff/365:.1f} years)"
           )
           if days_diff < 90:
               st.info(
                   "ℹ️ For more robust results, consider using at least 6–12 months of data."
               )


   st.write("")  # small breathing room


   return selected_portfolio, selected_benchmark, start_date, end_date, date_error




# ============================================
# RUN BACKTEST BUTTON
# ============================================




def render_run_button(
   selected_portfolio, selected_benchmark, start_date, end_date, date_error
):
   st.markdown("<br>", unsafe_allow_html=True)
   run_col1, run_col2, run_col3 = st.columns([1, 2, 1])


   with run_col2:
       st.markdown('<div class="primary-dark-btn">', unsafe_allow_html=True)
       clicked = st.button("Run Backtest", use_container_width=True, key="run_backtest")
       st.markdown("</div>", unsafe_allow_html=True)


       if clicked:
           if selected_portfolio == "No portfolios available":
               st.error("❌ Please select a valid portfolio before running a backtest.")
               return


           if date_error is not None:
               st.error("❌ Please fix date errors before running a backtest.")
               return


           show_stratify_loader(
               duration=2.5, style="cascade", speed="normal", message="Running backtest"
           )


           st.session_state["backtest_run"] = True
           st.session_state["backtest_portfolio"] = selected_portfolio
           st.session_state["backtest_benchmark"] = selected_benchmark
           st.session_state["backtest_start"] = start_date
           st.session_state["backtest_end"] = end_date


           st.rerun()


   st.markdown("---")




# ============================================
# RESULTS SECTION
# ============================================




def render_results():
   st.markdown("### Results")


   if st.session_state.get("backtest_run"):
       portfolio = st.session_state.get("backtest_portfolio", "N/A")
       benchmark = st.session_state.get("backtest_benchmark", "N/A")
       start = st.session_state.get("backtest_start", "")
       end = st.session_state.get("backtest_end", "")


       st.markdown('<div class="results-card">', unsafe_allow_html=True)


       # Header
       st.markdown(
           f"""
           <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1.5rem;padding-bottom:1rem;border-bottom:1px solid #334155;">
               <div>
                   <h3 style="margin:0; color:#60a5fa;">Backtest Results</h3>
                   <p style="margin:0.5rem 0 0 0; color:#94a3b8; font-size:0.9rem;">
                       Portfolio: <strong>{portfolio}</strong><br>
                       Benchmark: <strong>{benchmark}</strong><br>
                       Period: {start} to {end}
                   </p>
               </div>
               <div style="color:#22c55e; font-size:0.85rem; text-align:right;">
                   <div style="font-weight:600;">Status: Complete</div>
                   <div style="color:#94a3b8;">Sample placeholder data</div>
               </div>
           </div>
           """,
           unsafe_allow_html=True,
       )


       # Metrics grid (placeholders)
       st.markdown("#### Performance Metrics")


       st.markdown(
           f"""
           <div class="metric-row">
               <div class="metric-item">
                   <div class="metric-label">Total Return</div>
                   <div class="metric-value">--</div>
                   <div style="color:#64748b; font-size:0.8rem; margin-top:0.5rem;">
                       vs {benchmark}: --
                   </div>
               </div>


               <div class="metric-item">
                   <div class="metric-label">Annualized Return (CAGR)</div>
                   <div class="metric-value">--</div>
                   <div style="color:#64748b; font-size:0.8rem; margin-top:0.5rem;">
                       Risk-adjusted coming soon
                   </div>
               </div>


               <div class="metric-item">
                   <div class="metric-label">Volatility</div>
                   <div class="metric-value">--</div>
                   <div style="color:#64748b; font-size:0.8rem; margin-top:0.5rem;">
                       Std. deviation of returns
                   </div>
               </div>


               <div class="metric-item">
                   <div class="metric-label">Sharpe Ratio</div>
                   <div class="metric-value">--</div>
                   <div style="color:#64748b; font-size:0.8rem; margin-top:0.5rem;">
                       Risk-adjusted performance
                   </div>
               </div>


               <div class="metric-item">
                   <div class="metric-label">Max Drawdown</div>
                   <div class="metric-value">--</div>
                   <div style="color:#64748b; font-size:0.8rem; margin-top:0.5rem;">
                       Peak-to-trough loss
                   </div>
               </div>


               <div class="metric-item">
                   <div class="metric-label">Beta vs Benchmark</div>
                   <div class="metric-value">--</div>
                   <div style="color:#64748b; font-size:0.8rem; margin-top:0.5rem;">
                       Sensitivity to {benchmark}
                   </div>
               </div>
           </div>
           """,
           unsafe_allow_html=True,
       )


       st.markdown("<br>", unsafe_allow_html=True)


       # Chart placeholders
       st.markdown("#### Portfolio Performance Over Time")
       st.markdown(
           """
           <div class="empty-state">
               <h4>Chart placeholder</h4>
               <p>
                   Performance chart will display here once connected to historical price data.<br>
                   Expected: Portfolio value vs benchmark over the selected period.
               </p>
           </div>
           """,
           unsafe_allow_html=True,
       )


       st.markdown("<br>", unsafe_allow_html=True)


       col1, col2 = st.columns(2)


       with col1:
           st.markdown("#### Returns Distribution")
           st.markdown(
               """
               <div class="empty-state">
                   <h4>Histogram placeholder</h4>
                   <p style="font-size:0.9rem;">
                       Daily returns distribution (histogram) will be shown here.
                   </p>
               </div>
               """,
               unsafe_allow_html=True,
           )


       with col2:
           st.markdown("#### Rolling Volatility")
           st.markdown(
               """
               <div class="empty-state">
                   <h4>Rolling volatility placeholder</h4>
                   <p style="font-size:0.9rem;">
                       30-day rolling volatility chart will be displayed here.
                   </p>
               </div>
               """,
               unsafe_allow_html=True,
           )


       st.markdown("<br>", unsafe_allow_html=True)


       # Action buttons
       action_col1, action_col2, action_col3 = st.columns(3)


       with action_col1:
           st.markdown('<div class="dark-btn">', unsafe_allow_html=True)
           if st.button("Download Report", key="download_report"):
               st.info("Report generation coming soon.")
           st.markdown("</div>", unsafe_allow_html=True)


       with action_col2:
           st.markdown('<div class="dark-btn">', unsafe_allow_html=True)
           if st.button("Save Results", key="save_results"):
               st.info("Save functionality coming soon.")
           st.markdown("</div>", unsafe_allow_html=True)


       with action_col3:
           st.markdown('<div class="dark-btn">', unsafe_allow_html=True)
           if st.button("Run New Backtest", key="run_new"):
               st.session_state["backtest_run"] = False
               st.rerun()
           st.markdown("</div>", unsafe_allow_html=True)


       st.markdown("</div>", unsafe_allow_html=True)


   else:
       # Empty state when no backtest has been run yet
       st.markdown(
           """
           <div class="empty-state">
               <h3>Ready to run your first backtest</h3>
               <p style="max-width:600px; margin:0.5rem auto;">
                   Configure your portfolio, benchmark, and time period above, then click
                   <strong>Run Backtest</strong> to see how your strategy would have performed.
               </p>
               <p style="color:#64748b; font-size:0.9rem; margin-top:1rem;">
                   • Zero financial risk<br>
                   • Benchmark-relative performance<br>
                   • Risk metrics like volatility and drawdown
               </p>
           </div>
           """,
           unsafe_allow_html=True,
       )


   st.markdown("---")




# ============================================
# TIPS SECTION
# ============================================




def render_tips():
   with st.expander("Backtesting Best Practices"):
       st.markdown(
           """
           ### How to Run Effective Backtests


           **1. Choose Realistic Parameters** 
           - Use at least 1 year of historical data for meaningful results 
           - Include both bull and bear markets when possible 
           - In real setups, account for transaction costs and slippage 


           **2. Interpret Results Carefully** 
           - Past performance ≠ future performance 
           - Focus on risk-adjusted returns (Sharpe), not just raw returns 
           - Pay attention to maximum drawdown and volatility 


           **3. Compare Against Benchmarks** 
           - Always compare to a relevant index (e.g., S&P 500) 
           - Alpha = portfolio return − benchmark return 
           - Beta shows sensitivity to the market 


           **4. Document Your Rationale** 
           - Capture your investment thesis and assumptions 
           - Share results with portfolio managers / team 
           - Keep track of constraints and caveats 


           **5. Iterate and Refine** 
           - Run multiple parameter sets (e.g., rebalance frequency) 
           - Test stress scenarios and edge cases 
           - Revisit regularly as market regimes change 
           """
       )




# ============================================
# NAVIGATION BACK + FOOTER
# ============================================




def render_back_nav_and_footer():
   st.markdown("<br>", unsafe_allow_html=True)


   st.markdown('<div class="dark-btn">', unsafe_allow_html=True)
   if st.button("← Back to Analyst Dashboard", key="back_analyst"):
       show_stratify_loader(duration=0.8, style="simultaneous", speed="fast")
       st.switch_page("pages/10_Analyst_Home.py")
   st.markdown("</div>", unsafe_allow_html=True)


   st.markdown(
       """
       <div class="stratify-footer">
           <p style="margin:0;">Stratify Portfolio Intelligence | Backtest Dashboard</p>
           <p class="stratify-footer-subtext">
               Test strategies with confidence • Historical data–driven simulation
           </p>
       </div>
       """,
       unsafe_allow_html=True,
   )




# ============================================
# PAGE RENDER ORDER
# ============================================


render_header()
portfolio, benchmark, start_date, end_date, date_error = render_configuration()
render_run_button(portfolio, benchmark, start_date, end_date, date_error)
render_results()
render_tips()
render_back_nav_and_footer()
