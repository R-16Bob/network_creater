#https://blog.csdn.net/inside802/article/details/116547843
from collections import deque
# maps表用来记录各个节点的子节点
maps = dict()
maps['a'] = ['b', 'c']
maps['b'] = ['e']
maps['c'] = ['d', 'f']
maps['d'] = ['e']
maps['f'] = ['e']
maps['e'] = ['g']
maps['g'] = []
maps['h'] = []

# 定义起点和终点
start = 'a'
finish = 'g'
# 定义队列，初始值为起始点的子节点
my_deque = deque()
my_deque += maps[start]
# 定义已搜索过的点，避免重复搜索
searched = []
# 定义父节点表，这个表就是用来维护搜索过的点的父节点是谁。b、c的父节点是a
parents = dict()
parents['b'] = 'a'
parents['c'] = 'a'
# 定义路径，这里存放的是最短路径。由于是从后往前反推的，所以刚开始的值是终点的值
path = [finish]
# 一直查找，直到队列为空，或者循环内break。在这里为了简便，没有写成函数。
while my_deque:
    location = my_deque.popleft()
    if location not in searched:

        if location == finish:
            # print(parents)
            # 如果当前点是终点，就开始反推至起点。一直反推，直到找到起点
            key = finish
            while key != start:
                farther = parents[key]
                path.append(farther)
                key = farther
            # 反推完成后，将列表反转，打印从起点到终点的路径，符合人的习惯
            path.reverse()
            print(path)
            break
        else:
            # 如果当前节点不是终点，则把它的子节点加入队列
            my_deque += maps[location]
            for value in maps[location]:
                # 只要当前点之前没有父亲，就把它写入parents表里，指定它的父亲。父亲唯一，不可变更。
                if value not in parents:
                 parents[value] = location
            searched.append(location)
