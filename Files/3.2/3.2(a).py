# X1 = Number of stoves produced weekly
# X2 = Number of washers produced weekly
# X3 = Number of electric dryers produced weekly
# X4 = Number of gas dryers produced weekly
# X5 = Number of refrigerators produced weekly
#     MAX 110X1 + 90X2 + 75X3 + 80X4 + 130X5
#         S.T.
#         5.5X1 + 5.2X2 + 5.0X3 + 5.1X4 + 7.5X5 <= 4800 (Molding/pressing)
#         4.5X1 <= 1200 (Stove assembly)
#         4.5X2 + 4.0X3 + 3.0X4 <= 2400 (Washer/dryer assembly)
#         9.0X5 <= 1200 (Refrigerator assembly)
#         4.0X1 + 3.0X2 + 2.5X3 + 2.0X4 + 4.0X5 <= 3000 (Packaging)
#
#         All X's >=0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.2a", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
x5 = LpVariable("x5", 0)

# Define the objective function
prob += 110*x1 + 90*x2 + 75*x3 + 80*x4 + 130*x5

# Define the constraints
#         5.5X1 + 5.2X2 + 5.0X3 + 5.1X4 + 7.5X5 <= 4800 (Molding/pressing)
#         4.5X1 <= 1200 (Stove assembly)
#         4.5X2 + 4.0X3 + 3.0X4 <= 2400 (Washer/dryer assembly)
#         9.0X5 <= 1200 (Refrigerator assembly)
#         4.0X1 + 3.0X2 + 2.5X3 + 2.0X4 + 4.0X5 <= 3000 (Packaging_constraint)
prob += 5.5*x1 + 5.2*x2 + 5.0*x3 + 5.1*x4 + 7.5*x5 <= 4800, "Molding/pressing_constraint"
prob += 4.5*x1 <= 1200, "Stove_assembly_constraint"
prob += 4.5*x2 + 4.0*x3 + 3.0*x4 <= 2400, "Washer/dryer_assembly_constraint"
prob += 9.0*x5 <= 1200, "Refrigerator_assembly_constraint"
prob += 4.0*x1 + 3.0*x2 + 2.5*x3 + 2.0*x4 + 4.0*x5 <= 3000, "Packaging_constraint"


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



