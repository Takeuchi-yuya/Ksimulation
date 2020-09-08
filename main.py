import numpy as np
import project as pj
#project/InPutの関数を呼ぶときはIで省略します宣言
I = pj.InPut
q, m = I.inputPar()
t_repetition = I.inputTime()
x = I.inputPos()
v = I.inputVec()
sub = pj.subtool
Efield = sub.SampleFunc({"x":-50.0,"y":-50.0,"z":-50.0},{"x":50.0,"y":50.0,"z":50.0},{"x":0.0,"y":0.0,"z":0.0000000000005})
Bfield = sub.SampleFunc({"x":-50.0,"y":-50.0,"z":-50.0},{"x":50.0,"y":50.0,"z":50.0},{"x":0.0,"y":0.0,"z":0.0000000000025})

x, v = sub.runge(Efield, Bfield, q, m, t_repetition, x, v)

X = np.array([x[i][0] for i in range(t_repetition +1)])
Y = np.array([x[i][1] for i in range(t_repetition +1)])
Z = np.array([x[i][2] for i in range(t_repetition +1)])

plams = {"title":"runge","x":X,"y":Y,"z":Z}

oput = pj.OutPut.OutPut(plams)
oput.Show()
