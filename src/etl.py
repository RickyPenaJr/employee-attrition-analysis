"""
etl.py

Extract, transform, load pipeline for employee attrition data.
"""
import pandas as pd
from sqlalchemy import create_engine

def etl(csv_path, db_url):
    # Extract
    df = pd.read_csv(csv_path)
    
    # Transform
    df['AttritionFlag'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
    df['TenureYears'] = df['YearsAtCompany']
    df['SatisfactionLevel'] = df['JobSatisfaction'] / df['JobSatisfaction'].max()
    
    # Load
    engine = create_engine(db_url)
    df.to_sql('employees', engine, if_exists='replace', index=False)
    
    print(f"Loaded {len(df)} records into the database.")
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run ETL for HR attrition data")
    parser.add_argument("--csv", default="../data/employee_data_1.csv", help="Path to CSV file")
    parser.add_argument("--db", default="sqlite:///../db/employee_attrition.db", help="Database URL")
    args = parser.parse_args()
    etl(args.csv, args.db)
