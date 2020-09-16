import numpy as np
import math
import project as pj

sub = pj.subtool
Efield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":1.0,"y":1.0,"z":1.0},{"x":0.0,"y":0.0,"z":500.0})
Bfield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.0,"z":0.0})

I = pj.InPut
num, q, m, pos0, vec0, kind = I.inputCSV("OutTestSamE")

R = {}

for i in range(num):

    #以下ルンゲクッタ法。
    pos, vec = sub.runge(Efield, Bfield, q[i], m[i], pos0[i], vec0[i])

    l = len(pos)

    X = np.array([pos[j][0] for j in range(l)])
    X = 1000*X
    Y = np.array([pos[j][1] for j in range(l)])
    Y = 1000*Y
    Z = np.array([pos[j][2] for j in range(l)])
    Z = 1000*Z

    r = np.array([X, Y, Z])
    R[str(i + 1)] = r

plams = {"title":"Al_0.01%","x":R["1"][0],"y":R["1"][1],"z":R["1"][2]}
dt = 10**(-8)
print("設定した座標に到達するまでにかかった時間は、", (l-1) * dt, "[s]です。")
print("Excelで解析的に計算した結果は、1.22225577993463e-05[s]です")

oput = pj.OutPut.OutPut(plams)
oput.Show()
