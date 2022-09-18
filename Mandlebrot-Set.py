import numpy as np
import matplotlib.pyplot as plt

nmax = 20
N = 500
region = np.zeros([N, N])
xs = np.linspace(-2, 1, N)
ys = np.linspace(-1.5, 1.5, N)
count = 0
""" the code above the comment is just all the varibles that create the values i use for the mandlebrot and creates an array of zeros that i will store the values in so i can create a density plot of the set."""
for i in range(N):
    """i create two sets of values 'xn' and 'X' in this for loop because later on i will be storing xn in the tuple and if i only use xn the program gets confused and starts to use vaules from the equation instead of just the values in the array"""
    for j in range(N):
        """the same thing happens here so i had to create two variables of 'yn' and 'Y' i also recall count = 0 here because i want to make sure that everytime the while loop is run that it starts with the correct count value after incrementing up"""
        count = 0
        xn = xs[i]
        X = xs[i]
        yn = ys[j]
        Y = ys[j]
        while count < nmax:
            """this is the conditional statment tests to see if the value X and Y belong in the set or if it does not"""

            """this allows the program to run through all the values of the xs and ys to test if they are in the set or out of the set and once the if state ment is done the program increments to the nmax value and the restarts the for loop"""
            if xn ** 2 + yn ** 2 < 4:
                """this tells the array to set the value of the array equal to zero and then the that number from X and Y are in the set"""
                xn, yn = ((xn ** 2) - (yn ** 2)) + X, (2 * xn * yn) + Y
                X = xs[i]
                Y = ys[j]

            else:
                region[i, j] = count
                break

            count += 1
plt.imshow(region, origin='lower')
plt.colorbar()