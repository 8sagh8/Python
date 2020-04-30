""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""
from matplotlib import pyplot as plt
import csv

tests=[]
marks=[]

with open ("data.txt", 'r') as file:
    plots=csv.reader(file, delimiter=",")
    for row in plots:
        tests.append(int(row[0]))
        marks.append(int(row[1]))

plt.plot(tests, marks, label = "Load from file")
plt.title("Display File Data")
plt.show()
