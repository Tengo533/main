
import matplotlib.pyplot as plt 
title = "Height Histogram (cm)"
heights = [150, 153, 157, 157, 158, 159, 160, 161, 161, 161, 163, 165, 166, 166, 167, 169, 171, 175]
bins = 6
plt.hist(heights,bins, facecolor="green")
plt.show()