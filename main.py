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
outputDataSet = sub.Calc(inputDataSet,Efield,Bfield)
oput = func.OutPut.OutPut(outputDataSet,200,400)


#oput.TimePlot("x")



oput.Show()
print("output end")
