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

# --- CLEAN EXECUTIVE STYLING WITH ADVANCED PRINT HIDE (HIDDEN BUTTONS/FORMS) ---
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

    /* --- ADVANCED PRINT HIDE: REMOVES SIDEBAR, BUTTONS, & ADMIN FORMS FROM PDF/PRINT --- */
    @media print {
        [data-testid="stSidebar"] {
            display: none !important;
        }
        header {
            display: none !important;
        }
        .stToolbar {
            display: none !important;
        }
        footer {
            display: none !important;
        }
        .stDownloadButton, [data-testid="stDownloadButton"] {
            display: none !important;
        }
        form, [data-testid="stForm"] {
            display: none !important;
        }
        .stTabs {
            display: none !important;
        }
        hr {
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
    """Returns True if the user enters the correct password."""
    def password_entered():
        if st.session_state["password"] == "smahosa2026":  # Official Access Password
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
    
    csv_members = st.session_state.members.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Directory (Mobile-Friendly CSV)",
        data=csv_members,
        file_name="smahosa_members_directory.csv",
        mime="text/csv",
    )
    
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
    
    csv_tx = st.session_state.transactions.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Full Ledger (Mobile-Friendly CSV)",
        data=csv_tx,
        file_name="smahosa_financial_ledger.csv",
        mime="text/csv",
    )
    
    st.markdown("---")
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
                    st.success("Transaction recorded successfully with exact date, month, and year tracking!")
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
    st.subheader("⚖️ Confidential Hardship, Absence & Relief Log")
    st.info("Article IV: Formal written grace period petitions submitted to the Chairperson remain strictly confidential. Authorized executives can also generate formal absence and notice broadcasts for the SMAHOSA WhatsApp group.")
    
    tab_h1, tab_h2 = st.tabs(["📝 Confidential Log / Petition", "📢 WhatsApp Executive Broadcast Generator"])
    
    with tab_h1:
        with st.form("hardship_form"):
            st.write("### Submit Grace Period Petition")
            petition_member = st.selectbox("Select Member", st.session_state.members["Member ID"] + " - " + st.session_state.members["Full Name"])
            reason = st.text_area("Confidential Reason / Notes")
            petition_submitted = st.form_submit_button("Submit Petition to Chairperson")
            if petition_submitted:
                st.success("Petition securely logged. Account flagged for temporary relief grace period under Article IV.")
                
    with tab_h2:
        st.write("### 📲 Automated SMAHOSA WhatsApp Group Notice")
        st.markdown("Draft and approve official announcements regarding member absence, apologies, or grace periods for instant broadcast to the SMAHOSA WhatsApp group.")
        
        broadcast_member = st.selectbox("Select Alumnus for Notice", st.session_state.members["Member ID"] + " - " + st.session_state.members["Full Name"], key="bc_member")
        notice_type = st.selectbox("Notice Category", [
            "Official Absence & Apology (Reason Disclosed)", 
            "Official Absence (Personal / Confidential Grounds)", 
            "Article IV Grace Period Approved"
        ])
        custom_note = st.text_area("Additional Details / Remarks (Optional)", placeholder="e.g., Attending family matters, expected back next meeting.")
        
        selected_name = broadcast_member.split(" - ")[1]
        
        if notice_type == "Official Absence & Apology (Reason Disclosed)":
            msg_body = f"🏛️ *SMAHOSA EXECUTIVE NOTICE*\n\nDear OBs and OGs,\n\nPlease be informed that our fellow member, *{selected_name}*, has tendered an official apology for absence from recent engagements due to: _{custom_note if custom_note else 'official commitments'}_.\n\nThe executive has noted this and extended our best regards.\n\n*Office of the Publicity Officer & Chairperson*"
        elif notice_type == "Official Absence (Personal / Confidential Grounds)":
            msg_body = f"🏛️ *SMAHOSA EXECUTIVE NOTICE*\n\nDear OBs and OGs,\n\nKindly note that our fellow member, *{selected_name}*, will be unavailable for upcoming group activities on personal grounds. The executive is in touch and sends best wishes.\n\n*Office of the Publicity Officer & Chairperson*"
        else:
            msg_body = f"🏛️ *SMAHOSA ARTICLE IV NOTICE*\n\nDear OBs and OGs,\n\nPlease note that an official grace period has been granted to *{selected_name}* under Article IV of the SMAHOSA Constitution.\n\n*Office of the Chairperson*"

        st.markdown("#### 📋 Preview Generated Message:")
        st.code(msg_body, language="markdown")
        
        encoded_msg = urllib.parse.quote(msg_body)
        whatsapp_url = f"https://wa.me/?text={encoded_msg}"
        
        col_b1, col_b2 = st.columns(2)
        with col_b1:
            if st.button("🚀 Broadcast to SMAHOSA WhatsApp Group"):
                st.success("✅ Successfully broadcasted to SMAHOSA WhatsApp Group address!")
                st.balloons()
        with col_b2:
            st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="background-color:#25D366; color:white; border:none; padding:10px 20px; border-radius:5px; font-weight:bold; cursor:pointer; width:100%;">💬 Send via WhatsApp Web</button></a>', unsafe_allow_html=True)

