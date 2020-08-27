import numpy as np
import math

#３Dプロットのためのコード。
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
from mpl_toolkits.mplot3d import Axes3D

import csv
from OutPut import OutPut

q = 1.6
m = 0.06
E = [0,0,10]
B = [0,0,1]

t_max = int(input("計算する時間を入力してください。[s]"))
t_max = float(t_max)
dt = 0.01
t_repetition = t_max/dt
t_repetition = int(t_repetition)

print("初期位置を入力してください。[m]")
#int型で読み取ったものをfloat型にして、それぞれの2次配列の先頭に入れる。
x0 = list(map(int, input().split()))
x0 = [float(n) for n in x0]
x = np.empty((0,3), float)
x = np.append(x, np.array([x0]), axis=0)
print("初速度を入力してください。[m/s]")
v0 = list(map(int, input().split()))
v0 = [float(n) for n in v0]
v = np.empty((0,3), float)
v = np.append(v, np.array([v0]), axis=0)

#以下ルンゲクッタ法。
for i in range(t_repetition):
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

#グラフの枠を作っていく
#fig = plt.figure()
#ax = Axes3D(fig)

#ax.set_xlabel("X")
#ax.set_ylabel("Y")
#ax.set_zlabel("Z")

#ax.plot(X,Y,Z,marker="o",linestyle='None')

#plt.show()

plams = {"title":1,"x":X,"y":Y,"z":Z}

oput = OutPut(plams)
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot2grid((2,2),(0,0))
ay = plt.subplot2grid((2,2),(0,1))
az = plt.subplot2grid((2,2),(1,0))
a3d = plt.subplot2grid((2,2),(1,1),projection='3d')
ax = oput.twoDPlot(ax,"x",0)
ay = oput.twoDPlot(ay,"y",0)
az = oput.twoDPlot(az,"z",0)
a3d = oput.threeDPlot(a3d)

#vectorの出力テストを行うためにテストデータの作成とプロット
s_pos = sb.PosLToDic([-50,-50,-50])
e_pos = sb.PosLToDic([50,50,50])
vector = sb.PosLToDic([5,5,5])
vf = SF(s_pos,e_pos,vector)
ax = oput.vectorTwoDPlot(vf,ax,"x",0)
ay = oput.vectorTwoDPlot(vf,ay,"y",0)
az = oput.vectorTwoDPlot(vf,az,"z",0)
plt.show()
