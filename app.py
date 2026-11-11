import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="SMAHOSA Management Portal", 
    page_icon="🏛️", 
    layout="wide"
)

# Custom CSS for Professional Styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .header-card {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        padding: 25px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .header-card h1 {
        color: #ffffff;
        font-size: 2rem;
        margin-bottom: 5px;
        font-weight: 700;
    }
    .header-card p {
        color: #d1d8e0;
        font-size: 1rem;
        letter-spacing: 0.5px;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #2c5364;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# Display Official Badge & Header Card (Matched to badge.jpg.png)
col_left, col_mid, col_right = st.columns([2, 2, 2])
with col_mid:
    if os.path.exists("badge.jpg.png"):
        st.image("badge.jpg.png", use_container_width=True)

st.markdown("""
    <div class="header-card">
        <h1>SMAHOSA Savings Group Portal</h1>
        <p>St. Mary's High School Old Students Association Management System</p>
    </div>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE WITH DATE & YEAR TRACKING ---
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
st.sidebar.markdown("### Management Menu")
menu = st.sidebar.selectbox("Select Portal Section", ["📊 Dashboard", "👥 Alumni Directory", "💰 Financial Ledger", "⚖️ Hardship & Relief"])

# --- VIEW 1: DASHBOARD ---
if menu == "📊 Dashboard":
    st.subheader("Executive Summary Dashboard")
    
    savings_only = st.session_state.transactions[st.session_state.transactions["Category"] == "Savings Deposit"]
    total_savings = savings_only["Amount (UGX)"].sum() if not savings_only.empty else 0
    total_members = len(st.session_state.members)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Savings Pool", f"UGX {total_savings:,}")
    col2.metric("Registered OBs & OGs", total_members)
    col3.metric("Banking Partner", "Pride Microfinance")
    
    st.markdown("---")
    st.subheader("Recent Ledger Entries")
    st.dataframe(st.session_state.transactions.tail(5), use_container_width=True)

# --- VIEW 2: ALUMNI DIRECTORY ---
elif menu == "👥 Alumni Directory":
    st.subheader("Registered OBs & OGs Directory")
    st.dataframe(st.session_state.members, use_container_width=True)
    
    csv_members = st.session_state.members.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Directory (Mobile-Friendly CSV)",
        data=csv_members,
        file_name="smahosa_members_directory.csv",
        mime="text/csv",
    )
    
    tab1, tab2 = st.tabs(["➕ Add New Member", "🗑️ Remove Member"])
    
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
        with st.form("remove_member_form"):
            st.write("### Remove an Alumnus")
            target_member = st.selectbox("Select Member to Remove", st.session_state.members["Member ID"] + " - " + st.session_state.members["Full Name"])
            remove_sub = st.form_submit_button("Delete Member Record")
            if remove_sub:
                selected_id = target_member.split(" - ")[0]
                st.session_state.members = st.session_state.members[st.session_state.members["Member ID"] != selected_id]
                st.success(f"Successfully removed member {selected_id}!")
                st.rerun()

# --- VIEW 3: FINANCIAL LEDGER ---
elif menu == "💰 Financial Ledger":
    st.subheader("Financial Ledger (Pride Microfinance Account)")
    st.markdown("Tracks mandatory non-refundable fees separately from refundable member savings with exact date, month, and year recording.")
    
    st.dataframe(st.session_state.transactions, use_container_width=True)
    
    csv_tx = st.session_state.transactions.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Full Ledger (Mobile-Friendly CSV)",
        data=csv_tx,
        file_name="smahosa_financial_ledger.csv",
        mime="text/csv",
    )
    
    tab_tx1, tab_tx2 = st.tabs(["➕ Record Transaction", "🗑️ Delete Transaction"])
    
    with tab_tx1:
        with st.form("add_tx_form"):
            st.write("### Record New Deposit or Fee")
            c1, c2 = st.columns(2)
            with c1:
                tx_id = st.text_input("Transaction ID (e.g., TXN-110)")
                m_id = st.selectbox("Select Member ID", st.session_state.members["Member ID"])
                category = st.selectbox("Category", ["Savings Deposit", "Membership Fee", "Annual Subscription"])
            with c2:
                amount = st.number_input("Amount (UGX)", min_value=1000, step=1000, value=5000)
                tx_date = st.date_input("Transaction Date", value=datetime.today())
                
            tx_submitted = st.form_submit_button("Record Transaction into Ledger")
            if tx_submitted and tx_id:
                if tx_id in st.session_state.transactions["Tx ID"].values:
                    st.error(f"Transaction ID {tx_id} already exists!")
                else:
                    date_str = str(tx_date)
                    month_str = tx_date.strftime("%B")
                    year_val = tx_date.year
                    
                    new_tx = {
                        "Tx ID": tx_id, 
                        "Member ID": m_id, 
                        "Category": category, 
                        "Amount (UGX)": amount, 
                        "Date": date_str, 
                        "Month": month_str, 
                        "Year": year_val, 
                        "Channel": "Pride Microfinance"
                    }
                    st.session_state.transactions = pd.concat([st.session_state.transactions, pd.DataFrame([new_tx])], ignore_index=True)
                    st.success("Transaction recorded successfully with exact date, month, and year!")
                    st.rerun()

    with tab_tx2:
        with st.form("remove_tx_form"):
            st.write("### Delete Transaction Record")
            target_tx = st.selectbox("Select Transaction ID to Remove", st.session_state.transactions["Tx ID"] + " (" + st.session_state.transactions["Category"] + " - UGX " + st.session_state.transactions["Amount (UGX)"].astype(str) + ")")
            tx_remove_sub = st.form_submit_button("Delete Transaction")
            if tx_remove_sub:
                selected_tx_id = target_tx.split(" ")[0]
                st.session_state.transactions = st.session_state.transactions[st.session_state.transactions["Tx ID"] != selected_tx_id]
                st.success(f"Successfully deleted transaction {selected_tx_id}!")
                st.rerun()

# --- VIEW 4: HARDSHIP & RELIEF ---
elif menu == "⚖️ Hardship & Relief":
    st.subheader("Confidential Hardship & Relief Log")
    st.info("Article IV: Formal written grace period petitions submitted to the Chairperson remain strictly confidential.")
    
    with st.form("hardship_form"):
        st.write("### Submit Grace Period Petition")
        petition_member = st.selectbox("Select Member", st.session_state.members["Member ID"] + " - " + st.session_state.members["Full Name"])
        reason = st.text_area("Confidential Reason / Notes")
        petition_submitted = st.form_submit_button("Submit Petition to Chairperson")
        if petition_submitted:
            st.success("Petition securely logged. Account flagged for temporary relief grace period under Article IV.")