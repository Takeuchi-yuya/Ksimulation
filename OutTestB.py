import numpy as np
import functions as func
import math

print("input start")
I = func.InPut
inputDataSet = I.inputJson("OutTestB")
print(inputDataSet)

print("input end")
sub = func.subtool
#Ef = func.Efield
#Efield = Ef.Efield(Ef.makeGridParticle(0.000000000001))
Efield = sub.SampleFunc(inputDataSet["EFieldplams"])
Bfield = sub.SampleFunc(inputDataSet["BFieldplams"])
rungeLimit = 19748
outputDataSet = sub.Calc(inputDataSet,Efield,Bfield,rungeLimit)
oput = func.OutPut.OutPut(outputDataSet,200,400)

X = outputDataSet["pData"]["x"][0]
X = np.array(X)
Y = outputDataSet["pData"]["y"][0]
Y = np.array(Y)

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

print("Excelで解析的に求めた半径は18.4889751433615[mm]で、その差は", radius_ave-18.4889751433615, "[mm]です")

oput.Show()
print("output end")