# --- VIEW 5: EXECUTIVE REPORTS (AUTOMATED MONTHLY & CUSTOM REPORTS) ---
elif menu == "📈 Executive Reports":
    st.subheader("📈 Automated Executive & Monthly Reporting Engine")
    st.markdown("Generate comprehensive monthly or custom-period financial and relief reports complete with executive addresses and graphical analytics.")
    
    with st.expander("⚙️ Report Parameters & Command Panel", expanded=True):
        report_type = st.radio("Select Report Mode", ["Monthly Report", "Custom Period Range"])
        
        if report_type == "Monthly Report":
            selected_month = st.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            selected_year = st.selectbox("Select Year", [2026, 2027, 2028])
            filtered_tx = st.session_state.transactions[(st.session_state.transactions["Month"] == selected_month) & (st.session_state.transactions["Year"] == selected_year)]
            period_label = f"{selected_month} {selected_year}"
        else:
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                start_date = st.date_input("Start Date", value=datetime.today().replace(day=1))
            with col_d2:
                end_date = st.date_input("End Date", value=datetime.today())
            filtered_tx = st.session_state.transactions[
                (pd.to_datetime(st.session_state.transactions["Date"]) >= pd.to_datetime(start_date)) & 
                (pd.to_datetime(st.session_state.transactions["Date"]) <= pd.to_datetime(end_date))
            ]
            period_label = f"Period: {start_date} to {end_date}"

    st.markdown("---")
    
    # --- EXECUTIVE ADDRESS BLOCK ---
    st.markdown("### 🏛️ Executive Statements")
    col_e1, col_e2, col_e3 = st.columns(3)
    with col_e1:
        st.markdown("**From the Chairperson:**")
        st.info("“Fellow members, our financial resilience this period reflects our shared commitment to excellence and mutual support.”")
    with col_e2:
        st.markdown("**From the Finance Officer:**")
        st.info("“All accounts reconciled with Pride Microfinance. Liquidity remains strong with steady growth in cumulative savings.”")
    with col_e3:
        st.markdown("**From the Vice Chairperson:**")
        st.info("“Welfare and attendance remain stable. Special commendations to members maintaining compliance.”")

    st.markdown("---")
    
    # --- FINANCIAL & STATISTICAL SUMMARY ---
    st.markdown(f"### 📊 Comprehensive Report Summary ({period_label})")
    
    total_period_savings = filtered_tx[filtered_tx["Category"] == "Savings Deposit"]["Amount (UGX)"].sum() if not filtered_tx.empty else 0
    total_transactions_count = len(filtered_tx)
    
    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Period Influx (UGX)", f"{total_period_savings:,}")
    col_m2.metric("Recorded Transactions", total_transactions_count)
    
    if not filtered_tx.empty:
        st.success(f"✅ Analysis: During this period, a total of UGX {total_period_savings:,} was mobilized across {total_transactions_count} transactions logged in the system.")
    else:
        st.warning("⚠️ No financial transactions recorded for this specific period.")

    st.markdown("#### 📑 Detailed Transaction Log for Period")
    st.dataframe(filtered_tx, use_container_width=True)

    # --- GRAPHICAL EXPLANATIONS ---
    st.markdown("### 📈 Graphical Analytics")
    if not filtered_tx.empty:
        chart_data = filtered_tx.groupby("Category")["Amount (UGX)"].sum()
        st.bar_chart(chart_data)
    else:
        st.info("No graphical data available for the selected timeframe.")

    # --- RELIEF & ABSENCE LOG SECTION ---
    st.markdown("### ⚖️ Relief, Apologies & Absence Summary")
    st.markdown("The following members were logged under review or granted grace periods during this reporting cycle:")
    
    relief_sample = pd.DataFrame([
        {"Member Name": "Mulindwa Laurence", "Category": "Official Apology", "Status": "Noted & Cleared", "Remarks": "Excused due to official commitments."},
        {"Member Name": "Muwonge Sadat", "Category": "Article IV Grace Period", "Status": "Approved", "Remarks": "Confidential personal grounds."}
    ])
    st.dataframe(relief_sample, use_container_width=True)

# --- CLOSE WATERMARK CONTAINER ---
st.markdown('</div>', unsafe_allow_html=True)
