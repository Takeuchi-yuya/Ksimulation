import numpy as np
import math
from OutPut import OutPut
from CreatTestdata import SampleFunc

Na = 6.02*100000000000000000000000

kind = input("入射粒子を入力してください(e/p/other)")
if kind == "e":
    q = -1.6/10000000000000000000
    m = 9.11/10000000000000000000000000000000

elif kind == "p":
    q = 1.6/10000000000000000000
    m = 1.673/1000000000000000000000000000

elif kind == "Al":
    q = 3*1.6/10000000000000000000
    m = (26.98/Na)/1000

else:
    val = int(input("価数を入力してください"))
    q = val*1.6/10000000000000000000
    mass = float(input("原子量を入力してください[g/mol]"))
    m = (mass/Na)/1000

Efield = SampleFunc({"x":-500.0,"y":-500.0,"z":-500.0},{"x":500.0,"y":500.0,"z":500.0},{"x":0.0,"y":0.0,"z":0.1})
Bfield = SampleFunc({"x":-500.0,"y":-500.0,"z":-500.0},{"x":500.0,"y":500.0,"z":500.0},{"x":0.0,"y":0.0,"z":0.0})

t_max = float(input("計算する時間を入力してください。[s]"))
dt = 0.00001
t_repetition = t_max/dt
t_repetition = int(t_repetition)

print("初期位置を入力してください。[m]")
x0 = list(map(float, input().split()))
x = np.empty((0,3), float)
x = np.append(x, np.array([x0]), axis=0)
print("初速度を入力してください。[m/s]")
v0 = list(map(float, input().split()))
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
X = np.array([x[i][0] for i in range(t_repetition +1)])
Y = np.array([x[i][1] for i in range(t_repetition +1)])
Z = np.array([x[i][2] for i in range(t_repetition +1)])

plams = {"title":"runge","x":X,"y":Y,"z":Z}

oput = OutPut(plams,Efield,Bfield)
oput.Show()
