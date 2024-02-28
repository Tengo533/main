import matplotlib.pyplot as plt
title_txt = "Programming Language Popularity"
seg_labels = ("C", "Java", "Python", "C++", "SQL", "Other")
seg_sizes = [14.3, 11.2, 11.0, 7.1, 1.8, 54.6]
exp_seg = ""

plt.pie(seg_sizes, seg_labels, explode=seg_labels, shadow=True,)
plt.show()