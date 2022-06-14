import csv
import numpy as np
import random

class Network_1:
    def __init__(self,node_num,link_des):
        zero_rate = 0.4
        self.nodes=[]
        self.links=link_des
        self.node_data=[]
        self.flows=[]
        self.graph={}
        # 构造nodes
        for i in range(node_num):
            self.nodes.append(i)
        # 构造links
        for i in range(len(self.links)):
            if np.random.uniform() >= zero_rate:
                self.links[i][2]=random.uniform(256,1024)
        self.links=np.array(self.links)
        # 构造node_data
        for i in range(len(self.nodes)):
            nodes=self.nodes[:]
            nodes.remove(i)
            if np.random.uniform() >= zero_rate:
                amount=random.uniform(0,512)
                des= random.choice(nodes)
                self.node_data.append([amount,des])
            else:
                self.node_data.append([0,0])
        # 构造graph
        for i in range(len(self.nodes)):
            self.graph[i]=[]
        for link in self.links:
            self.graph[link[0]].append(link[1])
            self.graph[link[1]].append(link[0])
        # 构造flows
        for i in range(len(self.node_data)):
            if(self.node_data[i][0]!=0):
                self.flows.append(self.create_flow(i,self.node_data[i][1]))


    def create_flow(self,s,d):
        # TODO: 输入源和目的节点，输出一条源到目的的路径
        queue = []
        queue.append(s)
        seen = set()
        seen.add(s)
        parent = {s: None}
        while queue:
            vertex = queue.pop(0)
            nodes = self.graph[vertex]
            for m in nodes:
                if m not in seen:
                    queue.append(m)
                    seen.add(m)
                    parent[m] = vertex
        flow = []
        while d!=None:
            flow.append(d)
            d=parent[d]
        flow.reverse()
        return flow

    def create_label(self):
        # TODO: 对flows的每一条记录，计算出一个flow_label
        flow_label=[]
        return flow_label
# 保持到文件
    def save_data(self):
        # add link_data
        with open("network_1/link_data.csv", "a", newline='') as f_l:
            writer = csv.writer(f_l)
            writer.writerow('')
            writer.writerows(self.links.T)
        # add node_data
        with open("network_1/node_data.csv","a",newline='') as f_n:
            writer = csv.writer(f_n)
            writer.writerow('')
            writer.writerows(self.node_data)
        # add flow_data
        with open("network_1/flow_data.csv","a",newline='') as f_fd:
            writer = csv.writer(f_fd)
            writer.writerow('')
            writer.writerows(self.flows)

    def print_net(self):
        # print(self.nodes)
        # print(self.links)
        print(self.node_data)
        print(self.graph)
        print(self.flows)

# # original link_data
# link_des=[[0,1,0],[0,2,0],[0,3,0],[1,2,0],[1,7,0],[2,5,0],
#           [3,4,0],[3,8,0],[4,5,0],[4,6,0],[5,12,0],[5,13,0],
#           [6,7,0],[7,10,0],[8,9,0],[8,11,0],[9,12,0],[10,11,0],
#           [10,13,0],[11,12,0]]
# net1 = Network_1(14,link_des)
# net1.print_net()
# #net1.save_data()