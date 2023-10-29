from pulp import *

prob = LpProblem("Giapetto",LpMaximize)

x1 = LpVariable("x1", lowBound = 0 )
x2 = LpVariable("x2", lowBound = 0 )

prob += 20*x1 + 30*x2

prob += 1*x1 + 2*x2 <=100
prob += 2*x1 + 1*x2 <=100

prob.solve()

print("Status ", LpStatus[prob.status])

#print(str(value(x1)) + "," + str(value(x2))  + "," + str(value(prob.objective)))
value(x1), value(x2) , value(prob.objective)

for v in prob.variables():
    print(v.name + "=" + str(v.varValue) +"\tReduced cost = "+ str(v.dj))
print("objective function = " + str(value(prob.objective)))

print("Senstivity Analysis\n Constraints\t\t      ShadowPrice \t    Slack")

for name , c in prob.constraints.items():
    print(name , "1" , c , "\t  " , c.pi , "\t\t" ,c.slack)
