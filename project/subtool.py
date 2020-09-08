import numpy as np
#とりあえず小さめなdt（十分小さいかは不明)
dt = 10**(-5)
#とりあえず、電荷を気にせず特定の座標範囲に並行電場を生成する関数を作ってみる。
class SampleFunc():
    def __init__(self,s_pos,e_pos,vector):
        self.s_pos = s_pos
        self.e_pos = e_pos
        self.vector = vector
        self.zero_vector = {"x" : 0,"y" : 0 , "z" : 0}
    def VectorField(self,position):
        flag = True
        for ax in position:
            if self.s_pos[ax] <= position[ax] <= self.e_pos[ax]:
                 pass
            else:
                flag = False
        if flag:
            return self.vector
        else:
            return False

#vectorをlistからdicに変換する。
def PosLToDic(pos , title = ""):
    if title =="":
        return {"x":pos[0] , "y":pos[1] , "z":pos[2]}
    else:
        return {"x":pos[0] , "y":pos[1] , "z":pos[2] , "title":title}

def runge(Efield, Bfield, q, m, t_repetition, x, v):
    for i in range(t_repetition):
        dic_x = PosLToDic(x[i])
        E = Efield.VectorField(dic_x)
        E = [E["x"],E["y"],E["z"]]
        #E = np.array(E)
        B = Bfield.VectorField(dic_x)
        B = [B["x"],B["y"],B["z"]]
        #B = np.array(B)

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

    np.save('runge_posi',x)

    return x, v


def L2Nrom(pos1,pos2):
    return np.sqrt((pos1["x"]-pos2["x"])**2+(pos1["y"]-pos2["y"])**2+(pos1["z"]-pos2["z"])**2)

if __name__ == '__main__':
    print("test実行")
    s_pos = PosLToDic([-5,-5,-5])
    e_pos = PosLToDic([5,5,5])
    vector = PosLToDic([1,0,1])
    vf = SampleFunc(s_pos,e_pos,vector)
    pos = PosLToDic([0,0,0])
    tmp = vf.VectorField(pos)
    print(tmp)
