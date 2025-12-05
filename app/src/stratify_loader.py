"""
Stratify Loading Animation - Clean Overlay Version
Save as: stratify_loader.py

This loader creates a professional overlay that hovers above page content
without shifting any elements around.
"""

import streamlit as st
import time

def show_stratify_loader(duration=2, style="cascade", speed="normal", message="Loading"):
    """
    Display Stratify branded wiping loading animation as an overlay
    
    Args:
        duration: How long to show the loader (seconds)
        style: "cascade", "sequential", "simultaneous", or "reverse"
        speed: "slow", "normal", or "fast"
        message: Custom loading message (NOT DISPLAYED - kept for compatibility)
    """
    
    # Animation speed CSS
    speed_css = {
        "slow": "3s",
        "normal": "2s",
        "fast": "1.2s"
    }
    
    # Animation delay patterns
    delays = {
        "cascade": ["0s", "0.3s", "0.6s", "0.9s"],
        "sequential": ["0s", "0.5s", "1s", "1.5s"],
        "simultaneous": ["0s", "0s", "0s", "0s"],
        "reverse": ["1.5s", "1s", "0.5s", "0s"]
    }
    
    animation_duration = speed_css.get(speed, "2s")
    animation_delays = delays.get(style, delays["cascade"])
    
    # Overlay loader with fixed positioning - CLEAN VERSION
    loader_html = f"""
    <style>
        /* Full-screen overlay that doesn't affect document flow */
        .stratify-loader-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.25);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            backdrop-filter: blur(8px);
            animation: fadeIn 0.3s ease-in;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        
        .stratify-loader-content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        
        /* MADE 25% SMALLER: 200px -> 150px, 140px -> 105px */
        .stratify-loader {{
            width: 150px;
            height: 105px;
            position: relative;
            margin: 0 auto;
        }}

        .layer-container {{
            position: absolute;
            overflow: hidden;
            border-radius: 8px;
        }}

        /* MADE 25% SMALLER: All dimensions reduced */
        .layer-container-1 {{
            height: 15px;
            top: 7.5px;
            left: 15px;
            width: 120px;
        }}

        .layer-container-2 {{
            height: 15px;
            top: 30px;
            left: 0;
            width: 135px;
        }}

        .layer-container-3 {{
            height: 15px;
            top: 52.5px;
            left: 15px;
            width: 120px;
        }}

        .layer-container-4 {{
            height: 15px;
            top: 75px;
            left: 0;
            width: 135px;
        }}

        .s-layer {{
            height: 100%;
            border-radius: 8px;
            animation: wipeRight {animation_duration} ease-in-out infinite;
        }}

        .s-layer-1 {{
            background: linear-gradient(90deg, #93c5fd, #bfdbfe);
            animation-delay: {animation_delays[0]};
        }}

        .s-layer-2 {{
            background: linear-gradient(90deg, #60a5fa, #93c5fd);
            animation-delay: {animation_delays[1]};
        }}

        .s-layer-3 {{
            background: linear-gradient(90deg, #3b82f6, #60a5fa);
            animation-delay: {animation_delays[2]};
        }}

        .s-layer-4 {{
            background: linear-gradient(90deg, #2563eb, #3b82f6);
            animation-delay: {animation_delays[3]};
        }}

        @keyframes wipeRight {{
            0% {{
                transform: translateX(-100%);
            }}
            50% {{
                transform: translateX(0%);
            }}
            100% {{
                transform: translateX(100%);
            }}
        }}
    </style>
    
    <div class="stratify-loader-overlay">
        <div class="stratify-loader-content">
            <div class="stratify-loader">
                <div class="layer-container layer-container-1">
                    <div class="s-layer s-layer-1"></div>
                </div>
                <div class="layer-container layer-container-2">
                    <div class="s-layer s-layer-2"></div>
                </div>
                <div class="layer-container layer-container-3">
                    <div class="s-layer s-layer-3"></div>
                </div>
                <div class="layer-container layer-container-4">
                    <div class="s-layer s-layer-4"></div>
                </div>
            </div>
            <!-- NO TEXT OR BRANDING - CLEAN MINIMAL DESIGN -->
        </div>
    </div>
    """
    
    # Display the loader as an overlay
    loader_placeholder = st.empty()
    loader_placeholder.markdown(loader_html, unsafe_allow_html=True)
    
    # Simulate loading
    time.sleep(duration)
    
    # Clear the loader with fade out
    loader_placeholder.empty()
