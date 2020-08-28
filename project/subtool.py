import numpy as np
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
