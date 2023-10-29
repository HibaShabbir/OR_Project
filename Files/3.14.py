from pulp import *

prob = LpProblem("MotorHomeCabinetsProblem", LpMinimize)

XJR = LpVariable("xjr", 0, None, LpContinuous)
XJO = LpVariable("xj0", 0, None, LpContinuous)
XAR = LpVariable("xar", 0, None, LpContinuous)
XAO = LpVariable("xa0", 0, None, LpContinuous)
XSR = LpVariable("xsr", 0, None, LpContinuous)
XSO = LpVariable("xs0", 0, None, LpContinuous)
YJR = LpVariable("yjr", 0, None, LpContinuous)
YJO = LpVariable("yj0", 0, None, LpContinuous)
YAR = LpVariable("yar", 0, None, LpContinuous)
YAO = LpVariable("ya0", 0, None, LpContinuous)
YSR = LpVariable("ysr", 0, None, LpContinuous)
YSO = LpVariable("ys0", 0, None, LpContinuous)
SJ = LpVariable("sj", 0, None, LpContinuous)
SA = LpVariable("sa", 0, None, LpContinuous)
SS = LpVariable("ss", 0, None, LpContinuous)
TJ = LpVariable("tj", 0, None, LpContinuous)
TA = LpVariable("ta", 0, None, LpContinuous)
TS = LpVariable("ts", 0, None, LpContinuous)

prob += 188*XJR + 209*XJO + 194*XAR + 218*XAO + 200*XSR + 227*XSO + 280*YJR + 315*YJO + 290*YAR + 330*YAO + 300*YSR + 345*YSO + 6*SJ + 6*SA + 6*SS + 9*TJ + 9*TA + 9*TS

#  storage constraints
prob += XJR + XJO - SJ == 225
prob += XAR + XAO + SJ - SA == 250
prob += SA + XSR + XSO - SS == 150
prob += YJR + YJO - TJ == 80
prob += TJ + YAR + YAO - TA == 300
prob += TA + YSR + YSO - TS == 400
# Required for September
prob += SS >= 10, "Motor Home"
prob += TS >= 25, "Mobile Home"

#  Maximum Storage in any Month
prob += SJ + TJ <= 300, "Maximum Storage in July"
prob += SA + TA <= 300, "Maximum Storage in August"
prob += SS + TS <= 300, "Maximum Storage in September"

# Production
#     Regular Time
prob += 3*XJR + 5*YJR <= 2100, "Regular july"
prob += 3*XAR + 5*YAR <= 1500, "Regular august"
prob += 3*XSR + 5*YSR <= 1200, "Regular september"

# Overtime
prob += 3*XJO + 5*YJO <= 1050, "Overtime july "
prob += 3*XAO + 5*YAO <= 750, "Overtime august"
prob += 3*XSO + 5*YSO <= 600, "Overtime september"

# The problem is solved using PuLP's choice of Solver
prob.solve()

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name + "=" + str(v.varValue) +"\tReduced cost = "+ str(v.dj))
print ("The optimal value of the objective function is = ", value(prob.objective))

print("Senstivity Analysis\n Constraints\t\t\t      ShadowPrice \t    Slack")

for name , c in prob.constraints.items():
    print(name  , c , "\t  " , c.pi , "\t\t" ,c.slack)
