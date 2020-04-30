""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""

##  Scatter Plot
"""
Scatterplot is a type of data display that shows the relationship
between two numerical variables
"""

from matplotlib import pyplot as plt

#subject = ["math", "science", "language", "Urdu", "Python"]
subject = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stud1 = [97, 87, 52, 42, 99, 50, 99, 14, 25, 55]     #marks of student 1
stud2 = [79, 71, 25, 62, 85, 89, 91, 61, 75, 81]     #marks of student 2

plt.scatter(subject, stud1, label = "sam", color = "#00f", marker = "*", s = 200) # marker by defauld is circle but we can change & s is for size can be changed too
plt.scatter(subject, stud2, label = "zain", color = "#f00")

plt.xlabel("Marks")      # labeling x axis
plt.ylabel("Number of tests")# labeling y axis
plt.title("Test Scores")  # title
plt.legend()

plt.show()
