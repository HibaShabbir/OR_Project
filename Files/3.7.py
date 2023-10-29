# Question – 3.7:
# X1 = Number of Student models produced each week
# X2 = Number of Plus models produced each week
# X3 = Number of Net models produced each week
# X4 = Number of Pro models produced each week
#     MAX 70X1 + 80X2 + 130X3 + 150X4
#     S.T.
#     X3 >= 100 (Contract)
#     0.4X1 + 0.5X2 + 0.6X3 + 0.8X4 <= 750 (Production Hours)
#     X1 + + X3 <= 700 (Celeron)
#     X2 + X4 <= 550 (Pentium)
#     X1 + X2 + X3 + <= 800 (20gb Hard Drives)
#     X4 <= 950 (30gb Hard Drives)
#     X1 + X2 + 2X3 + X4 <= 1600 (Floppy Drives)
#     X1 + X2 + X4 <= 1000 (Zip Drives)
#     X1 + X3 + X4 <= 1600 (CD R/W's)
#     X2 + X3 + X4 <= 900 (DVD's)
#     X1 + X2 <= 850 (15-in. monitors)
#     X3 + X4 <= 800 (17-in. monitors)
#     X2 + X3 <= 1250 (Mini-tower cases)
#     X1 + X4 <= 750 (Tower cases)
#
# All X's  0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.7", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)

# Define the objective function
prob += 70*x1 + 80*x2 + 130*x3 + 150*x4

# Define the constraints
#      X3 >= 100 (Contract)
#      0.4X1 + 0.5X2 + 0.6X3 + 0.8X4 <= 750 (Production Hours)
#      X1 + + X3 <= 700 (Celeron)
#      X2 + X4 <= 550 (Pentium)
#      X1 + X2 + X3 + <= 800 (20gb Hard Drives)
#      X4 <= 950 (30gb Hard Drives)
#      X1 + X2 + 2X3 + X4 <= 1600 (Floppy Drives)
#      X1 + X2 + X4 <= 1000 (Zip Drives)
#      X1 + X3 + X4 <= 1600 (CD R/W's)
#      X2 + X3 + X4 <= 900 (DVD's)
#      X1 + X2 <= 850 (15-in. monitors)
#      X3 + X4 <= 800 (17-in. monitors)
#      X2 + X3 <= 1250 (Mini-tower cases)
#      X1 + X4 <= 750 (Tower cases)
prob += x3 >= 100, "Contract_constraint"
prob += 0.4*x1 + 0.5*x2 + 0.6*x3 + 0.8*x4 <= 750, "Production_hrs_constraint"
prob += x1 + x3 <= 700, "Celeron_constraint"
prob += x2 + x4 <= 550, "Pentium_constraint"
prob += x1 + x2 + x3 <= 800, "20GB_HardDrives_constraint"
prob += x4 <= 950, "30GB_HardDrives_constraint"
prob += x1 + x2 + 2*x3 + x4 <= 1600, "FloppyDrives_constraint"
prob += x1 + x2 + x4 <= 1000, "ZipDrives_constraint"
prob += x1 + x3 + x4 <= 1600, "CD_R/W_constraint"
prob += x2 + x3 + x4 <= 900, "DVD_constraint"
prob += x1 + x2 <= 850, "15inch_Monitors_constraint"
prob += x3 + x4 <= 800, "17inch_Monitors_constraint"
prob += x2 + x3 <= 1250, "Mini_Tower_Cases_constraint"
prob += x1 + x4 <= 750, "Tower_Cases_constraint"

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