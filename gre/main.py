import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time

# --- 1. CONFIGURATION: THE "GOD MODE" UI ---
st.set_page_config(page_title="NEXUS | The Universe", page_icon="🪐", layout="wide")

# --- 2. THE CSS (Hides the 'Streamlit' branding, adds Neon effects) ---
st.markdown("""
    <style>
    /* DEEP SPACE BACKGROUND */
    .stApp {
        background-color: #000000;
        background-image: 
            radial-gradient(circle at 50% 50%, #1a0b2e 0%, #000000 100%);
        color: #fff;
    }
    
    /* REMOVE WHITE BARS */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* GLOWING TEXT */
    h1 {
        text-shadow: 0 0 20px #bf00ff, 0 0 40px #bf00ff;
        font-family: 'Courier New', monospace;
        text-transform: uppercase;
    }
    
    /* GLASS CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(191, 0, 255, 0.1);
    }
    
    /* NEON BUTTONS */
    .stButton>button {
        background: linear-gradient(90deg, #bf00ff, #00d4ff);
        color: white;
        border: none;
        font-weight: bold;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px #bf00ff;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. THE 3D UNIVERSE (INTERACTIVE GLOBE) ---
def get_universe_map():
    # Trade Routes from India (Nagpur Center)
    fig = go.Figure()

    # 1. The Globe (Dark Mode)
    fig.add_trace(go.Scattergeo(
        lon=[79, -74, 139, -0.1],
        lat=[21, 40, 35, 51],
        text=['INDIA HQ', 'USA Branch', 'Japan Hub', 'London Desk'],
        mode='markers+text',
        marker=dict(size=[20, 10, 10, 10], color=['#bf00ff', '#00d4ff', '#00d4ff', '#00d4ff']),
        textposition="top center",
        textfont=dict(color="white", size=14)
    ))

    # 2. Glowing Flight Paths (The "Nerves")
    destinations = [(-74, 40), (139, 35), (-0.1, 51), (151, -33)] # NY, Tokyo, London, Sydney
    for lon, lat in destinations:
        fig.add_trace(go.Scattergeo(
            lon=[79, lon], lat=[21, lat],
            mode='lines',
            line=dict(width=2, color='#bf00ff'),
            opacity=0.6
        ))

    fig.update_geos(
        projection_type="orthographic",
        showcoastlines=True, coastlinecolor="#333",
        showland=True, landcolor="#050505",
        showocean=True, oceancolor="#020205",
        showlakes=False,
        bgcolor='rgba(0,0,0,0)'
    )
    fig.update_layout(
        height=600, margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# --- 4. LAYOUT ---
c1, c2 = st.columns([1, 2])

with c1:
    st.markdown("# NEXUS <br> <span style='color:#00d4ff; font-size:0.6em'>UNIVERSE EDITION</span>", unsafe_allow_html=True)
    st.caption("Initializing Global Procurement Protocols...")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📡 LIVE INTEL")
    st.write(" **STEEL (HRC)**: ₹56,200 <span style='color:#00ff00'>▲ 1.2%</span>", unsafe_allow_html=True)
    st.write(" **LITHIUM**: ₹18,40,000 <span style='color:#ff0044'>▼ 0.5%</span>", unsafe_allow_html=True)
    st.write(" **COPPER**: ₹720/kg <span style='color:#00ff00'>▲ 0.8%</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 💸 CREDIT ENGINE")
    st.metric("Available Limit", "₹ 5,20,00,000")
    if st.button("DISBURSE FUNDS ⚡"):
        st.balloons()
        st.success("FUNDS TRANSFERRED TO ESCROW")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    # THE 3D MAP
    st.plotly_chart(get_universe_map(), use_container_width=True)

# --- 5. BOTTOM TICKER ---
st.markdown("""
<div style="background: linear-gradient(90deg, #000, #1a0b2e, #000); padding: 10px; border-top: 1px solid #333; text-align: center; color: #888;">
    SYSTEM ONLINE  •  ENCRYPTION: AES-256  •  LATENCY: 12ms  •  CONNECTED NODES: 4,021
</div>
""", unsafe_allow_html=True)
