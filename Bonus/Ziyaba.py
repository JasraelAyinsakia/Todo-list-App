import streamlit as st
import pandas as pd

# Page title
st.title("Machine Rental Tracking System")

# Customer Information
st.header("Customer Information")
col1, col2, col3 = st.columns(3)

with col1:
    customer_no = st.text_input("Customer No")
    expiry_date = st.date_input("Expiry Date")
    action_required = st.text_area("Action Required (Yes/No)")

with col2:
    customer_name = st.text_input("Customer Name")
    rental_type = st.selectbox("Rental Type", ["Daily", "Weekly", "Monthly"])
    additional_notes = st.text_area("Additional Notes")

with col3:
    rental_status = st.selectbox("Rental Status", ["Active", "Expired", "Pending"])
    amount_due = st.number_input("Total Amount Due", min_value=0.0, step=0.01)

st.markdown("---")

# Table for Tools Information
data = pd.DataFrame(
    {
        "Tools Name": ["Excavator", "Forklift", "Bulldozer"],
        "Applicable Fees": [100, 200, 150],
        "Design Process": ["Standard", "Specialized", "Basic"],
        "P-Type": ["Type A", "Type B", "Type C"]
    }
)

st.header("Rental Details")
st.dataframe(data)

# Submission Button
if st.button("Submit Rental Information"):
    st.success("Rental details submitted successfully!")
