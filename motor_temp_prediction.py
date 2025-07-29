import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = {
    'Voltage': np.random.uniform(220, 240, 100),
    'Current': np.random.uniform(5, 15, 100),
    'Ambient_Temp': np.random.uniform(20, 40, 100),
    'Motor_Temperature': np.random.uniform(60, 100, 100)  # Target variable
}
df = pd.DataFrame(data)
print(df.head())
print(df.describe())
X = df[['Voltage', 'Current', 'Ambient_Temp']]
y = df['Motor_Temperature']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R² Score:", r2)
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel('Actual Temperature')
plt.ylabel('Predicted Temperature')
plt.title('Actual vs Predicted Motor Temperature')
plt.plot([60, 100], [60, 100], 'r--')
plt.grid(True)
plt.show()