
-- 1. Attrition rate by department
SELECT Department, 
       ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS AttritionRate
FROM employees
GROUP BY Department;

-- 2. Average monthly income by job role
SELECT JobRole, ROUND(AVG(MonthlyIncome), 2) AS AvgIncome
FROM employees
GROUP BY JobRole;

-- 3. Count of employees by attrition status
SELECT Attrition, COUNT(*) AS Count
FROM employees
GROUP BY Attrition;

-- 4. Job satisfaction average per department
SELECT Department, ROUND(AVG(JobSatisfaction), 2) AS AvgSatisfaction
FROM employees
GROUP BY Department;

-- 5. Average years at company for attrited vs retained employees
SELECT Attrition, ROUND(AVG(YearsAtCompany), 2) AS AvgYearsAtCompany
FROM employees
GROUP BY Attrition;

-- 6. Overtime distribution among attrited employees
SELECT OverTime, COUNT(*) AS Count
FROM employees
WHERE Attrition = 'Yes'
GROUP BY OverTime;

-- 7. Employees with > 5 years in current role
SELECT * FROM employees
WHERE YearsInCurrentRole > 5;

-- 8. Employees who have never done overtime
SELECT * FROM employees
WHERE OverTime = 'No';

-- 9. Distribution of income ranges
SELECT 
    CASE 
        WHEN MonthlyIncome < 3000 THEN 'Low'
        WHEN MonthlyIncome BETWEEN 3000 AND 6000 THEN 'Medium'
        ELSE 'High'
    END AS IncomeGroup,
    COUNT(*) AS Count
FROM employees
GROUP BY IncomeGroup;

-- 10. Average satisfaction by overtime status
SELECT OverTime, ROUND(AVG(JobSatisfaction), 2) AS AvgSatisfaction
FROM employees
GROUP BY OverTime;
