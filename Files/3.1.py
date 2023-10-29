# Question  3.1:
#     X1 = Number of 20-inch girls bicycles produced this week
#     X2 = Number of 20-inch boys bicycles produced this week
#     X3 = Number of 26-inch girls bicycles produced this week
#     X4 = Number of 26-inch boys bicycles produced this week
#
#     MAX 27X1 + 32X2 + 38X3 + 51X4
#     S.T.
#         X1          + X3        >= 200 (Min girls models)
#                  X2       +  X4 >= 200 (Min boys models)
#         12X1 + 12X2 + 9X3 + 9X4 <= 4800 (Production minutes)
#         6X1 + 9X2 + 12X3  + 18X4 <= 4800 (Assembly minutes)
#         2X1 + 2X2               <= 500 (20-inch tires)
#                      2X3 + 2X4  <= 800 (26-inch tires)
#         All X's >= 0
from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.1", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)

# Define the objective function
prob += 27*x1 + 32*x2 + 38*x3 + 51*x4

# Define the constraints
prob += x1 + x3 >= 200, "1st_constraint"
prob += x2 + x4 >= 200, "2nd_constraint"
prob += 12*x1 + 12*x2 + 9*x3 + 9*x4 <= 4800, "3rd_constraint"
prob += 6*x1 + 9*x2 + 12*x3 + 18*x4 <= 4800, "4th_constraint"
prob += 2*x1 + 2*x2 <= 500, "5th_constraint"
prob += 2*x3 + 2*x4 <= 800, "6th_constraint"


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

# Plot the optimal solution
# x = np.arange(0, 4)
# plt.plot(x, 200 - x, label = 'x1 + x3 >= 200')
# plt.plot(x, 4 - 2 * x, label= 'x2 + x4 >= 200')
# plt.plot(x, 6 - 3 * x, label = '12x1 + 12x2 +9x3 +9x4 <= 4800')
# plt.plot(x, 6 - 3 * x, label = '6x1 + 9x2 +12x3 +18x4 <= 4800')
# plt.plot(x, 2.5 - x, label = '2x1 + 2x2 <= 500')
# plt.plot(x, 4 - 2 * x, label= '2x3 + 2x4 <= 800')
#
# plt.axis([0, 3, 0, 6])
# plt.grid(True)
# plt.legend()
# plt.show()