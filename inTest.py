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
for i in range(num):
    #以下ルンゲクッタ法。
    x, v = sub.runge(Efield, Bfield, q[i], m[i], x0[i], v0[i])

    #グラフプロットをmm単位で。
    l = len(x)

    #確認のため
    print(l)

    X = np.array([x[i][0] for i in range(l)])
    X = 1000*X
    Y = np.array([x[i][1] for i in range(l)])
    Y = 1000*Y
    Z = np.array([x[i][2] for i in range(l)])
    Z = 1000*Z

    r = np.array([X, Y, Z])
    R[str(i)] = r
    #R = np.append(R, r)


plams = {"title":"Al_0.01%","x":R["0"][0],"y":R["0"][1],"z":R["0"][2]}

oput = pj.OutPut.OutPut(plams)
oput.Show()
