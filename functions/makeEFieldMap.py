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
V = 168 #[V/m]
#系内の最大の電位を入れる変数．ある有限の値を入れておく(ゼロ割り防止)
MaxPhi = 1.0e-10
def m2Dex(m):
    return int((m + lim)/dr)


print("dr",lim*2/N)
#とりあえず二次元
phimap = [[[0 for k in range(N)] for j in range(N)] for i in range(N)]
flagmap = [[[False for k in range(N)] for i in range(N)] for j in range(N)]
#とりあえず、y=0.1,-0.1,-0.1<x<0.1のとこに電荷置く
for z in np.arange(-0.2,0.2,dr):
    for y in np.arange(-0.2,0.2,dr):
        xDex = m2Dex(0.2)
        yDex = m2Dex(y)
        zDex = m2Dex(z)
        phimap[xDex][yDex][zDex] = V/2
        flagmap[xDex][yDex][zDex] = True
        yDex = m2Dex(-0.2)
        phimap[xDex][yDex][zDex] = -V/2
        flagmap[xDex][yDex][zDex] = True
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
            for z in range(1,N-1):
                if flagmap[x][y][z]:
                    continue
                Prev_phi = phimap[x][y][z]
                tmp =1/6 * (phimap[x+1][y][z]+phimap[x-1][y][z]+phimap[x][y+1][z]+phimap[x][y-1][z]+phimap[x][y][z+1]+phimap[x][y][z-1])
                if MaxPhi < abs(tmp):
                    MaxPhi = abs(tmp)
                phimap[x][y][z] = tmp
                CurErr = (abs(phimap[x][y][z] - Prev_phi))/MaxPhi
                if MaxErr < CurErr:
                     MaxErr = CurErr
    if count % 10 == 0:
        print(count,MaxErr)

np.save(phimap,phimap)
