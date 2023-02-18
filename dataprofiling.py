from nbformat import write
import streamlit as st
import pandas as pd
import numpy as np
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport


st.write("""
# Data Profiling App
**This app Explore the Data before modeling**
""")

st.sidebar.header('User Input Features')


# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input Excel file", type="xlsx")
if uploaded_file is not None:
    st.markdown('---')
    input_df = pd.read_excel(uploaded_file, engine="openpyxl")
    
    profile = ProfileReport(input_df,

                       title="New Data for profiling",

    )

    st.title("Detailed Report of the Data Used")

    st.write(input_df)

    st_profile_report(profile)    
    
else:
    st.write("You did not upload the new file")

