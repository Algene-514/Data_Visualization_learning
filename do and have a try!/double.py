from RandomWalk01 import RandomWalk
from die_8 import Die
from matplotlib import pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline

# 用Plotly来可视化随机漫步的情况

# 用Matplotlib来模拟掷骰子的结果
# 创建实例：
die = Die(6)
# 获取数据
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
# 分析数据


