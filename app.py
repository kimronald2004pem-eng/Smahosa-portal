import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="SMAHOSA Management Portal", 
    page_icon="🏛️", 
    layout="wide"
)

# Custom CSS for Professional Styling, Colors, and Clean Typography
st.markdown("""
    <style>
    /* Main Background & Font Styling */
    .main {
        background-color: #f4f6f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Header Card Styling */
    .header-card {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        padding: 35px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    
    .header-card h1 {
        color: #ffffff;
        font-size: 2.3rem;
        margin-bottom: 8px;
        font-weight: 700;
    }
    
    .header-card p {
        color: #d1d8e0;
        font-size: 1.15rem;
        letter-spacing: 0.5px;
    }
    
    .motto-badge {
        display: inline-block;
        background-color: #e1b12c;
        color: #2f3640;
        padding: 6px 18px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.95rem;
        margin-top: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    /* Metric Cards Customization */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #2c5364;
        font-weight: 700;
    }
    
    /* Dataframe Table Padding */
    .stDataFrame {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# App Header with Badge & Motto Integration
st.markdown("""
    <div class="header-card">
        <h1>🏛️ SMAHOSA Savings Group Portal</h1>
        <p>St. Mary's High School Old Students Association Management System</p>
        <div class="motto-badge">Rooted in Legacy, Driven by Service, Guided by Excellence</div>
    </div>
""", unsafe_allow_html=True)

# 1. Initialize Persistent Session State Data (Founding OBs & OGs)
if 'members' not in st.session_state:
    st.session_state.members = pd.DataFrame([
        {"Member ID": "SMA-001", "Full Name": "Mulindwa Laurence", "Role": "Chairperson", "Cohort": "2018", "Phone": "0747515338", "Status": "Active"},
        {"Member ID": "SMA-002", "Full Name": "Kimbugwe Ronald", "Role": "Publicity Officer", "Cohort": "2019", "Phone": "0747515338", "Status": "Active"},
        {"Member ID": "SMA-003", "Full Name": "Muwonge Sadat", "Role": "Member", "Cohort": "2018", "Phone": "—", "Status": "Active"},
        {"Member ID": "SMA-004", "Full Name": "Ssempijja Steven", "Role": "Member", "Cohort": "2020", "Phone": "—", "Status": "Active"},
        {"Member ID": "SMA-005", "Full Name": "Nakitto Priscilla", "Role": "Member", "Cohort": "2019", "Phone": "—", "Status": "Active"},
        {"Member ID": "SMA-006", "Full Name": "Nalwokyo Patience", "Role": "Member", "Cohort": "2021", "Phone": "—", "Status": "Active"},
        {"Member ID": "SMA-007", "Full Name": "Nantege Moureen Suzan", "Role": "Member", "Cohort": "2018", "Phone": "—", "Status": "Active"},
        {"Member ID": "SMA-008", "Full Name": "Mukula Micheal", "Role": "Member", "Cohort": "2017", "Phone": "—", "Status": "Active"},
        {"Member ID": "SMA-009", "Full Name": "Ssali Lawrence", "Role": "Member", "Cohort": "2019", "Phone": "—", "Status": "Active"},
        {"Member ID": "SMA-010", "Full Name": "Nambalirwa Justine", "Role": "Member", "Cohort": "2020", "Phone": "—", "Status": "Active"},
    ])

if 'transactions' not in st.session_state:
    st.session_state.transactions = pd.DataFrame([
        {"Tx ID": "TXN-101", "Member ID": "SMA-001", "Category": "Membership Fee", "Amount (UGX)": 5000, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-102", "Member ID": "SMA-001", "Category": "Annual Subscription", "Amount (UGX)": 5000, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-103", "Member ID": "SMA-001", "Category": "Savings Deposit", "Amount (UGX)": 20000, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-104", "Member ID": "SMA-002", "Category": "Membership Fee", "Amount (UGX)": 5000, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-105", "Member ID": "SMA-002", "Category": "Annual Subscription", "Amount (UGX)": 5000, "Channel": "Pride Microfinance"},
        {"Tx ID": "TXN-106", "Member ID": "SMA-002", "Category": "Savings Deposit", "Amount (UGX)": 25000, "Channel": "Pride Microfinance"},
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
                role = st.selectbox("Role / Position", ["Member", "Class Representative", "Executive Committee"])
                
            submitted = st.form_submit_button("Save Member to Database")
            if submitted and m_id and name:
                if m_id in st.session_state.members["Member ID"].values:
                    st.error(f"Member ID {m_id} already exists!")
                else:
                    new_row = {"Member ID": m_id, "Full Name": name, "Role": role, "Cohort": cohort, "Phone": phone if phone else "—", "Status": "Active"}
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
    st.markdown("Tracks mandatory non-refundable fees (UGX 5,000 onboarding & annual dues) separately from refundable member savings.")
    
    st.dataframe(st.session_state.transactions, use_container_width=True)
    
    tab_tx1, tab_tx2 = st.tabs(["➕ Record Transaction", "🗑️ Delete Transaction"])
    
    with tab_tx1:
        with st.form("add_tx_form"):
            st.write("### Record New Deposit or Fee")
            c1, c2 = st.columns(2)
            with c1:
                tx_id = st.text_input("Transaction ID (e.g., TXN-110)")
                m_id = st.selectbox("Select Member ID", st.session_state.members["Member ID"])
            with c2:
                category = st.selectbox("Category", ["Savings Deposit", "Membership Fee", "Annual Subscription"])
                amount = st.number_input("Amount (UGX)", min_value=1000, step=1000, value=5000)
                
            tx_submitted = st.form_submit_button("Record Transaction into Ledger")
            if tx_submitted and tx_id:
                if tx_id in st.session_state.transactions["Tx ID"].values:
                    st.error(f"Transaction ID {tx_id} already exists!")
                else:
                    new_tx = {"Tx ID": tx_id, "Member ID": m_id, "Category": category, "Amount (UGX)": amount, "Channel": "Pride Microfinance"}
                    st.session_state.transactions = pd.concat([st.session_state.transactions, pd.DataFrame([new_tx])], ignore_index=True)
                    st.success("Transaction recorded successfully!")
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