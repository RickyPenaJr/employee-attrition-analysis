"""
attrition_model.py

Train and evaluate a logistic regression model to predict employee attrition.
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import joblib

def train_model(df):
    X = df[['Age', 'MonthlyIncome', 'YearsAtCompany', 'JobSatisfaction']]
    y = df['AttritionFlag']
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    proba = model.predict_proba(X_test)[:,1]
    
    print(classification_report(y_test, preds))
    print("ROC AUC:", roc_auc_score(y_test, proba))
    
    joblib.dump(model, 'src/attrition_model.pkl')
    print("Model saved to attrition_model.pkl")

if __name__ == "__main__":
    df = pd.read_csv("../data/employee_data_1.csv")
    df['AttritionFlag'] = df['Attrition'].apply(lambda x: 1 if x=='Yes' else 0)
    train_model(df)
