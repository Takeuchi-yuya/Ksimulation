import numpy as np
import scipy.constants as cons
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
import subtool as sb
class Calculation():
    def __init__(self,ID,pos,vec,Q,time = 0):
        #とりあえずいらないかもしれないが粒子のそれぞれをきていするID
        self.ID = ID
        self.pos = pos
        self.vec = vec
        self.time = time # 開始時間
        self.Q = Q
    def set_force(self,particleList):
        force = np.array([0,0,0])

        #他の質点とのクーロン力
        k = 1/(4 * cons.pi)*1/cons.epsilon_0

        for p in particleList:

            if self.ID == p.ID:
                continue
            r  = sb.L2Nrom(self.pos,p.pos)
            dr = np.array([self.pos["x"]-p.pos["x"],self.pos["y"]-p.pos["y"],self.pos["z"]-p.pos["z"]])
            f = k*self.Q*p.Q/r**3*dr
            force  = f + force

        #磁場によるローレンツ力の項の計算は後回し
        self.force = sb.PosLToDic(force)
        return list(force)
    def calVector(self,t_repetition):
        for i in range(t_repetition):
            v1 = v[i]
            u1 = np.cross(v1,B)
            k1 = q*(E + u1)/m

            v2 = v1 + k1*dt/2
            u2 = np.cross(v2,B)
            k2 = q*(E + u2)/m

            v3 = v1 + k2*dt/2
            u3 = np.cross(v3,B)
            k3 = q*(E + u3)/m

            v4 = v1 + k3*dt
            u4 = np.cross(v4,B)
            k4 = q*(E + u4)/m

            v_tem = v[i] + dt*(k1 + 2*k2 + 2*k3 + k4)/6
            v = np.append(v, np.array([v_tem]), axis=0)

        return v.T

if __name__ == "__main__":
    print("test実行")
    test ={
        "name"  : "粒子二つ",
        "in" : [
            {
            "ID"    : "粒子１",
            "pos"   :{"x":0.0,"y":0.0,"z":0.0},
            "vec"   :{"x":0.0,"y":0.0,"z":0.0},
            "Q"     :5.0
            },
            {
            "ID"    : "粒子2",
            "pos"   :{"x":5.0,"y":0.0,"z":0.0},
            "vec"   :{"x":0.0,"y":0.0,"z":0.0},
            "Q"     :10.0
            }

        ],
        "want" :[[-1.7975103574736355*10**10, 0.00000000, 0.00000000],[1.7975103574736355*10**10, 0.00000000, 0.00000000]]
    }
    pl = []
    for IN in test["in"]:
        pl.append(Calculation(IN["ID"],IN["pos"],IN["vec"],IN["Q"]))
    print("check set_force")
    flag = True
    for p ,w in zip(pl,test["want"]):
        if w != p.set_force(pl):
            flag = False
            print("not match")
            print("w=",w)
            print("set_force=",p.set_force(pl))
    if flag:
        print("Ok")
