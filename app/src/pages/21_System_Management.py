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
# USER MANAGEMENT & ALERTS
st.markdown("---")
tab1, tab2, tab3 = st.tabs(["User Management", "Alert Configuration", "System Logs"])

with tab1:
    st.markdown("### 👥 User Management")
    
    # Fetch users from API
    users_data = []
    api_success = False
    try:
        response = requests.get("http://web-api:4000/user/users", timeout=3)
        if response.status_code == 200:
            result = response.json()
            if result.get("success") and result.get("data"):
                users_data = result.get("data", [])
                api_success = True
    except:
        pass  # Silent fallback to mock data
    
    # Fallback to mock users if API fails
    if not api_success or not users_data:
        users_data = [
            {"userID": 1, "name": "Noah Harrison", "email": "noah@stratify.com", "role": "data_analyst", "lastLogin": "2024-01-15T08:30:00Z"},
            {"userID": 2, "name": "Jonathan Chen", "email": "jonathan@stratify.com", "role": "analyst", "lastLogin": "2024-01-15T09:15:00Z"},
            {"userID": 3, "name": "Rajesh Singh", "email": "rajesh@stratify.com", "role": "administrator", "lastLogin": "2024-01-15T07:45:00Z"},
            {"userID": 4, "name": "Sarah Martinez", "email": "sarah@stratify.com", "role": "director", "lastLogin": "2024-01-15T10:00:00Z"}
        ]
    
    if users_data:
        df_users = pd.DataFrame(users_data)
        st.dataframe(
            df_users,
            use_container_width=True,
            hide_index=True,
            column_config={
                "userID": "ID",
                "name": "Name",
                "email": "Email",
                "role": "Role",
                "lastLogin": "Last Login"
            }
        )
        
        # Role update section
        st.markdown("#### Update User Role")
        user_ids = [f"{u.get('userID')} - {u.get('name', 'Unknown')}" for u in users_data]
        selected_user = st.selectbox("Select User", user_ids)
        new_role = st.selectbox("New Role", ["analyst", "data_analyst", "administrator", "director"])
        
        if st.button("Update Role"):
            try:
                user_id = int(selected_user.split(" - ")[0])
                response = requests.put(
                    f"http://web-api:4000/user/users/{user_id}/role",
                    json={"role": new_role},
                    timeout=5
                )
                if response.status_code == 200:
                    result = response.json()
                    if result.get("success"):
                        st.success(f"Role updated successfully!")
                        st.rerun()
                    else:
                        st.warning(f"API returned error: {result.get('error', 'Unknown error')}. Role may not be saved.")
                else:
                    st.warning("API request failed. Role may not be saved.")
            except Exception as e:
                st.warning(f"Could not connect to API: {str(e)}. Role may not be saved.")
    else:
        st.info("No users found.")

with tab2:
    st.markdown("### 🔔 Alert Configuration")
    
    # Fetch alerts from API
    alerts_data = []
    api_success = False
    try:
        response = requests.get("http://web-api:4000/alert/alerts", timeout=3)
        if response.status_code == 200:
            result = response.json()
            if result.get("success") and result.get("data"):
                alerts_data = result.get("data", [])
                api_success = True
    except:
        pass  # Silent fallback to mock data
    
    # Fallback to mock alerts if API fails
    if not api_success or not alerts_data:
        alerts_data = [
            {"alertID": 1, "type": "PRICE_THRESHOLD", "severity": "HIGH", "message": "AAPL dropped below $150", "timestamp": "2024-01-15T10:30:00Z"},
            {"alertID": 2, "type": "PORTFOLIO_DRIFT", "severity": "MEDIUM", "message": "Tech sector exposure > 40% (Policy Limit)", "timestamp": "2024-01-15T09:15:00Z"},
            {"alertID": 3, "type": "VOLUME_SPIKE", "severity": "LOW", "message": "Unusual volume detected for MSFT", "timestamp": "2024-01-15T08:45:00Z"}
        ]
    
    if alerts_data:
        df_alerts = pd.DataFrame(alerts_data)
        st.dataframe(
            df_alerts,
            use_container_width=True,
            hide_index=True,
            column_config={
                "alertID": "ID",
                "type": "Type",
                "severity": "Severity",
                "message": "Message",
                "timestamp": "Timestamp"
            }
        )
    else:
        st.info("No active alerts.")
    
    # Create new alert rule
    st.markdown("#### Create Alert Rule")
    with st.form("create_alert"):
        alert_name = st.text_input("Alert Name", placeholder="e.g. Price Drop Alert")
        alert_type = st.selectbox("Alert Type", ["PRICE_THRESHOLD", "VOLUME_SPIKE", "PORTFOLIO_DRIFT"])
        severity = st.selectbox("Severity", ["LOW", "MEDIUM", "HIGH", "CRITICAL"])
        portfolio_id = st.number_input("Portfolio ID", min_value=1, value=1)
        
        if st.form_submit_button("Create Alert Rule"):
            try:
                payload = {
                    "name": alert_name,
                    "type": alert_type,
                    "condition": {
                        "portfolioID": portfolio_id
                    },
                    "severity": severity,
                    "portfolioID": portfolio_id
                }
                response = requests.post("http://web-api:4000/alert/alerts", json=payload, timeout=5)
                if response.status_code == 201:
                    result = response.json()
                    if result.get("success"):
                        st.success("Alert rule created successfully!")
                        st.rerun()
                    else:
                        st.warning(f"API returned error: {result.get('error', 'Unknown error')}. Alert may not be saved.")
                else:
                    st.warning("API request failed. Alert may not be saved.")
            except Exception as e:
                st.warning(f"Could not connect to API: {str(e)}. Alert may not be saved.")

with tab3:
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
