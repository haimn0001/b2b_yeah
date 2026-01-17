import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import time
from datetime import datetime

# --- 1. CONFIGURATION: THE "OFFICE OF THE CEO" VIEW ---
st.set_page_config(
    page_title="BHARAT INFRA | The B2B Backbone",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS: PROFESSIONAL, DENSE, HIGH-CONTRAST ---
st.markdown("""
    <style>
    /* CORE THEME: Deep Blue & Industrial Grey (Like Top B2B Firms) */
    .stApp {
        background-color: #f0f2f6;
        color: #1a1a1a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* SIDEBAR: Dark Command Center */
    section[data-testid="stSidebar"] {
        background-color: #0e1117;
        color: white;
    }
    
    /* HEADINGS */
    h1, h2, h3 {
        color: #0f2942;
        font-weight: 800;
        text-transform: uppercase;
    }
    
    /* METRIC CARDS - WHITE & CLEAN */
    div[data-testid="metric-container"] {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #d93025; /* Industrial Red Accent */
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    /* DATAFRAME TABLES */
    .stDataFrame {
        border: 1px solid #ddd;
        border-radius: 5px;
    }
    
    /* TICKER */
    .ticker-container {
        background: #0f2942;
        color: #fff;
        padding: 10px;
        font-family: monospace;
        overflow: hidden;
        white-space: nowrap;
    }
    
    /* CUSTOM ALERTS */
    .alert-box {
        padding: 15px;
        background-color: #e8f0fe;
        border-left: 5px solid #1a73e8;
        color: #1a73e8;
        border-radius: 4px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS: GENERATING "REALISTIC" INDIAN DATA ---
def get_live_prices(sector):
    # Base prices in INR
    base = {
        "STEEL": {"TMT Bar (Fe550)": 52000, "HRC Coil": 56000, "Billet": 44500, "Scrap (Melting)": 34000},
        "POLYMERS": {"PP Raffia": 92000, "HDPE Blow": 98000, "PVC Resin": 78000, "LLDPE": 94000},
        "CHEMICALS": {"Phenol": 88000, "Methanol": 26000, "Acetic Acid": 34000, "Caustic Soda": 42000},
        "AGRI": {"Sugar (M-30)": 3600, "Wheat": 2400, "Maize": 2100, "Cotton Yarn": 240000},
        "ENERGY": {"Thermal Coal (RB2)": 12500, "Petcoke": 14000, "Bitumen (VG30)": 39000}
    }
    
    data = []
    for item, price in base[sector].items():
        # Random fluctuation to look "Live"
        fluctuation = np.random.randint(-200, 200)
        current_price = price + fluctuation
        change = round((fluctuation / price) * 100, 2)
        trend = "▲" if change > 0 else "▼"
        location = "Mandi Gobindgarh" if sector == "STEEL" else "Mundra Port" if sector == "CHEMICALS" else "Panipat"
        data.append([item, location, f"₹{current_price:,}", f"{change}% {trend}"])
    
    return pd.DataFrame(data, columns=["Material", "Hub / Port", "Spot Price (INR/MT)", "24h Change"])

# --- 4. SIDEBAR: THE "SMART PROCUREMENT" ENGINE ---
with st.sidebar:
    st.title("BHARAT INFRA")
    st.caption("Supply Chain | Finance | Intelligence")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/India_flag_icon.svg", width=50) # Just a flag placeholder
    
    st.markdown("---")
    
    menu = st.radio("Business Vertical", [
        "🏢 Dashboard (HQ)", 
        "🏗️ Steel & Infra", 
        "🧪 Chemicals & Poly", 
        "🏭 Manufacturing Hubs",
        "💰 Credit & Finance"
    ])
    
    st.markdown("---")
    st.success("CREDIT LINE AVAILABLE")
    st.metric("Your Buying Power", "₹ 2.5 Cr", "Pre-Approved")
    st.button("Request Disbursement")

# --- 5. PAGE CONTENT ---

# >>>> HEADER & TICKER <<<<
st.title("🇮🇳 BHARAT INFRA & TRADING CORP")
st.markdown("**Empowering Indian SMEs with Raw Materials & Working Capital**")

# Scrolling Ticker
st.markdown("""
<div class="ticker-container">
    MARKET LIVE: TMT (Rourkela) ₹52,400 ▲ | HRC (Mumbai) ₹56,100 ▼ | SCRAP (Alang) ₹33,800 ▲ | COAL (Paradip) ₹12,400 ▼ | SUGAR (Kolhapur) ₹3,550 ▲
</div>
<br>
""", unsafe_allow_html=True)

# >>>> SECTION 1: THE HQ DASHBOARD <<<<
if menu == "🏢 Dashboard (HQ)":
    # Top Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Live Orders", "1,240", "+12%")
    c2.metric("Tonnage Moving", "45,000 MT", "Across 14 States")
    c3.metric("Active Credit", "₹ 450 Cr", "Deployed")
    c4.metric("Port Congestion", "LOW", "Mundra / JNPT")

    st.markdown("### 📡 Live Material Rates (All Sectors)")
    
    tab1, tab2, tab3 = st.tabs(["STEEL & METALS", "POLYMERS & CHEM", "ENERGY & AGRI"])
    
    with tab1:
        st.dataframe(get_live_prices("STEEL"), use_container_width=True, hide_index=True)
        st.caption("Source: Primary Mills (JSW, Tata) & Secondary Markets (Raipur, Durgapur)")
    
    with tab2:
        c_a, c_b = st.columns(2)
        with c_a:
            st.write("**Polymers (Ex-Mundra)**")
            st.dataframe(get_live_prices("POLYMERS"), use_container_width=True, hide_index=True)
        with c_b:
            st.write("**Bulk Chemicals (Ex-Kandla)**")
            st.dataframe(get_live_prices("CHEMICALS"), use_container_width=True, hide_index=True)
            
    with tab3:
        st.dataframe(get_live_prices("ENERGY"), use_container_width=True, hide_index=True)

# >>>> SECTION 2: DEEP RESEARCH - HUBS & PORTS <<<<
elif menu == "🏭 Manufacturing Hubs":
    st.header("🗺️ The Indian Supply Network")
    st.write("Real-time tracking of 450+ Partner Factories, Warehouses, and Port Terminals.")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # MAP OF INDIA INDUSTRIAL HUBS
        # Coordinates for major industrial clusters
        df_hubs = pd.DataFrame({
            'lat': [30.7046, 21.1702, 21.2514, 22.5726, 13.0827, 22.8046, 28.6139],
            'lon': [76.7179, 72.8311, 81.6296, 88.3639, 80.2707, 70.1637, 77.2090],
            'name': ['Mandi Gobindgarh (Steel)', 'Surat (Textile/Chem)', 'Raipur (Sponge Iron)', 'Kolkata (Foundry)', 'Chennai (Auto)', 'Mundra Port (Import)', 'Delhi NCR (Construction)'],
            'type': ['Factory', 'Factory', 'Factory', 'Factory', 'Port', 'Port', 'Demand Center'],
            'volume': [500, 400, 450, 300, 350, 600, 550]
        })
        
        fig = px.scatter_geo(
            df_hubs, 
            lat='lat', 
            lon='lon', 
            size='volume',
            color='type',
            hover_name='name',
            scope='asia',
            title="Active Supply Clusters",
            color_discrete_map={'Factory': '#d93025', 'Port': '#1a73e8', 'Demand Center': '#188038'}
        )
        fig.update_geos(
            visible=False, resolution=50,
            showcountries=True, countrycolor="#cfd8dc",
            showsubunits=True, subunitcolor="#cfd8dc",
            fitbounds="locations" # Auto-zoom to India data
        )
        fig.update_layout(height=600, margin={"r":0,"t":40,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("### 🚚 Logistics Status")
        st.markdown("""
        <div class="alert-box">
        <b>Mundra Port:</b> Berthing Delay 12hrs. Container availability normal.
        </div>
        <div class="alert-box">
        <b>NH-48 (Delhi-Mumbai):</b> High traffic near Jaipur. +4hrs transit time.
        </div>
        <div class="alert-box">
        <b>Paradip Port:</b> Coal rake availability LOW.
        </div>
        """, unsafe_allow_html=True)

# >>>> SECTION 3: CREDIT & FINANCE (The 'OfBusiness' Secret) <<<<
elif menu == "💰 Credit & Finance":
    st.header("💸 SME Working Capital Finance")
    st.markdown("Stop blocking your cash flow. Buy raw materials now, pay in 90 days.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Why finance with us?**")
        st.markdown("""
        * **Zero Collateral** up to ₹2 Cr
        * **Interest Rates** starting @ 1.1% / month
        * **Direct Payment** to Supplier
        """)
        
        amount = st.slider("Required Credit Limit (₹ Lakhs)", 10, 500, 50)
        tenure = st.select_slider("Repayment Tenure", options=["30 Days", "60 Days", "90 Days", "120 Days"])
        
        interest = (amount * 100000) * 0.012 * (int(tenure.split()[0])/30)
        
        st.metric("Est. Interest Cost", f"₹ {int(interest):,}")
        st.button("Check Eligibility Instantly")
        
    with c2:
        # A Finance Chart
        st.write("<b>Credit Utilization Trend</b>", unsafe_allow_html=True)
        chart_data = pd.DataFrame(
            np.random.randn(12, 1).cumsum() + 50,
            columns=['Credit Score'],
            index=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        )
        st.bar_chart(chart_data)

# >>>> FALLBACK FOR OTHER MENUS <<<<
else:
    st.header(f"{menu} Section")
    st.write("Detailed procurement interface for this sector loading...")
    st.dataframe(get_live_prices("STEEL" if "Steel" in menu else "CHEMICALS"), use_container_width=True)
