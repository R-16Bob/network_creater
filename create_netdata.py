import csv
import numpy as np
import random

class Network_1:
    def __init__(self,node_num,link_des,network_name):
        zero_rate = 0.4
        self.nodes=[]
        self.links=link_des
        self.node_data=[]
        self.flows=[]
        self.graph={}
        self.flow_loads={}  # 字典，key:flow编号，value：每个flow每条链路的分配带宽
        self.flow_label=[]
        self.name=network_name
        self.delay=[]  # transmission delay
        self.padding=0  # 将label用-1填充的条数
        # 构造nodes
        for i in range(node_num):
            self.nodes.append(i)
        # 构造links
        for i in range(len(self.links)):
            if np.random.uniform() >= zero_rate:
                self.links[i][2]=random.uniform(256,512)
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
        # 初始化flow_loads
        for flow in self.flows:
            self.flow_loads[self.flows.index(flow)]=[]
        # print(self.flow_loads)
        # 进行分配
        self.flow_divide()
        # 构造flow_label
        # for i in range(len(self.flow_loads)):
        for i in range(len(self.flow_loads)):
            if(len(self.flow_loads[i])==0):
                self.flow_label.append(self.node_data[self.flows[i][0]][0])  # 若没有约束的link，flow_label取需求
            else:
                self.flow_label.append(min(self.flow_loads[i])) # 取flow_loads中最小的作为label

    def create_flow(self, s, d):
        # 输入源和目的节点，输出一条源到目的的路径，使用BFS
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

    def flow_divide(self):
        # 对每个约束非0的link,找到所有需要分配的经过该link的flows,max-min准备
        for link in self.links:
            # print('link:')
            # print(link)
            flows_index = []  # 需要分配的flow编号
            if link[2]!=0:  # 有约束条件
                for flow in self.flows:
                    if self.is_through(flow,link):
                        flows_index.append(self.flows.index(flow))
                # print(flows_index)
                flow_dem={}
                for index in flows_index:
                    flow_dem[index]=self.node_data[self.flows[index][0]][0]
                if len(flow_dem)!=0:
                    # print('max-min fairness:')
                    # print(link,flow_dem)
                    self.Max_Min(link[2],flow_dem)


    @staticmethod
    def is_through(flow,link):
        s_d=set(link[:2])
        for i in range(len(flow)):
            if set(flow[i:i+2])==s_d:
                return True
            if i+2==len(flow):
                break
        return False


    def Max_Min(self,link_bd,flow_dem):
        # TODO: 给定一个Link约束和其经过的flows,使用max-min fairness得到每个flow的分配并写入字典
        print('max-min fairness:')
        print(link_bd,flow_dem)
        flows = list(flow_dem.keys())
        # 若只有一个source需要分配，则直接分配其需要的资源即可
        if len(flows)==1:
            self.flow_loads[flows[0]].append(flow_dem[flows[0]])
        else:
            # 使用冒泡排序，由小到大排序flows
            for i in range(1,len(flows)):
                for j in range(0,len(flows)-i):
                    if flow_dem[flows[j]]>flow_dem[flows[j+1]]:
                        flows[j],flows[j+1]=flows[j+1],flows[j]
            print(flows)  # flow编号列表

            # max-min fairness核心
            left_num = len(flows)  # 剩余未分配数
            acc = link_bd / left_num  # 均分累计
            for flow in flows:
                if acc<flow_dem[flow]:  # 无法满足需求，平均分配
                    self.flow_loads[flow].append(acc)
                else:  # 可以满足，而且可能还有剩
                    self.flow_loads[flow].append(flow_dem[flow])
                    left_num-=1
                    if left_num!=0:
                        acc+=(acc-flow_dem[flow])/left_num
            print('max-min：结果:')
            print(self.flow_loads)

# 计算transmission delay
    def cal_transmission_delay(self):
        # (L/R)*link_num
        flows=self.flows
        for i in range(len(flows)):
            link_num = len(flows[i])-1
            L=self.node_data[flows[i][0]][0]
            R=self.flow_label[i]
            # print(L,R,link_num)
            self.delay.append((L/R)*link_num)



# 保存到文件
    def save_data(self):
        # add link_data
        with open(self.name+"/link_data.csv", "a", newline='') as f_l:
            writer = csv.writer(f_l)
            writer.writerow('')
            #  writer.writerows(self.links.T)
            writer.writerows(self.links)  # link不再转置，保持三列
        # add node_data
        with open(self.name+"/node_data.csv","a",newline='') as f_n:
            writer = csv.writer(f_n)
            writer.writerow('')
            writer.writerows(self.node_data)

        # add flow_data
        with open(self.name+"/flow_data.csv","a",newline='') as f_fd:
            writer = csv.writer(f_fd)
            writer.writerow('')
            # 不足长度5的补-1
            for flow in self.flows:
                while len(flow) < 5:
                    flow.append(-1)
            writer.writerows(self.flows)
            self.padding = 13-len(self.flows)
            for i in range(self.padding):
                writer.writerow([-1,-1,-1,-1,-1])
        # add flow_label
        with open(self.name+"/flow_label.csv", "a", newline='') as f_fl:
            writer = csv.writer(f_fl)
            writer.writerow('')
            for label in self.flow_label:
                writer.writerow([label])
            for i in range(self.padding):
                writer.writerow([-1])
        # add transmission delay
        # with open(self.name+"/delay.csv", "a", newline='') as f_d:
        #     writer = csv.writer(f_d)
        #     writer.writerow('')
        #     for d in self.delay:
        #         writer.writerow([d])

    def print_net(self):
        # print(self.nodes)
        print(self.links)
        print(self.node_data)
        print(self.graph)
        print(self.flows)
        print("flow_label:")
        print(self.flow_label)
        print("delay:")
        print(self.delay)

if __name__ == '__main__':
    # original link_data
    link_des=[[0,1,0],[0,2,0],[0,3,0],[1,2,0],[1,7,0],[2,5,0],
              [3,4,0],[3,8,0],[4,5,0],[4,6,0],[5,12,0],[5,13,0],
              [6,7,0],[7,10,0],[8,9,0],[8,11,0],[9,12,0],[10,11,0],
              [10,13,0],[11,12,0]]
    net1 = Network_1(14,link_des,'network_4')
    #net1.cal_transmission_delay()
    net1.print_net()
    net1.save_data()