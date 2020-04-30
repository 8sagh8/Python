""" 
Matplotlib is a Python 2D plotting library which produces publication quality
figures in a variety of hardcopy formats. 
It is for data visualization, it can be used in python scripts
can generate plots, histograms, power spectra, bar charts, pie charts, error charts, etc

Matplotlib is a sponsered project of NumFOCUS 
Matplotlib is hosted on GitHub
"""

##  Stack Plot
"""
Stack plot is a plot that shows the whole data set with easy easy visualization
of how each part makes up the whole.

Each constituent of the stack plot is stacked on top of each other. it shows the part
makeup of the unit, as well as the whole
"""

from matplotlib import pyplot as plt

days = [1,2,3,4,5,6,7]

sleeping = [8,7,6,7,5,4,9]
study = [4,2,6,1,3,5,5]
workout = [1,2,1,1,2,3,1]
phone=[5,3,2,4,1,3,4]
other=[6,10,9,11,13,9,5]

lbls = ["sleeping", "study", "workout", "phone", "other"] #labels list
clrs = ["m", "c", "r", "k", "b"] #colors list

plt.stackplot(days, sleeping, study, workout, phone, other, labels = lbls, colors = clrs)

plt.xlabel("Days")      # labeling x axis
plt.ylabel("Activities")# labeling y axis
plt.title("Daily Routine")  # title
plt.legend()

plt.show()
