# 🌾 Crop Recommendation System

A machine learning project that recommends the most suitable crop to grow based on soil nutrients and weather conditions. Given values like Nitrogen, Phosphorus, Potassium, temperature, humidity, pH and rainfall, the model predicts which crop will grow best on that land.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Workflow](#-workflow)
- [Model Performance](#-model-performance)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Prediction](#-example-prediction)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🧭 Overview
Farmers often choose crops based on tradition or guesswork, which can lead to poor yields when soil and climate conditions don't match the crop's needs. This project uses data-driven predictions to help farmers, agronomists and agricultural planners make better decisions.

The system:
- Analyzes soil and climate data
- Trains a classification model on 22 crop types
- Serves predictions through a simple web app (`app.py`)

---

## ❓ Problem Statement
Build a model that takes soil and environmental parameters as input and recommends the best crop to cultivate, to improve yield and reduce resource waste.

---

## 📊 Dataset
**File:** `Crop_recommendation.csv`

| Feature | Description | Unit |
|---|---|---|
| `N` | Nitrogen content in soil | ratio |
| `P` | Phosphorus content in soil | ratio |
| `K` | Potassium content in soil | ratio |
| `temperature` | Average temperature | °C |
| `humidity` | Relative humidity | % |
| `ph` | Soil pH value | 0–14 |
| `rainfall` | Rainfall | mm |
| `label` | Recommended crop (target) | — |

- **Rows:** 2,200
- **Classes:** 22 crops, balanced (100 samples each)

**Crops covered:** rice, maize, chickpea, kidney beans, pigeon peas, moth beans, mung bean, black gram, lentil, pomegranate, banana, mango, grapes, watermelon, muskmelon, apple, orange, papaya, coconut, cotton, jute, coffee.

---

## 📁 Project Structure
```
crop-recommendation/
│
├── Crop_Recommendation.ipynb      # EDA, preprocessing, model training & evaluation
├── Crop_recommendation.csv        # Dataset
├── crop_recommendation_model.pkl  # Trained model (saved with pickle)
├── app.py                         # Web app for making predictions
└── readme.md                      # Project documentation
```

---

## 🛠 Tech Stack
- **Language:** Python 3
- **Data handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Model saving:** Pickle
- **Web app:** Streamlit
- **Notebook:** Jupyter / Google Colab

---

## 🔄 Workflow

1. **Data Loading:** read the CSV with Pandas.
2. **Exploratory Data Analysis (EDA)**
   - Checked for missing values and duplicates
   - Studied feature distributions
   - Correlation heatmap between features
   - Compared nutrient and climate needs across crops
3. **Preprocessing**
   - Split features (`X`) and target (`y`)
   - Train-test split (80:20)
   - Feature scaling where required
4. **Model Training:** compared several classifiers:
   - Logistic Regression
   - Decision Tree
   - K-Nearest Neighbors
   - Support Vector Machine
   - Naive Bayes
   - Random Forest
5. **Evaluation:** accuracy, confusion matrix and classification report.
6. **Saving the Model:** best model exported to `crop_recommendation_model.pkl`.
7. **Deployment:** `app.py` loads the model and predicts crops from user input.

---

## 📈 Model Performance

| Model | Accuracy |
|---|---|
| Logistic Regression | XX % |
| Decision Tree | XX % |
| KNN | XX % |
| SVM | XX % |
| Naive Bayes | XX % |
| **Random Forest** | **XX %** |

✅ **Random Forest** was chosen as the final model for its high accuracy and robustness.

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/nitish1308/ML-Projects-.git
cd ML-Projects-/crop-recommendation
```

**2. (Optional) Create a virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

---

## 🚀 Usage

**Run the web app**
```bash
streamlit run app.py
```
Then open the local link shown in the terminal (usually `http://localhost:8501`), enter the soil and weather values, and click **Predict**.

**Explore the notebook**
```bash
jupyter notebook Crop_Recommendation.ipynb
```

**Use the model in your own Python code**
```python
import pickle
import numpy as np

model = pickle.load(open("crop_recommendation_model.pkl", "rb"))

# N, P, K, temperature, humidity, ph, rainfall
sample = np.array([[90, 42, 43, 20.8, 82.0, 6.5, 202.9]])
print("Recommended crop:", model.predict(sample)[0])
```

---

## 🧪 Example Prediction

| N | P | K | Temp (°C) | Humidity (%) | pH | Rainfall (mm) | Prediction |
|---|---|---|---|---|---|---|---|
| 90 | 42 | 43 | 20.8 | 82.0 | 6.5 | 202.9 | 🌾 Rice |

---

## 🔮 Future Improvements
- Add live weather data through a weather API using the user's location
- Recommend fertilizers based on nutrient deficiency
- Support regional languages for farmers
- Deploy online (Streamlit Cloud / Render / Hugging Face Spaces)
- Add crop yield and market price prediction
- Build a mobile-friendly version

---

## 👤 Author
**Nitish SaWant**
D Y Patil International University
GitHub: [@nitish1308](https://github.com/nitish1308)

---

⭐ If you found this project useful, consider giving the repo a star!
