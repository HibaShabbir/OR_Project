# Question – 3.6:
# X1 = number of 8-oz. portions of steak in the diet
# X2 = number of ounces of cheese in the diet
# X3 = number of apples in the diet
# X4 = number of 8-oz. portion of milk in the diet
#     MIN 51X1 + 9X2 + 1X3 + 8X4
#     S.T.
#     692X1 + 110X2 + 81X3 + 150X4 >= 1410 (=1800-390 minimum calories)
#     692X1 + 110X2 + 81X3 + 150X4 <= 1610 (=2000-390 maximum calories)
#     57X1 + 6X2 + 1X3 + 8X4 >= 85 (=100-15 grams of protein)
#     1X2 + 22X3 + 12X4 >= 25 (= 45-20 grams of carbs.)
#
# All X's >= 0

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Create an object of a model
prob = LpProblem("Prob_3.6", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)

# Define the objective function
prob += 51*x1 + 9*x2 + 1*x3 + 8*x4

# Define the constraints
#     692X1 + 110X2 + 81X3 + 150X4 >= 1410 (=1800-390 minimum calories)
#     692X1 + 110X2 + 81X3 + 150X4 <= 1610 (=2000-390 maximum calories)
#     57X1 + 6X2 + 1X3 + 8X4 >= 85 (=100-15 grams of protein)
#     1X2 + 22X3 + 12X4 >= 25 (= 45-20 grams of carbs.)
prob += 692*x1 + 110*x2 + 81*x3 + 150*x4 >= 1410, "Minimum_calories_constraint"
prob += 692*x1 + 110*x2 + 81*x3 + 150*x4 <= 1610, "Maximum_calories_constraint"
prob += 57*x1 + 6*x2 + 1*x3 + 8*x4 >= 85, "Protein_in_grams_constraint"
prob += 1*x2 + 22*x3 + 12*x4 >= 25, "Carbs_in_grams_constraint"


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