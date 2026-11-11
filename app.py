# --- VIEW 5: EXECUTIVE REPORTS (NEW) ---
elif menu == "📈 Executive Reports":
    st.subheader("📈 Automated Executive & Monthly Reporting Engine")
    st.markdown("Generate comprehensive monthly or custom-period financial, membership, and relief reports complete with executive addresses and graphical analytics.")
    
    # Report Configuration Panel
    with st.expander("⚙️ Report Parameters & Command Panel", expanded=True):
        report_type = st.radio("Select Report Mode", ["Monthly Report", "Custom Period Range"])
        
        if report_type == "Monthly Report":
            selected_month = st.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            selected_year = st.selectbox("Select Year", [2026, 2027, 2028])
            # Filter logic for month
            filtered_tx = st.session_state.transactions[(st.session_state.transactions["Month"] == selected_month) & (st.session_state.transactions["Year"] == selected_year)]
            period_label = f"{selected_month} {selected_year}"
        else:
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                start_date = st.date_input("Start Date", value=datetime.today().replace(day=1))
            with col_d2:
                end_date = st.date_input("End Date", value=datetime.today())
            # Filter logic for date range
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
    st.dataframe(relief_spec := relief_sample, use_container_width=True)
    
    st.markdown("---")
    st.info("💡 Tip: To export this complete multi-page executive report as a clean PDF (with date and page numbers, without sidebars or admin controls), press **Ctrl + P** in your browser.")
