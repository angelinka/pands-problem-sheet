# Program displays a plot of the functions f(x)=x, g(x)=x**2 and h(x)=x**3 
# in the range [0, 4] on the one set of axes.
#Author: Angelina Belotserkovskaya

import matplotlib.pyplot as plt
import numpy as np 

#np.random.seed(1)
#assuming that the range should include 4, we increase the stop point by one
# as its exclusive by defenition. As start point defaults to 0 we can omit it
# and just say range(5) 
xpoints = np.array(range(5))

# customising font for the title
font1 = {'family':'serif','color':'blue','size':18}

fpoints = xpoints
gpoints = xpoints**2
hpoints = xpoints**3

# Adding plots
# customising the graphs by selecting color, line type and adding the label for legend: 
plt.plot(xpoints, fpoints, 'r', label = 'f(x)=x')
plt.plot(xpoints, gpoints, 'b', ls = ':', label = 'g(x)=x**2')
plt.plot(xpoints, hpoints, 'g', ls = '--', label = 'h(x)=x**3')

plt.title('Plots for functions: f(x)=x,\n g(x)=x**2 and h(x)=x**3', fontdict = font1)
plt.legend()
plt.show()


