
""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""


## simple Bar Graph for single value
from matplotlib import pyplot as plt

subject = ["math", "science", "language", "Urdu", "Python"]
stud1 = [97, 87, 52, 42, 99]     #marks of student 1

plt.bar(subject, stud1, label = "sam")  # .bar will use to draw bar graph
 
plt.xlabel("Courses")      # labeling x axis
plt.ylabel("Test Marks")# labeling y axis
plt.title("Test Scores")  # title
plt.legend()  # legend function will show labels  in graph

plt.show()