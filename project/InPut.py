import numpy as np
import math as ma

def inputPar():
    while 1:
        kind = input("入射粒子を入力してください(e/p/other)")
        if kind == "e":
            q = -1.6/10000000000000000000
            m = 9.11/10000000000000000000000000000000


        elif kind == "p":
            q = 1.6/10000000000000000000
            m = 1.673/1000000000000000000000000000

        elif kind == "other":
            val = int(input("価数を入力してください"))
            q = val*1.6/10000000000000000000
            mass = float(input("原子量を入力してください[g/mol]"))
            Na = 6.02*100000000000000000000000
            m = mass/(Na/1000)
        else:
            print("please input \"e or p or other \" ")
            continue
        return q, m

def inputTime():
    while 1:
        try:
            t_max = float(input("計算する時間を入力してください。[s]"))
            break
        except:
            print("error Sampleinput is \"1\". ")
            continue
    dt = 0.01
    t_repetition = t_max/dt
    t_repetition = int(t_repetition)
    return t_repetition


def inputPos():
    print("初期位置を入力してください。[m]")
    while 1:
        try:
            x0 = list(map(float, input().split()))
            break
        except:
            print("error Sampleinput is \"1 1 1\". ")
            continue
    x = np.empty((0,3), float)
    x = np.append(x, np.array([x0]), axis=0)
    return x

def inputVec():
    print("初速度を入力してください。[m/s]")
    while 1:
        try:
            v0 = list(map(float, input().split()))
            break
        except:
            print("error Sampleinput is \"1 1 1\". ")
            continue
    v = np.empty((0,3), float)
    v = np.append(v, np.array([v0]), axis=0)
    return v
