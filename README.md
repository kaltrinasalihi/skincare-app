# Through the Label 🧴✨

A modern skincare analysis application that helps users make data-driven decisions about their skincare products.
Built as part of the *Fundamentals and Methods of Computer Science for Business Studies* course.

---

## 🌟 Main Features

### 🧬 Personal Profile

* Create a skin profile with:

  * skin type
  * age group
  * main concerns
  * sensitivity level
  * fragrance preference
  * budget
  * climate
  * sun exposure
* Profile data is stored securely in the Streamlit session state.
* The app provides simple product suggestions aligned with the user’s profile.
* Gauge charts help visualize sensitivity and budget positioning.

---

### 🔍 Ingredient Analysis

* Paste an INCI ingredient list directly into the app.
* The app parses and compares the list to the ingredient database.
* For each recognized ingredient, the app displays:

  * what it is
  * what it does
  * who it is good for
  * who should avoid it
  * an external link for further reading

* Unknown ingredients are clearly highlighted.
* Coverage charts summarize how many ingredients were recognized.
* Ingredient-based similarity is used to recommend matching products.

---

### 🧴 Product Discovery

* Browse a curated skincare product catalog.
* Filter by:

  * product type
  * brand
  * keyword search
* View product fields (name, type, brand, URL, ingredient list).
* Interactive charts show:

  * product type distribution
  * brand distribution
  * combined category breakdowns

---

### 📊 Dashboard & Analytics

* Overview metrics:

  * total products
  * total ingredients
  * number of brands
  * number of categories
* Interactive visualizations:

  * sunburst charts
  * bar charts
  * ingredient frequency analysis

---

## 🧠 Recommendation Algorithm (Machine Learning Component)

The application includes a content-based recommendation engine using a Jaccard-style similarity score.

**How it works:**

* Each product contains a cleaned list of ingredients.
* The user input list is parsed and normalized.
* Similarity is computed as:

      similarity = |intersection| / |union|

* Products with highest similarity scores are recommended.

This satisfies the machine learning requirement for the course project.

---

## 🎯 Alignment With Course Project Requirements

1. **Clearly defined problem:**
   Consumers struggle to understand skincare ingredient lists.

2. **Use of data from API/database:**
   The app loads structured CSV datasets:
   `ingredients_dict.csv` and `products.csv`.
   We got our datasets from Kaggle, and added an extra column for the brand in the products dataset.

3. **Meaningful data visualizations:**
   Used across all pages (Plotly): coverage, brand/type distribution, dashboards, gauges.

4. **User interaction:**
   Includes profile form, ingredient input, search and filter controls, interactive charts.

5. **Machine learning:**
   Similarity-based recommendation algorithm.

6. **Documented, well-structured code:**
   Organized into `src/`, `utils/`, `pages/`, with readable logic.

7. **Contribution matrix:**
   Submitted separately, included in the zip file.

8. **4-minute video presentation:**
   Demonstrates full app workflow, submitted separately, included in the zip file.

---

## 🚀 How to Run the App

**Run Online (Recommended)**

_You can access the full application instantly through the Streamlit Cloud deployment:_

👉 https://through-the-label.streamlit.app/

No installation, setup, or environment configuration needed.

---

## 🔗 Sources
   * Product datasets sourced from Kaggle:
         - https://www.kaggle.com/datasets/eward96/skincare-products-and-their-ingredients
   * Ingredient dictionary sourced from Kaggle:
         - https://www.kaggle.com/datasets/amaboh/skin-care-product-ingredients-inci-list
   * OpenAI ChatGPT was used for as an aid for guidance, icon creation, clarification of concepts, and support in refining the project’s code and documentation.
   * Voiceover for the video presentation was generated using elevenlabs:
         - https://elevenlabs.io/app/speech-synthesis/text-to-speech
   * IMovie was used for video editing:
         - https://www.apple.com/imovie/index.html

---

## 👩‍💻 Team

GitHub Profiles:

* [Kaltrina Salihi](https://github.com/kaltrinasalihi)
* [Luana Borma Brugger](https://github.com/luana-brugger)
* [Michele Natali](https://github.com/MikHUBjk)
* [Sara Penha dos Santos](https://github.com/saraapenha)


---

Made with ❤️ by the Through the Label Team