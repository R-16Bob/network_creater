# https://blog.csdn.net/qq_34950042/article/details/88387797
import math

nodes = ('A', 'B', 'C', 'D', 'E')
# dis矩阵为方阵
dis = [[0, 1, 2, math.inf, 4],
       [1, 0, math.inf, 8, 2],
       [2, math.inf, 0, math.inf, 6],
       [math.inf, 8, math.inf, 0, 3],
       [4, 2, 6, 3, 0]]


def shortDistance(dis):
    node_num = len(dis)
    for i in range(node_num):  # 十字交叉法的位置位置，先列后行
        for j in range(node_num):  # 列 表示dis[j][i]的值，即j->i
            for k in range(j + 1, node_num):  # 行 表示dis[i][k]的值，即i->k，i只是一个桥梁而已
                # 先列后行，形成一个传递关系，若比原来距离小，则更新
                if dis[j][k] > dis[j][i] + dis[i][k]:
                    dis[j][k] = dis[j][i] + dis[i][k]
                    dis[k][j] = dis[j][i] + dis[i][k]
print(dis)
shortDistance(dis)
print(dis)