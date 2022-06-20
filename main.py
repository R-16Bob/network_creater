from create_netdata import Network_1

# original link_data
link_des=[[0,1,0],[0,2,0],[0,3,0],[1,2,0],[1,7,0],[2,5,0],
          [3,4,0],[3,8,0],[4,5,0],[4,6,0],[5,12,0],[5,13,0],
          [6,7,0],[7,10,0],[8,9,0],[8,11,0],[9,12,0],[10,11,0],
          [10,13,0],[11,12,0]]

def create_data():
    net1 = Network_1(14,link_des)
    net1.print_net()
    net1.save_data()

for i in range(50):
    create_data()