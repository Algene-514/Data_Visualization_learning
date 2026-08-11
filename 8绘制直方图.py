from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint
class Die:
    """表示一共骰子的类"""
    def __init__(self,num_sides = 6):
        """骰子面数为6"""
        self.num_sides = num_sides
    def roll(self):
        """返回一个位于1和骰子之间的随机值"""
        return randint(1,self.num_sides)
die = Die()
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对结果进行可视化
x_values = list(range(1,die.num_sides+1))

data = [Bar(x=x_values, y=frequencies)]
# Bar()用于绘制条形图的数据集，需要一个存储x值的列表和一个存储y值的列表
# 这个类必须在方括号内，因为数据集可能包含多个元素
x_axis_config = {'title':'结果'}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷骰子10000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# 类Layout()返回一个指定图标布局和配置的对象
offline.plot({'data':data,'layout':my_layout},filename='d6.html')
# offline.plot()在这里用来生成图表