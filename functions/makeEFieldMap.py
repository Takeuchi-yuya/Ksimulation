import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons


#3次元プロットするためのモジュール
from mpl_toolkits.mplot3d import Axes3D
#行列N×N
N = 100
#演算範囲
lim = 0.5
#刻み幅
dr = lim*2/N
#真空中の誘電率
e = 8.854e-12
rho = 10**(-4)*cons.e
#系内の最大の電位を入れる変数．ある有限の値を入れておく(ゼロ割り防止)
MaxPhi = 1.0e-10
def m2Dex(m):
    return int((m + lim)/dr)


print("dr",lim*2/N)
#とりあえず二次元
rhomap = [[0 for j in range(N)] for i in range(N)]
phimap = rhomap.copy()
#flagmap = [[0 for j in range(N)] for i in range(N)]
rholist = []
#とりあえず、y=0.1,-0.1,-0.1<x<0.1のとこに電荷置く
for x in np.arange(-0.1,0.1,dr):
    xDex = m2Dex(x)
    yDex = m2Dex(0.1)
    rholist.append([xDex,yDex,rho])
    rhomap[yDex][xDex] = rho
    #flagmap[yDex][xDex] = 2
    yDex = m2Dex(-0.1)
    rholist.append([xDex,yDex,-rho])
    rhomap[yDex][xDex] = -rho
    #flagmap[yDex][xDex] = 2
#print(rhomap)
count = 0
'''
#外周の電位を計算して入れておく
def calc(pos):
    phi = 0
    for rho in rholist:
        r = np.sqrt((pos[0]-rho[0])**2 + (pos[0]-rho[0])**2)*dr
        #print(r)
        if r != 0:
            phi = 1/(4*np.pi*e)*rho[2]/r + phi
    print(phi)
    return phi
for i in range(N):
    phimap[0][i]   = calc([0,i])
    phimap[N-1][i] = calc([N-1,i])
    phimap[i][0]   = calc([i,0])
    phimap[i][N-1] = calc([i,N-1])
'''
MaxErr = 1
Conv = 10**(-6)
while MaxErr>Conv:
    #print(phimap)
    MaxErr = CurErr = 0.0
    count = 1 + count
    flag = False
    for x in range(1,N-1):
        for y in range(1,N-1):
            Prev_phi = phimap[y][x]
            tmp =1/4 * (rhomap[y][x]*dr*dr/e+phimap[y+1][x]+phimap[y-1][x]+phimap[y][x+1]+phimap[y][x-1])
            if MaxPhi < abs(tmp):
                MaxPhi = abs(tmp)
            phimap[y][x] = tmp
            CurErr = (abs(phimap[y][x] - Prev_phi))/MaxPhi
            if MaxErr < CurErr:
                 MaxErr = CurErr


print(count)
        #print(phimap)
xlist = np.array([])
ylist = np.array([])
philist = np.array([])
for x in range(N):
    for y in range(N):
        xlist = np.append(xlist , x)
        ylist = np.append(ylist , y)
        philist = np.append(philist , phimap[y][x])
print(x,y,phimap[y][x])
fig = plt.figure()
ax = Axes3D(fig)


#.plotで描画
#linestyle='None'にしないと初期値では線が引かれるが、3次元の散布図だと大抵ジャマになる
#markerは無難に丸
ax.plot(xlist,ylist,philist,marker="o",linestyle='None',markersize=1)


#最後に.show()を書いてグラフ表示
plt.show()
