
""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""

## graph with titles

from matplotlib import pyplot as plt

x = ["math", "science", "language", "Urdu", "Python"]
y = [97, 87, 52, 42, 99]

plt.plot(x, y)
plt.xlabel("Courses")      # labeling x axis
plt.ylabel("Test Marks")# labeling y axis
plt.title("Test Scores")  # title
plt.show()
