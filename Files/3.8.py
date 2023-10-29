# Question – 3.8:
# X1 = the number of Delta assemblies produced daily
# X2 = the number of Omega assemblies produced daily
# X3 = the number of Theta assemblies produced daily
#     MAX 800X1 + 900X2 + 600X3
#     S.T.
#     X1 + X2 + X3 <= 7 (X70686 chips)
#     2X1 + X2 + X3 <= 8 (Production hours)
#     80X1 + 160X2 + 80X3 <= 480 (Quality minutes)
# All X's >= 0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.8", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)

# Define the objective function
prob += 800*x1 + 900*x2 + 600*x3

# Define the constraints
#     X1 + X2 + X3 <= 7 (X70686 chips)
#     2X1 + X2 + X3 <= 8 (Production hours)
#     80X1 + 160X2 + 80X3 <= 480 (Quality minutes)

prob += x1 + x2 + x3 <= 7, "X70686_chips_constraint"
prob += 2*x1 + x2 + x3 <= 8, "Production_hours_constraint"
prob += 80*x1 + 160*x2 + 80*x3 <= 480, "Quality_mins_constraint"

# Solve the linear programming problem
prob.solve()

# Print the results 1

print ("Status: ", LpStatus[prob.status])

for v in prob.variables():
    print(v.name + "=" + str(v.varValue) +"\tReduced cost = "+ str(v.dj))
print ("The optimal value of the objective function is = ", value(prob.objective))

print("Senstivity Analysis\n Constraints\t\t\t      ShadowPrice \t    Slack")

for name , c in prob.constraints.items():
    print(name  , c , "\t  " , c.pi , "\t\t" ,c.slack)