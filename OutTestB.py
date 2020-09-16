import numpy as np
import math
import project as pj

sub = pj.subtool
Efield = sub.SampleFunc({"x":-1000,"y":-1000,"z":-1000},{"x":1000,"y":1000,"z":1000},{"x":0.0,"y":0.0,"z":0.0})
Bfield = sub.SampleFunc({"x":-1000,"y":-1000,"z":-1000},{"x":1000,"y":1000,"z":1000},{"x":0.0,"y":0.0,"z":0.005})

I = pj.InPut
num, q, m, pos0, vec0, kind, number = I.inputCSV("OutTestSamB")

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

#円の中心を求める
cen_X = sum(X) / len(X)
cen_Y = sum(Y) / len(Y)
print("中心の座標は、[X, Y] = ", cen_X, cen_Y, "です")

#各座標と中心との距離を計算する
radius_X = X-cen_X
radius_Y = Y-cen_Y
radius = np.empty(0)
for i in range(len(X)):
    radius_tem = math.sqrt(radius_X[i]**2 + radius_Y[i]**2)
    radius = np.append(radius, radius_tem)

#平均から半径を決定する
radius_ave = sum(radius) / len(radius)
print("平均値から求めた半径は、", radius_ave, "です")

#分散を計算する
error = [(radius[i] - radius_ave)**2 for i in range(len(radius))]
error_ave = sum(error) / len(error)
print("分散は、", error_ave, "です")

print("Excelで解析的に求めた半径は186.738648947951[mm]で、その差は", radius_ave-186.738648947951, "[mm]です")

oput = pj.OutPut.OutPut(plams,Efield,Bfield,400,400)
oput.Show()
