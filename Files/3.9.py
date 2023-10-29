# Question – 3.9:
# X1 = the number in group I contacted by telephone
# X2 = the number in group II contacted by telephone
# X3 = the number in group III contacted by telephone
# X4 = the number in group IV contacted by telephone
# X5 = the number in group I contacted in person
# X6 = the number in group II contacted in person
# X7 = the number in group III contacted in person
# X8 = the number in group IV contacted in person
#
# MIN 15X1 + 12X2 + 20X3 + 18X4 + 35X5 + 30X6 + 50X7 + 40X8
# S.T.
#     X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 = 2000 (Total)
#     X1 + X2 + X5 + X6 >= 1000 (W&R)
#     X5 + X6 + X7 + X8 >= 500 (In person)
#     -.5X1 + .5X5 >= 0 (W&R,ip)
#     X2 + X4 + X6 + X8 <= 800(Small)
#     - .25X2 - .25X4+ .75X6 + .75X8 <= 0 (Small,ip)
#     X1 + X5 >= 200 (Min I)
#     X2 + X6 >= 200 (Min II)
#     X3 + X7 >= 200 (Min III)
#     X4 + X8 >= 200 (Min IV)
#     X1 + X5 <= 1000 (Max I)
#     X2 + X6 <= 1000 (Max II)
#     X3 + X7 <= 1000 (Max III)
#     X4 + X8 <= 1000 (Max IV)
#
# All X's >= 0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.9", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
x5 = LpVariable("x5", 0)
x6 = LpVariable("x6", 0)
x7 = LpVariable("x7", 0)
x8 = LpVariable("x8", 0)


# Define the objective function
prob += 15*x1 + 12*x2 + 20*x3 + 18*x4 + 35*x5 + 30*x6 + 50*x7 + 40*x8

# Define the constraints
#     X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 = 2000 (Total)
#     X1 + X2 + X5 + X6 >= 1000 (W&R)
#     X5 + X6 + X7 + X8 >= 500 (In person)
#     -.5X1 + .5X5 >= 0 (W&R,ip)
#     X2 + X4 + X6 + X8 <= 800(Small)
#     - .25X2 - .25X4+ .75X6 + .75X8 <= 0 (Small,ip)
#     X1 + X5 >= 200 (Min I)
#     X2 + X6 >= 200 (Min II)
#     X3 + X7 >= 200 (Min III)
#     X4 + X8 >= 200 (Min IV)
#     X1 + X5 <= 1000 (Max I)
#     X2 + X6 <= 1000 (Max II)
#     X3 + X7 <= 1000 (Max III)
#     X4 + X8 <= 1000 (Max IV)
prob += x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 == 2000, "Total"
prob += x1 + x2 + x5 + x6 >= 1000, "W&R_constraint"
prob += x5 + x6 + x7 + x8 >= 500, "In_Person"
prob += -0.5*x1 + 0.5*x5 >= 0, "W&R.ip_constraint"
prob += x2 + x4 + x6 + x8 <= 800, "Small_constraint"
prob += -0.25*x2 - 0.25*x4 + 0.75*x6 + 0.75*x8 <= 0, "Small.ip_constraint"
prob += x1 + x5 >= 200, "MinI_constraint"
prob += x2 + x6 >= 200, "MinII_constraint"
prob += x3 + x7 >= 200, "MinIII_constraint"
prob += x4 + x8 >= 200, "MinIV_constraint"
prob += x1 + x5 <= 1000, "MaxI_constraint"
prob += x2 + x6 <= 1000, "MaxII_constraint"
prob += x3 + x7 <= 1000, "MaxIII_constraint"
prob += x4 + x8 <= 1000, "MaxIV_constraint"



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