import numpy as np
import math
import project as pj

sub = pj.subtool
Efield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":50.0,"y":0.0,"z":0.0})
Bfield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.005,"z":0.0})
print("input start")
I = pj.InPut
num, q, m, pos0, vec0 , kind, number = I.inputCSV("sam2")
print("input end")
R = []

for i in range(num):

    #以下ルンゲクッタ法。
    print("runge start")
    pos, vec = sub.runge(Efield, Bfield, q[i], m[i], pos0[i], vec0[i])
    print("runge end")
    l = len(pos)

    X = np.array([pos[j][0] for j in range(l)])
    X = 1000*X
    Y = np.array([pos[j][1] for j in range(l)])
    Y = 1000*Y
    Z = np.array([pos[j][2] for j in range(l)])
    Z = 1000*Z

    r = np.array([X, Y, Z])
    R.append(r)
    plams = {"title":number[i] + ":" +  kind[i],"x":R[i][0],"y":R[i][1],"z":R[i][2]}
    print("output start")
    if i == 0:
        oput = pj.OutPut.OutPut(plams,Efield,Bfield,200,400)
    else:
        oput.AddPlams(plams)


oput.Show()
print("output end")
