import numpy as np
from project import *

q, m = inputPar()
t_repetition = inputTime()
x = inputPos()
v = inputVec()

Efield = SampleFunc({"x":-50.0,"y":-50.0,"z":-50.0},{"x":50.0,"y":50.0,"z":50.0},{"x":0.0,"y":0.0,"z":0.0000000000005})
Bfield = SampleFunc({"x":-50.0,"y":-50.0,"z":-50.0},{"x":50.0,"y":50.0,"z":50.0},{"x":0.0,"y":0.0,"z":0.0000000000025})

x, v = runge(Efield, Bfield, q, m, t_repetition, x, v)

X = np.array([x[i][0] for i in range(t_repetition +1)])
Y = np.array([x[i][1] for i in range(t_repetition +1)])
Z = np.array([x[i][2] for i in range(t_repetition +1)])

plams = {"title":"runge","x":X,"y":Y,"z":Z}

oput = OutPut(plams)
oput.Show()
