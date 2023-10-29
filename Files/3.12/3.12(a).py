# Question – 3.12:
#    (a)
#     X1 = Number of plates made per day
#     X2 = Number of mugs made per day
#     X3 = Number of steins made per day
#     X4 = Total daily production
#         MAX 2.50X1 + 3.25X2 + 3.90X3
#         S.T.
#         2X1 + 3X2 + 6X3 <= 1920 ((4)(8)(60) Molding min.)
#         8X1 + 12X2 + 14X3 <= 3840 ((8)(8)(60) Finishing min.)
#         X2 >= 150 (Minimum mugs)
#         -2X1 - 2X2 + X3 <= 0 (Steins <= 2(Plates + Mugs)
#         X1 + X2 + X3 - X4 = 0 (Total Definition)
#         X1 - .3X4 <= 0 (Plates <= 30% Total Produced)
#         All X's >= 0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.12(a)", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)

# Define the objective function
prob += 2.50*x1 + 3.25*x2 + 3.90*x3

# Define the constraints
#     2X1 + 3X2 + 6X3 <= 1920 ((4)(8)(60) Molding min.)
#     8X1 + 12X2 + 14X3 <= 3840 ((8)(8)(60) Finishing min.)
#     X2 >= 150 (Minimum mugs)
#     -2X1 - 2X2 + X3 <= 0 (Steins <= 2(Plates + Mugs)
#     X1 + X2 + X3 - X4 = 0 (Total Definition)
#     X1 - .3X4 <= 0 (Plates <= 30% Total Produced)
#     All X's >= 0

prob += 2*x1 + 3*x2 + 6*x3 <= 1920, "Molding_min_constraint"
prob += 8*x1 + 12*x2 + 14*x3 <= 3840, "Finishing_min_constraint"
prob += x2 >= 150, "Minimum_Mugs_constraint"
prob += -2*x1 - 2*x2 + x3 <= 0, "Steins<=2(Plates + Mugs)"
prob += x1 + x2 + x3 - x4 == 0, "Total_definition"
prob += x1 - 0.3*x4 <= 0, "Plates<=30%TotalProduced"

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