import pandas as pd
import numpy as np

data = pd.read_csv('students.csv')
#print first 5 rows of the dataframe
print(data.head())
#print how many rows and columns are in the dataframe
print(data.shape)
#print basic information about the dataframe
print(data.info())

#pandas profiling - filtering and selected data

#print only marks and columns of the dataframe
print(data[['name', 'marks']].head())

#print only students who are from delhi
delhi_students = data[data['city'] == 'Delhi']

#print student who scored more than 80 marks
high_scorers = data[data['marks'] > 80]

#pandas - Handling missing data

#check rows with missing values
print(data.isnull())

#fill missing values with mean of the column
data['marks'].fillna(data['marks'].mean(), inplace=True)

# pandas - Grouping and summarizing data
# find the average marks of students from each city
print(data.groupby('city')['marks'].mean())

#find the highest marks scored by students from each city
print(data.groupby('city')['marks'].max())

#NUMPY BASICS - Fast array computations
marks_array = data['marks'].to_numpy()
#find the mean of marks using numpy
mean_marks = np.mean(marks_array)
print(f'Mean marks of students: {mean_marks}')

#find how many students scored above the mean marks
above_mean_count = np.sum(marks_array > mean_marks)
print(f'Number of students who scored above mean marks: {above_mean_count}')

# Create a new column called "result" in the data:
#          "Pass" if marks >= 60, else "Fail"
new_column = np.where(data['marks'] >= 60, 'Pass', 'Fail')
data['result'] = new_column

#print how many students passed and failed
result_counts = data['result'].value_counts()
print(f'Number of students who passed: {result_counts["Pass"]}')
print(f'Number of students who failed: {result_counts["Fail"]}')



