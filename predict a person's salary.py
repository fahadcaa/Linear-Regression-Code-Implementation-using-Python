Linear Regression: Code Implementation using Python 🧠💻

🔸 Problem Statement:  
We want to predict a person's salary based on their years of experience using Simple Linear Regression.

🔹 Sample Data:  
Experience – Salary  
1 Year – 30,000  
2 Years – 35,000  
3 Years – 40,000  
4 Years – 45,000  
5 Years – 50,000  

🔹 Python Code:  
``` 
import pandas as pd  
from sklearn.linear_model import LinearRegression  
import matplotlib.pyplot as plt  

data = {'Experience': [1, 2, 3, 4, 5],  
        'Salary': [30000, 35000, 40000, 45000, 50000]}  
df = pd.DataFrame(data)

X = df[['Experience']]  
y = df['Salary']

model = LinearRegression()  
model.fit(X, y)

pred = model.predict([[6]])  
print(f"Predicted Salary: pred[0]:.2f")

plt.scatter(X, y, color='blue')  
plt.plot(X, model.predict(X), color='red')  
plt.xlabel('Experience (Years)')  
plt.ylabel('Salary')  
plt.title('Experience vs Salary')  
plt.show()
“`

🔹 Output:  
Predicted Salary for 6 years of experience → 55,000
