import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta
import time

# --- 1. PAGE CONFIGURATION & "GAND FAD" THEME ---
st.set_page_config(
    page_title="NEXUS PRIME | Institutional Trading",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ADVANCED CSS (ANIMATIONS, GLOWS, TRANSITIONS) ---
st.markdown("""
    <style>
    /* IMPORT FUTURISTIC FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;500;700&family=Roboto+Mono:wght@400;700&display=swap');

    /* CORE THEME */
    .stApp {
        background-color: #000000;
        background-image: 
            linear-gradient(rgba(0, 255, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 255, 0.03) 1px, transparent 1px);
        background-size: 30px 30px;
        color: #e0e0e0;
        font-family: 'Rajdhani', sans-serif;
    }

    /* ANIMATED TICKER TAPE */
    .ticker-wrap {
        width: 100%;
        overflow: hidden;
        background-color: #0a0a0a;
        border-bottom: 1px solid #333;
        white-space: nowrap;
        padding: 5px 0;
    }
    .ticker {
        display: inline-block;
        animation: marquee 20s linear infinite;
    }
    @keyframes marquee {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    .ticker-item {
        display: inline-block;
        padding: 0 2rem;
        font-family: 'Roboto Mono', monospace;
        font-weight: bold;
    }
    .up { color: #00ff00; }
    .down { color: #ff0044; }

    /* DYNAMIC TEXT ANIMATION (The "Pop Up" Headline) */
    .dynamic-text:before {
        content: 'Reliable Supply';
        animation: animate infinite 9s;
        color: #00d4ff;
        font-weight: 800;
    }
    @keyframes animate {
        0% { content: 'Reliable Supply'; opacity: 0; }
        10% { opacity: 1; }
        30% { opacity: 1; }
        40% { opacity: 0; }
        
        41% { content: 'Best Market Rates'; opacity: 0; }
        50% { opacity: 1; }
        70% { opacity: 1; }
        80% { opacity: 0; }

        81% { content: 'Trusted Global Trade'; opacity: 0; }
        90% { opacity: 1; }
        100% { opacity: 0; }
    }

    /* GLASSMORPHISM CARDS */
    .glass-panel {
        background: rgba(20, 20, 30, 0.7);
        border: 1px solid rgba(0, 212, 255, 0.2);
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.1);
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
    }

    /* NEON BUTTONS */
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff, #005bea);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px #00d4ff;
        transform: scale(1.02);
        color: white;
    }
    
    /* INPUT STYLING */
    input, select {
        background-color: #0a0a0a !important;
        color: #00d4ff !important;
        border: 1px solid #333 !important;
    }
    
    h1, h2, h3 {
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---
def generate_live_data():
    # Simulate live candlestick data
    dates = pd.date_range(end=datetime.now(), periods=60, freq='1min')
    base_price = 15000 + np.cumsum(np.random.randn(60) * 50)
    
    df = pd.DataFrame({
        'Date': dates,
        'Open': base_price,
        'High': base_price + np.random.rand(60) * 50,
        'Low': base_price - np.random.rand(60) * 50,
        'Close': base_price + np.random.randn(60) * 20
    })
    return df

# --- 4. TOP TICKER (MARQUEE) ---
st.markdown("""
<div class="ticker-wrap">
    <div class="ticker">
        <span class="ticker-item">LITHIUM: $15,240 <span class="up">▲ 1.2%</span></span>
        <span class="ticker-item">COBALT: $32,100 <span class="down">▼ 0.5%</span></span>
        <span class="ticker-item">STEEL: $580 <span class="up">▲ 0.8%</span></span>
        <span class="ticker-item">COPPER: $8,400 <span class="up">▲ 2.1%</span></span>
        <span class="ticker-item">ALUMINUM: $2,250 <span class="down">▼ 0.1%</span></span>
        <span class="ticker-item">NICKEL: $19,800 <span class="up">▲ 1.5%</span></span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. MAIN HEADER WITH MOVING TEXT ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("<h1>NEXUS <span style='color:#00d4ff'>PRIME</span></h1>", unsafe_allow_html=True)
    # This is the "Pop Up" Changing Heading
    st.markdown("### The Most <span class='dynamic-text'></span> Platform", unsafe_allow_html=True)

with col2:
    st.metric(label="LIVE SERVER STATUS", value="ONLINE 🟢", delta="LATENCY: 12ms")

st.markdown("---")

# --- 6. LIVE MARKET DASHBOARD ---
# Layout: Chart on Left (2/3), Order Panel on Right (1/3)
c1, c2 = st.columns([3, 1])

with c1:
    st.markdown("### 📈 LIVE MARKET FEED: LITHIUM CARBONATE (Li2CO3)")
    
    # Generate Fake Live Chart
    chart_data = generate_live_data()
    
    fig = go.Figure(data=[go.Candlestick(
        x=chart_data['Date'],
        open=chart_data['Open'],
        high=chart_data['High'],
        low=chart_data['Low'],
        close=chart_data['Close'],
        increasing_line_color='#00ff00', 
        decreasing_line_color='#ff0044'
    )])
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        height=500,
        margin=dict(l=0, r=0, t=20, b=0),
        xaxis_rangeslider_visible=False
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown("### ⚡ QUICK TRADE")
    
    tab1, tab2 = st.tabs(["BUY", "SELL"])
    
    with tab1:
        st.markdown("**Order Type:**")
        order_type = st.selectbox("Type", ["Market Order", "Limit Order", "Stop Loss"], key="buy_type")
        
        st.markdown("**Commodity:**")
        asset = st.selectbox("Asset", ["Lithium", "Steel Scrap", "Cobalt", "Nickel"], key="buy_asset")
        
        qty = st.number_input("Quantity (MT)", min_value=1, value=10)
        
        # Live Price Calculation Simulation
        price = 15240
        total = qty * price
        
        st.markdown(f"""
        <div style='background:#111; padding:10px; border-radius:5px; margin: 10px 0;'>
            <small>Est. Price / MT</small><br>
            <strong style='color:#00d4ff; font-size: 1.2em'>${price:,.2f}</strong><br>
            <hr style='border-color: #333'>
            <small>Total Value</small><br>
            <strong style='color:#fff; font-size: 1.2em'>${total:,.2f}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 EXECUTE BUY ORDER"):
            with st.spinner("Connecting to Exchange..."):
                time.sleep(1.5) # Fake loading for realism
            st.success(f"ORDER FILLED: {qty} MT of {asset} @ ${price}")
            st.balloons()
            
    with tab2:
        st.info("Log in to access Seller Liquidity Pool.")
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. TRUST & STATS BAR (The "Trustfull" Part) ---
st.markdown("---")
st.markdown("### 🛡️ INSTITUTIONAL GRADE SECURITY")

stat1, stat2, stat3, stat4 = st.columns(4)

def stat_card(label, value, sub):
    st.markdown(f"""
    <div class="glass-panel" style="text-align: center;">
        <h2 style="margin:0; color:#00d4ff;">{value}</h2>
        <p style="margin:0; font-weight:bold;">{label}</p>
        <small style="color:#888;">{sub}</small>
    </div>
    """, unsafe_allow_html=True)

with stat1: stat_card("Verified Suppliers", "500+", "Global Network")
with stat2: stat_card("Trade Volume", "$120M", "Last 24 Hours")
with stat3: stat_card("Escrow Secured", "100%", "Bank Grade Vault")
with stat4: stat_card("Latency", "12ms", "High-Frequency Core")
