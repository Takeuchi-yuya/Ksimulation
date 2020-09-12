import numpy as np
import math
import project as pj

sub = pj.subtool
Efield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.0,"z":0.0})
Bfield = sub.SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.005,"z":0.0})

I = pj.InPut
q, m, x, v = I.inputCSV("sam")

#以下ルンゲクッタ法。
x, v = sub.runge(Efield, Bfield, q, m, x, v)

#2次元配列からそれぞれの座標を取り出す。
#グラフプロットをmm単位で。
l = len(x)
X = np.array([x[i][0] for i in range(l)])
X = 1000*X
Y = np.array([x[i][1] for i in range(l)])
Y = 1000*Y
Z = np.array([x[i][2] for i in range(l)])
Z = 1000*Z

plams = {"title":"Al_0.01%","x":X,"y":Y,"z":Z}

oput = pj.OutPut.OutPut(plams,Efield,Bfield)
oput.Show()
