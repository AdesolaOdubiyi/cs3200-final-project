# pages/21_System_Management.py
# Stratify - System Configuration & Maintenance
# Persona: Rajesh Singh (Admin)

import sys
import streamlit as st
import requests
import pandas as pd

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="System Management - Stratify",
    page_icon="🛠️",
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
.config-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.log-table {
    width: 100%;
    border-collapse: collapse;
}
.log-table th {
    text-align: left;
    color: #94a3b8;
    border-bottom: 1px solid #334155;
    padding: 0.5rem;
}
.log-table td {
    padding: 0.5rem;
    border-bottom: 1px solid #1e293b;
    color: #e2e8f0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.9rem;
}
</style>
""",
    unsafe_allow_html=True,
)
# HEADER

st.markdown(
    """
    <div style="padding: 1.5rem 0 1rem 0;">
        <h1 style="font-size: 2.5rem; color: #94a3b8; margin-bottom: 0.25rem;">
            System Management
        </h1>
        <p style="font-size: 1rem; color: #64748b; margin: 0;">
            Advanced configuration, feature flags, and maintenance
        </p>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)
# FETCH DATA

config_data = {}
logs_data = []

try:
    config_res = requests.get("http://web-api:4000/system/config")
    if config_res.status_code == 200:
        config_data = config_res.json()
        
    logs_res = requests.get("http://web-api:4000/system/logs")
    if logs_res.status_code == 200:
        logs_data = logs_res.json()
except:
    st.error("Backend connection failed. Using mock data.")
    config_data = {
        "environment": "Unknown", "version": "0.0.0", 
        "feature_flags": {"beta_features": False, "dark_mode_default": True}
    }
# CONFIGURATION

c1, c2 = st.columns([1, 1])

with c1:
    st.markdown('<div class="config-card">', unsafe_allow_html=True)
    st.markdown("### ⚙️ Global Configuration")
    
    st.text_input("Environment", value=config_data.get('environment', 'Production'), disabled=True)
    st.text_input("System Version", value=config_data.get('version', '1.0.0'), disabled=True)
    
    st.markdown("#### Feature Flags")
    flags = config_data.get('feature_flags', {})
    
    beta = st.toggle("Enable Beta Features", value=flags.get('beta_features', False))
    dark = st.toggle("Force Dark Mode Default", value=flags.get('dark_mode_default', True))
    rate = st.toggle("API Rate Limiting", value=flags.get('api_rate_limiting', True))
    
    if st.button("Save Configuration", type="primary"):
        show_stratify_loader(duration=1.5, message="Applying Settings...", style="sequential")
        # Call backend to save
        try:
            new_config = {
                "feature_flags": {
                    "beta_features": beta,
                    "dark_mode_default": dark,
                    "api_rate_limiting": rate
                }
            }
            requests.post("http://web-api:4000/system/config", json=new_config)
            st.success("Configuration updated successfully.")
        except:
            st.error("Failed to save configuration.")
            
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="config-card">', unsafe_allow_html=True)
    st.markdown("### 💾 Database Maintenance")
    
    st.info("Last backup: 2024-10-24 03:00:00 UTC")
    
    if st.button("Trigger Immediate Backup"):
        show_stratify_loader(duration=2, message="Backing up Database...", style="simultaneous")
        try:
            res = requests.post("http://web-api:4000/system/backup")
            if res.status_code == 200:
                st.success(f"Backup started. ID: {res.json()['backup_id']}")
        except:
            st.error("Backup failed to start.")
            
    st.markdown("#### Migration Status")
    st.markdown(
        """
        <div style="font-family:'JetBrains Mono'; font-size:0.9rem; color:#94a3b8;">
        > 001_initial_schema (Applied)<br>
        > 002_add_users_table (Applied)<br>
        > 003_add_audit_logs (Applied)<br>
        > 004_update_indices (Pending)
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Run Pending Migrations"):
        show_stratify_loader(duration=3, message="Migrating Schema...", style="cascade")
        st.success("Schema updated to version 004.")
        
    st.markdown('</div>', unsafe_allow_html=True)
# SYSTEM LOGS

st.markdown("### 📜 Recent System Logs")

if logs_data:
    df_logs = pd.DataFrame(logs_data)
    st.dataframe(
        df_logs,
        use_container_width=True,
        hide_index=True,
        column_config={
            "timestamp": "Time",
            "level": "Level",
            "source": "Source",
            "message": "Message"
        }
    )
else:
    st.info("No logs available.")
# FOOTER

st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Back to Admin Console"):
    st.switch_page("pages/20_Admin_Home.py")
