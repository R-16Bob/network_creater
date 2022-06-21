from create_netdata import Network_1

# 拓扑来源：https://github.com/BNN-UPC/NetworkModelingDatasets/tree/master/datasets_v1
# NSFNet topology
NSFNet=[[0,1,0],[0,2,0],[0,3,0],[1,2,0],[1,7,0],[2,5,0],
          [3,4,0],[3,8,0],[4,5,0],[4,6,0],[5,12,0],[5,13,0],
          [6,7,0],[7,10,0],[8,9,0],[8,11,0],[9,12,0],[10,11,0],
          [10,13,0],[11,12,0]]
# GBN topology
# flow_data有点超过5
GBN=[[0,2,0],[0,8,0],[1,2,0],[1,3,0],[1,4,0],[2,4,0],[3,4,0],[3,9,0],
     [4,8,0],[4,9,0],[4,10,0],[5,6,0],[5,8,0],[6,7,0],[7,8,0],[9,10,0],
     [9,12,0],[10,11,0],[10,12,0],[11,13,0],[12,14,0],[12,16,0],[13,14,0],
     [14,15,0],[15,16,0]]
# GEANT2 topology
GEANT2=[[0,1,0],[0,2,0],[1,3,0],[1,6,0],[1,9,0],[2,3,0],[2,4,0],[3,5,0],[3,6,0],
        [4,7,0],[5,8,0],[6,8,0],[6,9,0],[7,8,0],[7,11,0],[8,11,0],[8,12,0],[8,17,0],
        [8,18,0],[8,20,0],[9,10,0],[9,12,0],[9,13,0],[10,13,0],[11,14,0],[11,20,0],
        [12,13,0],[12,19,0],[12,21,0],[14,15,0],[15,16,0],[16,17,0],[17,18,0],[18,21,0],
        [19,23,0],[21,22,0],[22,23,0]]
def create_net1():
    net1 = Network_1(14,NSFNet,'network_1')
    net1.cal_transmission_delay()
    net1.print_net()
    net1.save_data()

def create_net2():
    net1 = Network_1(17,GBN,'network_2')
    net1.print_net()
    net1.save_data()

def create_net3():
    net1 = Network_1(24,GEANT2,'network_3')
    net1.print_net()
    net1.save_data()

for i in range(50):  # 需要的数据条数
    create_net1()
    # create_net2()
    # create_net3()