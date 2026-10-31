"""Streamlit app for checking college admission eligibility."""

import streamlit as st

from college_admission_checker import (
    CATEGORY_PERCENTAGE_REQUIREMENTS,
    MAX_AGE,
    MIN_AGE,
    MIN_ENTRANCE_SCORE,
    qualifies_for_admission,
)


st.set_page_config(page_title="College Admission Checker", page_icon="🎓")
st.title("College Admission Eligibility Checker")
st.write("Enter the student's details to check admission eligibility.")

name = st.text_input("Student name")
category = st.selectbox(
    "Category",
    options=("general", "reserved"),
    format_func=str.title,
)
percentage = st.number_input(
    "Class 12 percentage",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.1,
)
entrance_score = st.number_input(
    "Entrance score",
    value=0.0,
    step=0.1,
)
age = st.number_input(
    "Age",
    min_value=0,
    max_value=120,
    value=17,
    step=1,
)

st.caption(
    f"Required Class 12 percentage: "
    f"{CATEGORY_PERCENTAGE_REQUIREMENTS[category]}% · "
    f"Minimum entrance score: {MIN_ENTRANCE_SCORE} · "
    f"Age range: {MIN_AGE}-{MAX_AGE}"
)

if st.button("Check eligibility", type="primary"):
    try:
        qualifies = qualifies_for_admission(
            category, percentage, entrance_score, age
        )
    except ValueError as error:
        st.error(str(error))
    else:
        student = name.strip() or "The student"
        if qualifies:
            st.success(f"{student} is eligible for admission.")
        else:
            st.warning(f"{student} is not eligible for admission.")
