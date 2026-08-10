import matplotlib.pyplot as plt # 导入模块
squares = [1,4,33,22,3]  # 先创建数据
fig, ax = plt.subplots() # 调用subplots()函数，在图片中绘制图表
ax.plot(squares) # 调用plot()方法，根据给定的数值以有意义的方式绘制图表
#plot()接三个参数，第一个为x轴数据，第二个为y轴数据，第三个为线条宽度
plt.show() # 调用show()来展示图表

"""
0,导入模块
1,导入数据
2，在图片中绘制图表 subplots()
3，以有意义的方式绘制数据 plot()
4，展示图表数据 show()
"""


