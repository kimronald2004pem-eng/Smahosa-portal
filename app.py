import streamlit as st
import pandas as pd
import os
import base64
from datetime import datetime
import urllib.parse

# Page Configuration
st.set_page_config(
    page_title="SMAHOSA Management Portal", 
    page_icon="🏛️", 
    layout="wide"
)

# --- CONVERT BADGE TO BASE64 FOR WATERMARK ---
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

badge_base64 = get_base64_image("badge.jpg.png")

# --- CLEAN EXECUTIVE STYLING ---
css_template = """
    <style>
    .main {
        background-color: #f4f7f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .watermark-box {
        position: relative;
        background-image: url("data:image/png;base64,REPLACE_BASE64");
        background-repeat: no-repeat;
        background-position: center;
        background-size: 25% auto;
    }
    .header-card {
        background: linear-gradient(135deg, #0d1b2a, #1b263b, #415a77);
        padding: 25px;
        border-radius: 14px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(13, 27, 42, 0.2);
        border-bottom: 4px solid #e0a96d;
    }
    .header-card h1 {
        color: #ffffff;
        font-size: 2.1rem;
        margin-bottom: 6px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .header-card p {
        color: #e0e1dd;
        font-size: 1rem;
        letter-spacing: 0.5px;
        font-weight: 400;
    }
    h2, h3 {
        color: #1b263b !important;
        font-weight: 600;
    }
    [data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border-left: 5px solid #1b263b;
    }
    [data-testid="stMetricLabel"] {
        color: #415a77 !important;
        font-weight: 600;
        font-size: 0.95rem;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.7rem;
        color: #0d1b2a !important;
        font-weight: 700;
    }
    [data-testid="stSidebar"] {
        background-color: #0d1b2a;
    }
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] .stMarkdown {
        color: #e0e1dd !important;
    }
    .stAlert {
        border-radius: 8px;
    }
    @media print {
        [data-testid="stSidebar"], header, footer, .stToolbar {
            display: none !important;
        }
        .main {
            background-color: #ffffff !important;
        }
    }
    </style>
"""
st.markdown(css_template.replace("REPLACE_BASE64", badge_base64), unsafe_allow_html=True)

