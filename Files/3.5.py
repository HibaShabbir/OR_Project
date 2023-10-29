# Question – 3.5:
#
# Unit Profit
#
#     X1 = Number of full comforters produced daily 19-3(.50)-55(.20) = 6.50
#     X2 = Number of queen comforters produced daily 26-4(.50)-75(.20) = 9.00
#     X3 = Number of king comforters produced daily 32-6(.50)-95(.20) = 10.00
#     MAX 6.50X1 + 9.00X2 + 10.00X3
#     S.T.
#     3X1 + 4X2 + 6X3 <= 2,700 (Stuffing)
#     55X1 + 75X2 + 95X3 <= 48,000 (Fabric)
#     3X1 + 5X2 + 6X3 <= 3,000 (Cutting minutes)
#     5X1 + 6X2 + 8X3 <= 12,000 (Sewing minutes)
#
#     All X's >= 120

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.5", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 120)
x2 = LpVariable("x2", 120)
x3 = LpVariable("x3", 120)

# Define the objective function
prob += 6.50*x1 + 9.00*x2 + 10.00*x3

# Define the constraints
#     3X1 + 4X2 + 6X3 <= 2,700 (Stuffing)
#     55X1 + 75X2 + 95X3 <= 48,000 (Fabric)
#     3X1 + 5X2 + 6X3 <= 3,000 (Cutting minutes)
#     5X1 + 6X2 + 8X3 <= 12,000 (Sewing minutes)

prob += 3*x1 + 4*x2 + 6*x3 <= 2700, "Stuffing_constraint"
prob += 55*x1 + 75*x2 + 95*x3 <= 48000, "Fabric_constraint"
prob += 3*x1 + 5*x2 + 6*x3 <= 3000, "Cutting__minutes_constraint"
prob += 5*x1 + 6*x2 + 8*x3 <= 12000, "Sewing_minutes_constraint"


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