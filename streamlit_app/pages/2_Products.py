import streamlit as st
import pandas as pd

st.title("product overview")
st.caption("catalog preview")
path=("data/products.csv")
df=pd.read_csv(path)

st.write(df.head())
