
import functions as func
import numpy as np
import matplotlib.pyplot as plt

print("input start")
I = func.InPut
inputDataSet = I.inputJson("RealData")
print(inputDataSet)

print("input end")
sub = func.subtool
#Ef = func.Efield
#Efield = Ef.Efield(Ef.makeGridParticle(0.000000000001))
Efield = sub.SampleFunc(inputDataSet["EFieldplams"])
Bfield = sub.SampleFunc(inputDataSet["BFieldplams"])
outputDataSet = sub.Calc(inputDataSet,Efield,Bfield)
oput = func.OutPut.OutPut(outputDataSet,125,200)

outputDataSet2 = outputDataSet["pData"]
outputDataSet2 = outputDataSet2["x"]
l = len(outputDataSet2)
oput2 = np.array([outputDataSet2[i][-1] for i in range(l)])
p = sub.NumberOfParticles(100)
for i in range(len(p)):
    for j in range(p[i]):
        oput2 = np.append(oput2, oput2[i])


#oput.TimePlot("x")



oput.Show()

#5.8mm間隔で並ぶ43個のチャンネルトロン
fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.hist(oput2, bins=43, range=(-129, 129))
ax2.hist(oput2, bins=129, range=(-129, 129))

plt.show()
print("output end")
