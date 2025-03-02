import streamlit as st
from StudentRegistrationDB import insert_student_data
# Streamlit Web Page
st.title("Student Registration for Tuition Classes")

# Form Fields
name = st.text_input("Student Name")
class_for_tution = st.text_input("Class for Tuition")
mobile = st.text_input("Mobile Number")
subject = st.selectbox("Select Subject", ["Eng", "Phy", "Chem", "Math"])

# Submit Button
if st.button("Submit"):
    if name and class_for_tution and mobile and subject:
        insert_student_data(name, class_for_tution, mobile, subject)
        st.success(f"Student {name} has been registered successfully!")
    else:
        st.error("Please fill all the fields before submitting.")
