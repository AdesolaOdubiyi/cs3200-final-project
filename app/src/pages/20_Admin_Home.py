# pages/20_Admin_Home.py
# Stratify - System Administration & Infrastructure
# Persona: Rajesh Singh (Senior Systems Administrator)

import sys
import streamlit as st
import time

sys.path.append("..")
from stratify_loader import show_stratify_loader  # noqa: E402

st.set_page_config(
    page_title="Admin Console - Stratify",
    page_icon="⚙️",
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
.admin-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.status-indicator {
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    margin-right: 8px;
}
.status-green { background-color: #22c55e; box-shadow: 0 0 8px #22c55e; }
.status-red { background-color: #ef4444; box-shadow: 0 0 8px #ef4444; }
.status-yellow { background-color: #f59e0b; box-shadow: 0 0 8px #f59e0b; }

.log-entry {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    padding: 0.5rem;
    border-bottom: 1px solid #334155;
    color: #94a3b8;
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
    <div style="padding: 1.5rem 0 1rem 0; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="font-size: 2rem; color: #94a3b8; margin-bottom: 0.25rem;">
                <span style="color: #3b82f6;">System</span> Administrator
            </h1>
            <p style="font-size: 0.9rem; color: #64748b; margin: 0;">
                Infrastructure monitoring and user management
            </p>
        </div>
        <div style="text-align: right;">
            <span style="background: #1e293b; padding: 0.5rem 1rem; border-radius: 20px; border: 1px solid #334155; font-size: 0.8rem; color: #22c55e;">
                ● Systems Operational
            </span>
        </div>
    </div>
    <hr style="border-color: #334155; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True,
)

# ============================================
# SYSTEM HEALTH
# ============================================
st.markdown("### 🖥️ Infrastructure Health")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="admin-card">
            <div style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">API Latency</div>
            <div style="font-size:1.8rem; font-weight:bold; color:#22c55e;">24ms</div>
            <div style="font-size:0.8rem; color:#64748b;">99.9% Uptime</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="admin-card">
            <div style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">Database Load</div>
            <div style="font-size:1.8rem; font-weight:bold; color:#3b82f6;">42%</div>
            <div style="font-size:0.8rem; color:#64748b;">12 Active Connections</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="admin-card">
            <div style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">Failed Pipelines</div>
            <div style="font-size:1.8rem; font-weight:bold; color:#ef4444;">1</div>
            <div style="font-size:0.8rem; color:#64748b;">ETL_MARKET_DATA_03</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        """
        <div class="admin-card">
            <div style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">Active Users</div>
            <div style="font-size:1.8rem; font-weight:bold; color:#f59e0b;">8</div>
            <div style="font-size:0.8rem; color:#64748b;">Across 3 departments</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================
# MANAGEMENT TABS
# ============================================
tab1, tab2, tab3 = st.tabs(["User Management", "Audit Logs", "System Alerts"])

# --- USER MANAGEMENT ---
with tab1:
    st.markdown("#### 👥 User Roles & Permissions")
    
    users = [
        {"Name": "Jonathan Chen", "Role": "Analyst", "Access": "Read/Write", "Status": "Active"},
        {"Name": "Noah Harrison", "Role": "Data Analyst", "Access": "Full Data", "Status": "Active"},
        {"Name": "Sarah Martinez", "Role": "Director", "Access": "View All", "Status": "Active"},
        {"Name": "John Doe", "Role": "Advisor", "Access": "Restricted", "Status": "Inactive"},
    ]
    
    for u in users:
        st.markdown(
            f"""
            <div style="display:flex; justify-content:space-between; align-items:center; padding:1rem; border-bottom:1px solid #334155;">
                <div style="width:25%; font-weight:bold;">{u['Name']}</div>
                <div style="width:20%; color:#94a3b8;">{u['Role']}</div>
                <div style="width:20%; color:#64748b;">{u['Access']}</div>
                <div style="width:15%;"><span style="color:{'#22c55e' if u['Status']=='Active' else '#64748b'}">{u['Status']}</span></div>
                <div style="width:20%; text-align:right;">
                    <button style="background:none; border:1px solid #334155; color:#94a3b8; border-radius:4px; cursor:pointer;">Edit</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Add New User"):
        show_stratify_loader(duration=1, message="Loading Form...")

# --- AUDIT LOGS ---
with tab2:
    st.markdown("#### 📜 Compliance Audit Trail")
    
    logs = [
        "[2024-10-24 14:32:01] USER:Jonathan_Chen ACTION:EXECUTE_TRADE SYMBOL:AAPL QTY:100",
        "[2024-10-24 14:15:22] USER:Noah_Harrison ACTION:EXPORT_DATASET TYPE:CSV SIZE:45MB",
        "[2024-10-24 13:45:00] SYSTEM:ETL_PIPELINE STATUS:SUCCESS DURATION:12s",
        "[2024-10-24 11:20:15] USER:Sarah_Martinez ACTION:VIEW_DASHBOARD ID:RISK_OVERVIEW",
        "[2024-10-24 09:00:01] SYSTEM:AUTH_SERVICE STATUS:STARTED PORT:8080"
    ]
    
    st.markdown('<div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:1rem; height:300px; overflow-y:auto;">', unsafe_allow_html=True)
    for log in logs:
        st.markdown(f'<div class="log-entry">{log}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Export Logs for Compliance"):
        show_stratify_loader(duration=2, message="Generating Report...")
        st.success("✅ Audit logs exported to PDF")

# --- SYSTEM ALERTS ---
with tab3:
    st.markdown("#### 🚨 Automated Alerts Configuration")
    
    c_a, c_b = st.columns(2)
    with c_a:
        st.toggle("Notify on Pipeline Failure", value=True)
        st.toggle("Notify on High Latency (>100ms)", value=True)
        st.toggle("Notify on Unauthorized Access Attempt", value=True)
    with c_b:
        st.toggle("Weekly Usage Reports", value=False)
        st.toggle("Disk Space Warnings (<10%)", value=True)

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("← Return to Main Menu"):
    st.switch_page("Home.py")