import matplotlib.pyplot as plt
from random import choice
# 为模拟随机漫步，要创建一个名为RandomWalk的类，它随机地选择前进的方向
# 这个类需要三个属性，一个是存储随机漫步次数的变量，其他是两个列表，分别存储x与y坐标
# RandomWalk只包含2个方法，初始化和fill_walk(),后者计算随机漫步经过的所有点

class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points = 5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        #所有随机漫步都始于(0,0)
        self.x_value = [0]
        self.y_value = [0]
        # 选择方向
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        #不断漫步,直到列表达到指定的长度
        while len(self.x_value) < self.num_points:
            # 决定前进方向以及言这个方向前进的距离
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0  and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            x = self.x_value[-1] + x_step # 注意-1指列表中的最后一个元素
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)

while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()
    # 将所有的点都绘制出来
    plt.style.use('classic')
    fig,ax = plt.subplots()
    ax.scatter(rw.x_value,rw.y_value,c = "blue",s=10)
    plt.show()

    keep_running = input("要继续漫步吗?(y/n)")
    if keep_running == "n":
        break