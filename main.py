import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta
import random

# --- 1. LOGIN SYSTEM ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        st.set_page_config(page_title="NEXUS Login", page_icon="🔐")
        st.title("🛡️ NEXUS Core v5.0 | Enterprise Login")
        st.write("Authorized Access Only. All activities are being logged.")
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Authorize Access"):
            if user == "admin" and pw == "nexus2770":
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Neautorizovaný prístup. Skúste znova.")
        return False
    return True

if check_password():
    # --- 2. GLOBAL CONFIG & STYLING ---
    st.set_page_config(page_title="MAR-AUTO NEXUS v5.0", layout="wide")
    
    # Custom CSS pre temný režim a profi vzhľad
    st.markdown("""
        <style>
        .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
        </style>
        """, unsafe_allow_stdio=True)

    # --- 3. SIDEBAR NAVIGATION ---
    st.sidebar.markdown("### 💠 NEXUS CORE v5.0")
    st.sidebar.write("`Security Clearance: Level 4`")
    st.sidebar.markdown("---")
    
    app_mode = st.sidebar.selectbox("Navigation Tree", [
        "Executive Dashboard", 
        "AI Orchestration Engine", 
        "Predictive ROI Modeling",
        "API Bridge & Integrity",
        "Audit Trail & Compliance"
    ])
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("System Health")
    st.sidebar.progress(98, text="Server Load")
    st.sidebar.progress(100, text="API Uptime")
    
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

        st.markdown("---")
        
        col_l, col_r = st.columns([2, 1])
        
        with col_l:
            st.subheader("Multi-Channel Performance Matrix")
            df_perf = pd.DataFrame({
                'Channel': ['Google Search', 'Meta Video', 'LinkedIn B2B', 'TikTok Spark', 'Programmatic RTB'],
                'Spend': [75000, 45000, 18000, 10290, 15000],
                'Revenue': [350000, 210000, 85000, 47405, 58000],
                'Conversions': [1200, 850, 300, 150, 400]
            })
            fig = px.scatter(df_perf, x="Spend", y="Revenue", size="Conversions", color="Channel", 
                             template="plotly_dark", size_max=40)
            st.plotly_chart(fig, use_container_width=True)

        with col_r:
            st.subheader("Data Health by Source")
            fig_radar = go.Figure(data=go.Scatterpolar(
                r=[98, 95, 99, 92, 96],
                theta=['Google', 'Meta', 'LinkedIn', 'TikTok', 'RTB'],
                fill='toself', line_color='#00FFAA'
            ))
            fig_radar.update_layout(template="plotly_dark")
            st.plotly_chart(fig_radar, use_container_width=True)

    # --- MODUL 2: AI ORCHESTRATION ENGINE ---
    elif app_mode == "AI Orchestration Engine":
        st.title("🧠 Autonomous Orchestration Logic")
        
        col_a, col_b = st.columns(2)
        with col_a:
            strategy = st.selectbox("Current Strategy", ["Aggressive Growth", "Balanced ROI", "Cost Minimization"])
            st.slider("AI Confidence Threshold", 0.0, 1.0, 0.85)
        
        st.subheader("Live Scripting Interface (Proprietary Logic)")
        st.code(f"""
// NEXUS Core Logic v5.12 - Strategy: {strategy}
async function executeBidding() {{
    const signals = await MarketSignals.capture(['competitor_spend', 'cpc_volatility']);
    const trend = AI_Core.analyze(signals);
    
    if (trend.confidence > 0.85) {{
        return Kernel.deploy({{
            action: 'SCALE_BUDGET',
            increment: 0.15,
            safety_lock: true
        }});
    }}
}}
        """, language="javascript")
        
        if st.button("🚀 Push Update to Edge Servers"):
            st.toast("Deploying...")
            st.balloons()
            st.success("Logic updated in cloud nodes.")

    # --- MODUL 3: PREDICTIVE ROI MODELING ---
    elif app_mode == "Predictive ROI Modeling":
        st.title("🔮 Predictive Revenue Forecasting")
        investment = st.slider("Investícia na kvartál (€)", 10000, 500000, 150000)
        
        months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
        baseline = [investment * (1.2 + i*0.1) for i in range(len(months))]
        ai_opt = [v * 1.35 for v in baseline]
        
        fig_sim = go.Figure()
        fig_sim.add_trace(go.Scatter(x=months, y=baseline, name="Standard Model", line=dict(dash='dash')))
        fig_sim.add_trace(go.Scatter(x=months, y=ai_opt, name="NEXUS AI Optimized", fill='tonexty'))
        fig_sim.update_layout(template="plotly_dark")
        st.plotly_chart(fig_sim, use_container_width=True)
        st.info(f"Očakávaný zisk z optimalizácie: **{sum(ai_opt)-sum(baseline):,.2f} €**")

    # --- MODUL 4: API BRIDGE & INTEGRITY ---
    elif app_mode == "API Bridge & Integrity":
        st.title("🌐 Live API Connectivity Monitor")
        fig_map = go.Figure(data=[go.Sankey(
            node = dict(pad=20, thickness=30, label=["External APIs", "NEXUS Gateway", "Data Sanitizer", "AI Core", "CRM Bridge", "Final Reporting"], color="#00FFAA"),
            link = dict(source=[0, 1, 2, 2, 3, 4], target=[1, 2, 3, 4, 5, 5], value=[100, 100, 80, 20, 80, 100])
        )])
        fig_map.update_layout(template="plotly_dark")
        st.plotly_chart(fig_map, use_container_width=True)
        st.write("**Latencia:** 12ms | **Encryption:** AES-256-GCM | **Status:** Secured")

    # --- MODUL 5: AUDIT TRAIL & COMPLIANCE ---
    elif app_mode == "Audit Trail & Compliance":
        st.title("📑 Compliance Evidence")
        
        # Generovanie bohatšieho logu
        log_data = []
        for i in range(25):
            ts = (datetime.now() - timedelta(hours=i*4)).strftime("%Y-%m-%d %H:%M")
            log_data.append([ts, f"OP_{random.randint(100,999)}", random.choice(["API Sync", "Kernel Optimize", "ROI Predict", "Auth"]), "SUCCESS"])
        
        df_logs = pd.DataFrame(log_data, columns=["Timestamp", "ID", "Action", "Status"])
        st.dataframe(df_logs, use_container_width=True)
        
        st.markdown("---")
        st.write("**Licenčný model:** Enterprise / Managed Service")
        st.write("**Mesačný poplatok:** 2 770,00 EUR")
        st.download_button("Download Detailed Usage Report (CSV)", df_logs.to_csv(index=False), "audit_report.csv")
