import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Define a polynomial named 'f'
f = Polynomial([2.0, 1.0, -6.0, -2.0, 2.5, 1.0])

# Define the first derivative of polynomial 'f' named 'f_prime'
f_prime = f.deriv(1)

# Draw the X-axis
plt.axhline(y=0, color='k')

# Generate 100 values of x.
x = np.linspace(-2.5, 1.6, 100)

# Calculate y-values of corresponding x-values of f(x).
y = f(x)

# Plot the graph of f(x) using x-values and y-values
plt.plot(x, y)

# Plot the roots of the graph
plt.plot(f.roots(), f(f.roots()), 'ro')

# Print the roots of the function f(x)
print(f.roots())

# Calcuate y-values for corresponding x-values of f'(x).
y = f_prime(x)

# Plot the graph of f'(x)
plt.plot(x, y)

# Plot the roots of f'(x). Notice that, where f'(x) is zero the slop of f(x) is zero.
plt.plot(f_prime.roots(), f_prime(f_prime.roots()), 'bo')

# Print the roots of f'(x).
print(f_prime.roots())

# Start with an initial value
# Uncomment this line and set a value for xk
# try experimenting with different values
xk = 2


# Create a list for storing values of x's after each iteration
list_x = [xk, ]

# Create a list for storing values of f(x)'s after each iteration
list_f = [f(xk), ]

while True:
    #+--------------------+
    #| Start of your code |
    #+--------------------+

    # Calculate newer values of xk    
    

    # append xk into list_x
    

    # append f(xk) into list_f
    

    # Write the breaking condition



    #+------------------+
    #| End of your code |
    #+------------------+
    pass

df = pd.DataFrame({"x": list_x, "f(x)": list_f})
print(df)



####################


import matplotlib.pyplot as plt
from numpy import arange
from numpy import meshgrid

# Define a small value
delta = 0.01

# Create a set of x-values in the specified range with delta difference
# for example in this case the x values will be, -4.00, -3.99, -3.98, ... 4.99, 5.00 etc.
xrange = arange(-4, 5, delta)
yrange = arange(-3, 6, delta)

# Create a meshgrid (what is a meshgrid? it is basically co-ordinate matrix. you don't need to worry about this too much for this assignment)
# If you are interested take a look here: https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html
X, Y = meshgrid(xrange,yrange)

# Let's define two functions as F1 and F2
F1 = X*Y - Y**3 - 1
F2 = X**2*Y + Y - 5

# Draw the plots for F1 (red) and F2 (blue).
plt.contour(X, Y, (F1), [0], colors=['red'])
plt.contour(X, Y, (F2), [0], colors=['blue'])
plt.show()


###################


# These lines are included for beautification
from google.colab.output._publish import javascript
url = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js"
javascript(url=url)
# Don't worry about these lines

# import sympy
import sympy as sp
import math

# Defing x and y as mathematical symbols
vars = sp.symbols('x y')
x, y = vars

# Create an expression
expr1 = sp.sqrt(5 * x**3 + 1/x)
print("Expression 1:")
display(expr1)
print()
# We can substitute values like this
print(expr1.subs({x: 2*x}))

# Create another expression 
expr2 = x**y - sp.exp(x**2)
print("\nExpression 2:")
display(expr2)
print()
print(expr2.subs({x: 0.1, y:0.2}))

# We can also differentiate
expr3 = 4*x**3 - 3*x**2 + sp.sqrt(1+x**2)
print("\nExpression 3:")
display(expr3)
print("\nd/d(x) of expr3:") 
display(sp.diff(expr3))
print()

# Similarly we can also calculate partial derivative
expr4 = 4*x**3*y**2 - 3*x**2*y**3 + (sp.sqrt(1+x**2+y**2))
print("\nExpression 4:")
display(expr4)
print("\nd/d(x) of expr4:") 
display(sp.diff(expr4, x))
print()
print("\nd/d(y) of expr4:") 
display(sp.diff(expr4, y))
print()




######################
#code below

import numpy as np
import sympy as sp

# Define x and y as mathematical symbols
vars = sp.symbols('x y')
x, y = vars

# Define the functions 
f = sp.Matrix([x*y - y**3 - 1, x**2 * y + y - 5])

# Initialise Jacobian matrix
J = sp.zeros(len(f),len(vars))

# Fill Jacobian matrix with entries
for i, fi in enumerate(f):
    for j, s in enumerate(vars):
        J[i,j] = sp.diff(fi, s)

print(J)
# Find the inverse of Jacobian Matrix
J_inv = sp.Matrix.inv(J)
print(J_inv)

# Initialize solution s with starting value x_0 = 2.0 and y_0 = 3.0
s = sp.Matrix([
    2.0,
    3.0
])

# Make a dictionary using the initial values
dictionary = {
    x: s[0],
    y: s[1]
}

# calculate f(s_k) using initial values
f_sk = f.subs(dictionary)

# Start iterating using while loop
i = 0
while i<10:
    # Calculate value of inverse jacobian, j^-1(sk), j_val
    # j_val = ??


    # Calculate the new value of s using iterative formula
    # s = ??


    # Update the dictionary using newer values
    # dictionary = ??





    # Update f(s_k) using newer values of s_k
    # f_sk = ??





    print(s)
    i += 1

print()