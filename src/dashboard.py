"""
dashboard.py

Streamlit dashboard for employee attrition analysis.
"""
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    return pd.read_csv("data/employee_data_1.csv")

@st.cache
def load_model():
    return joblib.load("src/attrition_model.pkl")

st.title("Employee Attrition Dashboard")

df = load_data()
st.sidebar.header("Filters")
dept = st.sidebar.multiselect("Department", options=df['Department'].unique(), default=df['Department'].unique())
df = df[df['Department'].isin(dept)]

st.subheader("Attrition Summary")
st.write(df['Attrition'].value_counts(normalize=True).mul(100).round(2))

model = load_model()
X = df[['Age','MonthlyIncome','YearsAtCompany','JobSatisfaction']]
df['Attrition_Prob'] = model.predict_proba(X)[:,1]

st.subheader("Risk Probabilities")
st.bar_chart(df['Attrition_Prob'])

st.subheader("Salary vs Probability")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='MonthlyIncome', y='Attrition_Prob', hue='Attrition', ax=ax)
st.pyplot(fig)
