import streamlit as st

st.set_page_config(
    page_title = "Through the Label",
    page_icon= "🧴",
    layout="wide",
)

st.title("Through the Label 🧴✨")
st.caption("Make data driven skincare choices :D")

left, right = st.columns([2, 1])
with left:
    st.subheader("Your customized skincare bestie 💧!")
    st.write("Understand the ingredients that you put in your skin and perfect matching products for your skin by making smarter choices")
with right:
    st.image("https://via.placeholder.com/300") #IMPORTANT JUST PLACEHOLDER NEED TO CHANGE!



features = st.container()
with features:
    st.markdown("## How it works")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🧬 Profile")
        st.write("Tell us about your skin type and preferences!")

    with col2:
        st.subheader("🔍 Ingredient Analysis")
        st.write("Paste ingredient list of your choice and look what's inside!")


    with col3:
        st.subheader("🧴 Recommendations")
        st.write("Discover matching products for your skin!")

cta = st.container()
with cta:
    st.markdown("### Start your skincare journey")

    left, middle, right = st.columns([1, 1, 1])
    with left:
        if st.button("Go to Profile 🧬"):
             st.switch_page("pages/1_Profile.py")

    with right:
        if st.button("Browse Products 🧴"):
             st.switch_page("pages/2_Products.py")



