import pandas as pd
import re


def load_ingredient_data(path: str = "data/ingredients_dict.csv"):
    """
    Loads ingredient dataset from CSV.
    Expected columns: name, short_description, what_is_it,
    what_does_it_do, who_is_it_good_for, who_should_avoid, url
    """
    df = pd.read_csv(path)

    # Normalize column names
    df.columns = [col.lower() for col in df.columns]

    # Clean name column for matching
    df["name_clean"] = df["name"].str.strip().str.lower()

    return df


# Global ingredient database (loaded once)
INGREDIENT_DF = load_ingredient_data()


def parse_ingredient_list(text: str):
    """
    Converts raw ingredient text into a clean list.
    Example:
    'Aqua, Glycerin; Niacinamide'
    -> ['aqua', 'glycerin', 'niacinamide']
    """
    parts = re.split(r",|;", text)
    ingredients = [p.strip().lower() for p in parts if p.strip()]
    return ingredients


def get_ingredient_info(name: str):
    """
    Searches for ingredient details inside the CSV.
    Returns a dictionary with info or None.
    """
    name_clean = name.strip().lower()

    # 1. exakte Übereinstimmung
    match = INGREDIENT_DF[INGREDIENT_DF["name_clean"] == name_clean]

    # 2. wenn nichts gefunden: Teilstring-Suche
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
