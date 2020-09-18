import numpy as np
import math as ma
import csv
import json

Na = 6.02*100000000000000000000000
q_e = 1.6/10000000000000000000

#原子量のディクショナリ
atm = {"H":1.00794,"He":4.00260,"Li":6.941,"Be":9.01218,"B":10.81,"C":12.01,"N":14.007,"O":16.00,"F":18.9984, \
    "Ne":20.180,"Na":22.99,"Mg":24.305,"Al":26.98,"Si":28.1,"P":30.97,"S":32.1,"Cl":35.45,"Ar":39.95,"K":39.10, \
    "Ca":40.08,"Sc":44.96,"Ti":47.88,"V":50.94,"Cr":52.00,"Mn":54.94,"Fe":55.85,"Co":58.93,"Ni":58.69,"Cu":63.55, \
    "Zn":65.39,"Ga":69.72,"Ge":72.61,"As":74.92,"Se":78.96,"Br":79.90,"Kr":83.80,"Rb":85.47,"Sr":87.62,"Y":88.91, \
    "Zr":91.22,"Nb":92.91,"Mo":95.94,"Tc":99,"Ru":101.1,"Rh":102.9,"Pb":106.4,"Ag":107.9,"Cd":112.4,"In":114.8, \
    "Sn":118.7,"Sb":121.8,"Te":127.6,"I":126.9,"Xe":131.3,"Cs":132.9,"Ba":137.3,"La":138.9,"Ce":140.1,"Pr":140.9, \
    "Nd":144.2}
input_PATH = 'functions/data/'
def inputCSV(name):
    path = input_PATH + name +'.csv'
    particlePlams = []
    with open(path) as f:
        reader = csv.reader(f)
        list = [row for row in reader]

    #使う変数を初期化
    #電場
    E_start = {}
    E_end = {}
    E_vec = {}
    #磁場
    B_start = {}
    B_end = {}
    B_vec = {}
    #ラベル
    name = np.empty(0)
    #粒子の種類
    kind = np.empty(0)
    #価数
    val = np.empty(0)
    #初期位置
    pos = np.empty((0,3), float)
    #初速度
    vec = np.empty((0,3), float)

    #この後に計算する電荷と質量
    q = np.empty(0)
    m = np.empty(0)

    for i in range(len(list)):
        header = list[i][0]
        if header=="Efield":
            E_start["x"] = float(list[i][2])
            E_start["y"] = float(list[i][4])
            E_start["z"] = float(list[i][6])
            E_end["x"] = float(list[i][9])
            E_end["y"] = float(list[i][11])
            E_end["z"] = float(list[i][13])
            E_vec["x"] = float(list[i][16])
            E_vec["y"] = float(list[i][18])
            E_vec["z"] = float(list[i][20])
        elif header=="Bfield":
            B_start["x"] = float(list[i][2])
            B_start["y"] = float(list[i][4])
            B_start["z"] = float(list[i][6])
            B_end["x"] = float(list[i][9])
            B_end["y"] = float(list[i][11])
            B_end["z"] = float(list[i][13])
            B_vec["x"] = float(list[i][16])
            B_vec["y"] = float(list[i][18])
            B_vec["z"] = float(list[i][20])
        elif header=="name":
            name_in = list[i][1]
            name = np.append(name, name_in)
        elif header=="kind":
            kind_in = list[i][1]
            kind = np.append(kind, kind_in)
        elif header=="val":
            val_in = int(list[i][1])
            val = np.append(val, val_in)
        elif header=="pos":
            pos0 = [float(list[i][a]) for a in range(1,4)]
            pos = np.append(pos, np.array([pos0]), axis=0)
        elif header=="vec":
            vec0 = [float(list[i][a]) for a in range(1,4)]
            vec = np.append(vec, np.array([vec0]), axis=0)

    for i in range(len(kind)):
        if kind[i] == "e":
            q0 = -q_e
            m0 = 9.11/10000000000000000000000000000000
        elif kind[i] == "p":
            q0 = q_e
            m0 = 1.673/1000000000000000000000000000
        else:
            q0 = val[i]*q_e
            m0 = atm[kind[i]]/Na/1000
        m = np.append(m, m0)
        q = np.append(q, q0)

    for i in range(len(kind)):
        particlePlams.append({
                                "name":     name[i],
                                "kind":     kind[i],
                                "val":      val[i],
                                "pos":      pos[i],
                                "vec":      vec[i],
                                "q":        q[i],
                                "m":        m[i],
                                })

    inputDataSet = {
                     "EFieldplams": {
                                    "startPos":  E_start,
                                    "endPos":    E_end,
                                    "vector":    E_vec,
                     },
                     "BFieldplams": {
                                    "startPos":  B_start,
                                    "endPos":    B_end,
                                    "vector":    B_vec,
                     },
                     "particlePlams": particlePlams,
    }




    return inputDataSet

def inputJson(name):
    path = input_PATH + name +'.json'
    with open(path, 'r') as f:
        inputDataSet = json.load(f)

    for num in range(len(inputDataSet["particlePlams"])):
        if inputDataSet["particlePlams"][num]["kind"] == "e":
            q = -q_e
            m = 9.11/10000000000000000000000000000000
        elif inputDataSet["particlePlams"][num]["kind"] == "p":
            q = q_e
            m = 1.673/1000000000000000000000000000
        else:
            q = inputDataSet["particlePlams"][num]["val"]*q_e
            m = atm[inputDataSet["particlePlams"][num]["kind"]]/Na/1000
        inputDataSet["particlePlams"][num]["q"] = q
        inputDataSet["particlePlams"][num]["m"] = m
    return inputDataSet

def inputManual():
    q, m = inputPar()
    x0 = inputPos()
    v0 = inputVec()
    return q, m, x0, v0

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
            m = (mass/Na)/1000

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
