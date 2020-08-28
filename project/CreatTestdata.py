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
            return self.zero_vector


if __name__ == '__main__':
    import OutPut as op
    print("test実行")
    s_pos = op.PosLToDic([-5,-5,-5])
    e_pos = op.PosLToDic([5,5,5])
    vector = op.PosLToDic([1,0,1])
    vf = SampleFunc(s_pos,e_pos,vector)
    pos = op.PosLToDic([0,0,0])
    tmp = vf.VectorField(pos)
    print(tmp)
