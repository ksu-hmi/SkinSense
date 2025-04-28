import streamlit as st
import csv
import os

# Basic Page Setup
st.set_page_config(page_title="SkinSense", layout="centered")

# Sidebar
st.sidebar.title("SkinSense Tracker 🧴")
st.sidebar.markdown("Track your skincare routines and ingredients.")

# Main Title
st.title("Daily Skincare Routine Logger")

# Form Section
with st.form("routine_form"):
    routine_type = st.radio("Select your routine:", ["Morning", "Evening"])
    products_used = st.text_area("Enter products used (one per line)")
    skin_reaction = st.text_area("Any skin reactions or notes?")
    skin_type = st.selectbox("Select your skin type:", ["Normal", "Oily", "Dry", "Combination"])
    submitted = st.form_submit_button("Submit Routine")

# Form Submission
if submitted:
    st.success("Your skincare routine has been submitted!")
    st.write("### Routine Summary")
    st.write("Routine: " + routine_type)
    st.write("Products Used: " + products_used)
    st.write("Skin Reaction Notes: " + skin_reaction)
    st.write("Skin Type: " + skin_type)

     # Save to CSV
    file_exists = os.path.isfile('routine_log.csv')
    
    with open('routine_log.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Routine Type", "Products Used", "Skin Reaction", "Skin Type"])
        writer.writerow([routine_type, products_used, skin_reaction, skin_type])