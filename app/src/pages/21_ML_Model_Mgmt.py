# pages/21_ML_Model_Mgmt.py
# Stratify - Machine Learning Model Operations (MLOps)
# Persona: Noah Harrison (Data Analyst) / Rajesh Singh (Admin)

import sys
import streamlit as st
import pandas as pd
import requests
import time

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="ML Model Management - Stratify",
    page_icon="🧠",
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
.model-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.status-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: bold;
}
.status-active { background: rgba(34, 197, 94, 0.2); color: #22c55e; border: 1px solid #22c55e; }
.status-training { background: rgba(59, 130, 246, 0.2); color: #3b82f6; border: 1px solid #3b82f6; }
.status-deprecated { background: rgba(148, 163, 184, 0.2); color: #94a3b8; border: 1px solid #94a3b8; }
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
        <h1 style="font-size: 2.5rem; color: #3b82f6; margin-bottom: 0.25rem;">
            ML Model Registry
        </h1>
        <p style="font-size: 1rem; color: #94a3b8; margin: 0;">
            Train, deploy, and monitor predictive models
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# MODEL REGISTRY
# ============================================
st.markdown("### 🤖 Active Models")

# Fetch models from backend
try:
    response = requests.get("http://web-api:4000/ml/models")
    if response.status_code == 200:
        models = response.json()
    else:
        st.error("Failed to fetch models.")
        models = []
except:
    st.error("Backend connection failed. Using mock data.")
    models = []

for m in models:
    status_class = "status-active" if m['status'] == "Active" else "status-training" if m['status'] == "Training" else "status-deprecated"
    
    st.markdown(
        f"""
        <div class="model-card">
            <div style="width: 30%;">
                <div style="font-weight: bold; font-size: 1.1rem; color: #e2e8f0;">{m['name']}</div>
                <div style="font-size: 0.8rem; color: #64748b;">ID: {m['id']} • {m['type']}</div>
            </div>
            <div style="width: 20%;">
                <div style="font-size: 0.8rem; color: #94a3b8;">Accuracy</div>
                <div style="font-weight: bold; color: #e2e8f0;">{m['accuracy']}</div>
            </div>
            <div style="width: 20%;">
                <div style="font-size: 0.8rem; color: #94a3b8;">Last Trained</div>
                <div style="color: #e2e8f0;">{m['last_trained']}</div>
            </div>
            <div style="width: 15%;">
                <span class="status-badge {status_class}">{m['status']}</span>
            </div>
            <div style="width: 15%; text-align: right;">
                <button style="background: #1e293b; border: 1px solid #334155; color: #3b82f6; padding: 0.5rem 1rem; border-radius: 6px; cursor: pointer;">Manage</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================
# TRAINING INTERFACE
# ============================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🏋️ Train New Model")

with st.expander("Configure Training Job"):
    c1, c2 = st.columns(2)
    with c1:
        model_name = st.text_input("Model Name", placeholder="e.g. Sector_Rotation_Classifier")
        algo = st.selectbox("Algorithm", ["Random Forest", "Gradient Boosting", "Neural Network", "K-Means Clustering"])
    with c2:
        dataset = st.selectbox("Dataset", ["Market_Data_2024", "Alternative_Data_Q3", "User_Behavior_Logs"])
        split = st.slider("Training/Test Split", 50, 90, 80)
        
    if st.button("Start Training Job", type="primary"):
        show_stratify_loader(duration=3, message="Initializing Training Cluster...", style="simultaneous")
        
        # Call backend to start training
        try:
            payload = {"model_name": model_name, "algorithm": algo, "dataset": dataset}
            res = requests.post("http://web-api:4000/ml/train", json=payload)
            if res.status_code == 200:
                job_info = res.json()
                st.success(f"{job_info['message']} (Job ID: {job_info['job_id']})")
                st.info(f"Estimated completion time: {job_info['estimated_time']}")
            else:
                st.error("Failed to start training job.")
        except:
            st.error("Backend connection failed.")

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Back to Admin Console"):
    st.switch_page("pages/20_Admin_Home.py")
