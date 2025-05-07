# Employee Attraction Analysis
<img src="https://github.com/user-attachments/assets/dd9b5455-50ac-4186-b23a-5d60b935479e" alt="Employee-Attrition" width="400" />

<br>
<br>


## Project Description
Analyze employee attrition using SQL and Python with IBM's HR Analytics dataset.

---

## 📂 Project Structure

```
employee_attrition_project/
├── data/                  # Raw dataset (CSV)
├── db/                    # SQL schema and analysis queries
├── src/                   # Python analysis scripts
├── dashboard/             # (Optional) Streamlit dashboard
├── notebooks/             # (Optional) Jupyter notebooks
└── README.md
```

---

## 🧰 Technologies

- Python (Pandas, Matplotlib, Seaborn)
- SQL (SQLite/PostgreSQL)
- CSV data format
- Optional: Streamlit, Scikit-learn

---

## 📊 Key SQL Queries

- Attrition rate by department
- Average income by role
- Job satisfaction vs overtime
- Years at company grouped by attrition
- Income group analysis

---

## 📈 Python Analysis

- Attrition by department (bar chart)
- Overtime vs attrition heatmap
- Satisfaction score distributions

## 🔍 Analysis Questions & SQL Insights

## 🔍 Analysis Questions & SQL Insights

Here are key business questions answered with SQL queries and summarized insights:

---

### 1. What is the overall attrition rate?
```sql
SELECT Attrition, COUNT(*) AS Count FROM employees GROUP BY Attrition;
```
✅ ~16% of employees have left the company.

---

### 2. Which department has the highest attrition?
```sql
SELECT Department, SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attritions
FROM employees
GROUP BY Department;
```
✅ Sales department shows the highest attrition.

---

### 3. Does overtime correlate with attrition?
```sql
SELECT OverTime, Attrition, COUNT(*) FROM employees GROUP BY OverTime, Attrition;
```
✅ Most employees who left were working overtime.

---

### 4. What’s the average monthly income of those who left vs stayed?
```sql
SELECT Attrition, AVG(MonthlyIncome) FROM employees GROUP BY Attrition;
```
✅ Employees who left had lower average income.

---

#### 5. Which job roles have the highest turnover?
```sql
SELECT JobRole, SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attritions
FROM employees
GROUP BY JobRole;
```
✅ Sales Executives and Lab Technicians show the most attrition.

---

### 6. How does job satisfaction affect attrition?
```sql
SELECT JobSatisfaction, COUNT(*) AS Count
FROM employees
WHERE Attrition = 'Yes'
GROUP BY JobSatisfaction;
```
✅ Most who left had job satisfaction ratings of 1 or 2.

---

### 7. Do employees with fewer years at the company leave more?
```sql
SELECT Attrition, AVG(YearsAtCompany) FROM employees GROUP BY Attrition;
```
✅ Yes — they averaged fewer years at the company.

---

### 8. Are certain education fields more prone to attrition?
```sql
SELECT EducationField, COUNT(*) AS Total, 
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attritions
FROM employees
GROUP BY EducationField;
```
✅ Life Sciences and Medical fields had the most attrition.

---

## 📊 Visualizations

Here are some key visualizations included in the project:

### 📌 Attrition by Job Role
![Attrition by Job Role](src/attrition_by_jobrole.png)

### 📌 Monthly Income by Attrition
![Monthly Income by Attrition](src/income_by_attrition.png)

### 📌 Job Satisfaction vs Attrition
![Job Satisfaction vs Attrition](src/satisfaction_by_attrition.png)

### 📌 Years at Company vs Attrition
![Years at Company vs Attrition](src/years_at_company.png)

---

### 9. What is the average age of employees who left vs stayed?
```sql
SELECT Attrition, AVG(Age) FROM employees GROUP BY Attrition;
```
✅ Employees who left were slightly younger on average.

---

### 10. Does marital status influence attrition?
```sql
SELECT MaritalStatus, COUNT(*) AS Total, 
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attritions
FROM employees
GROUP BY MaritalStatus;
```
✅ Single employees showed higher attrition counts.

---

### 11. Is there a pattern between distance from home and attrition?
```sql
SELECT Attrition, AVG(DistanceFromHome) FROM employees GROUP BY Attrition;
```
✅ Employees who left tended to live farther from work.



### 12. What is the attrition breakdown by gender?
```sql
SELECT Gender, Attrition, COUNT(*) FROM employees GROUP BY Gender, Attrition;
```
✅ Males had slightly more attritions than females.



### 13. What stock option levels are most common among employees who stay?
```sql
SELECT StockOptionLevel, COUNT(*) 
FROM employees 
WHERE Attrition = 'No'
GROUP BY StockOptionLevel;
```
✅ Most retained employees had Stock Option Level 1.



### 14. How does the number of companies worked impact attrition?
```sql
SELECT NumCompaniesWorked, Attrition, COUNT(*) 
FROM employees
GROUP BY NumCompaniesWorked, Attrition;
```
✅ Employees who worked at more companies were more likely to leave.



### 15. Do employees with better work-life balance leave less?
```sql
SELECT WorkLifeBalance, Attrition, COUNT(*) 
FROM employees
GROUP BY WorkLifeBalance, Attrition;
```
✅ Those with poor work-life balance had higher attrition.

---



---

## 📎 Dataset Source

[IBM HR Analytics Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## 👤 Author

**Ricky Peña Jr.**  
🔗 [rickypenajr.github.io](https://rickypenajr.github.io)  
🐙 [GitHub](https://github.com/rickypenajr) • [LinkedIn](https://linkedin.com/in/rickypenajr)
