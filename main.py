import numpy as np
import math
import functions as func


print("input start")
I = func.InPut
inputDataSet = I.inputJson("sample")
print(inputDataSet)

print("input end")
sub = func.subtool
Ef = func.Efield
Efield = Ef.Efield(Ef.makeGridParticle(10))
Bfield = sub.SampleFunc(inputDataSet["BFieldplams"])
outputDataSet = sub.Calc(inputDataSet,Efield,Bfield)
oput = func.OutPut.OutPut(outputDataSet,200,400)


#oput.TimePlot("x")



oput.Show()
print("output end")
