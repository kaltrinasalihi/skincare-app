import streamlit as st
st.header("Your Profile")

if "profile" not in st.session_state:
    st.session_state["profile"] = {}


with st.form("profile_form"):

    st.subheader("Basic information")
    skin_type = st.selectbox(
        "Skin type",
        ["oily", "dry", "combination", "normal", "sensitive"]
    )

    age_group = st.selectbox(
        "Age group",
        ["Teen 13-19 years", "Young Adult 20-29 years", "Adult 30-44 years", "Mature 45+ years"]
    )

    st.subheader("Skin concerns")
    concerns = st.multiselect(
        "Choose up to 3 skin concerns",
        ["acne", "redness", "hyperpigmentation", "wrinkles", "oiliness", "dehydration"]
    )

    st.subheader("Sensitivities & preferences")
    sensitivity = st.selectbox(
        "Skin sensitivity level",
        ["low", "medium", "high"]
    )

    fragrance = st.selectbox(
        "Fragrance level",
        ["no preference", "fragrance-free", "light fragrance OK"]
    )

    budget = st.slider(
        "Budget per Product (CHF)",
        min_value=5,
        max_value=80,
        value=25
    )

    st.subheader("Environment")
    climate = st.selectbox(
        "Climate",
        ["cold", "moderate", "hot"]
    )

    sun = st.selectbox(
        "Sun exposure",
        ["mostly indoors", "mixed", "mostly outdoors"]
    )

    submit = st.form_submit_button("Save Profile")

    if submit:
        st.session_state["profile"] = {
            "skin_type": skin_type,
            "age_group": age_group,
            "concerns": concerns,
            "sensitivity": sensitivity,
            "fragrance": fragrance,
            "budget": budget,
            "climate": climate,
            "sun": sun,
        }
        st.success("Profile saved!")

    if "profile" in st.session_state:
        st.write("### Current profile:")
        st.json(st.session_state["profile"])

