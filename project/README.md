# 基本構造

### 始めに
これは、研究で粒子の軌道をシミュレーションするためのプログラムです。
電場、磁場、粒子の電価、初期位置初速を設定して軌跡をプロットすることを行う。
### 開発環境

- 開発エディタは [atom](https://atom.io)

```Python
 $ python --version
 Python 3.7.0

 $ python -c 'import matplotlib as mpl; print(mpl.__version__)'
 2.2.3

 $ python -c 'import csv as mpl; print(mpl.__version__)'
 1.0
```
### 基本方針

 入力 InPut.py
 基本csvで入力

 　　↓　　　

演算処理
- Runge–Kutta法を用いて演算していく。
- 基本的に、クーロン力、ローレンツ力を考慮した運動方程式と、ベーテブロッホの式から減衰を考える。

　　↓　

出力 OutPut.py
- matplotlibのグラフ出力を利用する。余裕があればアニメーションとかもやりたい！
- CADから3D描画したい [参照](https://resp-kke.azurewebsites.net/2020/02/24/programtipspython_plotly3d/)
