import streamlit as st
st.title("Student Registration Form")
name= st.text_input("Student Name")
roll_no= st.text_input("Student Roll Number")
age=st.slider("Select Age",18,40,21)
course= st.text_input("Course")
mobile_num= st.text_input("Mobile Number")
address= st.text_area("Address")
gender= st.radio("Gender",["Male","Female","Others"])
nationality= st.selectbox("Nationality",["INDIA","USA","AUSTRALIA","ICELAND","UK"])
agree= st.checkbox("I agree to the terms & conditions")
if st.button("SUBMIT"):
    st.subheader("Student Information") 
    st.write("Student name:",name)
    st.write("Roll Number:",roll_no)
    st.write("Your Age:",age)
    st.write("Couse Selected:",course)
    st.write("Mobile Number:",mobile_num)
    st.write("Address:",address)
    st.write("Gender:",gender)
    st.write("Nationality:",nationality)

if agree:
    st.write("Thank you for registering.")

