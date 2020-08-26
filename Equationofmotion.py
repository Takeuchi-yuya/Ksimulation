import numpy as np
import math

q = 1.6
m = 0.06
E = [1,0,0]
B = [0,1,0]

t_max = int(input("計算する時間を入力してください。[s]"))
t_max = float(t_max)
dt = 0.1
t_repetition = t_max/dt
t_repetition = int(t_repetition)

print("初期位置を入力してください。[m]")
#int型で読み取ったものをfloat型にして、それぞれの2次配列の先頭に入れる。
x0 = list(map(int, input().split()))
x0 = [float(n) for n in x0]
x = np.empty((0,3), float)
x = np.append(x, np.array([x0]), axis=0)
print("初速度を入力してください。[m/s]")
v0 = list(map(int, input().split()))
v0 = [float(n) for n in v0]
v = np.empty((0,3), float)
v = np.append(v, np.array([v0]), axis=0)

for i in range(t_repetition):
    v1 = v[i]
    u1 = np.cross(v1,B)
    k1 = q*(E + u1)/m
    l1 = v[i]

    v2 = v1 + k1*dt/2
    u2 = np.cross(v2,B)
    k2 = q*(E + u2)/m
    l2 = v[i] + l1/2

    v3 = v1 + k2*dt/2
    u3 = np.cross(v3,B)
    k3 = q*(E + u3)/m
    l3 = v[i] + l2/2

    v4 = v1 + k3*dt
    u4 = np.cross(v4,B)
    k4 = q*(E + u4)/m
    l4 = v[i] + l3

    v_tem = v[i] + dt*(k1 + 2*k2 + 2*k3 + k4)/6
    v = np.append(v, np.array([v_tem]), axis=0)
    x_tem = x[i] + dt*(l1 + 2*l2 + 2*l3 + l4)/6
    x = np.append(x, np.array([x_tem]), axis=0)

print(x)



#def bethe(self,):

#dE = 4*PI()*/
