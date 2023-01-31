import streamlit as st
import pandas
import openpyxl
import os.path

st.set_page_config(layout="wide")

st.title("The Best Company")

with open("blurb.txt") as file:
    blurb = file.read()

st.write(blurb)

st.header("Our Team")

data_col1, space_col1, data_col2, space_col2, data_col3, space_col3 = st.columns([1.0, 0.5,1.0, 0.5, 1.0, 0.5])

# Look to see which file is present, data.csv, data.xls, or data.xlsx.
if os.path.isfile("data.csv"):
    df = pandas.read_csv("data.csv")
elif os.path.isfile("date.xls"):
    df = pandas.read_excel("data.xls")
elif os.path.isfile():
    df = pandas.read_excel("data.xlsx")

with data_col1:
    for index, row in df[0::3].iterrows():
        first_name = row['first name'].lower().capitalize()
        last_name = row['last name'].lower().capitalize()
        st.header(f"{first_name} {last_name}")
        role = row['role'].lower().title()
        st.write(role)
        st.image("images/" + row['image'])

with data_col2:
    for index, row in df[1::3].iterrows():
        first_name = row['first name'].lower().capitalize()
        last_name = row['last name'].lower().capitalize()
        st.header(f"{first_name} {last_name}")
        role = row['role'].lower().title()
        st.write(role)
        st.image("images/" + row['image'])

with data_col3:
    for index, row in df[2::3].iterrows():
        first_name = row['first name'].lower().capitalize()
        last_name = row['last name'].lower().capitalize()
        st.header(f"{first_name} {last_name}")
        role = row['role'].lower().title()
        st.write(role)
        st.image("images/" + row['image'])
