import numpy as np
import math
from OutPut import OutPut
from CreatTestdata import SampleFunc

#動作確認はなんとなくアルミニウムイオンで。
Na = 6.02*100000000000000000000000
q = 3*1.6/10000000000000000000
m = (26.98/Na)/1000


Efield = SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":149.896229,"y":0.0,"z":0.0})
Bfield = SampleFunc({"x":-0.1,"y":-0.1,"z":-0.1},{"x":0.1,"y":0.1,"z":0.1},{"x":0.0,"y":0.005,"z":0.0})

t_max = 0.00001
dt = 0.000000001
t_repetition = t_max/dt
t_repetition = int(t_repetition)

x0 = [0.0, 0.0, -0.2]
x = np.empty((0,3), float)
x = np.append(x, np.array([x0]), axis=0)
v0z = 0.0001*299792458
v0 = [0, 0, v0z]
v = np.empty((0,3), float)
v = np.append(v, np.array([v0]), axis=0)

#以下ルンゲクッタ法。
for i in range(t_repetition):
    E = Efield.VectorField(x[i])
    E = [E["x"],E["y"],E["z"]]
    #E = np.array(E)
    B = Bfield.VectorField(x[i])
    B = [B["x"],B["y"],B["z"]]
    #B = np.array(B)

    v1 = v[i]
    u1 = np.cross(v1,B)
    k1 = q*(E + u1)/m
    l1 = v[i]

    v2 = v1 + k1*dt/2
    u2 = np.cross(v2,B)
    k2 = q*(E + u2)/m
    l2 = v[i] + l1/2

    v3 = v1 + k2*dt/2
    u3 = np.cross(v3,B)
    k3 = q*(E + u3)/m
    l3 = v[i] + l2/2

    v4 = v1 + k3*dt
    u4 = np.cross(v4,B)
    k4 = q*(E + u4)/m
    l4 = v[i] + l3

    v_tem = v[i] + dt*(k1 + 2*k2 + 2*k3 + k4)/6
    v = np.append(v, np.array([v_tem]), axis=0)
    x_tem = x[i] + dt*(l1 + 2*l2 + 2*l3 + l4)/6
    x = np.append(x, np.array([x_tem]), axis=0)

np.save('runge_posi',x)

#2次元配列からそれぞれの座標を取り出す。
#グラフプロットをmm単位で。
X = np.array([x[i][0] for i in range(t_repetition +1)])
X = 1000*X
Y = np.array([x[i][1] for i in range(t_repetition +1)])
Y = 1000*Y
Z = np.array([x[i][2] for i in range(t_repetition +1)])
Z = 1000*Z

plams = {"title":"Al_0.01%","x":X,"y":Y,"z":Z}

oput = OutPut(plams)
oput.Show()
