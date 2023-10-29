from pulp import *

prob = LpProblem("Prob_3.13", LpMaximize)

X1 = LpVariable("x1", 0, None, LpContinuous)
X2 = LpVariable("x2", 0, None, LpContinuous)
X3 = LpVariable("x3", 0, None, LpContinuous)
X4 = LpVariable("x4", 0, None, LpContinuous)
X5 = LpVariable("x5", 0, None, LpContinuous)
X6 = LpVariable("x6", 0, None, LpContinuous)
X7 = LpVariable("x7", 0, None, LpContinuous)

prob += .0775*X1 + 0.1125*X2 + .1425*X3 + .9875*X4 + .0445*X5

prob += X1 + X2 + X3 + X4 + X5 == 68000000, "Total"
prob += X5 >= 5000000, "Save"
prob += X1 + X2 + X3 + - X6 == 0,"Res Tr."
prob += X1 + X2 + X3 + X4 - 1*X7 == 0, "Total Tr"
prob += X6 - .8*X7 >= 0, "80% Res."
prob += X1 - .6*X6 >= 0, "60% First"
prob += 4*X1 + 6*X2 + 9*X3 + 3*X4 <= 340000000, "average Risk factor"


# The problem is solved using PuLP's choice of Solver
prob.solve()

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name + "=" + str(v.varValue) +"\tReduced cost = "+ str(v.dj))
print ("The optimal value of the objective function is = ", value(prob.objective))

print("Senstivity Analysis\n Constraints\t\t\t      ShadowPrice \t    Slack")

for name , c in prob.constraints.items():
    print(name  , c , "\t  " , c.pi , "\t\t" ,c.slack)