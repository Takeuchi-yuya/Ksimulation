import numpy as np
import math as ma

def inputTime():
    t_max = int(input("計算する時間を入力してください。[s]"))
    t_max = float(t_max)
    dt = 0.1
    t_repetition = t_max/dt
    t_repetition = int(t_repetition)
    return t_repetition


def inputPos():
    print("初期位置を入力してください。[m]")
    #int型で読み取ったものをfloat型にして、それぞれの2次配列の先頭に入れる。
    x0 = list(map(int, input().split()))
    x0 = [float(n) for n in x0]
    x = np.empty((0,3), float)
    x = np.append(x, np.array([x0]), axis=0)
    return x

def inputVec():
    print("初速度を入力してください。[m/s]")
    v0 = list(map(int, input().split()))
    v0 = [float(n) for n in v0]
    v = np.empty((0,3), float)
    v = np.append(v, np.array([v0]), axis=0)
    return v
