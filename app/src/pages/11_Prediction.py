# pages/11_Prediction.py
# Stratify - AI Price Prediction & Market Forecasting
# Persona: Noah Harrison (Data Analyst) / Jonathan Chen (Asset Analyst)

import sys
import streamlit as st
import pandas as pd
import numpy as np
import requests

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="AI Prediction - Stratify",
    page_icon="🔮",
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
.pred-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.confidence-high {
    color: #22c55e;
    font-weight: bold;
}
.confidence-med {
    color: #f59e0b;
    font-weight: bold;
}
.confidence-low {
    color: #ef4444;
    font-weight: bold;
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
        <h1 style="font-size: 2.5rem; color: #a855f7; margin-bottom: 0.25rem;">
            AI Market Forecasting
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Predictive analytics powered by Stratify Neural Engine
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# PREDICTION INTERFACE
# ============================================
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="pred-card">', unsafe_allow_html=True)
    st.markdown("### 🎛️ Model Parameters")
    
    ticker = st.text_input("Asset Ticker", value="NVDA")
    horizon = st.selectbox("Forecast Horizon", ["7 Days", "30 Days", "90 Days", "1 Year"])
    model_type = st.selectbox("Model Architecture", ["LSTM (Deep Learning)", "XGBoost Ensemble", "ARIMA (Statistical)"])
    
    st.markdown("#### Feature Selection")
    st.checkbox("Include Macro Indicators", value=True)
    st.checkbox("Include Sentiment Analysis", value=True)
    st.checkbox("Include Technical Indicators", value=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Generate Forecast", type="primary", use_container_width=True):
        show_stratify_loader(duration=2.5, message="Running Neural Network...", style="cascade")
        st.session_state['prediction_run'] = True
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.session_state.get('prediction_run'):
        st.markdown('<div class="pred-card">', unsafe_allow_html=True)
        st.markdown(f"### 📈 Forecast Results: {ticker}")
        
        # Mock Prediction Data
        dates = pd.date_range(start=pd.Timestamp.now(), periods=30)
        base_price = 450.0
        trend = np.linspace(0, 20, 30)
        noise = np.random.normal(0, 5, 30)
        prices = base_price + trend + noise
        
        upper_bound = prices + 15
        lower_bound = prices - 15
        
        df = pd.DataFrame({
            "Date": dates,
            "Forecast": prices,
            "Upper Confidence": upper_bound,
            "Lower Confidence": lower_bound
        })
        
        st.line_chart(df.set_index("Date"), color=["#3b82f6", "#22c55e", "#ef4444"])
        
        res_c1, res_c2, res_c3 = st.columns(3)
        with res_c1:
            st.metric("Target Price (30d)", f"${prices[-1]:.2f}", "+4.2%")
        with res_c2:
            st.markdown("Model Confidence")
            st.markdown('<span class="confidence-high">87.5% (High)</span>', unsafe_allow_html=True)
        with res_c3:
            st.markdown("Key Driver")
            st.info("Earnings Momentum")
            
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("👈 Configure parameters and click 'Generate Forecast' to see AI predictions.")
        
        # Placeholder for "How it works"
        st.markdown("### How Stratify AI Works")
        st.markdown("""
        1.  **Data Ingestion**: Aggregates price, volume, news sentiment, and macro data.
        2.  **Feature Engineering**: Calculates RSI, MACD, Bollinger Bands, and custom alpha signals.
        3.  **Neural Processing**: Feeds data into a Long Short-Term Memory (LSTM) network.
        4.  **Ensemble Scoring**: Combines outputs from multiple models to reduce variance.
        """)

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Back to Data Analyst Workspace"):
    st.switch_page("pages/00_Data_Analyst_Home.py")
