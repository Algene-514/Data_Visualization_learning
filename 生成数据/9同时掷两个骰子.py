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
die1 = Die()
die2 = Die()
results = []
for roll_num in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title':'结果','dtick':1} # dtick指定了x轴显示的刻度间距
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷两个D6骰子10000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout}, filename='d6.html')
