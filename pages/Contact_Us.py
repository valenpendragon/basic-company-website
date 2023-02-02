import streamlit as st
import pandas
import os
import openpyxl
from email_control import send_email

with st.form(key="email form"):
    user_email = st.text_input("Your Email Address")

    if os.path.isfile("topics.csv"):
        df = pandas.read_csv("topics.csv")
    elif os.path.isfile("date.xls"):
        df = pandas.read_excel("topics.xls")
    elif os.path.isfile():
        df = pandas.read_excel("topics.xlsx")

    topic_choice = st.selectbox(label="Which topic would you like to discuss", options=df['topic'])
    raw_msg = st.text_area("Your Message")
    button = st.form_submit_button("Submit")
    if button:
        message = f"""
Subject: New contact email from {user_email} on topic {topic_choice} via Company Website

From: {user_email}
Topic {topic_choice}
{raw_msg}
"""
        send_email(message)
        st.info("Your message was sent successfully.")
