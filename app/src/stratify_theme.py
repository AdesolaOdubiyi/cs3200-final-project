"""
Stratify Complete CSS Theme - Light Mode
Save as: stratify_theme.py

Import and apply to any Streamlit page:
    from stratify_theme import apply_stratify_theme
    apply_stratify_theme()
"""

import streamlit as st

# Stratify Brand Colors - Dark Mode
COLORS = {
    # Primary Palette
    "primary": "#3b82f6",           # Electric Blue
    "primary_light": "#60a5fa",     # Medium Blue
    "primary_lighter": "#93c5fd",   # Light Sky Blue
    "primary_lightest": "#bfdbfe",  # Lightest Blue
    "primary_dark": "#2563eb",      # Deep Blue
    "primary_darker": "#1e40af",    # Darker Blue
    
    # Background - Dark Mode
    "background": "#0f172a",        # Main Background (alias)
    "bg_white": "#0f172a",          # Dark Slate (main background)
    "bg_light": "#1e293b",          # Slate 800 (cards)
    "bg_medium": "#334155",         # Slate 700 (hover states)
    "bg_border": "#1e293b",         # Border color
    
    # Text - Dark Mode
    "text_primary": "#f8fafc",      # White/Very Light Gray (main text)
    "text_secondary": "#cbd5e1",    # Light Gray (secondary text)
    "text_tertiary": "#94a3b8",     # Muted Gray (captions)
    
    # Semantic Colors
    "success": "#22c55e",           # Green
    "warning": "#f59e0b",           # Orange
    "error": "#ef4444",             # Red
    "info": "#3b82f6",              # Blue
}

# Export common colors as variables for easy import
background = COLORS['background']
primary = COLORS['primary']
secondary = COLORS['text_secondary']

