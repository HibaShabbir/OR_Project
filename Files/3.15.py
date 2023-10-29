from pulp import *

prob = LpProblem("Prob_3.15", LpMaximize)

# declare variables

X1 = LpVariable("x1", 0, None, LpContinuous)
X2 = LpVariable("x2", 0, None, LpContinuous)
X3 = LpVariable("x3", 0, None, LpContinuous)
X4 = LpVariable("x4", 0, None, LpContinuous)

prob += 622*X1 + 690*X2 + 231*X3 + 684*X4

prob += 4*X1 + 5*X2 + 3*X3 + 10*X4 <= 1800, "Labor hours"
prob += 50*X1 + 75*X2 + 30*X3 + 60*X4 <= 25000, "Expenses"
prob += 2*X1 + 6*X2 + X3 + 4*X4 <= 1200, "Water"
prob += 210*X1 >= 30000, "Min. Wheat"
prob += 300*X2 >= 30000, "Min. Corn"
prob += 180*X3 <= 25000, "Max Oats"
prob += X1 + X2 + X3 + X4 <= 300, "Total acres"

# The problem is solved using PuLP's choice of Solver
prob.solve()

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name + "=" + str(v.varValue) +"\tReduced cost = "+ str(v.dj))
print ("The optimal value of the objective function is = ", value(prob.objective))

print("Senstivity Analysis\n Constraints\t\t\t      ShadowPrice \t    Slack")

for name , c in prob.constraints.items():
    print(name  , c , "\t  " , c.pi , "\t\t" ,c.slack)
