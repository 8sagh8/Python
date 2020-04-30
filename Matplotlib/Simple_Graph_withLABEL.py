
""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""

## graph with labels

from matplotlib import pyplot as plt

"""
x = ["math", "science", "language", "Urdu", "Python"]
y = [97, 87, 52, 42, 99]

plt.plot(x, y)
plt.xlabel("Courses")      # labeling x axis
plt.ylabel("Test Marks")# labeling y axis

plt.show()
"""

"""
## graph with titles

subject = ["math", "science", "language", "Urdu", "Python"]
stud1 = [97, 87, 52, 42, 99]     #marks of student 1
stud2 = [77, 79, 89, 95, 55]     #marks of student 2

plt.plot(subject, stud1, label = "sam")  # label will mark label with marks line
plt.plot(subject, stud2, label = "zain")  # label will mark student 2 name with mark line
 
plt.xlabel("Courses")      # labeling x axis
plt.ylabel("Test Marks")# labeling y axis
plt.title("Test Scores")  # title
plt.legend()  # legend function will show labels  in graph

plt.show()
"""