from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x_data = [[1,2,1,1],[2,1,3,2],[3,1,3,4],[4,1,5,5],[1,7,5,5],[1,2,5,6],[1,6,6,6],[1,7,7,7]]
y_data = [[0,0,1],[0,0,1],[0,0,1],[0,1,0],[0,1,0],[0,1,0],[1,0,0],[1,0,0,]]
color = ['r','g','b']
label = ['x','^','o']
def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
# Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

for i in range(0,len(x_data)):
     x=x_data[i][0]
     y=x_data[i][1]
     z=-1
     for j in range(0,len(y_data[i])):     
          if y_data[i][j] == 1:
               z=j
     c=color[z]
     m=label[z]
     ax.scatter(x, y, z, c=c, marker=m)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

