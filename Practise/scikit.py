import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error

#data load or tyaar krna
data = pd.read_csv('students.csv')

data['marks'] = data['marks'].fillna(data['marks'].mean())
data['attendance'] = data['attendance'].fillna(data['attendance'].mean())

# result column bnao - agar marks >= 60 toh "Pass", nahi toh "Fail"
data['result'] = np.where(data['marks'] >= 60, 'Pass', 'Fail')
#print krna hai 
print(data[['marks', 'attendance', 'result']])

#feature x or target y define krna
x = data[['marks', 'attendance']]
y = data['result']

#train test split krna
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("\nTraining data size:", len(x_train))
print("Testing data size:", len(x_test))

#model bnao aur train krna
model = LogisticRegression()
model.fit(x_train, y_train)

#prediction krna
predictions = model.predict(x_test)
print("\nPredictions:", list(predictions))
print("Actual:     ", list(y_test))

#accuracy check krna 
accuracy = accuracy_score(y_test, predictions)
print("\nAccuracy:", accuracy)

