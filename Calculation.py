import numpy as np
import scipy.constants as cons
import subtool as sb
class Calculation():
    __init__(self,ID,pos,vec,Q,time = 0):
    #とりあえずいらないかもしれないが粒子のそれぞれをきていするID
    self.ID = ID
    self.pos = pos
    self.vec = vec
    self.time = time
    self.Q = Q
    def set_force(self,particleList):
        force = np.array([0,0,0])

        #他の質点とのクーロン力
        k = 1/(4 * cons.pi)*1/cons.epsilon_0
        for p in particleList:
            r  = sb.L2Nrom(self.pos,p.pos)
            dr = np.array([self.pos["x"]-p.pos["x"],self.pos["y"]-p.pos["y"],self.pos["z"]-p.pos["z"]])
            f = k*self.Q*p.pos/r**3*dr
            force += f

        #磁場によるローレンツ力の項の計算は後回し

        return force
