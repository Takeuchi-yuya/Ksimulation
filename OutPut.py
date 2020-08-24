import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

from CreatTestdata import SampleFunc as SF

#とりあえず、二次元三次元アニメーションを外で選択できるようにclassで書いていく。
class OutPut():
    def __init__(self,plams):
        self.title = plams["title"]
        self.x = plams["x"]
        self.y = plams["y"]
        self.z = plams["z"]

    #とりあえず、最初から三次元データが入力された状態で二次元に切り取って出力したい。
    #xy,yz,xzをそれぞれz,x,yで選択し値設定することで出力を試みる。
    def twoDPlot(self,ax,losAxis,value):
        horizontal_list = np.array([])
        vertical_list = np.array([])
        if "y" ==losAxis:
            horizontal_name = "x"
            vertical_name = "z"
            for tmp_x , check_y ,tmp_z in zip(self.x , self.y , self.z):
                if check_y == value:
                    horizontal_list = np.append(horizontal_list,float(tmp_x))
                    vertical_list = np.append(vertical_list , float(tmp_z))
        elif "z" ==losAxis:
            horizontal_name = "x"
            vertical_name = "y"
            for tmp_x , tmp_y ,check_z in zip(self.x , self.y , self.z):
                if check_z == value:
                    horizontal_list = np.append(horizontal_list,float(tmp_x))
                    vertical_list = np.append(vertical_list , float(tmp_y))
        else:
            horizontal_name = "y"
            vertical_name = "z"
            for check_x , tmp_y ,tmp_z in zip(self.x , self.y , self.z):
                if check_x == value:
                    horizontal_list = np.append(horizontal_list,float(tmp_y))
                    vertical_list = np.append(vertical_list , float(tmp_z))
        ax.scatter(horizontal_list,vertical_list)
        ax.set_title(self.title + " 2DPlot(" + losAxis +" = "+ str(value)+")")
        ax.set_xlabel(horizontal_name)
        ax.set_ylabel(vertical_name)

        return ax
    def threeDPlot(self,ax):
        ax.scatter3D(self.x,self.y,self.z)
        ax.set_title("Scatter Plot")
        return ax


    def vectorTwoDPlot(self,vf,ax,losAxis,value):
        grid_count = 10
        if losAxis == "x":
            horizontal_list = np.array([])
            vertical_list   = np.array([])
            U_list = np.array([])
            V_list = np.array([])
            max_y = max(self.y)
            min_y = min(self.y)
            max_z = max(self.z)
            min_z = min(self.z)
            for y in np.linspace(min_y,max_y,grid_count):
                for z in np.linspace(min_z,max_z,grid_count):
                    vector = vf.VectorField({"x":float(value),"y":y,"z":z})
                    if vector:
                        horizontal_list = np.append(horizontal_list,y)
                        vertical_list = np.append(vertical_list,z)
                        U_list = np.append(U_list,vector["y"])
                        V_list = np.append(V_list,vector["z"])
        elif losAxis == "y":
            horizontal_list = np.array([])
            vertical_list   = np.array([])
            U_list = np.array([])
            V_list = np.array([])
            max_x = max(self.x)
            min_x = min(self.x)
            max_z = max(self.z)
            min_z = min(self.z)
            for x in np.linspace(min_x,max_x,grid_count):
                for z in np.linspace(min_z,max_z,grid_count):
                    vector = vf.VectorField({"x":x , "y": value , "z":z})
                    if vector:
                        horizontal_list = np.append(horizontal_list,x)
                        vertical_list = np.append(vertical_list,z)
                        U_list = np.append(U_list,vector["x"])
                        V_list = np.append(V_list,vector["z"])
        else:
                horizontal_list = np.array([])
                vertical_list   = np.array([])
                U_list = np.array([])
                V_list = np.array([])
                max_y = max(self.y)
                min_y = min(self.y)
                max_x = max(self.x)
                min_x = min(self.x)
                for y in np.linspace(min_y,max_y,grid_count):
                    for x in np.linspace(min_x,max_x,grid_count):
                        vector = vf.VectorField({"x":x , "y":y , "z":value})
                        if vector:
                            horizontal_list = np.append(horizontal_list,x)
                            vertical_list = np.append(vertical_list,y)
                            U_list = np.append(U_list,vector["x"])
                            V_list = np.append(V_list,vector["y"])
        ax.quiver(horizontal_list,vertical_list,U_list,V_list,color='red',angles='xy',scale_units='xy', scale=6.5)
        return ax

#vectorをlistからdicに変換する。
def PosLToDic(pos):
    return {"x":pos[0] , "y":pos[1] , "z":pos[2]}

if __name__ == '__main__':
    print("test実行")
    with open('data/sample.csv') as f:
         reader = csv.reader(f)
         list = [row for row in reader]
    #dict型に変換
    plams = {}
    for l in list:
        if l[0] == "x" or l[0] == "y" or l[0] == "z":
            if l[0] in plams:
                plams[l[0]] = np.append(plams[l[0]],np.array([float(i) for i in l[1:]]))
            else:
                plams[l[0]] = np.array([float(i) for i in l[1:]])
        else:
            plams[l[0]] = l[1]
            
    #OutPutをインスタンス化のち、グラフのプロット
    oput = OutPut(plams)
    fig = plt.figure(figsize=(10, 7))
    ax = plt.subplot2grid((2,2),(0,0))
    ay = plt.subplot2grid((2,2),(0,1))
    az = plt.subplot2grid((2,2),(1,0))
    a3d = plt.subplot2grid((2,2),(1,1),projection='3d')
    ax = oput.twoDPlot(ax,"x",0)
    ay = oput.twoDPlot(ay,"y",0)
    az = oput.twoDPlot(az,"z",0)
    a3d = oput.threeDPlot(a3d)

    #vectorの出力テストを行うためにテストデータの作成とプロット
    s_pos = PosLToDic([-50,-50,-50])
    e_pos = PosLToDic([50,50,50])
    vector = PosLToDic([5,5,5])
    vf = SF(s_pos,e_pos,vector)
    ax = oput.vectorTwoDPlot(vf,ax,"x",0)
    ay = oput.vectorTwoDPlot(vf,ay,"y",0)
    az = oput.vectorTwoDPlot(vf,az,"z",0)
    plt.show()
