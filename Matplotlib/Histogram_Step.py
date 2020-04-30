""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""

##  Histogram in steps
#histogram is a bar graph of raw data that creates a picture of the data distribution

from matplotlib import pyplot as plt

#subject = ["math", "science", "language", "Urdu", "Python"]
subject = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stud1 = [97, 87, 52, 42, 99, 50, 99, 14, 25, 55]     #marks of student 1

bins = [0, 20, 40, 60, 80, 100]  # making groups to see how many scores falls in it
plt.hist(stud1, bins, histtype = "step", rwidth = 1, color = "#02f5ff") #type is imp, now we want histogram in step

plt.xlabel("Marks")      # labeling x axis
plt.ylabel("Number of tests")# labeling y axis
plt.title("Test Scores")  # title

plt.show()
