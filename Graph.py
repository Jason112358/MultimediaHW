# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:13:30 2019

@author: Jason Xu
"""
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt

N = open("X:\\0931Xu\\Study\\多媒体技术\\Homework\\第四次作业\\structure.col")
i = 0
matrix = np.zeros((501,501),dtype = 'int16')    # 创建500*500全零二维数组
Colors = np.zeros(501,dtype = 'int16')  # 创建规模500的全零一维数组
G = nx.Graph()

for line in N:
    if line[0] in ['E','e']:
        node1=""
        node2=""
        r = 2
        while line[r] not in [' ']:
            node1 += line[r]
            r = r+1
        r = r+1
        while line[r] not in [' ','\n']:
            node2 += line[r]
            r = r+1
        Node1 = int(node1)  #传入结点1
        Node2 = int(node2)  #传入结点2
        matrix[Node1][Node2] = 1
        G.add_edge(Node1,Node2)
#        print(line[0:-1])
N.close()
pos = nx.spring_layout(G)
"""
for m in range(1,50):
    for n in range(1,5):
        print(matrix[m][n])
"""
C = open("X:\\0931Xu\\Study\\多媒体技术\\Homework\\第四次作业\\coloring.txt")
r = 0
R = 0
color = ''
flag = 0
for line in C:
    for tmp in range(0,501):
        color = ''
        while line[r] not in ['\n',' ']:       
            color += line[r]
            r = r+1
            flag = 1    #表示有新数据
        if line[r] in ['\n']:   #当结束时退出循环
            break
        if flag == 1:   #若有新数据则添加
            Colors[R] = int(color)  #记录该点颜色
            r = r+1
            R = R+1
            flag = 0    #重置标记

C.close()#关闭color文件

nx.draw_networkx_nodes(G,pos,node_size=40,node_color=Colors[0:500]) #数组长度不匹配时有错误
nx.draw_networkx_edges(G,pos)   #画边
#nx.draw_networkx_labels(G,pos) #标记点的标签

plt.axis('off') #无坐标系
#plt.savefig("color_nodes_labels.png",dpi=200)#规定像素保存图像
plt.show()#显示在console中