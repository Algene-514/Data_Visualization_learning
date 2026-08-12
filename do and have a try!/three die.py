from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice_visal import my_layout, x_axis_config


class Die():
    def __init__(self,number_points = 6):
        self.number_points = number_points
    def roll(self):
        return randint (1,self.number_points)

die1 = Die(12)
die2 = Die(12)
die3 = Die(12)
# 获取数据
results= []
max_value = die1.number_points + die2.number_points + die3.number_points
for i in range(100000):
    result = die1.roll() + die2.roll() +die3.roll()
    results.append(result)
# 处理数据
frequencies = []
for value in range(3,max_value+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
# 可视化数据
x_values = list(range(3,max_value+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Results'}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title="我喜欢你",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot(my_layout, filename='three_visal.html')