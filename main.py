import numpy as np
import math
import functions as func


print("input start")
I = func.InPut
num, inputDataSet = I.inputCSV("sam2")

print("input end")
sub = func.subtool
Efield = sub.SampleFunc(inputDataSet["EFieldplams"])
Bfield = sub.SampleFunc(inputDataSet["BFieldplams"])
R = []

for particlePlams in inputDataSet["particlePlams"]:

    #以下ルンゲクッタ法。
    print("runge start")
    pos, vec ,timestamp = sub.NewRunge(Efield, Bfield, particlePlams)
    #pos, vec = sub.runge(Efield, Bfield, q[i], m[i], pos0[i], vec0[i])
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
    plams = {"title":particlePlams["name"],"x":X,"y":Y,"z":Z}
    print("output start")
    if particlePlams["num"] == 0:
        oput = func.OutPut.OutPut(plams,Efield,Bfield,200,400,timestamp)

    else:
        oput.AddPlams(plams,timestamp)

#oput.TimePlot("x")



oput.Show()
print("output end")
