import numpy as np
import math as ma
import csv

Na = 6.02*100000000000000000000000
ion = {"H":1.00794,"He":4.00260,"Li":6.941,"Be":9.01218,"B":10.81,"C":12.01,"N":14.007,"O":16.00,"F":18.9984,"Ne":20.180,"Na":22.99,"Mg":24.305,"Al":26.98,"Si":28.1,"P":30.97,"S":32.1,"Cl":35.45,"Ar":39.95,"K":39.10,"Ca":40.08,"Sc":44.96,"Ti":47.88,"V":50.94}

def inputCSV():
    while 1:
        with open('sample.csv') as f:
            reader = csv.reader(f)
            list = [row for row in reader]

            kind = float(row[0][0])
            if kind == "e":
                q = -1.6/10000000000000000000
                m = 9.11/10000000000000000000000000000000

            elif kind == "p":
                q = 1.6/10000000000000000000
                m = 1.673/1000000000000000000000000000

            else:
                m = (ion[kind]/Na)/1000
                val = float(row[0][1])
                q = val*1.6/10000000000000000000

            t_max = float(row[1][0])
            dt = t_max/10000
            t_repetition = t_max/dt

            x0 = float(row[3])
            x = np.empty((0,3), float)
            x = np.append(x, np.array([x0]), axis=0)
            v0 = float(row[4])
            v = np.empty((0,3), float)
            v = np.append(v, np.array([v0]), axis=0)
        return q, m, t_repetition, x, v

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
<<<<<<< HEAD
            Na = 6.02*100000000000000000000000
            m = mass/(Na/1000)
=======
            m = (mass/Na)/1000
>>>>>>> input
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

def inputManual():
    q, m = inputPar()
    t_repetition = inputTime()
    x = inputPos()
    v = inputVec()
    return q, m, t_repetition, x, v
