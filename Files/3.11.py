# Question – 3.11:
# X1 = Number of refrigerator/ovens produced
# X2 = Number of French fry makers produced
# X3 = Number of French toast makers produced
#     MIN 140X1 + 50X2 + 36X3
#     S.T.
#     100X1 + 35X2 + 27X3  2,000,000 (Min Profit)
#     X1 >= 5,000 (Min Refrig/oven)
#     X2 >= 4,000 (Min French fry maker)
#     X3 >= 2,300 (Min French toast maker)
#     X1 <= 15,000 (Max Refrig/oven)
#     X2 <= 15,000 (Max French fry maker)
#     X3 <= 15,000 (Max French toast maker)
#     All X's >= 0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.11", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)

# Define the objective function
prob += 140*x1 + 50*x2 + 36*x3

# Define the constraints
#     100X1 + 35X2 + 27X3 >= 2,000,000 (Min Profit)
#     X1 >= 5,000 (Min Refrig/oven)
#     X2 >= 4,000 (Min French fry maker)
#     X3 >= 2,300 (Min French toast maker)
#     X1 <= 15,000 (Max Refrig/oven)
#     X2 <= 15,000 (Max French fry maker)
#     X3 <= 15,000 (Max French toast maker)

prob += 100*x1 + 35*x2 + 27*x3 >= 2000000, "MinProfit_constraint"
prob += x1 >= 5000, "Min_Refrig/oven_constraint"
prob += x2 >= 4000, "(Min_French_fry_maker_constraint"
prob += x3 >= 2300, "(Min_French_toast_maker_constraint"

prob += x1 <= 15000, "Max_Refrig/oven_constraint"
prob += x2 <= 15000, "(Max_French_fry_maker_constraint"
prob += x3 <= 15000, "(Max_French_toast_maker_constraint"

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