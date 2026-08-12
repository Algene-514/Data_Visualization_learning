# 修改标签文字和线条粗细
import matplotlib.pyplot as plt
# 设置支持中文的字体（Windows系统常用的黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
squares = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256]
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(value,squares,linewidth=3) # 第一个参数接收数据，第二个参数linewidth接收线条宽度
#plot()接三个参数，第一个为x轴数据，第二个为y轴数据，第三个为线条宽度
# 设置图表标题并给坐标轴加上标签，第一个参数接收名称，第二个参数接收字的大小
ax.set_title("平方数",fontsize=24) # 图表标题的设置
ax.set_xlabel("值",fontsize=14) # x轴说明的设置
ax.set_ylabel("值的平方",fontsize=14) # y轴说明的设置
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14) #axis = "both"指定的实参影响x轴和y轴上的刻度
# 第二个”labelsize“设置刻度标记的字号
# 名称解读： tick为刻度的意思，param是参数的缩写，全拼为parameter
plt.show()

"""
0,导入模块
1,导入数据
2，在图片中绘制图表 subplots()
3，以有意义的方式绘制数据 plot()
4，设置图表参数与样式：标题，字号
5，展示图表数据 show()
"""


# 使用内置样式：
#plt.style.use("样式名")，如上
