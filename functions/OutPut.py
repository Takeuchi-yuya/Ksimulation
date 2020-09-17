import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
from . import subtool as sb
#from CreatTestdata import SampleFunc as SF
#とりあえず、二次元三次元アニメーションを外で選択できるようにclassで書いていく。

class OutPut():
    def __init__(self,plams,E = "",B = "",horizontalLim = 4000,verticalLim = 4000,timestamp = ""):
        self.title = [plams["title"]]
        self.x = [plams["x"]]
        self.y = [plams["y"]]
        self.z = [plams["z"]]
        self.E = E
        self.B = B
        self.horizontalLim = horizontalLim
        self.verticalLim = verticalLim
        starttime = 0
        endtime = starttime + len(self.x)*sb.dt
        if timestamp == "":
            timestamp = np.arange(starttime , endtime , sb.dt)
        self.timestamp = [timestamp]
    #とりあえず、最初から三次元データが入力された状態で二次元に切り取って出力したい。
    #xy,yz,xzをそれぞれz,x,yで選択し値設定することで出力を試みる。
    def AddPlams(self , plams ,timestamp = ""):
        self.title.append(plams["title"])
        self.x.append(plams["x"])
        self.y.append(plams["y"])
        self.z.append(plams["z"])
        starttime = 0
        endtime = starttime + len(self.x)*sb.dt
        if timestamp == "":
            timestamp = np.arange(starttime , endtime , sb.dt)
        self.timestamp.append(timestamp)
    def TimePlot(self , axis):
        starttime = 0
        dt = sb.dt
        for x,y,z,title,timestamp in zip(self.x,self.y,self.z,self.title,self.timestamp):
            if axis =="x":
                plt.plot(timestamp,x)
                plt.ylabel("x[mm]")
            elif axis =="y":
                plt.plot(timestamp,y)
                plt.ylabel("y[mm]")

            else:
                plt.scatter(timestamp,z)
                plt.ylabel("z[mm]")
            plt.xlabel("timestamp[div/" +str(dt) + "]")
            plt.title(title)
            plt.show()



    def Show(self):
        fig = plt.figure(figsize=(10, 7))
        ax = plt.subplot2grid((2,2),(0,0))
        ay = plt.subplot2grid((2,2),(0,1))
        az = plt.subplot2grid((2,2),(1,0))
        a3d = plt.subplot2grid((2,2),(1,1),projection='3d')
        ax = self.twoDPlot(ax,"x")
        ay = self.twoDPlot(ay,"y")
        az = self.twoDPlot(az,"z")
        a3d = self.threeDPlot(a3d)


        if self.E != "":
            ax = self.vectorTwoDPlot(self.E,ax,"x",'E')
            ay = self.vectorTwoDPlot(self.E,ay,"y",'E')
            az = self.vectorTwoDPlot(self.E,az,"z",'E')
        if self.B != "":
            ax = self.vectorTwoDPlot(self.B ,ax,"x",'B')
            ay = self.vectorTwoDPlot(self.B ,ay,"y",'B')
            az = self.vectorTwoDPlot(self.B ,az,"z",'B')
        plt.tight_layout()
        plt.show()


    def twoDPlot(self,ax,losAxis,value = ""):
        for x,y,z,title in zip(self.x,self.y,self.z,self.title):
            horizontal_list = np.array([])
            vertical_list = np.array([])
            if "y" ==losAxis:
                horizontal_name = "x"
                vertical_name = "z"
                if value =="":
                    horizontal_list = np.array(x)
                    vertical_list = np.array(z)
                else:
                    for tmp_x , check_y ,tmp_z in zip(x , y , z):
                        if check_y == value:
                            horizontal_list = np.append(horizontal_list,float(tmp_x))
                            vertical_list = np.append(vertical_list , float(tmp_z))
            elif "z" ==losAxis:
                horizontal_name = "x"
                vertical_name = "y"
                if value =="":
                    horizontal_list = np.array(x)
                    vertical_list = np.array(y)
                else:
                    for tmp_x , tmp_y ,check_z in zip(x , y , z):
                        if check_z == value:
                            horizontal_list = np.append(horizontal_list,float(tmp_x))
                            vertical_list = np.append(vertical_list , float(tmp_y))
            else:
                horizontal_name = "y"
                vertical_name = "z"
                if value =="":
                    horizontal_list = np.array(y)
                    vertical_list = np.array(z)
                else:
                    for check_x , tmp_y ,tmp_z in zip(x , y , z):
                        if check_x == value:
                            horizontal_list = np.append(horizontal_list,float(tmp_y))
                            vertical_list = np.append(vertical_list , float(tmp_z))
            ax.scatter(horizontal_list,vertical_list ,s = 0.1 , label = title)
        if value == "":
            ax.set_title(" 2DPlot(" + horizontal_name + vertical_name +")")
        else:
            ax.set_title(" 2DPlot(" + losAxis +" = "+ str(value)+")")
        ax.legend()
        ax.set_xlabel(horizontal_name + "[mm]")
        ax.set_ylabel(vertical_name + "[mm]")
        ax.set_xlim([-self.horizontalLim,self.horizontalLim])
        ax.set_ylim([-self.verticalLim,self.verticalLim])
        return ax

    def threeDPlot(self,ax):
        for x,y,z in zip(self.x,self.y,self.z):
            ax.scatter3D(x,y,z, s = 0.05)
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        ax.set_title("Scatter Plot")
        ax.set_xlim([-self.horizontalLim,self.horizontalLim])
        ax.set_ylim([-self.verticalLim,self.verticalLim])
        return ax


    def vectorTwoDPlot(self,vf,ax,losAxis,type,value = 0):
        grid_count = 100
        horizontal_list = np.array([])
        vertical_list   = np.array([])
        U_list = np.array([])
        V_list = np.array([])
        for horizontal in np.linspace(-self.horizontalLim,self.horizontalLim,grid_count):
            for vertical in np.linspace(-self.verticalLim,self.verticalLim,grid_count):
                if losAxis == "x":
                    vector = vf.OutPutVectorField({"x":float(value),"y":horizontal,"z":vertical})
                    if vector != {"x" : 0,"y" : 0 , "z" : 0}:
                        horizontal_list = np.append(horizontal_list,horizontal)
                        vertical_list = np.append(vertical_list,vertical)
                        U_list = np.append(U_list,vector["y"])
                        V_list = np.append(V_list,vector["z"])
                elif losAxis == "y":
                    vector = vf.OutPutVectorField({"x":horizontal , "y": float(value) , "z":vertical})
                    if vector != {"x" : 0,"y" : 0 , "z" : 0}:
                        horizontal_list = np.append(horizontal_list,horizontal)
                        vertical_list = np.append(vertical_list,vertical)
                        U_list = np.append(U_list,vector["x"])
                        V_list = np.append(V_list,vector["z"])
                else:
                    vector = vf.OutPutVectorField({"x":horizontal , "y":vertical , "z":float(value)})
                    if vector != {"x" : 0,"y" : 0 , "z" : 0}:
                        horizontal_list = np.append(horizontal_list,horizontal)
                        vertical_list = np.append(vertical_list,vertical)
                        U_list = np.append(U_list,vector["x"])
                        V_list = np.append(V_list,vector["y"])
        #bairitu
        magnification = 10
        if type == 'E':
            #print(U_list)
            #print(V_list)
            ax.quiver(horizontal_list,vertical_list,magnification*U_list,magnification*V_list,color = 'red' ,angles='xy',scale_units='xy', scale=6.5)
        elif type == 'B':
            #print(U_list)
            #print(V_list)
            ax.quiver(horizontal_list,vertical_list,magnification*magnification*magnification*magnification*U_list,magnification*magnification*magnification*V_list,color = 'blue' ,angles='xy',scale_units='xy', scale=6.5)
        else:

            ax.quiver(horizontal_list,vertical_list,magnification*magnification*U_list,magnification*V_list,color = 'black' ,angles='xy',scale_units='xy', scale=6.5)
        ax.set_xlim([-self.horizontalLim,self.horizontalLim])
        ax.set_ylim([-self.verticalLim,self.verticalLim])
        return ax