#!/usr/local/bin/python3

import matplotlib.pyplot as plt
#plt.plot([1,2,3,4])
plt.plot([1,2,3,4],[1,4,9,16],'ro')
"""
The axis() command in the example above takes a list of 
[xmin, xmax, ymin, ymax] and specifies the viewport of the axes.
"""
plt.axis([0,6,0,20])
plt.show()

