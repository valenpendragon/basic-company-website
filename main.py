import streamlit as st
import pandas
import openpyxl

st.set_page_config(layout="wide")

st.title("The Best Company")

with open("blurb.txt") as file:
    blurb = file.read()

st.write(blurb)

st.header("Our Team")