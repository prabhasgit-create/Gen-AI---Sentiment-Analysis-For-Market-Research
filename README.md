
# 🛍️ Gen-AI---Sentiment-Analysis-For-Market-Research

## 📌 Project Overview

This project is a **GenAI-powered Sentiment Analysis Tool** that analyzes product reviews directly from an e-commerce product URL.

Instead of manually entering reviews, users can:

* Paste a product link
* Automatically extract reviews
* Analyze customer sentiment
* Get a clear **Buy / Not Buy recommendation**
* Perform basic **market research**

---

## 🚀 Features

* 🔗 Extract reviews from product URL
* 📊 Sentiment Analysis (Positive, Negative, Neutral)
* 📈 Visual charts (Bar + Pie)
* 🧠 Keyword-based Pros & Cons extraction
* 🛒 Buy / Not Buy recommendation system
* 🏷️ Automatic Product Name detection
* ⚡ Built with Streamlit for interactive UI

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python
* **Libraries**:

  * pandas
  * matplotlib
  * selenium
  * webdriver-manager
  * beautifulsoup4
  * requests

---

## 📂 Project Structure

```
sentiment-genai-project/
│── app.py
│── model.py
│── utils.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/your-repo-name.git
cd sentiment-genai-project
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

If requirements.txt is not available:

```
pip install streamlit pandas matplotlib selenium webdriver-manager beautifulsoup4 requests
```

---

### 4️⃣ Run the Application

```
streamlit run app.py
```

---

## 📊 How It Works

1. User enters product URL
2. Selenium scrapes product reviews
3. Text is cleaned and processed
4. Sentiment model classifies reviews
5. Results are visualized
6. Pros & Cons are extracted
7. Final recommendation is generated

---

## 🧠 Output Includes

* Sentiment Distribution
* Review Count
* Product Name
* Pros & Cons Summary
* Buy Recommendation

---

## ⚠️ Limitations

* Works best with supported e-commerce sites (Amazon, Flipkart, etc.)
* Dynamic websites may require updates in scraping logic
* Requires Chrome browser for Selenium

---

## 🔮 Future Improvements

* Add support for multiple e-commerce platforms
* Improve NLP model accuracy
* Add real-time price tracking
* Deploy as a web app (Cloud)

---

## 🙌 Author

**T Prabhas**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🛠️ Contribute improvements

---
