# Sales Prediction Using Python

This project predicts **sales** based on **advertising spend on TV, Radio, and Newspaper** using **machine learning techniques** in Python. The goal is to help businesses optimize advertising budgets and maximize sales.

## Project Structure

- `Sales Prediction.ipynb` → Jupyter Notebook with EDA, ML model training, evaluation  
- `app.py` → Streamlit app for live sales prediction  
- `finalmodel.pkl` → Trained Random Forest model  
- `requirements.txt` → Python packages required  

## Features

- Exploratory Data Analysis (EDA) of advertising dataset  
- Comparison of multiple regression models (Linear Regression, Random Forest, etc.)  
- Feature selection (TV & Radio) for best performance  
- Streamlit web app for predicting sales in real time  


---

# **Step 6: Add How to Use / Run**

```markdown
## How to Run

### 1. Jupyter Notebook
- Open `Sales Prediction.ipynb` to explore EDA and model training.

### 2. Streamlit App
- Run the app:
```bash
streamlit run app.py


---

# **Step 7: Add Results / Evaluation**

```markdown
## Model Evaluation

Random Forest Model Performance (TV + Radio):

- MAE: 0.83  
- MSE: 1.24  
- RMSE: 1.11  
- R2 Score: 0.959  

Observation: Dropping Newspaper improved model accuracy.
## Author

Shravani Deotale

## Tools Used

- Python, pandas, numpy, scikit-learn, matplotlib, seaborn  
- Streamlit for web app  
