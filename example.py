from isfread import isfread
import matplotlib.pyplot as plt

x, y, head = isfread("isf_file_to_plot.isf")
print head

plt.plot(x, y)
plt.show()
