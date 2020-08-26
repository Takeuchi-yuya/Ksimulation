# 基本構造

### 始めに
- 追加事項があればその都度追記していく。
- この [命名規則](https://qiita.com/naomi7325/items/4eb1d2a40277361e898b) に則っていく
### 環境

- 私の開発エディタは [atom](https://atom.io)
- このファイルはmarkdownで書かれているのでatomでみる場合は、control+shift+mでPreviewをみる。
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
 （CAD、CLIどっちかもしくは両方？　両方の場合はmapはCAD、電磁場や粒子のパラメータをCLIで）

 　　↓　　　

演算処理 

- 基本的に、クーロン力、ローレンツ力を考慮した運動方程式と、ベーテブロッホの式から減衰を考える。

　　↓　

出力 OutPut.py
- matplotlibのグラフ出力を利用する。余裕があればアニメーションとかもやりたい！
- CADから3D描画したい [参照](https://resp-kke.azurewebsites.net/2020/02/24/programtipspython_plotly3d/)

### 追記
