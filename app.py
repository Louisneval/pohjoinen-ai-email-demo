import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

from services.generator import generate_customer_output

st.set_page_config(page_title="Pohjoinen AI Demo")

st.title("📧 AI Email Personalization Demo")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("Please upload a CSV file")
    df = None

if df is not None and st.button("Generate Emails"):

    for _, row in df.iterrows():

        st.divider()
        st.subheader(f"Customer: {row['customer']}")

        result = generate_customer_output(row)
        st.text(result)