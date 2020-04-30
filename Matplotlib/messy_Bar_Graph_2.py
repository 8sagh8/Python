
""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""

##  Overlapping Bar Graph 2 for two student values 

from matplotlib import pyplot as plt

#subject = ["math", "science", "language", "Urdu", "Python"]
subject = [1, 2, 3, 4, 5]
stud1 = [97, 87, 52, 42, 99]     #marks of student 1
stud2 = [77, 79, 89, 95, 55]     #marks of student 2

#some changes in as i
plt.bar([i+0.1 for i in subject], stud1, width=0.2, label = "sam")  # changing width
plt.bar([i-0.1 for i in subject], stud2, width=0.2, label = "zain")  # changing width of bar
 
plt.xlabel("Courses")      # labeling x axis
plt.ylabel("Test Marks")# labeling y axis
plt.title("Test Scores")  # title
plt.legend()  # legend function will show labels  in graph

plt.show()