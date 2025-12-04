import streamlit as st
from ingredient_utils import parse_ingredient_list, get_ingredient_info
from product_utils import recommend_products

st.title("🔍 Ingredient Analysis")

st.write(
    "Paste the full ingredient list of a skincare product and we will show "
    "what we know about each ingredient."
)

ingredient_text = st.text_area(
    "Ingredient list (comma-separated, in English INCI):",
    placeholder="Aqua, Glycerin, Niacinamide, Hyaluronic Acid, Parfum...",
    height=150,
)

if st.button("Analyze ingredients"):
    if not ingredient_text.strip():
        st.warning("Please paste an ingredient list first.")
    else:
        # 1) Zutaten parsen
        ingredients = parse_ingredient_list(ingredient_text)

        st.write("### Parsed ingredients")
        st.write(ingredients)

        # 2) Infos zu jedem Ingredient anzeigen
        st.write("### Ingredient details")
        for ing in ingredients:
            info = get_ingredient_info(ing)

            if info is None:
                st.write(f"- **{ing}** — no information in our database yet.")
            else:
                with st.expander(info["name"]):
                    if info["short_description"]:
                        st.write(info["short_description"])

                    if info["what_is_it"]:
                        st.markdown(f"**What is it?** {info['what_is_it']}")

                    if info["what_does_it_do"]:
                        st.markdown(f"**What does it do?** {info['what_does_it_do']}")

                    if info["who_is_it_good_for"]:
                        st.markdown(f"**Good for:** {info['who_is_it_good_for']}")

                    if info["who_should_avoid"]:
                        st.markdown(
                            f"**Who should avoid it:** {info['who_should_avoid']}"
                        )

                    if info["url"]:
                        st.markdown(f"[More info]({info['url']})")

        # 3) Empfehlungen auf Basis der Ingredients
        if ingredients:
            st.write("---")
            st.write("### Recommended products based on these ingredients")

            recs = recommend_products(ingredients, top_k=3)

            for _, row in recs.iterrows():
                st.markdown(f"**{row['product_name']}**")
                st.write(row["product_type"])
                st.write(f"[View product online]({row['product_url']})")
                st.caption(f"Similarity score: {row['similarity']:.2f}")
                st.write("")  # Abstand
