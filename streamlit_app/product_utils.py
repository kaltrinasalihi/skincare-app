import pandas as pd
import ast


def load_products(path: str = "data/products.csv"):

    df = pd.read_csv(path)


    df["clean_ingreds"] = df["clean_ingreds"].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) else []
    )


    df["clean_ingreds"] = df["clean_ingreds"].apply(
        lambda lst: [ing.strip().lower() for ing in lst]
    )

    return df



PRODUCTS_DF = load_products()


def recommend_products(ingredient_list, top_k: int = 3):

    user_set = set([i.strip().lower() for i in ingredient_list if i.strip()])

    scores = []

    for idx, row in PRODUCTS_DF.iterrows():
        prod_set = set(row["clean_ingreds"])

        if not prod_set:
            sim = 0.0
        else:
            inter = len(user_set & prod_set)
            union = len(user_set | prod_set)
            sim = inter / union if union > 0 else 0.0

        scores.append(sim)

    PRODUCTS_DF["similarity"] = scores


    recs = PRODUCTS_DF.sort_values(by="similarity", ascending=False).head(top_k).copy()
    return recs
