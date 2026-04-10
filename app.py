import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import time

from model import analyze_sentiment
from utils import clean_text

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

st.set_page_config(page_title="AI Sentiment Analysis ", layout="wide")

st.title("📊 Gen-AI Sentiment Analysis For Market Research ")
st.write("Analyze real product reviews & sentiment analysis directly from e-commerce URLs.")

# ---------------- STOPWORDS ----------------
stopwords = set([
    "the", "is", "and", "to", "it", "this", "that", "for", "with",
    "was", "are", "in", "of", "on", "very", "a", "an"
])

# ---------------- KEYWORD EXTRACTION ----------------
def extract_keywords(text_list):
    words = " ".join(text_list).lower()
    words = re.findall(r'\b[a-z]{3,}\b', words)
    filtered = [w for w in words if w not in stopwords]
    return Counter(filtered).most_common(5)

# ---------------- SELENIUM SCRAPER ----------------
def scrape_amazon(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    time.sleep(3)

    # Product name
    try:
        product_name = driver.find_element(By.ID, "productTitle").text
    except:
        product_name = "Product Name Not Found"

    reviews = []

    try:
        review_elements = driver.find_elements(By.CSS_SELECTOR, "span[data-hook='review-body']")
        for r in review_elements:
            reviews.append(r.text)
    except:
        pass

    driver.quit()

    return product_name, reviews[:30]

# ---------------- ANALYSIS FUNCTION ----------------
def show_analysis(df):

    st.subheader("📊 Sentiment Percentage")
    percent = df["Sentiment"].value_counts(normalize=True) * 100
    st.write(percent)

    fig, ax = plt.subplots()
    percent.plot(kind="bar", ax=ax)
    st.pyplot(fig)

    total = len(df)
    positive = (df["Sentiment"] == "POSITIVE").sum()
    negative = (df["Sentiment"] == "NEGATIVE").sum()

    st.subheader("📈 Insights")
    st.write(f"Total Reviews: {total}")
    st.write(f"Positive: {positive}")
    st.write(f"Negative: {negative}")

    score = (positive / total) * 100
    st.subheader("⭐ Product Score")
    st.write(f"{score:.2f} / 100")

    st.subheader("🛒 Recommendation")
    if positive > negative * 1.5:
        st.success("✅ Strong Buy")
    elif positive > negative:
        st.warning("⚖️ Mixed Reviews")
    else:
        st.error("❌ Not Recommended")

    # 🔍 Pros & Cons
    st.subheader("🔍 Pros & Cons")

    positive_reviews = df[df["Sentiment"] == "POSITIVE"]["review"].tolist()
    negative_reviews = df[df["Sentiment"] == "NEGATIVE"]["review"].tolist()

    pos_words = extract_keywords(positive_reviews)
    neg_words = extract_keywords(negative_reviews)

    col1, col2 = st.columns(2)

    with col1:
        st.write("👍 Pros")
        for w, c in pos_words:
            st.write(f"{w} ({c})")

    with col2:
        st.write("👎 Cons")
        for w, c in neg_words:
            st.write(f"{w} ({c})")

    # Download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Results", data=csv, file_name="results.csv")

# ---------------- UI ----------------
url = st.text_input("🔗 Enter Amazon Product URL")

if st.button("Analyze Product"):
    if url.strip():
        with st.spinner("Scraping real reviews..."):
            product_name, reviews = scrape_amazon(url)

        if not reviews:
            st.error("❌ No reviews found. Try another product.")
        else:
            st.subheader(f"🛍️ {product_name}")
            st.success(f"Fetched {len(reviews)} reviews")

            df = pd.DataFrame({"review": reviews})

            results = df["review"].apply(lambda x: analyze_sentiment(clean_text(str(x))))
            df["Sentiment"] = results.apply(lambda x: x[0])
            df["Confidence"] = results.apply(lambda x: x[1])

            st.dataframe(df.head())

            show_analysis(df)

    else:
        st.warning("Enter a URL")