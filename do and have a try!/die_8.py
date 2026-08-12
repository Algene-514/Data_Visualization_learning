from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die():

    def __init__(self,number_points = 6):
        self.number_points = number_points

    def roll(self):
        return randint (1,self.number_points)

die = Die(8)
# 获取数据
results = []
for i in range(1000000):
    result = die.roll()
    results.append(result)
# 分析数据
frequencies = []
for value in range(1,die.number_points+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 数据可视化

x_values = list(range(1,die.number_points+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Results'}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title="咕咕嘎嘎！！！！！",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,"layout":my_layout},filename="咕咕嘎嘎.html")