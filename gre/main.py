import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import time

# --- 1. CONFIGURATION & METAVERSE THEME ---
st.set_page_config(
    page_title="BHARAT NEXUS | The Industrial Core",
    page_icon="🕉️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE "GOAT" CSS (Deep Space & Motion) ---
st.markdown("""
    <style>
    /* FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Space+Grotesk:wght@300;500;700&display=swap');

    /* UNIVERSE BACKGROUND */
    .stApp {
        background-color: #030305;
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(255, 136, 0, 0.08) 0%, transparent 25%), 
            radial-gradient(circle at 85% 30%, rgba(0, 100, 255, 0.08) 0%, transparent 25%);
        color: #e0e0e0;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* HEADINGS */
    h1 {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to right, #FF9933, #FFFFFF, #138808); /* INDIA FLAG GRADIENT */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        animation: glow 3s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px rgba(255, 153, 51, 0.2); }
        to { text-shadow: 0 0 20px rgba(19, 136, 8, 0.4); }
    }

    /* CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 12px;
        padding: 25px;
        transition: transform 0.4s ease, border-color 0.4s ease;
    }
    .glass-card:hover {
        transform: translateY(-8px);
        border-color: #FF9933;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* NAVIGATION */
    section[data-testid="stSidebar"] {
        background: #0a0a0f;
        border-right: 1px solid #222;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---
def draw_3d_globe():
    # Focused on INDIA coordinates + Global Trade Routes
    df_places = pd.DataFrame({
        'lat': [20.5937, 28.6139, 19.0760, 51.5074, 40.7128, 35.6895, -33.8688],
        'lon': [78.9629, 77.2090, 72.8777, -0.1278, -74.0060, 139.6917, 151.2093],
        'city': ['INDIA CORE', 'New Delhi (HQ)', 'Mumbai (Port)', 'London', 'New York', 'Tokyo', 'Sydney'],
        'size': [30, 15, 15, 10, 10, 10, 10]
    })
    
    fig = go.Figure(data=go.Scattergeo(
        lon = df_places['lon'],
        lat = df_places['lat'],
        text = df_places['city'],
        mode = 'markers+text',
        marker = dict(
            size = df_places['size'],
            color = ['#FF9933', '#ffffff', '#138808', '#555', '#555', '#555', '#555'],
            line = dict(width=1, color='rgba(255,255,255,0.5)')
        )
    ))

    # Flight paths from India to World
    for i in range(3, 7):
        fig.add_trace(
            go.Scattergeo(
                lon = [78.9629, df_places['lon'][i]],
                lat = [20.5937, df_places['lat'][i]],
                mode = 'lines',
                line = dict(width=1, color='#FF9933'),
                opacity = 0.5
            )
        )

    fig.update_geos(
        projection_type="orthographic",
        landcolor="#1a1a1a",
        oceancolor="#050510",
        showocean=True,
        lakecolor="#050510"
    )
    fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor='rgba(0,0,0,0)')
    return fig

# --- 4. NAVIGATION SYSTEM ---
page = st.sidebar.radio("NEXUS NAVIGATION", ["🌌 THE METAVERSE (Home)", "📊 MARKET INTEL (Live)", "🇮🇳 INDIA STRATEGY"])

# --- PAGE 1: THE METAVERSE (HOME) ---
if page == "🌌 THE METAVERSE (Home)":
    
    # HERO SECTION
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1>BHARAT NEXUS</h1>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size: 1.5rem; color: #aaa; margin-bottom: 20px;">
        The Central Nervous System of Indian Industrial Supply Chains.
        </div>
        """, unsafe_allow_html=True)
        
        # Animated Text
        st.markdown("""
        <div style="border-left: 3px solid #FF9933; padding-left: 15px;">
            <i>"Not just a trader. We are the architect of the material flow."</i>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Stats Row
        c1, c2, c3 = st.columns(3)
        c1.metric("Global Reach", "14 Nations")
        c2.metric("India Hubs", "28 States")
        c3.metric("Material Flow", "2.4 MT/Year")

    with col2:
        # THE ROTATING GLOBE
        st.plotly_chart(draw_3d_globe(), use_container_width=True)

    # SCROLLING TICKER
    st.markdown("---")
    st.markdown("""
    <marquee style="color: #888; font-family: 'Space Grotesk'; font-size: 1.2rem;">
    LIVE: TATA STEEL +1.2%  •  JSW STEEL -0.4%  •  COAL INDIA +2.1%  •  HINDALCO +0.8%  •  VEDANTA -0.1%  •  ADANI ENT +3.4%
    </marquee>
    """, unsafe_allow_html=True)

# --- PAGE 2: MARKET INTEL (LIVE CHARTS) ---
elif page == "📊 MARKET INTEL (Live)":
    st.markdown("## 📡 LIVE COMMODITY INTELLIGENCE")
    st.markdown("Tracking critical raw material prices across Indian Spot Markets.")
    
    # FILTER BAR
    col1, col2, col3 = st.columns([1,1,2])
    with col1:
        metal = st.selectbox("Select Commodity", ["Steel (HRC)", "Aluminium Ingot", "Copper Cathode", "Lithium Carbonate"])
    with col2:
        market = st.selectbox("Market Hub", ["Mumbai Spot", "Delhi NCR", "Chennai Port", "Kolkata"])
    
    # LIVE CHART GENERATION
    # Generating a sophisticated looking "Area Chart" with gradient
    dates = pd.date_range(end=datetime.now(), periods=100, freq='D')
    base = 45000 if "Steel" in metal else 750000 if "Lithium" in metal else 200000
    prices = base + np.cumsum(np.random.randn(100) * (base * 0.02))
    
    df_chart = pd.DataFrame({'Date': dates, 'Price': prices})
    
    fig = px.area(df_chart, x='Date', y='Price', title=f"{metal} Price Trend - {market}")
    fig.update_traces(line_color='#FF9933', fillcolor='rgba(255, 153, 51, 0.1)')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#aaa',
        xaxis_showgrid=False,
        yaxis_gridcolor='rgba(255,255,255,0.1)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ANALYST NOTE
    st.info(f"ANALYST NOTE: {metal} showing strong accumulation patterns in {market} due to pre-monsoon stocking by auto-manufacturers.")

# --- PAGE 3: INDIA STRATEGY (DEEP RESEARCH) ---
elif page == "🇮🇳 INDIA STRATEGY":
    st.markdown("## 🏗️ THE INDIA VERTICAL")
    st.write("Deep-dive into the raw material ecosystem of the subcontinent.")
    
    # 3 COLUMNS OF CARDS
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="glass-card">
            <h3>🏭 Urban Mining</h3>
            <p>Leveraging India's 3.2M tons of e-waste. Creating a circular economy for Copper, Gold, and Palladium extraction.</p>
            <small style="color:#FF9933">Focus: Delhi NCR, Bengaluru</small>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="glass-card">
            <h3>⛏️ Mineral Security</h3>
            <p>Securing Lithium and Cobalt supply chains for India's 2030 EV targets. B2B procurement for battery gigafactories.</p>
            <small style="color:#FF9933">Focus: Gujarat, Karnataka</small>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="glass-card">
            <h3>🚢 Trade Finance</h3>
            <p>Bridging the working capital gap for SME manufacturers in Haryana and Punjab. Factoring and credit lines.</p>
            <small style="color:#FF9933">Focus: Ludhiana, Panipat</small>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("### 🗺️ REGIONAL DOMINANCE MAP")
    
    # STATIC MAP OF INDUSTRIAL HUBS
    st.markdown("Activating Satellite View of Key Industrial Clusters...")
    
    # Fake Map Data focusing on industrial belts
    map_data = pd.DataFrame({
        'lat': [28.4089, 21.1702, 12.9716, 22.5726],
        'lon': [77.3178, 72.8311, 77.5946, 88.3639],
        'hub': ['Haryana (Auto)', 'Surat (Diamond/Tex)', 'Bengaluru (Tech/Waste)', 'Kolkata (Steel)']
    })
    
    st.map(map_data, zoom=4, use_container_width=True)
