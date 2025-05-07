
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/employee_data.csv')

# Plot attrition by department
sns.countplot(data=df, x='Department', hue='Attrition')
plt.title('Attrition Count by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('attrition_by_department.png')
plt.show()
