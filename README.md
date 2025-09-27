# 📩 SMS Spam Detection

**🚀 Live Demo:** [Click here to try the app](https://sms-spam-detection-sp8tmb898ygftrzkkvi6b8.streamlit.app/)  

## 📝 Project Overview
This project is an **SMS Spam Detection System** using **Machine Learning**. It classifies incoming SMS messages as **Spam** or **Ham (not spam)**. The model is trained on a dataset of SMS messages and uses **Natural Language Processing (NLP)** techniques to predict message types.

---

## ✨ Features
- 🔹 Predicts whether an SMS is **Spam** or **Ham**  
- 🔹 Interactive **web interface** built using **Streamlit**  
- 🔹 High accuracy using **Multinomial Naive Bayes** and **TF-IDF vectorization**  
- 🔹 Easy-to-use: input messages directly on the app and get instant predictions  

---

## 🛠 Technology Stack
- **Python 3.x** 🐍  
- **Machine Learning:** Scikit-learn (Multinomial Naive Bayes) 🤖  
- **Data Processing:** Pandas, NumPy, NLTK 📊  
- **Visualization:** Matplotlib, Seaborn 📈  
- **Web App Framework:** Streamlit 🌐  

---

## 📂 Dataset
- Original dataset: [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)  
- Columns used:  
  - `v1` → Label (`ham` or `spam`)  
  - `v2` → SMS message text  

---

## ⚙️ How It Works
1. **Preprocessing:**  
   - Clean text data using regex 🧹  
   - Remove stopwords using NLTK 🗑️  
2. **Feature Extraction:**  
   - Convert text messages into numerical vectors using **TF-IDF Vectorizer** 🔢  
3. **Model Training:**  
   - Train **Multinomial Naive Bayes** classifier on the processed dataset 🏋️  
4. **Prediction:**  
   - Input new SMS messages via the Streamlit app 💻  
   - Model predicts `Spam` or `Ham` ✅  

---

## 📊 Usage
1. Open the app using the live demo link 🌐  
2. Enter your SMS message in the input box 📝  
3. Click **Predict** 🔮  
4. The app will display whether the message is **Spam** or **Ham** ✅  

---

## 🧪 Example
| Message | Prediction |
|---------|------------|
| "Congratulations! You won a $1000 gift card." 🎉 | Spam 🚫 |
| "Hey, are we meeting today?" 🙂 | Ham ✅ |

---

## 📈 Model Performance
- **Accuracy:** 96.23% 🎯  
- **Precision, Recall, F1-Score:**  
  - Ham: 0.96 / 1.00 / 0.98 🟢  
  - Spam: 1.00 / 0.72 / 0.84 🔴  

---

## 📂 Files
- `spam_model.pkl` → Trained ML model 🤖  
- `vectorizer.pkl` → TF-IDF vectorizer 🔢  
- `sms-spam-detection.py` → Streamlit app 🌐  
- `spam.csv` → Dataset (if included) 📄  
- `requirements.txt` → Python dependencies 📦  

---

## 🚀 Future Improvements
- 🌐 Add support for multiple languages  
- 📲 Integrate with SMS API for real-time spam detection  
- 🤖 Use deep learning models for better accuracy  

---

## 👤 Author
**Rupesh Kumar Shah**  
- [LinkedIn](#) | [GitHub](#)  
