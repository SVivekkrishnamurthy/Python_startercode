"""Streamlit app for checking scholarship eligibility."""

import streamlit as st

from scholarship_eligibility_checker import (
    CATEGORY_PERCENTAGE_REQUIREMENTS,
    INCOME_LIMIT,
    MIN_ATTENDANCE,
    qualifies_for_scholarship,
)


st.set_page_config(page_title="Scholarship Eligibility Checker", page_icon="🎓")
st.title("Scholarship Eligibility Checker")
st.write("Enter the student's details to check whether they qualify.")

name = st.text_input("Student name")
category = st.selectbox(
    "Category",
    options=("general", "reserved"),
    format_func=str.title,
)
percentage = st.number_input(
    "Percentage scored",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.1,
)
family_income = st.number_input(
    "Family income (Rs.)",
    min_value=0.0,
    value=0.0,
    step=1000.0,
)
attendance = st.number_input(
    "Attendance percentage",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.1,
)

st.caption(
    f"Required percentage: {CATEGORY_PERCENTAGE_REQUIREMENTS[category]}% · "
    f"Maximum family income: Rs. {INCOME_LIMIT:,.0f} · "
    f"Minimum attendance: {MIN_ATTENDANCE}%"
)

if st.button("Check eligibility", type="primary"):
    if not name.strip():
        st.error("Please enter the student's name.")
    elif qualifies_for_scholarship(
        category, percentage, family_income, attendance
    ):
        st.success(f"{name.strip()} qualifies for the scholarship.")
    else:
        st.warning(f"{name.strip()} does not qualify for the scholarship.")
