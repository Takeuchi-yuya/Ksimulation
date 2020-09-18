import numpy as np
import scipy.constants as cons

class Efield():
    def __init__(self, facts):
        self.facts = facts
    def VectorField(self,pos):
        force = np.array([0,0,0])

        #他の質点とのクーロン力
        k = 1/(4 * cons.pi)*1/cons.epsilon_0
        for fact in self.facts:
            #print(str(pos))
            #print(str(fact))
            r  = np.sqrt((pos["x"]-fact["x"])**2 + (pos["y"]-fact["y"])**2 + (pos["z"]-fact["z"])**2 )
            vec_r = np.array([pos["x"]-fact["x"],pos["y"]-fact["y"],pos["z"]-fact["z"]])
            f = k*fact["Q"]/r**3*vec_r
            force  = f + force

        #磁場によるローレンツ力の項の計算は後回し
        return {"x":force[0],"y":force[1],"z":force[2]}
    def OutPutVectorField(self,pos):
        force = np.array([0,0,0])

        #他の質点とのクーロン力
        k = 1/(4 * cons.pi)*1/cons.epsilon_0
        for fact in self.facts:
            #print(str(pos))
            #print(str(fact))
            r  = np.sqrt((pos["x"]-fact["x"])**2 + (pos["y"]-fact["y"])**2 + (pos["z"]-fact["z"])**2 )
            vec_r = np.array([pos["x"]-fact["x"],pos["y"]-fact["y"],pos["z"]-fact["z"]])
            f = k*fact["Q"]/r**3*vec_r
            force  = f + force

        #磁場によるローレンツ力の項の計算は後回し
        return {"x":force[0],"y":force[1],"z":force[2]}
def makeGridParticle(Q):
    z1 = -0.1
    z2 = 0.1
    length =0.2
    grid = 100
    q = Q/grid**2
    facts = []
    for x in np.arange(-length/2,length/2,grid):
        for y in np.arange(-length/2,length/2,grid):
            facts.append({"x":x,"y":y,"z":z1,"Q":q})
            facts.append({"x":x,"y":y,"z":z2,"Q":-q})
    return facts
