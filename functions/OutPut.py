import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
import csv
from . import subtool as sub
#from CreatTestdata import SampleFunc as SF
#とりあえず、二次元三次元アニメーションを外で選択できるようにclassで書いていく。

class OutPut():
    def __init__(self,OPD,horizontalLim = 4000,verticalLim = 4000):
        self.title = OPD["pData"]["title"]
        self.x = OPD["pData"]["x"]
        self.y = OPD["pData"]["y"]
        self.z = OPD["pData"]["z"]
        self.timestamp = OPD["pData"]["timestamp"]
        self.q = OPD["pData"]["q"]
        self.E = OPD["E"]
        self.B = OPD["B"]
        self.horizontalLim = horizontalLim
        self.verticalLim = verticalLim
    #とりあえず、最初から三次元データが入力された状態で二次元に切り取って出力したい。
    #xy,yz,xzをそれぞれz,x,yで選択し値設定することで出力を試みる。
    def TimePlot(self , axis):
        starttime = 0
        dt = sub.dt
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
        fig = plt.figure()
        ax = plt.subplot2grid((1,1),(0,0))
        #a3d = plt.subplot2grid((1,2),(0,1),projection='3d')
        ax = self.twoDPlot(ax,"y")
        #a3d = self.threeDPlot(a3d)


        if self.E != "":
            ax = self.vectorTwoDPlot(self.E,ax,"y",'E')
        if self.B != "":
            ax = self.vectorTwoDPlot(self.B ,ax,"y",'B')
        plt.tight_layout()
        plt.show()


    def twoDPlot(self,ax,losAxis,value = ""):
        #UnboundLocalErrorがでたので初期化
        horizontal_name = ""
        vertical_name = ""
        
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
        ax.legend(markerscale = 10, ncol=2)
        ax.grid()
        ax.set_xlabel(horizontal_name + "[mm]")
        ax.set_ylabel(vertical_name + "[mm]")
        ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(10))
        ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))
        ax.tick_params(axis = "x",top = True,labeltop = True,labelrotation = 45 , which = "both")
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
        print("vectorplot start")
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
        print("end")
        #bairitu
        #magnification = 10
        if type == 'E':
            magnification = 0.001
            print(U_list)
            print(V_list)
            ax.quiver(horizontal_list,vertical_list,magnification*U_list,magnification*V_list,color = 'red' ,angles='xy',scale_units='xy', scale=6.5)
        elif type == 'B':
            magnification = 8
            #print(U_list)
            #print(V_list)
            ax.quiver(horizontal_list,vertical_list,magnification*magnification*magnification*magnification*U_list,magnification*magnification*magnification*V_list,color = 'blue' ,angles='xy',scale_units='xy', scale=6.5)
        else:

            ax.quiver(horizontal_list,vertical_list,magnification*magnification*U_list,magnification*V_list,color = 'black' ,angles='xy',scale_units='xy', scale=6.5)
        ax.set_xlim([-self.horizontalLim,self.horizontalLim])
        ax.set_ylim([-self.verticalLim,self.verticalLim])
        return ax
