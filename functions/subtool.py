import numpy as np
#とりあえず小さめなdt（十分小さいかは不明)
#Eの確認は10**(-8)、Bの確認は10**(-6)
dt = 10**(-8)
#とりあえず、電荷を気にせず特定の座標範囲に並行電場を生成する関数を作ってみる。
class SampleFunc():
    def __init__(self,fieldplams):
        #print("setdata" + str(s_pos) + str(e_pos) + str(vector))
        self.s_pos = fieldplams["startPos"]
        self.e_pos = fieldplams["endPos"]
        self.vector = fieldplams["vector"]
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

def runge(Efield, Bfield, pPlams):
    q = pPlams["q"]
    m = pPlams["m"]
    pos0 = pPlams["pos"]
    vec0 = pPlams["vec"]
    pos = np.empty((0,3), float)
    pos = np.append(pos, np.array([pos0]), axis=0)
    vec = np.empty((0,3), float)
    vec = np.append(vec, np.array([vec0]), axis=0)
    i = 0
    limit = 20063
    flag = False
    while 1:
        t = i*dt
        dic_x = PosLToDic(pos[i])
        E = Efield.VectorField(dic_x)
        E = [E["x"],E["y"],E["z"]]

        B = Bfield.VectorField(dic_x)
        B = [B["x"],B["y"],B["z"]]

        k1_x = vec[i]
        k1_v = Force(t, pos[i], vec[i], E, B, q, m)
        k2_x = vec[i] + k1_v*dt/2
        k2_v = Force(t + dt/2, pos[i] + k1_x*dt/2, vec[i] + k1_v*dt/2, E, B, q, m)
        k3_x = vec[i] + k2_v*dt/2
        k3_v = Force(t + dt/2, pos[i] + k2_x*dt/2, vec[i] + k2_v*dt/2, E, B, q, m)
        k4_x = vec[i] + k3_v*dt
        k4_v = Force(t + dt, pos[i] + k3_x*dt, vec[i] + k3_v*dt, E, B, q, m)

        vec_tem = vec[i] + dt*(k1_v + 2*k2_v + 2*k3_v + k4_v)/6
        vec = np.append(vec, np.array([vec_tem]), axis=0)
        pos_tem = pos[i] + dt*(k1_x + 2*k2_x + 2*k3_x + k4_x)/6
        pos = np.append(pos, np.array([pos_tem]), axis=0)

        i = i + 1

        if i%1000 == 0:
            print(i, "回目のループです")

        for j in range(3):

            if pos_tem[j] < -0.4:
                flag = True
            elif pos_tem[j] > 0.4:
                flag = True

        if flag:
            break

        if i > limit:
            break

    np.save('runge_posi',pos)

    return pos, vec
def NewRunge(Efield, Bfield,pPlams):
    q = pPlams["q"]
    m = pPlams["m"]
    pos0 = pPlams["pos"]
    vec0 = pPlams["vec"]
    pos = np.empty((0,3), float)
    pos = np.append(pos, np.array([pos0]), axis=0)
    vec = np.empty((0,3), float)
    vec = np.append(vec, np.array([vec0]), axis=0)
    timestamp = [0]
    i = 0
    limit = float("inf")
    t = 0
    flag = False
    while 1:
        dic_x = PosLToDic(pos[i])
        E = Efield.VectorField(dic_x)
        B = Bfield.VectorField(dic_x)
        #力の強いところで細かく刻む
        if E == {"x" : 0,"y" : 0 , "z" : 0} and B == {"x" : 0,"y" : 0 , "z" : 0}:
            tmp_dt = dt *100
        else:
            tmp_dt = dt
        t = t + tmp_dt
        timestamp.append(t)
        B = [B["x"],B["y"],B["z"]]
        E = [E["x"],E["y"],E["z"]]
        k1_x = vec[i]
        k1_v = Force(t, pos[i], vec[i], E, B, q, m)
        k2_x = vec[i] + k1_v*tmp_dt/2
        k2_v = Force(t + tmp_dt/2, pos[i] + k1_x*tmp_dt/2, vec[i] + k1_v*tmp_dt/2, E, B, q, m)
        k3_x = vec[i] + k2_v*tmp_dt/2
        k3_v = Force(t + tmp_dt/2, pos[i] + k2_x*tmp_dt/2, vec[i] + k2_v*tmp_dt/2, E, B, q, m)
        k4_x = vec[i] + k3_v*tmp_dt
        k4_v = Force(t + tmp_dt, pos[i] + k3_x*tmp_dt, vec[i] + k3_v*tmp_dt, E, B, q, m)

        vec_tem = vec[i] + tmp_dt*(k1_v + 2*k2_v + 2*k3_v + k4_v)/6
        vec = np.append(vec, np.array([vec_tem]), axis=0)
        pos_tem = pos[i] + tmp_dt*(k1_x + 2*k2_x + 2*k3_x + k4_x)/6
        pos = np.append(pos, np.array([pos_tem]), axis=0)

        i = i + 1

        if i%1000 == 0:
            print(i, "回目のループです")

        for j in range(3):

            if pos_tem[j] < -0.4:
                flag = True
            elif pos_tem[j] > 0.4:
                flag = True

        if flag:
            break

        if i > limit:
            break

    np.save('runge_posi',pos)

    return pos, vec, timestamp

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
