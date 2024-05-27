# Import the necessary library
import streamlit as st
import pandas as pd

# Title of the app
st.title('Simple CSV Data Explorer')

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the data frame
    st.write("## Data")
    st.write(df)
    
    # Show basic statistics
    st.write("## Basic Statistics")
    st.write(df.describe())
