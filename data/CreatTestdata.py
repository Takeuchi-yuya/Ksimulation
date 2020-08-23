
#とりあえず、電荷を気にせず特定の座標範囲に並行電場を生成する関数を作ってみる。
class SampleFunc():
    def __init__(self,s_pos,e_pos,vector):
        self.s_pos = s_pos
        self.e_pos = e_pos
        self.vector = vector
        self.zero_vector = {"x" : 0,"y" : 0 , "z" : 0}
    def SampleVectorField(position):
        flag = True
        for ax in position:
            if s_pos[ax] <= position[ax] <= e_pos[ax]:
                 pass
            else:
                flag = False
        if flag:
            return self.E
        else:
            return self.zero_vector
