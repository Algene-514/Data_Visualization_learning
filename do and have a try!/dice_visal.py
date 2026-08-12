from random import randint

from plotly.graph_objs import Bar, Layout
from plotly import offline
from plotly.graph_objs.layout.scene import _xaxis


class Die():
    def __init__(self,number_points = 6):
        self.number_points = number_points
    def roll(self):
        return randint (1,self.number_points)

die1 = Die()
die2 = Die(10)
# 获取结果
results = []
for i in range(10000 + 1):
    result = die1.roll() + die2.roll()
    results.append(result)
# 分析结果
frequencies = []
max_result = die1.number_points + die2.number_points
print(max_result)
for num in range(2 , max_result+1):
    frequency = results.count(num)
    frequencies.append(frequency)
print(frequencies)
x_values = list(range(2,max_result+1))
data = [Bar(x = x_values, y = frequencies,)]
x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的值'}
my_layout = Layout(title="咕咕嘎嘎！！！",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data,'layout' :my_layout},filename='visal.html')