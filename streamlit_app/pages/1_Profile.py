import streamlit as st
st.header("Your Profile")
if "skin_type" not in st.session_state:
    st.session_state["skin_type"]="Oily"
st.session_state["skin_type"]=st.selectbox("select skin type",["Oily", "Dry", "Combination", "Sensitive"], index=0)
st.success("Selected Skin Type: "+ st.session_state["skin_type"])
