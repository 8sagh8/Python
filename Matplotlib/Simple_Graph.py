""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""

## simple graph

from matplotlib import pyplot as ppt


x = ["Maths", "English", "Python"]
y = [97, 87, 52]

ppt.plot(x, y)
ppt.show()