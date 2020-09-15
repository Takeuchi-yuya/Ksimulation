import numpy as np
import math
import project as pj

sub = pj.subtool
Efield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.0,"z":0.0})
Bfield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.005,"z":0.0})
print("input start")
I = pj.InPut
num, q, m, x0, v0 , kind = I.inputCSV("sam2")
print("input end")
R = []

for i in range(num):

    #以下ルンゲクッタ法。
    print("runge start")
    x, v = sub.runge(Efield, Bfield, q[i], m[i], x0[i], v0[i])
    print("runge end")
    l = len(x)

    X = np.array([x[j][0] for j in range(l)])
    X = 1000*X
    Y = np.array([x[j][1] for j in range(l)])
    Y = 1000*Y
    Z = np.array([x[j][2] for j in range(l)])
    Z = 1000*Z

    r = np.array([X, Y, Z])
    R.append(r)
    plams = {"title":kind[i],"x":R[i][0],"y":R[i][1],"z":R[i][2]}
    print("output start")
    if i == 0:
        oput = pj.OutPut.OutPut(plams,Efield,Bfield)
    else:
        oput.AddPlams(plams)


oput.Show()
print("output end")
