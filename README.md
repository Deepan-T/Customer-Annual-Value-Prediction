# Customer Annual Value Prediction using Machine Learning

## 📌 Project Overview

This project predicts the **Annual Value of a Customer** using Machine Learning regression algorithms.

The model uses customer demographic, subscription, usage, satisfaction, payment, and service-related information to predict the expected annual value of a customer.

Multiple regression algorithms are implemented and their predictions are compared. The trained models are then integrated into a **Flask web application** to provide predictions based on user input.

---

## 🎯 Objective

The main objective of this project is to:

* Predict customer annual value using Machine Learning.
* Apply different regression algorithms.
* Compare predictions from multiple models.
* Process categorical customer information using Label Encoding.
* Save trained models using Pickle.
* Deploy the prediction system using Flask.

---

## 📊 Dataset Features

The project uses customer-related features such as:

* Age
* Gender
* Plan Type
* Tenure Months
* Monthly Usage Hours
* Support Tickets
* Satisfaction Score
* Monthly Charges
* Data Usage GB
* Payment Delay Days
* Contract Months
* Average Login Days
* Service Count
* Discount Percent

### Target

**Customer Annual Value**

The target variable represents the annual value predicted for a customer.

---

## 🤖 Machine Learning Algorithms

The project uses four regression algorithms:

### 1. Linear Regression

A basic regression algorithm used to model the relationship between input features and the target value.

### 2. Decision Tree Regression

Uses a tree-based structure to make predictions by splitting the data based on feature values.

### 3. Random Forest Regression

Uses multiple decision trees and combines their predictions to produce the final prediction.

### 4. Support Vector Regression (SVR)

A Support Vector Machine-based regression algorithm used to predict continuous numerical values.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Label Encoding
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Linear Regression
Decision Tree
Random Forest
SVR
   ↓
Model Saving using Pickle
   ↓
Flask Web Application
   ↓
User Input
   ↓
Predictions
   ↓
Average Prediction
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* Pickle
* HTML
* Jupyter Notebook

---

## 📁 Project Structure

```text
Customer-Annual-Value-Prediction/
│
├── Customer_AnnualVal_prediction.ipynb
├── Customer_Regression_Practice_20000.csv
│
├── app.py
│
├── model1.pkl
├── model2.pkl
├── model3.pkl
├── model4.pkl
│
├── gender_encoder.pkl
├── plan_encoder.pkl
│
├── templates/
│   └── index.html
│
├── .gitignore
└── README.md
```

---

## 💾 Saved Models

The Flask application loads four trained models:

| Model File   | Algorithm                 |
| ------------ | ------------------------- |
| `model1.pkl` | Linear Regression         |
| `model2.pkl` | Decision Tree Regression  |
| `model3.pkl` | Random Forest Regression  |
| `model4.pkl` | Support Vector Regression |

The application also uses saved encoders for:

* Gender
* Plan Type

---

## 🌐 Flask Web Application

The trained models are integrated into a Flask application.

The user enters customer information through the web interface. The application processes the input and generates predictions using all four trained models.

The application displays:

* Linear Regression prediction
* Decision Tree prediction
* Random Forest prediction
* SVR prediction
* Average prediction

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/customer-annual-value-prediction-ml.git
```

### Step 2: Open the Project

```bash
cd customer-annual-value-prediction-ml
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy scikit-learn flask
```

### Step 4: Run Flask

```bash
python app.py
```

### Step 5: Open the Application

Open the local Flask URL shown in the terminal, commonly:

```text
http://127.0.0.1:5000/
```

---

## 🔮 Prediction Process

The application accepts customer details, converts categorical values using saved encoders, creates the required input format, and sends the data to the four trained models.

The predictions are then combined to calculate an average prediction.

---

## 🚀 Future Improvements

* Add model performance comparison using MAE, MSE and R².
* Improve the web interface.
* Add data visualization.
* Add database integration.
* Deploy the Flask application online.
* Add more advanced regression algorithms.

---

## 👨‍💻 Author

**Deepan Thangaraj**

Data Analytics | Machine Learning | Python | SQL | Power BI
