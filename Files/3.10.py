# Question – 3.10:
# X1 = the number of ounces of Multigrain Cheerios in the mixture
# X2 = the number of ounces of Grape Nuts in the mixture
# X3 = the number of ounces of Product 19 in the mixture
# X4 = the number of ounces of Frosted Bran in the mixture
# X5 = the total number of ounces in the mixture
#     MIN 12X1 + 9X2 + 9X3 + 15X4
#     S.T.
#     30X1 + 30X2 + 20X3 + 20X4 >= 50 (Vitamin A)
#     25X1 + 2X2 + 100X3 + 25X4 >= 50 (Vitamin C)
#     25X1 + 25X2 + 25X3 + 25X4 >= 50 (Vitamin D)
#     25X1 + 25X2 + 100X3 + 25X4 >= 50 (Vitamin B6)
#     45X1 + 45X2 + 100X3 + 25X4 >= 50 (Iron)
#     X1 + X2 + X3 + X4 - X5 = 0 (Total)
#     X1 - .1X5 >= 0 ( 10% M/G Cheerios)
#     X2 - .1X5 >= 0 ( 10% Grape Nuts)
#     X3 - .1X5 >= 0 ( 10% Product 19)
#     X4 - .1X5 >= 0 ( 10% Frosted Bran)
#
# All X's >= 0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.10", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
x5 = LpVariable("x5", 0)

# Define the objective function
prob += 12*x1 + 9*x2 + 9*x3 + 15*x4 + 0*x5

# Define the constraints
#     30X1 + 30X2 + 20X3 + 20X4 >= 50 (Vitamin A)
#     25X1 + 2X2 + 100X3 + 25X4 >= 50 (Vitamin C)
#     25X1 + 25X2 + 25X3 + 25X4 >= 50 (Vitamin D)
#     25X1 + 25X2 + 100X3 + 25X4 >= 50 (Vitamin B6)
#     45X1 + 45X2 + 100X3 + 25X4 >= 50 (Iron)
#     X1 + X2 + X3 + X4 - X5 = 0 (Total)
#     X1 - .1X5 >= 0 ( 10% M/G Cheerios)
#     X2 - .1X5 >= 0 ( 10% Grape Nuts)
#     X3 - .1X5 >= 0 ( 10% Product 19)
#     X4 - .1X5 >= 0 ( 10% Frosted Bran)

prob += 30*x1 + 30*x2 + 20*x3 + 20*x4 >= 50, "VitaminA_constraint"
prob += 25*x1 + 2*x2 + 100*x3 + 25*x4 >= 50, "VitaminC_constraint"
prob += 25*x1 + 25*x2 + 25*x3 + 25*x4 >= 50, "VitaminD_constraint"
prob += 25*x1 + 25*x2 + 100*x3 + 25*x4 >= 50, "VitaminB6_constraint"
prob += 45*x1 + 45*x2 + 100*x3 + 25*x4 >= 50, "Iron_constraint"
prob += x1 + x2 + x3 + x4 - x5 == 0, "Total"
prob += x1 - 0.1*x5 >= 0, "10%_M/G_Cheerios_constraint"
prob += x2 - 0.1*x5 >= 0, "10%_GrapeNuts_constraint"
prob += x3 - 0.1*x5 >= 0, "10%_Product19_constraint"
prob += x4 - 0.1*x5 >= 0, "10%_FrostedBran_constraint"

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