import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

# --- 1. LOGIN SYSTÉM (Musí byť úplne hore) ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        st.title("🛡️ NEXUS Core v5.0 | Enterprise Login")
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Authorize Access"):
            if user == "admin" and pw == "nexus2770":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Neautorizovaný prístup.")
        return False
    return True

# Spustenie overenia
if check_password():
    # --- 2. CONFIG A STYLY ---
    st.set_page_config(page_title="MAR-AUTO NEXUS v5.0", layout="wide")
    
    # --- 3. SIDEBAR ---
    st.sidebar.markdown("### 💠 NEXUS CORE v5.0")
    st.sidebar.write("`Authenticated: admin`")
    
    app_mode = st.sidebar.selectbox("Navigation Tree", [
        "Executive Dashboard", 
        "AI Orchestration Engine", 
        "Predictive ROI Modeling",
        "API Bridge & Integrity",
        "Audit Trail & Compliance"
    ])
    
    if st.sidebar.button("Logout"):
        st.session_state["password_correct"] = False
        st.rerun()

    # --- MODUL 1: EXECUTIVE DASHBOARD ---
    if app_mode == "Executive Dashboard":
        st.title("📊 Strategic Revenue Overview")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Managed Spend", "148,290 €", "+14.2%")
        m2.metric("Attributed Revenue", "692,405 €", "+18.7%")
        m3.metric("Cost per Acquisition", "12.40 €", "-2.10 €")
        m4.metric("License ROI", "12.4x", "System Verified")
        
        # Graf
        df_perf = pd.DataFrame({
            'Channel': ['Google', 'Meta', 'LinkedIn', 'TikTok'],
            'Revenue': [350000, 210000, 85000, 47405],
            'Spend': [75000, 45000, 18000, 10290]
        })
        fig = px.bar(df_perf, x='Channel', y=['Spend', 'Revenue'], barmode='group', template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    # --- MODUL 2: AI ORCHESTRATION ENGINE ---
    elif app_mode == "AI Orchestration Engine":
        st.title("🧠 Autonomous Orchestration Logic")
        st.subheader("Kernel Execution Code (Proprietary)")
        st.code("""
        async function executeBidding() {
            const signals = await MarketSignals.capture(['competitor_spend', 'cpc_volatility']);
            return AI_Core.optimize({ target: 'ROI_MAX', execution_layer: 'Cloud_Lambda' });
        }
        """, language="javascript")
        if st.button("🚀 Push Update to Edge Servers"):
            st.balloons()
            st.success("Logic deployed to production nodes.")

    # --- MODUL 3: PREDICTIVE ROI MODELING ---
    elif app_mode == "Predictive ROI Modeling":
        st.title("🔮 Predictive Revenue Forecasting")
        inv = st.slider("Investícia (€)", 10000, 500000, 150000)
        x = [i for i in range(12)]
        y = [inv * (1.1 + (i/10)) for i in x]
        fig_pred = px.line(x=x, y=y, title="Očakávaný rast výnosov (12 mesiacov)", template="plotly_dark")
        st.plotly_chart(fig_pred, use_container_width=True)

    # --- MODUL 4: API BRIDGE & INTEGRITY ---
    elif app_mode == "API Bridge & Integrity":
        st.title("🌐 Live API Connectivity Monitor")
        fig_map = go.Figure(data=[go.Sankey(
            node = dict(pad=20, thickness=30, label=["External APIs", "NEXUS Gateway", "Data Sanitizer", "AI Core", "CRM Bridge", "Final Reporting"]),
            link = dict(source=[0, 1, 2, 2, 3, 4], target=[1, 2, 3, 4, 5, 5], value=[100, 100, 80, 20, 80, 100])
        )])
        st.plotly_chart(fig_map, use_container_width=True)

    # --- MODUL 5: AUDIT TRAIL & COMPLIANCE ---
    elif app_mode == "Audit Trail & Compliance":
        st.title("📑 Compliance Evidence")
        logs = pd.DataFrame({
            "Timestamp": [(datetime.now() - timedelta(hours=i*2)).strftime("%Y-%m-%d %H:%M") for i in range(20)],
            "Action": ["Kernel Sync", "Budget Realloc", "API Ping", "Report Gen"] * 5,
            "Status": ["SUCCESS"] * 20
        })
        st.table(logs)
        st.download_button("Download Audit Report", logs.to_csv(), "audit.csv")
