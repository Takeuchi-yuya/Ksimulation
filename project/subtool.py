import numpy as np
#とりあえず小さめなdt（十分小さいかは不明)
dt = 10**(-8)
#とりあえず、電荷を気にせず特定の座標範囲に並行電場を生成する関数を作ってみる。
class SampleFunc():
    def __init__(self,s_pos,e_pos,vector):
        print("setdata" + str(s_pos) + str(e_pos) + str(vector))
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
            return self.zero_vector
    def OutPutVectorField(self,position):
        flag = True
        for ax in position:
            if self.s_pos[ax]*1000 <= position[ax] <= self.e_pos[ax]*1000:
                 pass
            else:
                flag = False
        if flag:
            return self.vector
        else:
            return self.zero_vector

#vectorをlistからdicに変換する。
def PosLToDic(pos , title = ""):
    if title =="":
        return {"x":pos[0] , "y":pos[1] , "z":pos[2]}
    else:
        return {"x":pos[0] , "y":pos[1] , "z":pos[2] , "title":title}

def Force(t, x, v, E, B, q, m):
    u = np.cross(v, B)
    f = q*(E + u)/m
    return f


def runge(Efield, Bfield, q, m, x0, v0):
    x = np.empty((0,3), float)
    x = np.append(x, np.array([x0]), axis=0)
    v = np.empty((0,3), float)
    v = np.append(v, np.array([v0]), axis=0)
    i = 0
    limit = 10000
    while 1:
        t = i*dt
        dic_x = PosLToDic(x[-1])
        E = Efield.VectorField(dic_x)
        E = [E["x"],E["y"],E["z"]]

        B = Bfield.VectorField(dic_x)
        B = [B["x"],B["y"],B["z"]]

        k1_x = v[i]
        k1_v = Force(t, x[i], v[i], E, B, q, m)
        k2_x = v[i] + k1_v*dt/2
        k2_v = Force(t + dt/2, x[i] + k1_x*dt/2, v[i] + k1_v*dt/2, E, B, q, m)
        k3_x = v[i] + k2_v*dt/2
        k3_v = Force(t + dt/2, x[i] + k2_x*dt/2, v[i] + k2_v*dt/2, E, B, q, m)
        k4_x = v[i] + k3_v*dt
        k4_v = Force(t + dt, x[i] + k3_x*dt, v[i] + k3_v*dt, E, B, q, m)

        v_tem = v[i] + dt*(k1_v + 2*k2_v + 2*k3_v + k4_v)/6
        v = np.append(v, np.array([v_tem]), axis=0)
        x_tem = x[i] + dt*(k1_x + 2*k2_x + 2*k3_x + k4_x)/6
        x = np.append(x, np.array([x_tem]), axis=0)

        #print(x_tem)

        i = i + 1

        if x_tem[2] < -0.4:
            break
        elif x_tem[2] > 0.4:
            break
        elif i > limit:
            break

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
