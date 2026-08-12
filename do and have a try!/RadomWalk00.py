from random import choice

from matplotlib import pyplot as plt


class RandomWalk:
    def __init__(self,num_point = 5000):
        self.num_point = num_point
        # 起始点位于(0,0)
        # 为x的值与y的值各创建一个列表，列表初始元素为0，说明第一个点位于(0，0)
        self.x_values = [0]
        self.y_values = [0]
    def get_step(self):
        direction = choice([-1,1])
        distance = choice([0,1,2,3,5])
        step = direction * distance
        return step
    def fill_walk(self):
        # 不断随机漫步，直到列表到底指定长度
        # 目的是获取随机漫步的列表数据
        while len(self.x_values) < self.num_point:
            x_step = self.get_step()
            y_step =self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值与y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            # 将计算过的x，y值存入列表
            self.x_values.append(x)
            self.y_values.append(y)

while True:
    rm = RandomWalk()
    rm.fill_walk()
    plt.style.use('classic')
    point_numbers = range(rm.num_point)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(rm.x_values,rm.y_values,c = point_numbers,
               cmap=plt.cm.Blues,edgecolors='none',s=5)
    plt.show()
    out = input("是否要继续随机漫步？(y/n)")
    if out == "n":
        break

