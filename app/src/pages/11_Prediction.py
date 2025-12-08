# pages/11_Prediction.py
# Stratify - AI Price Prediction & Market Forecasting
# Persona: Noah Harrison (Data Analyst) / Jonathan Chen (Asset Analyst)

import sys

import numpy as np
import pandas as pd
import streamlit as st

sys.path.append("..")

from stratify_loader import show_stratify_loader  # noqa: E402
from modules.nav import SideBarLinks
from stratify_theme import apply_stratify_theme


# ------------------------------------------------------------------------------
# PAGE CONFIG & THEME
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Prediction - Stratify",
    page_icon="🔮",
    layout="wide",
)

apply_stratify_theme()
SideBarLinks()


# ------------------------------------------------------------------------------
# CUSTOM STYLES
# ------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .pred-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0 1rem 0;
    }

    /* Stronger selectors for Streamlit submit buttons inside pred-card */
    .pred-card form button,
    .pred-card form [type="submit"],
    .pred-card .stButton > button,
    .pred-card button.st-a11yButton {
        background: var(--primary) !important;
        color: #ffffff !important;
        border: 1px solid var(--primary-dark) !important;
        width: 100% !important;
        padding: 0.6rem 1rem !important;
        border-radius: 8px !important;
    }

    .pred-card form button:disabled,
    .pred-card .stButton > button:disabled {
        opacity: 0.65 !important;
    }

    /* Hide empty block placeholders (top rounded empty boxes) */
    main div:empty {
        display: none !important;
    }
    main > div > div:empty {
        display: none !important;
    }
    main > div > div > div:empty {
        display: none !important;
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


# ------------------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------------------
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


# ------------------------------------------------------------------------------
# PREDICTION INTERFACE
# ------------------------------------------------------------------------------
col1, col2 = st.columns([1, 2])

with col1:
    # Compact input form inside a single card
    st.markdown('<div class="pred-card">', unsafe_allow_html=True)
    with st.form("prediction_form"):
        st.markdown("### 🎛️ Model Parameters")

        ticker = st.text_input("Asset Ticker", value="NVDA")
        horizon = st.selectbox(
            "Forecast Horizon",
            ["7 Days", "30 Days", "90 Days", "1 Year"],
        )
        model_type = st.selectbox(
            "Model Architecture",
            ["LSTM (Deep Learning)", "XGBoost Ensemble", "ARIMA (Statistical)"],
        )

        st.markdown("#### Feature Selection")
        inc_macro = st.checkbox("Include Macro Indicators", value=True)
        inc_sent = st.checkbox("Include Sentiment Analysis", value=True)
        inc_tech = st.checkbox("Include Technical Indicators", value=True)

        submitted = st.form_submit_button("Generate Forecast")
    st.markdown("</div>", unsafe_allow_html=True)

    if submitted:
        show_stratify_loader(
            duration=2.5,
            message="Running Neural Network...",
            style="cascade",
        )
        st.session_state["prediction_run"] = True
        st.session_state["prediction_ticker"] = ticker


with col2:
    if st.session_state.get("prediction_run"):
        st.markdown('<div class="pred-card">', unsafe_allow_html=True)
        st.markdown(f"### 📈 Forecast Results: {st.session_state['prediction_ticker']}")

        # Mock Prediction Data (demo placeholder)
        dates = pd.date_range(start=pd.Timestamp.now(), periods=30)
        base_price = 450.0
        trend = np.linspace(0, 20, 30)
        noise = np.random.normal(0, 5, 30)
        prices = base_price + trend + noise

        upper_bound = prices + 15
        lower_bound = prices - 15

        df = pd.DataFrame(
            {
                "Date": dates,
                "Forecast": prices,
                "Upper Confidence": upper_bound,
                "Lower Confidence": lower_bound,
            }
        )

        st.line_chart(
            df.set_index("Date"),
            color=["#3b82f6", "#22c55e", "#ef4444"],
        )

        res_c1, res_c2, res_c3 = st.columns(3)

        with res_c1:
            st.metric("Target Price (30d)", f"${prices[-1]:.2f}", "+4.2%")

        with res_c2:
            st.markdown("Model Confidence")
            st.markdown(
                '<span class="confidence-high">87.5% (High)</span>',
                unsafe_allow_html=True,
            )

        with res_c3:
            st.markdown("Key Driver")
            st.info("Earnings Momentum")

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown('<div class="pred-card">', unsafe_allow_html=True)
        st.markdown("### How Stratify AI Works")
        st.markdown(
            """
            1. **Data Ingestion**: Aggregates price, volume, news sentiment, and macro data.  
            2. **Feature Engineering**: Calculates RSI, MACD, Bollinger Bands, and custom alpha signals.  
            3. **Neural Processing**: Feeds data into a Long Short-Term Memory (LSTM) network.  
            4. **Ensemble Scoring**: Combines outputs from multiple models to reduce variance.  
            """
        )
        st.markdown("</div>", unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# FOOTER (Client-side cleanup + Back button)
# ------------------------------------------------------------------------------
st.markdown(
    """
    <script>
    setTimeout(function(){
        try {
            const main = document.querySelector('main');
            if (!main) return;
            const candidates = Array.from(main.querySelectorAll('div'));
            for (let el of candidates.slice(0, 10)) {
                const style = window.getComputedStyle(el);
                const bg = style.backgroundColor || '';
                const br = parseFloat(style.borderRadius) || 0;
                const h = el.clientHeight || 0;
                // Heuristic: rounded rectangle, moderate height, non-transparent background
                if (br >= 8 && h >= 28 && h <= 160 && bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') {
                    if (!el.textContent || !el.textContent.trim()) {
                        el.remove();
                    }
                }
            }
        } catch (e) {
            console && console.warn && console.warn(e);
        }
    }, 300);
    </script>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("← Back to Data Analyst Workspace"):
    st.switch_page("pages/00_Data_Analyst_Home.py")