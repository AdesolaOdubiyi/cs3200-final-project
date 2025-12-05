# pages/12_API_Test.py
# Stratify - System Integration Tester
# Persona: System Administrator (Rajesh Singh)

import sys
import streamlit as st
import requests
import pandas as pd
import json

sys.path.append("..")
from stratify_theme import apply_stratify_theme
from modules.nav import SideBarLinks

apply_stratify_theme()
SideBarLinks()

# ============================================
# STYLES
# ============================================
st.markdown(
    """
<style>
.api-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.status-ok {
    color: #22c55e;
    font-weight: bold;
}
.status-err {
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
        <h1 style="font-size: 2.5rem; color: #94a3b8; margin-bottom: 0.25rem;">
            <span style="color: #22c55e;">API</span> Integration Tester
        </h1>
        <p style="font-size: 1rem; color: #64748b; margin: 0;">
            Endpoint verification and payload inspection
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# ENDPOINT TESTER
# ============================================
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="api-card">', unsafe_allow_html=True)
    st.markdown("### 📡 Request Configuration")
    
    endpoint_type = st.selectbox("Service", ["Backtest", "Performance", "Macro", "Geo", "Prediction"])
    
    url = ""
    if endpoint_type == "Backtest":
        url = "http://web-api:4000/backtest/results/BT-1001"
    elif endpoint_type == "Performance":
        url = "http://web-api:4000/performance/firm/summary"
    elif endpoint_type == "Macro":
        url = "http://web-api:4000/macro/data/GDP?year=2022"
    elif endpoint_type == "Geo":
        url = "http://web-api:4000/geo/assets"
    elif endpoint_type == "Prediction":
        url = "http://web-api:4000/prediction/10/25"
        
    custom_url = st.text_input("Endpoint URL", value=url)
    method = st.selectbox("Method", ["GET", "POST", "PUT", "DELETE"])
    
    if st.button("Send Request", type="primary", use_container_width=True):
        show_stratify_loader(duration=1, message="Sending Request...", style="sequential")
        try:
            response = requests.request(method, custom_url, timeout=5)
            st.session_state['api_response'] = {
                "status": response.status_code,
                "headers": dict(response.headers),
                "body": response.json() if response.content else {}
            }
        except Exception as e:
            st.session_state['api_response'] = {"error": str(e)}
            
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="api-card">', unsafe_allow_html=True)
    st.markdown("### 📨 Response Inspector")
    
    if 'api_response' in st.session_state:
        resp = st.session_state['api_response']
        
        if "error" in resp:
            st.error(f"Connection Failed: {resp['error']}")
        else:
            c_status, c_time = st.columns(2)
            with c_status:
                status_color = "status-ok" if 200 <= resp['status'] < 300 else "status-err"
                st.markdown(f"Status: <span class='{status_color}'>{resp['status']}</span>", unsafe_allow_html=True)
            
            st.markdown("#### Response Body")
            st.json(resp['body'])
            
            with st.expander("View Headers"):
                st.json(resp['headers'])
    else:
        st.info("Send a request to view the response payload.")
        
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Back to Admin Console"):
    st.switch_page("pages/20_Admin_Home.py")
