"""
Utilities for creating visualizations and charts
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


def create_skin_type_distribution(df: pd.DataFrame, column: str = 'skin_type') -> go.Figure:
    """Creates a chart for skin type distribution."""
    if df.empty or column not in df.columns:
        return None
    
    counts = df[column].value_counts()
    
    fig = px.pie(
        values=counts.values,
        names=counts.index,
        title="Skin Type Distribution",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=400, showlegend=True)
    
    return fig


def create_product_type_chart(df: pd.DataFrame) -> go.Figure:
    """Creates a bar chart for product types."""
    if df.empty or 'product_type' not in df.columns:
        return None
    
    counts = df['product_type'].value_counts().head(10)
    
    fig = px.bar(
        x=counts.values,
        y=counts.index,
        orientation='h',
        title="Top 10 Product Types",
        labels={'x': 'Quantity', 'y': 'Product Type'},
        color=counts.values,
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(height=500, showlegend=False)
    
    return fig


def create_brand_distribution(df: pd.DataFrame, top_n: int = 15) -> go.Figure:
    """Creates a chart for brand distribution."""
    if df.empty or 'brand_name' not in df.columns:
        return None
    
    counts = df['brand_name'].value_counts().head(top_n)
    
    fig = px.bar(
        x=counts.index,
        y=counts.values,
        title=f"Top {top_n} Brands",
        labels={'x': 'Brand', 'y': 'Number of Products'},
        color=counts.values,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        height=500,
        xaxis_tickangle=-45,
        showlegend=False
    )
    
    return fig


def create_ingredient_frequency_chart(ingredients_list: list, top_n: int = 20) -> go.Figure:
    """Creates a chart for most common ingredients."""
    if not ingredients_list:
        return None
    
    # Flatten lista de ingredientes
    all_ingredients = []
    for ing_list in ingredients_list:
        if isinstance(ing_list, list):
            all_ingredients.extend(ing_list)
    
    if not all_ingredients:
        return None
    
    # Contar frequência
    ingredient_counts = pd.Series(all_ingredients).value_counts().head(top_n)
    
    fig = px.bar(
        x=ingredient_counts.values,
        y=ingredient_counts.index,
        orientation='h',
        title=f"Top {top_n} Most Common Ingredients",
        labels={'x': 'Frequency', 'y': 'Ingredient'},
        color=ingredient_counts.values,
        color_continuous_scale='Teal'
    )
    
    fig.update_layout(height=600, showlegend=False)
    
    return fig


def create_concern_distribution(concerns_data: list) -> go.Figure:
    """Creates a chart for most common skin concerns."""
    if not concerns_data:
        return None
    
    # Flatten lista de concerns
    all_concerns = []
    for concern_list in concerns_data:
        if isinstance(concern_list, list):
            all_concerns.extend(concern_list)
        elif isinstance(concern_list, str):
            all_concerns.append(concern_list)
    
    if not all_concerns:
        return None
    
    concern_counts = pd.Series(all_concerns).value_counts()
    
    fig = px.bar(
        x=concern_counts.index,
        y=concern_counts.values,
        title="Most Common Skin Concerns",
        labels={'x': 'Concern', 'y': 'Frequency'},
        color=concern_counts.values,
        color_continuous_scale='Reds'
    )
    
    fig.update_layout(height=400, showlegend=False)
    
    return fig


def create_ingredient_category_pie(categories: dict) -> go.Figure:
    """Creates a pie chart for ingredient categories."""
    if not categories:
        return None
    
    fig = go.Figure(data=[go.Pie(
        labels=list(categories.keys()),
        values=list(categories.values()),
        hole=0.3
    )])
    
    fig.update_layout(
        title="Ingredient Categories",
        height=400
    )
    
    return fig


def create_similarity_comparison(products_df: pd.DataFrame) -> go.Figure:
    """Creates a chart for product similarity comparison."""
    if products_df.empty or 'similarity' not in products_df.columns:
        return None
    
    fig = px.bar(
        products_df,
        x='product_name',
        y='similarity',
        title="Product Similarity Comparison",
        labels={'product_name': 'Product', 'similarity': 'Similarity (%)'},
        color='similarity',
        color_continuous_scale='Greens'
    )
    
    fig.update_layout(
        height=400,
        xaxis_tickangle=-45,
        showlegend=False
    )
    
    return fig


def create_price_distribution(df: pd.DataFrame, price_column: str = 'price') -> go.Figure:
    """Creates a histogram for price distribution."""
    if df.empty or price_column not in df.columns:
        return None
    
    # Remover valores nulos
    prices = df[price_column].dropna()
    
    if prices.empty:
        return None
    
    fig = px.histogram(
        prices,
        nbins=30,
        title="Price Distribution",
        labels={'value': 'Price (CHF)', 'count': 'Frequency'},
        color_discrete_sequence=['#3b82f6']
    )
    
    fig.update_layout(height=400, showlegend=False)
    
    return fig


def create_summary_metrics_table(data: dict) -> pd.DataFrame:
    """Creates a summary metrics table."""
    df = pd.DataFrame(list(data.items()), columns=['Metric', 'Value'])
    return df


def create_ingredient_comparison_table(ingredients: list, info_list: list) -> pd.DataFrame:
    """Creates a comparative table of ingredients."""
    if not ingredients or not info_list:
        return pd.DataFrame()
    
    data = {
        'Ingredient': [],
        'Category': [],
        'Main Benefit': [],
        'Good For': []
    }
    
    for ing, info in zip(ingredients, info_list):
        if info:
            data['Ingredient'].append(info.get('name', ing))
            data['Category'].append(info.get('what_is_it', 'N/A')[:50] + '...' if info.get('what_is_it') else 'N/A')
            data['Main Benefit'].append(info.get('what_does_it_do', 'N/A')[:50] + '...' if info.get('what_does_it_do') else 'N/A')
            data['Good For'].append(info.get('who_is_it_good_for', 'N/A')[:50] + '...' if info.get('who_is_it_good_for') else 'N/A')
    
    return pd.DataFrame(data)


def create_gauge_chart(value: float, title: str, max_value: float = 100) -> go.Figure:
    """Creates a gauge (meter) chart."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        title={'text': title},
        delta={'reference': max_value * 0.5},
        gauge={
            'axis': {'range': [None, max_value]},
            'bar': {'color': "#3b82f6"},
            'steps': [
                {'range': [0, max_value * 0.33], 'color': "#fee2e2"},
                {'range': [max_value * 0.33, max_value * 0.66], 'color': "#fef3c7"},
                {'range': [max_value * 0.66, max_value], 'color': "#d1fae5"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': max_value * 0.9
            }
        }
    ))
    
    fig.update_layout(height=300)
    
    return fig
