import csv
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
x = []
y = []
z = []

with open('image2_test.txt', mode = 'r')as file:
      csvFile = csv.reader(file, delimiter =',')
    
      for lines in csvFile:
          x.append('x')
          y.append('y')
          z.append('z')
          
plt.scatter(x,y,z)
plt.show()


