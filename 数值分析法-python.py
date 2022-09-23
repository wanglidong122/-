#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 初始数据准备，前面是一组未调用的数据，以下数据来自[1] 赵小柠.物流中心规划与设计[M].成都：西南交通出版社，2011. P63.
"""
P = [['X', 'Y', 'V', 'R', 'd'],
     [3, 8, 2000, 0.05, 1],
     [8, 2, 3000, 0.05, 1]]
M = [['X', 'Y', 'V', 'R', 'd'],
     [2, 5, 2520, 0.075, 1],
     [6, 4, 1000, 0.075, 1],
     [8, 8, 1500, 0.075, 1]]
"""
import matplotlib.pyplot as plt

P = [['X', 'Y', 'V', 'R', 'd'],
     [9, 8, 1971, 0.05, 1],
     [7, 10, 3496, 0.05, 1]]
M = [['X', 'Y', 'V', 'R', 'd'],
     [13, 4, 2520, 0.07, 1],
     [5, 12, 1334, 0.07, 1],
     [11, 6, 1613, 0.07, 1]]
all_data = P[1:] + M[1:]
n_, x_, y_, m_, xy = [], [], [], [], []


# 绘图函数，需要预先安装matplotlib库
# 包括成本变化曲线图，X，Y坐标值变化趋势图和物流中心定位变化图。
def draw(b):
    global n_, x_, y_, m_, xy, P, M
    plt.figure()
    plt.title('Cost Change Chart')
    plt.ylabel('Cost')
    plt.xlabel('Number of iterations')
    plt.plot(n_[:b], m_[:b], color='blue')
    plt.figure()
    plt.title('Coordinate change diagram')
    plt.ylabel('X_Y_Range')
    plt.xlabel('Number of iterations')
    l1, = plt.plot(n_[:b], x_[:b], color='red')
    l2, = plt.plot(n_[:b], y_[:b], color='green')
    plt.legend(handles=[l1, l2], labels=['X', 'Y'])
    plt.figure()
    plt.title('Location Map')
    plt.xlabel('X')
    plt.ylabel('Y')
    px, py = [], []
    mx, my = [], []
    for i in range(len(P) - 1):
        px.append(P[i + 1][0])
        py.append(P[i + 1][1])
    for i in range(len(M) - 1):
        mx.append(M[i + 1][0])
        my.append(M[i + 1][1])
    plt.scatter(x_[:b], y_[:b], color='blue')
    plt.scatter(px, py, color='red')
    plt.scatter(mx, my, color='green')
    plt.legend(labels=['Product Location', 'Market position ', 'Logistics Centre'])
    plt.show()


# 初始变换函数
def origin(data):
    vrx, vry, vr, x0, y0 = 0, 0, 0, 0, 0
    for i in range(len(data)):
        vrx += (data[i][2]) * (data[i][3]) * (data[i][0]) / (data[i][4])
        vry += (data[i][2]) * (data[i][3]) * (data[i][1]) / (data[i][4])
        vr += (data[i][2]) * (data[i][3]) / (data[i][4])
    x0 = vrx / vr
    y0 = vry / vr
    for i in range(len(data)):
        data[i][4] = (pow((data[i][0]) - x0, 2) + pow((data[i][1]) - y0, 2)) ** 0.5
    return x0, y0, data


# 成本计算函数
def cost(data):
    money = 0
    for i in range(len(data)):
        money += (data[i][2]) * (data[i][3]) * (data[i][4])
    return money


# 迭代函数
def diedai(data, n, a, b):
    for i in range(n + 1):
        x, y, d = origin(data)
        m = cost(d)
        n_.append(i)
        x_.append(x)
        y_.append(y)
        m_.append(m)
        if a > 0:
            x, y, m = round(x, a), round(y, a), round(m, a)
        print('迭代次数{}，拟建物流中心坐标（{}，{}）,此时总运输成本={}'.format(str(i).rjust(4, ' '), x, y, m))
    if b < 0:
        b = n
    draw(b)


diedai(all_data, 20, 10, 15)
# 迭代20次，精确到小数后面10位，绘制前15次变化图
