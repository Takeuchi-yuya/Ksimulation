import numpy as np
import math
import project as pj

sub = pj.subtool
Efield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.0,"z":0.0})
Bfield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.005,"z":0.0})

I = pj.InPut
num, q, m, x0, v0 = I.inputCSV("sam2")

R = {}

for i in range(num):

    #以下ルンゲクッタ法。
    x, v = sub.runge(Efield, Bfield, q[i], m[i], x0[i], v0[i])

    l = len(x)

    X = np.array([x[j][0] for j in range(l)])
    X = 1000*X
    Y = np.array([x[j][1] for j in range(l)])
    Y = 1000*Y
    Z = np.array([x[j][2] for j in range(l)])
    Z = 1000*Z

    r = np.array([X, Y, Z])
    R[str(i + 1)] = r

plams = {"title":"Al_0.01%","x":R["1"][0],"y":R["1"][1],"z":R["1"][2]}

oput = pj.OutPut.OutPut(plams,Efield,Bfield)
oput.Show()
