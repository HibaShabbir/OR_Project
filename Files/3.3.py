# # Question – 3.3:
#     X1 = the number of standard Z345’s produced weekly
#     X2 = the number of industrial Z345’s produced weekly
#     X3 = the number of standard W250’s produced weekly
#     X4 = the number of industrial W250’s produced weekly
#     X5 = the total number of products produced weekly
#
#     MAX 400X1 + 560X2 + 560X3 + 700X4
#     S.T.
#     25X1 + 46X2 + 16X3 + 34X4 <= 2500 (zinc)
#     50X1 + 30X2 + 28X3 + 12X4 <= 2800 (iron)
#     X1 + X2                   >= 20 (Min Z345’s)
#     X1 + X2 + X3 + X4 - X5    = 0 (X5 definition)
#     X2 + X4 - .50X5           >= 0 (Industrial min.)
#     X1 + X2 - .75X5           <= 0 (Max Z345’s)
#     X3 + X4 - .75X5           <= 0 (Max W250’s)
#
# X1, X2, X3, X4, X5 >= 0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.3", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
x5 = LpVariable("x5", 0)

# Define the objective function
prob += 400*x1 + 560*x2 + 560*x3 + 700*x4 + 0*x5

# Define the constraints
#     25X1 + 46X2 + 16X3 + 34X4 <= 2500 (zinc)
#     50X1 + 30X2 + 28X3 + 12X4 <= 2800 (iron)
#     X1 + X2                   >= 20 (Min Z345’s)
#     X1 + X2 + X3 + X4 - X5    = 0 (X5 definition)
#     X2 + X4 - .50X5           >= 0 (Industrial min.)
#     X1 + X2 - .75X5           <= 0 (Max Z345’s)
#     X3 + X4 - .75X5           <= 0 (Max W250’s)

# x1 + x2 + x3 + x4 - x5 = 0 , "X5 definition"
prob += 25*x1 + 46*x2 + 16*x3 + 34*x4 <= 2500, "zinc_constraint"
prob += 50*x1 + 30*x2 + 28*x3 + 12*x4 <= 2800, "iron_constraint"
prob += x1 + x2 >= 20, "Min_Z345_constraint"
prob += x1 + x2 + x3 + x4 - x5 == 0 , "X5 definition"
prob += x2 + x4 - .50*x5 >= 0 , "Industrial_min"
prob += x1 + x2 - .75*x5 <= 0 , "Max_Z345_constraint"
prob += x3 + x4 - 0.75*x5 <= 0, "Max_W250_constraint"


# Solve the linear programming problem
prob.solve()

# Print the results 1

print ("Status: ", LpStatus[prob.status])

for v in prob.variables():
    print(v.name + "=" + str(v.varValue) +"\tReduced cost = "+ str(v.dj))
print("objective function = " + str(value(prob.objective)))

print("Senstivity Analysis\n Constraints\t\t\t      ShadowPrice \t    Slack")

for name , c in prob.constraints.items():
    print(name  , c , "\t  " , c.pi , "\t\t" ,c.slack)