# Complete Stratify CSS Theme - Dark Mode
STRATIFY_CSS = f"""
<style>

/* ============================================
   STRATIFY THEME - DARK MODE
   Portfolio Intelligence Platform
   ============================================ */

/* ==================== FONTS ==================== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

/* ==================== BASE STYLES ==================== */

/* Root Variables */
:root {{
    --primary: {COLORS['primary']};
    --primary-light: {COLORS['primary_light']};
    --primary-lighter: {COLORS['primary_lighter']};
    --primary-dark: {COLORS['primary_dark']};
    --bg-white: {COLORS['bg_white']};
    --bg-light: {COLORS['bg_light']};
    --bg-medium: {COLORS['bg_medium']};
    --bg-border: {COLORS['bg_border']};
    --text-primary: {COLORS['text_primary']};
    --text-secondary: {COLORS['text_secondary']};
    --text-tertiary: {COLORS['text_tertiary']};
    --success: {COLORS['success']};
    --warning: {COLORS['warning']};
    --error: {COLORS['error']};
    --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-mono: 'JetBrains Mono', 'Courier New', monospace;
}}

/* Main App Background - Dark */
.stApp {{
    background-color: var(--bg-white) !important;
    background-image: 
        linear-gradient(rgba(59, 130, 246, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(59, 130, 246, 0.03) 1px, transparent 1px);
    background-size: 50px 50px;
    font-family: var(--font-main) !important;
    color: var(--text-primary) !important;
}}

/* ==================== SIDEBAR ==================== */

section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%) !important;
    border-right: 1px solid #334155 !important;
}}

/* Sidebar content wrapper */
section[data-testid="stSidebar"] .stMarkdown a {{
    color: var(--primary-light) !important;
    text-decoration: none !important;
    transition: all 0.3s ease !important;
}}

section[data-testid="stSidebar"] .stMarkdown a:hover {{
    color: var(--primary) !important;
    text-decoration: underline !important;
}}

section[data-testid="stSidebar"] button {{
    transition: all 0.3s ease !important;
    background-color: transparent !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--bg-medium) !important;
}}

section[data-testid="stSidebar"] button:hover {{
    border-color: var(--primary) !important;
    background-color: rgba(59, 130, 246, 0.1) !important;
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.2) !important;
}}

/* Sidebar Logo Area */
section[data-testid="stSidebar"] > div:first-child {{
    padding-top: 2rem !important;
    text-align: center !important;
    border-bottom: 1px solid var(--bg-medium) !important;
    margin-bottom: 1rem !important;
    padding-bottom: 1rem !important;
}}

/* ==================== HEADER & TOP BAR ==================== */

header[data-testid="stHeader"] {{
    background-color: var(--bg-white) !important;
    border-bottom: 1px solid var(--bg-medium) !important;
}}

/* Sidebar Collapse Button */
button[kind="header"] {{
    background-color: transparent !important;
    color: var(--text-secondary) !important;
    border: none !important;
}}

button[kind="header"]:hover {{
    color: var(--primary) !important;
    background-color: var(--bg-light) !important;
}}

/* Hide the decoration bar at the top */
div[data-testid="stDecoration"] {{
    display: none !important;
}}

/* ==================== TYPOGRAPHY ==================== */

html, body, [class*="stMarkdown"], p, label {{
    color: var(--text-primary) !important;
    font-family: var(--font-main) !important;
}}

/* Headers */
h1, h2, h3, h4, h5, h6 {{
    color: var(--text-primary) !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
    font-family: var(--font-main) !important;
    margin-top: 1.5rem !important;
    margin-bottom: 1rem !important;
}}

h1 {{
    font-size: 2.5rem !important;
    border-bottom: 3px solid var(--primary) !important;
    padding-bottom: 0.75rem !important;
    margin-bottom: 1.5rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    color: var(--primary-dark) !important;
}}

h2 {{
    font-size: 2rem !important;
    color: var(--text-primary) !important;
    border-bottom: 2px solid var(--bg-border) !important;
    padding-bottom: 0.5rem !important;
}}

h3 {{
    font-size: 1.5rem !important;
    color: var(--text-primary) !important;
}}

h4 {{
    font-size: 1.25rem !important;
    color: var(--text-secondary) !important;
}}

/* Links */
a {{
    color: var(--primary) !important;
    text-decoration: none !important;
    transition: all 0.3s ease !important;
}}

a:hover {{
    color: var(--primary-dark) !important;
    text-decoration: underline !important;
}}

/* ==================== BUTTONS ==================== */

/* Primary Buttons */
div.stButton > button {{
    background: #3b82f6 !important;
    color: #ffffff !important;
    border: 1px solid #2563eb !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    border-radius: 8px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s ease !important;
    font-family: var(--font-main) !important;
}}

div.stButton > button:hover {{
    background: #2563eb !important;
    border-color: #60a5fa !important;
    box-shadow: 0 6px 12px rgba(59, 130, 246, 0.4) !important;
    transform: translateY(-2px) !important;
    color: #ffffff !important;
}}

div.stButton > button:active {{
    transform: translateY(0px) !important;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3) !important;
}}

div.stButton > button:disabled {{
    background: #334155 !important;
    color: #94a3b8 !important;
    border-color: #475569 !important;
    box-shadow: none !important;
    cursor: not-allowed !important;
}}

/* Download Button */
.stDownloadButton > button {{
    background: linear-gradient(135deg, var(--success) 0%, #16a34a 100%) !important;
    color: white !important;
    border: none !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 6px rgba(34, 197, 94, 0.25) !important;
    transition: all 0.3s ease !important;
}}

.stDownloadButton > button:hover {{
    background: linear-gradient(135deg, #16a34a 0%, #15803d 100%) !important;
    box-shadow: 0 6px 12px rgba(34, 197, 94, 0.35) !important;
    transform: translateY(-2px) !important;
}}

/* ==================== METRICS & KPIs ==================== */

[data-testid="stMetricValue"] {{
    font-size: 2.25rem !important;
    font-weight: 700 !important;
    color: var(--primary) !important;
    font-family: var(--font-mono) !important;
}}

[data-testid="stMetricLabel"] {{
    font-size: 0.85rem !important;
    color: var(--text-secondary) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    font-weight: 600 !important;
}}

[data-testid="stMetricDelta"] {{
    font-family: var(--font-mono) !important;
    font-size: 0.9rem !important;
}}

[data-testid="stMetricDelta"][data-arrow="up"] {{
    color: var(--success) !important;
}}

[data-testid="stMetricDelta"][data-arrow="down"] {{
    color: var(--error) !important;
}}

/* ==================== DATA TABLES ==================== */

.stDataFrame {{
    background-color: var(--bg-white) !important;
    border: 1px solid var(--bg-border) !important;
    border-radius: 8px !important;
    font-family: var(--font-mono) !important;
    overflow: hidden !important;
}}

.stDataFrame thead tr th {{
    background-color: var(--primary) !important;
    color: white !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.05em !important;
    padding: 1rem !important;
    border-bottom: 2px solid var(--primary-dark) !important;
}}

.stDataFrame tbody tr {{
    transition: all 0.2s ease !important;
    background-color: var(--bg-white) !important;
}}

.stDataFrame tbody tr:nth-child(even) {{
    background-color: var(--bg-light) !important;
}}

.stDataFrame tbody tr:hover {{
    background-color: rgba(59, 130, 246, 0.08) !important;
}}

.stDataFrame tbody tr td {{
    color: var(--text-primary) !important;
    padding: 0.75rem 1rem !important;
    border-bottom: 1px solid var(--bg-border) !important;
}}

/* ==================== FORMS & INPUTS ==================== */

/* Text Input */
input, textarea, select {{
    background-color: var(--bg-white) !important;
    border: 1px solid var(--bg-border) !important;
    color: var(--text-primary) !important;
    border-radius: 6px !important;
    padding: 0.75rem !important;
    font-family: var(--font-mono) !important;
    transition: all 0.3s ease !important;
}}

input:focus, textarea:focus, select:focus {{
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
    outline: none !important;
}}

input:hover, textarea:hover, select:hover {{
    border-color: var(--primary-light) !important;
}}

/* Labels */
label {{
    color: var(--text-secondary) !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    margin-bottom: 0.5rem !important;
}}

/* Selectbox */
[data-baseweb="select"] {{
    background-color: var(--bg-white) !important;
    border: 1px solid var(--bg-border) !important;
    border-radius: 6px !important;
}}

[data-baseweb="select"]:hover {{
    border-color: var(--primary) !important;
}}

/* Number Input */
[data-testid="stNumberInput"] input {{
    font-family: var(--font-mono) !important;
}}

/* Text Input */
[data-testid="stTextInput"] input {{
    font-family: var(--font-mono) !important;
}}

/* Text Area */
[data-testid="stTextArea"] textarea {{
    font-family: var(--font-mono) !important;
    min-height: 100px !important;
}}

/* ==================== NOTIFICATIONS ==================== */

/* Info Box */
.stAlert, [data-baseweb="notification"] {{
    background-color: var(--bg-light) !important;
    border-left: 4px solid var(--primary) !important;
    border-radius: 6px !important;
    padding: 1rem !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--bg-border) !important;
}}

[data-baseweb="notification"][kind="info"] {{
    background-color: rgba(59, 130, 246, 0.08) !important;
    border-left: 4px solid var(--primary) !important;
}}

/* Success Box */
[data-baseweb="notification"][kind="success"] {{
    background-color: rgba(34, 197, 94, 0.08) !important;
    border-left: 4px solid var(--success) !important;
}}

/* Warning Box */
[data-baseweb="notification"][kind="warning"] {{
    background-color: rgba(245, 158, 11, 0.08) !important;
    border-left: 4px solid var(--warning) !important;
}}

/* Error Box */
[data-baseweb="notification"][kind="error"] {{
    background-color: rgba(239, 68, 68, 0.08) !important;
    border-left: 4px solid var(--error) !important;
}}

/* ==================== CONTAINERS & CARDS ==================== */

/* General containers */
.element-container {{
    border-radius: 8px !important;
}}

/* Expander */
.streamlit-expanderHeader {{
    background-color: var(--bg-light) !important;
    border: 1px solid var(--bg-border) !important;
    border-radius: 6px !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}}

.streamlit-expanderHeader:hover {{
    background-color: var(--bg-medium) !important;
    border-color: var(--primary) !important;
}}

.streamlit-expanderContent {{
    background-color: var(--bg-white) !important;
    border: 1px solid var(--bg-border) !important;
    border-top: none !important;
    border-radius: 0 0 6px 6px !important;
}}

/* ==================== TABS ==================== */

.stTabs [data-baseweb="tab-list"] {{
    gap: 8px !important;
    background-color: var(--bg-light) !important;
    border-radius: 8px !important;
    padding: 0.5rem !important;
}}

.stTabs [data-baseweb="tab"] {{
    background-color: transparent !important;
    border-radius: 6px !important;
    color: var(--text-secondary) !important;
    font-weight: 600 !important;
    padding: 0.75rem 1.5rem !important;
    transition: all 0.3s ease !important;
}}

.stTabs [data-baseweb="tab"]:hover {{
    background-color: rgba(59, 130, 246, 0.08) !important;
    color: var(--primary) !important;
}}

.stTabs [aria-selected="true"] {{
    background-color: var(--primary) !important;
    color: white !important;
}}

/* ==================== CHARTS & VISUALIZATIONS ==================== */

.js-plotly-plot {{
    background-color: var(--bg-white) !important;
    border-radius: 8px !important;
    border: 1px solid var(--bg-border) !important;
    padding: 1rem !important;
}}

/* ==================== CODE BLOCKS ==================== */

code {{
    background-color: var(--bg-light) !important;
    color: var(--primary) !important;
    padding: 0.2rem 0.4rem !important;
    border-radius: 4px !important;
    font-family: var(--font-mono) !important;
    font-size: 0.9em !important;
}}

pre {{
    background-color: var(--bg-light) !important;
    border: 1px solid var(--bg-border) !important;
    border-radius: 8px !important;
    padding: 1rem !important;
}}

pre code {{
    background-color: transparent !important;
}}

/* ==================== DIVIDERS ==================== */

hr {{
    border-color: var(--bg-border) !important;
    margin: 2rem 0 !important;
    opacity: 1 !important;
}}

/* ==================== SCROLLBAR ==================== */

::-webkit-scrollbar {{
    width: 10px !important;
    height: 10px !important;
}}

::-webkit-scrollbar-track {{
    background: var(--bg-light) !important;
}}

::-webkit-scrollbar-thumb {{
    background: var(--primary) !important;
    border-radius: 5px !important;
}}

::-webkit-scrollbar-thumb:hover {{
    background: var(--primary-dark) !important;
}}

/* ==================== FILE UPLOADER ==================== */

[data-testid="stFileUploader"] {{
    background-color: var(--bg-light) !important;
    border: 2px dashed var(--bg-border) !important;
    border-radius: 8px !important;
    padding: 2rem !important;
    transition: all 0.3s ease !important;
}}

[data-testid="stFileUploader"]:hover {{
    border-color: var(--primary) !important;
    background-color: rgba(59, 130, 246, 0.05) !important;
}}

/* ==================== PROGRESS BAR ==================== */

.stProgress > div > div {{
    background-color: var(--primary) !important;
}}

/* ==================== SPINNER ==================== */

.stSpinner > div {{
    border-top-color: var(--primary) !important;
}}

/* ==================== RADIO & CHECKBOX ==================== */

.stRadio > div {{
    background-color: var(--bg-light) !important;
    border-radius: 6px !important;
    padding: 0.5rem !important;
}}

.stCheckbox {{
    color: var(--text-primary) !important;
}}

/* ==================== SLIDER ==================== */

.stSlider [data-baseweb="slider"] {{
    background: linear-gradient(to right, var(--primary), var(--primary-dark)) !important;
}}

/* ==================== COLUMNS ==================== */

[data-testid="column"] {{
    padding: 0.5rem !important;
}}

/* ==================== TOOLTIPS ==================== */

.stTooltipIcon {{
    color: var(--primary) !important;
}}

/* ==================== DATE & TIME INPUTS ==================== */

[data-testid="stDateInput"] input,
[data-testid="stTimeInput"] input {{
    font-family: var(--font-mono) !important;
}}

/* ==================== CUSTOM CLASSES ==================== */

/* Metric Card */
.metric-card {{
    background: var(--bg-white) !important;
    border: 2px solid var(--bg-border) !important;
    border-radius: 12px !important;
    padding: 1.5rem !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05) !important;
    transition: all 0.3s ease !important;
}}

.metric-card:hover {{
    border-color: var(--primary) !important;
    box-shadow: 0 4px 16px rgba(59, 130, 246, 0.15) !important;
    transform: translateY(-2px) !important;
}}

/* Terminal-style Numbers */
.terminal-number {{
    font-family: var(--font-mono) !important;
    color: var(--primary) !important;
    font-weight: 600 !important;
}}

/* Status Indicators */
.status-online {{
    color: var(--success) !important;
}}

.status-warning {{
    color: var(--warning) !important;
}}

.status-error {{
    color: var(--error) !important;
}}

/* ==================== FOOTER ==================== */

.footer {{
    text-align: center !important;
    color: var(--text-tertiary) !important;
    font-size: 0.85rem !important;
    padding: 2rem 0 !important;
    border-top: 1px solid var(--bg-border) !important;
    margin-top: 3rem !important;
}}

/* ==================== RESPONSIVE ==================== */

@media (max-width: 768px) {{
    h1 {{
        font-size: 2rem !important;
    }}
    
    h2 {{
        font-size: 1.5rem !important;
    }}
    
    [data-testid="stMetricValue"] {{
        font-size: 1.75rem !important;
    }}
    
    div.stButton > button {{
        padding: 0.6rem 1.5rem !important;
        font-size: 0.9rem !important;
    }}
}}

/* ==================== ANIMATIONS ==================== */

@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.fade-in {{
    animation: fadeIn 0.5s ease-in-out;
}}

</style>
"""


def apply_stratify_theme():
    """
    Apply the complete Stratify theme to the current Streamlit page
    
    Usage:
        from stratify_theme import apply_stratify_theme
        apply_stratify_theme()
    """
    st.markdown(STRATIFY_CSS, unsafe_allow_html=True)


def get_color(color_name):
    """
    Get a specific color from the Stratify palette
    
    Args:
        color_name: Key from COLORS dict (e.g., 'primary', 'success', etc.)
    
    Returns:
        str: Hex color code
    
    Usage:
        primary_color = get_color('primary')
        st.markdown(f'<div style="color: {primary_color}">Text</div>', unsafe_allow_html=True)
    """
    return COLORS.get(color_name, COLORS['primary'])
