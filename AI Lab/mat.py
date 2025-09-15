import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Science", "English", "History"]
marks = [85,90, 78, 88]

# Bar Chart
plt.bar(subjects, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Line Graph
plt.plot(subjects, marks, marker='o')
plt.title("Student Marks - Line Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
