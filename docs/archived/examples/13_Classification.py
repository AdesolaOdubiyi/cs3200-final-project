# pages/13_Classification.py
# Stratify - Asset Classification Engine
# Persona: Data Analyst / Asset Analyst

import sys
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="Asset Classifier - Stratify",
    page_icon="🏷️",
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
.class-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.result-box {
    text-align: center;
    padding: 2rem;
    border: 2px dashed #3b82f6;
    border-radius: 12px;
    background: rgba(59, 130, 246, 0.05);
}
</style>
""",
    unsafe_allow_html=True,
)
# HEADER

st.markdown(
    """
    <div style="padding: 1.5rem 0 1rem 0;">
        <h1 style="font-size: 2.5rem; color: #f472b6; margin-bottom: 0.25rem;">
            Asset Classifier
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            AI-powered sector and risk category classification
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)
# CLASSIFICATION INTERFACE

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="class-card">', unsafe_allow_html=True)
    st.markdown("### 🧬 Asset Features")
    
    # Inputs for classification (Simulated)
    volatility = st.slider("Volatility (Beta)", 0.0, 3.0, 1.2)
    market_cap = st.slider("Market Cap (Billions)", 0.1, 2000.0, 50.0)
    pe_ratio = st.slider("P/E Ratio", 0.0, 100.0, 25.0)
    dividend_yield = st.slider("Dividend Yield (%)", 0.0, 10.0, 1.5)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Classify Asset", type="primary", use_container_width=True):
        show_stratify_loader(duration=1.5, message="Analyzing Features...", style="simultaneous")
        st.session_state['classify_run'] = True
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.session_state.get('classify_run'):
        st.markdown('<div class="class-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Classification Results")
        
        # Simple logic to simulate classification
        if volatility > 1.5:
            sector = "Technology / Growth"
            risk = "High Risk"
            color = "#ef4444"
        elif dividend_yield > 3.0:
            sector = "Utilities / Value"
            risk = "Low Risk"
            color = "#22c55e"
        else:
            sector = "Consumer / Industrial"
            risk = "Moderate Risk"
            color = "#f59e0b"
            
        st.markdown(
            f"""
            <div class="result-box">
                <div style="font-size: 1rem; color: #94a3b8; text-transform: uppercase;">Predicted Sector</div>
                <div style="font-size: 3rem; font-weight: 800; color: #e2e8f0; margin: 1rem 0;">{sector}</div>
                <div style="display: inline-block; padding: 0.5rem 1.5rem; background: {color}; color: white; border-radius: 20px; font-weight: bold;">
                    {risk}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("#### Probability Distribution")
        chart_data = pd.DataFrame({
            "Category": ["Tech", "Finance", "Healthcare", "Energy", "Utilities"],
            "Probability": np.random.dirichlet(np.ones(5), size=1)[0]
        })
        st.bar_chart(chart_data.set_index("Category"))
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("👈 Adjust asset features and click 'Classify Asset' to run the model.")
# FOOTER

st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Dashboard"):
    st.switch_page("Home.py")