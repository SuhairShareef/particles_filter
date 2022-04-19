import matplotlib.pyplot as plt
import numpy as np
import random
 
plt.rcParams["figure.figsize"] = [20.00, 3.50]
plt.rcParams["figure.autolayout"] = True
# 100 linearly spaced numbers
x = np.arange(0, 10, 0.001)

# the function, which is y=cosθ+1/2*cos(3*θ+0.23) +1/2*cos(5*θ−0.4)+1/2*cos(7*θ+2.09)+1/2*cos(9*θ−3)
y = np.cos(x) + 0.5 * np.cos(3 * x + 0.23) + 0.5 * np.cos(5 * x -
                                                          0.4) + 0.5 * np.cos(7 * x + 2.09) + 0.5 * np.cos(9 * x - 3)

# setting the axes at the centre
fig = plt.figure()
plt.ylim(-3, 5)
plt.xlim(0, 10)
plt.margins(x=1, y=0)
plt.grid()
#plt.scatter(x, y)
plt.xticks(np.arange(10, step=1))
plt.plot(x, y, 'b')
positions = [i/10 for i in range(100)]
y = []
for i in range(100):
    y.append(random.uniform(3, 3.1))

plt.margins(x=1, y=0)
plt.scatter(positions, y, marker="o")


# show the plot
plt.show()
