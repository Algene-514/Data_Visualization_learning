import matplotlib.pyplot as plt
from random import choice
class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points = 5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        self.x_value = [0]
        self.y_value = [0]
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_value) < self.num_points:
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4,5,6,7,8,9,10])
            x_step = x_direction * x_distance
            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4,5,6,7,8,9,10])
            y_step = y_direction * y_distance
            if x_step == 0  and y_step == 0:
                continue
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)



# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    # 用subplots()中的figsize参数调节屏幕大小
    fig,ax = plt.subplots(figsize=(10,6))
    point_numbers = range(rw.num_points)
    # 给点着色
    ax.scatter(rw.x_value,rw.y_value,c =point_numbers
                ,cmap=plt.cm.Blues,edgecolors='none',s=4)
    # 突出起点和终点
    # 起点
    ax.scatter(0,0,c="green",edgecolors='none',s=50)
    # 终点
    ax.scatter(rw.x_value[-1],rw.y_value[-1],c="red",edgecolors='none',s=50)
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("要继续漫步吗?(y/n)")
    if keep_running == "n":
        print("随机漫步程序已结束")
        break

