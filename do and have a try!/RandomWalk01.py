from random import choice
from matplotlib import pyplot as plt

class RandomWalk:
    def __init__(self,step_num = 5000):
        self.step_num = step_num
        # 从(0,0)开始
        self.x_value = [0]
        self.y_value = [0]
        self.num = 0

    def get_walk(self):
        direction = choice([-2,-1,1,2])
        distance = choice([0,1,2,3,4,5,6,7,9,10])
        step = direction * distance
        return step

    def walk(self):
        while self.num < self.step_num + 1 :
            x = self.get_walk()
            y = self.get_walk()
            if x == 0 and y == 0:
                continue
            x = self.x_value[-1] + x
            y = self.y_value[-1] + y
            self.x_value.append(x)
            self.y_value.append(y)
            self.num += 1


while True:
    import matplotlib.pyplot as plt

    # 设置支持中文的字体（Windows系统常用的黑体）
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决负号显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False
    rw = RandomWalk()
    rw.walk()
    fig, ax = plt.subplots(figsize=(10,6))
    plt.style.use('classic')
    num = range(len(rw.x_value))
    ax.scatter(rw.x_value, rw.y_value, c = num ,
               cmap=plt.cm.Blues, edgecolors="none", s=5)
    ax.set_title('RandomWalk', fontsize=20)
    ax.set_xlabel('x', fontsize=20)
    ax.set_ylabel('y', fontsize=20)
    # 显示起点和终点：
    ax.scatter(0 , 0 , c = "green" ,
               edgecolors='none' , s=30)
    ax.scatter(rw.x_value[-1] , rw.y_value[-1] , c = "red"
               , edgecolors='none', s=30)
    plt.show()
    plt.show()
    out = input("是否进行下一次(y/n)")
    if out == "n":
        break

