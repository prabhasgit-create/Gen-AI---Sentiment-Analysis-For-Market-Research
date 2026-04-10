import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

sentiment_pipeline = load_model()

def analyze_sentiment(text):
    result = sentiment_pipeline(text[:512])[0]  # limit long text
    return result['label'], result['score']