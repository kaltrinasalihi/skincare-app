"""
Centralized settings for the Through the Label app
"""

# Page settings
PAGE_CONFIG = {
    "page_title": "Through the Label",
    "page_icon": "🧴",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Data paths
DATA_PATHS = {
    "ingredients": "data/ingredients_dict.csv",
    "products": "data/products.csv"
}

# Profile options
SKIN_TYPES = ["Oily", "Dry", "Combination", "Normal", "Sensitive"]

AGE_GROUPS = [
    "Teen (13-19 years)",
    "Young Adult (20-29 years)",
    "Adult (30-44 years)",
    "Mature (45+ years)"
]

SKIN_CONCERNS = [
    "Acne",
    "Redness",
    "Hyperpigmentation",
    "Wrinkles",
    "Oiliness",
    "Dehydration"
]

SENSITIVITY_LEVELS = ["Low", "Medium", "High"]

FRAGRANCE_PREFERENCES = [
    "No preference",
    "Fragrance-free",
    "With fragrance"
]

CLIMATE_OPTIONS = ["Cold", "Moderate", "Hot"]

SUN_EXPOSURE_OPTIONS = ["Mostly indoors", "Mixed", "Mostly outdoors"]

# Budget settings
BUDGET_MIN = 5
BUDGET_MAX = 80
BUDGET_DEFAULT = 25

# Custom CSS for better appearance and responsiveness
CUSTOM_CSS = """
<style>
    /* Remove extra top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Improve cards and containers */
    .stExpander {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin-bottom: 0.5rem;
    }
    
    /* Nicer buttons */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 3rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Improve forms */
    .stTextArea textarea, .stTextInput input {
        border-radius: 8px;
    }
    
    /* Headers with better spacing */
    h1, h2, h3 {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Feature cards */
    .feature-card {
        padding: 1.5rem;
        border-radius: 12px;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem;
        }
        
        .stButton > button {
            height: 2.5rem;
            font-size: 0.9rem;
        }
    }
    
    /* Better JSON visualization */
    .stJson {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
    }
</style>
"""
