import numpy as np
import functions as func
import math

print("input start")
I = func.InPut
inputDataSet = I.inputJson("OutTestE")
print(inputDataSet)

print("input end")
sub = func.subtool
#Ef = func.Efield
#Efield = Ef.Efield(Ef.makeGridParticle(0.000000000001))
Efield = sub.SampleFunc(inputDataSet["EFieldplams"])
Bfield = sub.SampleFunc(inputDataSet["BFieldplams"])

outputDataSet = sub.Calc(inputDataSet,Efield,Bfield)
oput = func.OutPut.OutPut(outputDataSet,200,400)

l = len(outputDataSet["pData"]["x"][0])
dt = sub.dt
print("設定した座標に到達するまでにかかった時間は、", (l-1) * dt, "[s]です。")
print("Excelで解析的に計算した結果は、8.64265350336229e-06[s]です")
print("その差は",(l-1) * dt-0.00000864265350336229,"[s]です")

oput.Show()
print("output end")