# --- PASSWORD PROTECTION GATE ---
def check_password():
    def password_entered():
        if st.session_state["password"] == "smahosa2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    col_l, col_m, col_r = st.columns([2, 2, 2])
    with col_m:
        if os.path.exists("badge.jpg.png"):
            st.image("badge.jpg.png", use_container_width=True)

    if "password_correct" not in st.session_state:
        st.markdown("""
            <div style="text-align: center; padding: 15px;">
                <h2 style="color: #1b263b;">SMAHOSA Management Portal</h2>
                <p style="color: #415a77;">St. Mary's High School Old Students Association</p>
            </div>
        """, unsafe_allow_html=True)
        st.info("🔒 Please enter the official access password to unlock the portal.")
        st.text_input("Access Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("""
            <div style="text-align: center; padding: 15px;">
                <h2 style="color: #1b263b;">SMAHOSA Management Portal</h2>
            </div>
        """, unsafe_allow_html=True)
        st.text_input("Access Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Incorrect password. Please check with the executive committee.")
        return False
    else:
        return True

if not check_password():
    st.stop()

# --- WRAP DASHBOARD CONTENT IN WATERMARK CONTAINER ---
st.markdown('<div class="watermark-box">', unsafe_allow_html=True)

# --- DISPLAY SINGLE HEADER CARD ---
st.markdown("""
    <div class="header-card">
        <h1>SMAHOSA Savings Group Portal</h1>
        <p>St. Mary's High School Old Boys & Old Girls Official Management System</p>
    </div>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE WITH DATA ---
if 'members' not in st.session_state:
    st.session_state.members = pd.DataFrame([
        {"Member ID": "SMA-001", "Full Name": "Mulindwa Laurence", "Role": "Chairperson", "Cohort": "2018", "Phone": "0747515338", "Join Date": "2026-01-15", "Status": "Active"},
        {"Member ID": "SMA-002", "Full Name": "Kimbugwe Ronald", "Role": "Publicity Officer", "Cohort": "2019", "Phone": "0747515338", "Join Date": "2026-01-15", "Status": "Active"},
        {"Member ID": "SMA-003", "Full Name": "Muwonge Sadat", "Role": "Member", "Cohort": "2018", "Phone": "—", "Join Date": "2026-01-20", "Status": "Active"},
        {"Member ID": "SMA-004", "Full Name": "Ssempijja Steven", "Role": "Member", "Cohort": "2020", "Phone": "—", "Join Date": "2026-01-20", "Status": "Active"},
        {"Member ID": "SMA-005", "Full Name": "Nakitto Priscilla", "Role": "Member", "Cohort": "2019", "Phone": "—", "Join Date": "2026-02-01", "Status": "Active"},
        {"Member ID": "SMA-006", "Full Name": "Nalwokyo Patience", "Role": "Member", "Cohort": "2021", "Phone": "—", "Join Date": "2026-02-01", "Status": "Active"},
        {"Member ID": "SMA-007", "Full Name": "Nantege Moureen Suzan", "Role": "Member", "Cohort": "2018", "Phone": "—", "Join Date": "2026-02-10", "Status": "Active"},
        {"Member ID": "SMA-008", "Full Name": "Mukula Micheal", "Role": "Member", "Cohort": "2017", "Phone": "—", "Join Date": "2026-02-10", "Status": "Active"},
        {"Member ID": "SMA-009", "Full Name": "Ssali Lawrence", "Role": "Member", "Cohort": "2019", "Phone": "—", "Join Date": "2026-02-15", "Status": "Active"},
        {"Member ID": "SMA-010", "Full Name": "Nambalirwa Justine", "Role": "Member", "Cohort": "2020", "Phone": "—", "Join Date": "2026-02-15", "Status": "Active"},
    ])

if 'transactions' not in st.session_state:
    st.session_state.transactions = pd.DataFrame([
        {"Tx ID": "TXN-101", "Member ID": "SMA-001", "Category": "Membership Fee", "Amount (UGX)": 5000, "Date": "2026-01-15", "Month": "January", "Year": 2026, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-102", "Member ID": "SMA-001", "Category": "Annual Subscription", "Amount (UGX)": 5000, "Date": "2026-01-15", "Month": "January", "Year": 2026, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-103", "Member ID": "SMA-001", "Category": "Savings Deposit", "Amount (UGX)": 20000, "Date": "2026-02-01", "Month": "February", "Year": 2026, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-104", "Member ID": "SMA-002", "Category": "Membership Fee", "Amount (UGX)": 5000, "Date": "2026-01-15", "Month": "January", "Year": 2026, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-105", "Member ID": "SMA-002", "Category": "Annual Subscription", "Amount (UGX)": 5000, "Date": "2026-01-15", "Month": "January", "Year": 2026, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-106", "Member ID": "SMA-002", "Category": "Savings Deposit", "Amount (UGX)": 25000, "Date": "2026-02-01", "Month": "February", "Year": 2026, "Channel": "Pride Microfinance"},
    ])

# Sidebar Navigation Menu
st.sidebar.markdown("<h2 style='color: #ffffff; font-size: 1.3rem;'>🧭 Management Menu</h2>", unsafe_allow_html=True)
menu = st.sidebar.selectbox("Select Portal Section", ["📊 Dashboard", "👥 Alumni Directory", "💰 Financial Ledger", "⚖️ Hardship & Relief", "📈 Executive Reports"])

# --- COMMON STYLING FOR EXPORTABLE HTML REPORTS ---
base_html_style = """
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; color: #1b263b; padding: 40px; line-height: 1.6; background: #ffffff; }
        h1, h2, h3 { color: #0d1b2a; }
        .header { text-align: center; border-bottom: 3px solid #e0a96d; padding-bottom: 15px; margin-bottom: 30px; }
        .section { margin-bottom: 30px; page-break-inside: avoid; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { border: 1px solid #cbd5e1; padding: 10px; text-align: left; font-size: 14px; }
        th { background-color: #1b263b; color: white; }
        .metric-box { background: #f8fafc; border-left: 5px solid #1b263b; padding: 15px; margin: 15px 0; }
        @media print {
            body { padding: 10px; }
            button { display: none !important; }
        }
    </style>
"""

# --- VIEW 1: DASHBOARD ---
if menu == "📊 Dashboard":
    st.subheader("📊 Executive Summary Dashboard")
    
    savings_only = st.session_state.transactions[st.session_state.transactions["Category"] == "Savings Deposit"]
    total_savings = savings_only["Amount (UGX)"].sum() if not savings_only.empty else 0
    total_members = len(st.session_state.members)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Savings Pool", f"UGX {total_savings:,}")
    col2.metric("Registered OBs & OGs", total_members)
    col3.metric("Banking Partner", "Pride Microfinance")
    
    st.markdown("---")
    st.subheader("🕒 Recent Financial & Membership Entries")
    st.dataframe(st.session_state.transactions.tail(5), use_container_width=True)

# --- VIEW 2: ALUMNI DIRECTORY ---
elif menu == "👥 Alumni Directory":
    st.subheader("👥 Registered OBs & OGs Directory")
    st.dataframe(st.session_state.members, use_container_width=True)
    
    # --- DOWNLOAD PRINTABLE DIRECTORY REPORT ---
    members_rows = ""
    for _, r in st.session_state.members.iterrows():
        members_rows += f"<tr><td>{r['Member ID']}</td><td>{r['Full Name']}</td><td>{r['Role']}</td><td>{r['Cohort']}</td><td>{r['Phone']}</td><td>{r['Join Date']}</td><td>{r['Status']}</td></tr>"
    
    dir_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>SMAHOSA Alumni Directory</title>{base_html_style}</head><body>
    <div style="text-align: right; margin-bottom: 20px;"><button onclick="window.print()" style="background-color:#1b263b; color:white; border:none; padding:12px 24px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:16px;">🖨️ Print / Save as PDF</button></div>
    <div class="header"><h1>SMAHOSA Savings Group Portal</h1><h3>Official Alumni Membership Directory</h3><p>Total Registered Members: {len(st.session_state.members)}</p></div>
    <div class="section"><table><tr><th>Member ID</th><th>Full Name</th><th>Role</th><th>Cohort</th><th>Phone</th><th>Join Date</th><th>Status</th></tr>{members_rows}</table></div></body></html>"""
    
    st.download_button("📥 Download Printable Directory Report (HTML)", data=dir_html, file_name="SMAHOSA_Alumni_Directory.html", mime="text/html")
    
    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["➕ Add New Member", "✏️ Edit / Update Member", "🗑️ Remove Member"])
    
    with tab1:
        with st.form("add_member_form"):
            st.write("### Register New Alumnus")
            c1, c2 = st.columns(2)
            with c1:
                m_id = st.text_input("Member ID (e.g., SMA-011)")
                name = st.text_input("Full Name")
                phone = st.text_input("Phone Number (Optional)")
            with c2:
                cohort = st.text_input("Alumni Cohort Year")
                join_date = st.date_input("Registration Date", value=datetime.today())
                role = st.selectbox("Role / Position", ["Member", "Class Representative", "Executive Committee"])
                
            submitted = st.form_submit_button("Save Member to Database")
            if submitted and m_id and name:
                if m_id in st.session_state.members["Member ID"].values:
                    st.error(f"Member ID {m_id} already exists!")
                else:
                    new_row = {
                        "Member ID": m_id, 
                        "Full Name": name, 
                        "Role": role, 
                        "Cohort": cohort, 
                        "Phone": phone if phone else "—", 
                        "Join Date": str(join_date), 
                        "Status": "Active"
                    }
                    st.session_state.members = pd.concat([st.session_state.members, pd.DataFrame([new_row])], ignore_index=True)
                    st.success(f"Successfully registered {name}!")
                    st.rerun()

    with tab2:
        with st.form("edit_member_form"):
            st.write("### Edit Existing Alumnus Information")
            selected_member_str = st.selectbox("Select Member to Update", st.session_state.members["Member ID"] + " - " + st.session_state.members["Full Name"], key="edit_member_select")
            
            selected_m_id = selected_member_str.split(" - ")[0]
            member_row = st.session_state.members[st.session_state.members["Member ID"] == selected_m_id].iloc[0]
            
            c1, c2 = st.columns(2)
            with c1:
                edit_name = st.text_input("Full Name", value=member_row["Full Name"])
                edit_phone = st.text_input("Phone Number", value=member_row["Phone"])
            with c2:
                edit_cohort = st.text_input("Alumni Cohort Year", value=member_row["Cohort"])
                roles_list = ["Member", "Class Representative", "Executive Committee", "Chairperson", "Publicity Officer"]
                default_role_idx = roles_list.index(member_row["Role"]) if member_row["Role"] in roles_list else 0
                edit_role = st.selectbox("Role / Position", roles_list, index=default_role_idx)
                
            edit_status = st.selectbox("Membership Status", ["Active", "Inactive", "Grace Period"], index=0 if member_row["Status"] == "Active" else 1)
            
            update_submitted = st.form_submit_button("Update Member Information")
            if update_submitted:
                st.session_state.members.loc[st.session_state.members["Member ID"] == selected_m_id, ["Full Name", "Phone", "Cohort", "Role", "Status"]] = [edit_name, edit_phone, edit_cohort, edit_role, edit_status]
                st.success(f"Successfully updated record for {edit_name}!")
                st.rerun()

    with tab3:
        with st.form("remove_member_form"):
            st.write("### Remove an Alumnus Record")
            target_member = st.selectbox("Select Member to Remove", st.session_state.members["Member ID"] + " - " + st.session_state.members["Full Name"])
            remove_sub = st.form_submit_button("Delete Member Record")
            if remove_sub:
                selected_id = target_member.split(" - ")[0]
                st.session_state.members = st.session_state.members[st.session_state.members["Member ID"] != selected_id]
                st.success(f"Successfully removed member {selected_id}!")
                st.rerun()

# --- VIEW 3: FINANCIAL LEDGER ---
elif menu == "💰 Financial Ledger":
    st.subheader("💰 Financial Ledger (Pride Microfinance Account)")
    st.markdown("Tracks mandatory non-refundable fees separately from refundable member savings with precise date, month, and year recording.")
    
    st.dataframe(st.session_state.transactions, use_container_width=True)
    
    # --- DOWNLOAD PRINTABLE LEDGER REPORT ---
    ledger_rows = ""
    for _, r in st.session_state.transactions.iterrows():
        ledger_rows += f"<tr><td>{r['Tx ID']}</td><td>{r['Member ID']}</td><td>{r['Category']}</td><td>UGX {r['Amount (UGX)']:,}</td><td>{r['Date']}</td><td>{r['Month']}</td><td>{r['Year']}</td><td>{r['Channel']}</td></tr>"
    
    total_
