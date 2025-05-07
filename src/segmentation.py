"""
segmentation.py

Customer segmentation via clustering to find attrition risk groups.
"""
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def segment_risk(df, n_clusters=3):
    features = df[['Age', 'MonthlyIncome', 'YearsAtCompany', 'AttritionFlag']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['RiskCluster'] = kmeans.fit_predict(features)
    return df, kmeans

def plot_clusters(df):
    plt.figure(figsize=(8,6))
    plt.scatter(df['MonthlyIncome'], df['YearsAtCompany'], c=df['RiskCluster'], cmap='viridis')
    plt.xlabel('Monthly Income')
    plt.ylabel('Years at Company')
    plt.title('Attrition Risk Clusters')
    plt.tight_layout()
    plt.savefig('src/attrition_clusters.png')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("../data/employee_data_1.csv")
    df['AttritionFlag'] = df['Attrition'].apply(lambda x: 1 if x=='Yes' else 0)
    df, model = segment_risk(df)
    plot_clusters(df)
