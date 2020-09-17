import numpy as np
import math
import functions as func


print("input start")
I = func.InPut
num, q, m, pos0, vec0 , kind, name, E_start, E_end, E_vec, B_start, B_end, B_vec = I.inputCSV("sam2")

print("input end")
sub = func.subtool
Efield = sub.SampleFunc(E_start, E_end, E_vec)
Bfield = sub.SampleFunc(B_start, B_end, B_vec)
R = []

for i in range(num):

    #以下ルンゲクッタ法。
    print("runge start")
    pos, vec ,timestamp= sub.NewRunge(Efield, Bfield, q[i], m[i], pos0[i], vec0[i])
    #pos, vec = sub.runge(Efield, Bfield, q[i], m[i], pos0[i], vec0[i])
    print("runge end")
    l = len(pos)

    X = np.array([pos[j][0] for j in range(l)])
    X = 1000*X
    Y = np.array([pos[j][1] for j in range(l)])
    Y = 1000*Y
    Z = np.array([pos[j][2] for j in range(l)])
    Z = 1000*Z
    print(len(Z))
    print(len(timestamp))
    r = np.array([X, Y, Z])
    R.append(r)
    plams = {"title":name[i],"x":R[i][0],"y":R[i][1],"z":R[i][2]}
    print("output start")
    if i == 0:
        oput = func.OutPut.OutPut(plams,Efield,Bfield,200,400,timestamp)

    else:
        oput.AddPlams(plams,timestamp)

oput.TimePlot("x")



oput.Show()
print("output end")
