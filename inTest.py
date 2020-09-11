import numpy as np
import math
import project as pj

sub = pj.subtool
Efield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.0,"z":0.0})
Bfield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.005,"z":0.0})

I = pj.InPut
num, q, m, x0, v0 = I.inputCSV('project/data/sam2.csv')

#R = np.empty((0, 0, 0), float)
R = {}
#for i in range(num):
print(q[0], m[0], x0[0], v0[0])
#以下ルンゲクッタ法。
x, v = sub.runge(Efield, Bfield, q[0], m[0], x0[0], v0[0])

l = len(x)

#確認のため
print(l)

X = np.array([x[0][0] for i in range(l)])
X = 1000*X
Y = np.array([x[0][1] for i in range(l)])
Y = 1000*Y
Z = np.array([x[0][2] for i in range(l)])
Z = 1000*Z

r = np.array([X, Y, Z])
R[str(0 + 1)] = r
    #R = np.append(R, r)


plams = {"title":"Al_0.01%","x":R["1"][0],"y":R["1"][1],"z":R["1"][2]}

oput = pj.OutPut.OutPut(plams)
oput.Show()
