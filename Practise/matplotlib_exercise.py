import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('students.csv')

#bar chart for average marks of students
average_marks = data.groupby('city')['marks'].mean()

#bar chart bnao
plt.bar(average_marks.index, average_marks.values)
plt.title('Average Marks of Students by City')
plt.xlabel('City')
plt.ylabel('Average Marks')
plt.show()

#line chart for marks of students
plt.plot(data['name'], data['marks'])
plt.title('Marks of Students')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.xticks(rotation=45)
plt.show()

#histogram for marks distribution
plt.hist(data['marks'], bins=10, edgecolor='black')
plt.title('Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()

#scatter plot for marks vs age
plt.scatter(data['age'], data['marks'])
plt.title('Marks vs Age of Students')
plt.xlabel('Age')
plt.ylabel('Marks')
plt.show()

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
#bar chart for average marks of students
average_marks = data.groupby('city')['marks'].mean()
axs[0, 0].bar(average_marks.index, average_marks.values)
axs[0, 0].set_title('Average Marks of Students by City')


axs[0, 1].hist(data['marks'], bins=10, edgecolor='black')
axs[0, 1].set_title("Marks Distribution")


axs[1, 0].scatter(data["attendance"], data["marks"])
axs[1, 0].set_title("Attendance vs Marks")
 
axs[1, 1].plot(data["name"], data["marks"])
axs[1, 1].set_title("Student Marks")
axs[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()  
plt.show()


