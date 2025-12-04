import pandas as pd
import re


def load_ingredient_data(path: str = "data/ingredients_dict.csv"):

    df = pd.read_csv(path)


    df.columns = [col.lower() for col in df.columns]


    df["name_clean"] = df["name"].str.strip().str.lower()

    return df



INGREDIENT_DF = load_ingredient_data()


def parse_ingredient_list(text: str):

    parts = re.split(r",|;", text)
    ingredients = [p.strip().lower() for p in parts if p.strip()]
    return ingredients


def get_ingredient_info(name: str):

    name_clean = name.strip().lower()


    match = INGREDIENT_DF[INGREDIENT_DF["name_clean"] == name_clean]


    if match.empty:
        mask = INGREDIENT_DF["name_clean"].str.contains(name_clean, na=False)
        match = INGREDIENT_DF[mask]

    if match.empty:
        return None

    row = match.iloc[0]

    return {
        "name": row["name"],
        "short_description": row.get("short_description", ""),
        "what_is_it": row.get("what_is_it", ""),
        "what_does_it_do": row.get("what_does_it_do", ""),
        "who_is_it_good_for": row.get("who_is_it_good_for", ""),
        "who_should_avoid": row.get("who_should_avoid", ""),
        "url": row.get("url", "")
    }
