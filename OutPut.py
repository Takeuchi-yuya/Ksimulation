import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv


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
        ax.set_title(self.title + " TwoDPlot")
        ax.set_xlabel(horizontal_name)
        ax.set_ylabel(vertical_name)

        return ax
    def threeDPlot(self,ax):
        x = np.array([float(i) for i in self.x])
        y = np.array([float(i) for i in self.y])
        z = np.array([float(i) for i in self.z])
        ax.scatter3D(x,y,z)
        ax.set_title("Scatter Plot")
        return ax

if __name__ == '__main__':
    print("test実行")
    with open('data/sample.csv') as f:
         reader = csv.reader(f)
         list = [row for row in reader]
    #dict型に変換
    plams = {"title":"testdata"}
    for l in list:
        plams[l[0]] = l[1:]
    oput = OutPut(plams)
    fig = plt.figure(figsize=(12, 8))
    ax = plt.subplot2grid((2,2),(0,0))
    ay = plt.subplot2grid((2,2),(0,1))
    az = plt.subplot2grid((2,2),(1,0))
    a3d = plt.subplot2grid((2,2),(1,1),projection='3d')
    ax = oput.twoDPlot(ax,"x","0")
    ay = oput.twoDPlot(ay,"y","0")
    az = oput.twoDPlot(az,"z","0")
    a3d = oput.threeDPlot(a3d)
    plt.show()
