from random import randint,choice
class Die():

    def __init__(self,number_points = 6):
        self.number_points = number_points

    def roll(self):
        return randint (1,self.number_points)
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
from matplotlib import pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline
# 用Matplotlib来模拟掷骰子的结果
# 创建实例：
die = Die(6)
# 获取数据
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)
# 分析数据
frequencies = []
for num in range(1,1 + die.number_points):
    frequency = results.count(num)
    frequencies.append(frequency)
# 数据可视化
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(8,6))
x_values = list(range(1,1+die.number_points))
ax.scatter(x_values, frequencies,c = frequencies,
           cmap = plt.cm.Blues,edgecolors='none',s = 100)
plt.title('Frequency of Results')
plt.xlabel('Number of Results')
plt.ylabel('Frequency')
plt.show()

