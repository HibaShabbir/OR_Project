# Question - 3.4
# X1 = amount invested in EAL stock
# X2 = amount invested in BRU stock
# X3 = amount invested in TAT stock
# X4 = amount invested in long term bonds
# X5 = amount invested in short term bonds
# X6 = amount invested in the tax deferred annuity
# X7 = the total amount invested in stocks only
#     MAX .15X1 + .12 X2 + .09X3 + .11X4 + .085X5 + .06X6
#     S.T.
#     X1 + X2 + X3 + X4 + X5 + X6 = 50,000 (Total)
#     X6                          >= 10,000 (TDA)
#     X1 + X2 + X3 - X7            = 0 (Stocks)
#     X3 -.25X7                   >= 0 (Min TAT)
#     X4 + X5 - X7                >= 0(Bond  stock)
#     X3 + X5 + X6                <= 12,500 (Low %)
#
#     All X's >= 0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.4", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
x5 = LpVariable("x5", 0)
x6 = LpVariable("x6", 0)
x7 = LpVariable("x7", 0)

# Define the objective function
prob += 0.15*x1 + 0.12*x2 + 0.09*x3 + 0.11*x4 + 0.085*x5 + 0.06*x6

# Define the constraints
#     X1 + X2 + X3 + X4 + X5 + X6 = 50,000 (Total)
#     X6                          >= 10,000 (TDA)
#     X1 + X2 + X3 - X7            = 0 (Stocks)
#     X3 -.25X7                   >= 0 (Min TAT)
#     X4 + X5 - X7                >= 0(Bond >= stock)
#     X3 + X5 + X6                <= 12,500 (Low %)

prob += x1 + x2 + x3 + x4 + x5 + x6 == 50000, "Total"
prob += x6 >= 10000, "TDA"
prob += x1 + x2 + x3 - x7 == 0, "Stocks"
prob += x3 - .25*x7 >= 0, "Min_TAT"
prob += x4 + x5 - x7 >= 0, "Bond_constraint"
prob += x3 + x5 + x6 <= 12500, "Low%_constraint"


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