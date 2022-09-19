import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


zs = np.loadtxt('stm.txt')
ny,nx = zs.shape  #forces ny and nx to have the same dimensions as zs so that the plot surface command will work
xs = np.arange(nx) #creates a horizontal array for the xs
ys = np.arange(ny)[:,np.newaxis] # creates a vertical array for the ys
my_graph = plt.axes(projection='3d') #this creates the 3d set of axis's
my_graph.set_xlabel("x-axis") # the next 3 lines are just labeling
my_graph.set_ylabel("y-axis")
my_graph.set_title("STM of the surface of silicon")
my_graph.plot_surface(xs,ys,zs, edgecolor = 'none', cmap = plt.cm.jet )# this createsand colors the surface
fig = cm.ScalarMappable(cmap=cm.jet) #the next 2 lines creates a colorbar so that it is easier to interpret
plt.colorbar(fig)
plt.show()