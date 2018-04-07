#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import matplotlib.pyplot as plt


def pie(dataList):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    labels=list(dataList.keys())
    datas=list(dataList.values())  
    plt.figure(1, figsize=(6,6))  
    colors  = ["blue","red","coral","green","yellow","orange"]  #设置颜色（循环显示）  
    plt.pie(datas,colors=colors, labels=labels, shadow=True)  
    plt.title('商品分布', bbox={'facecolor':'0.8', 'pad':5})  
    plt.show()
    plt.close()  


