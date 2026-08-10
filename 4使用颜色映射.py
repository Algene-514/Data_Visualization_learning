# 颜色映射colormap是一些列颜色，从其实颜色渐变到终止颜色，可用来突出数据
#如可以用较浅的颜色表示较小的值

import matplotlib.pyplot as plt
# 设置支持中文的字体（Windows系统常用的黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
fig, ax = plt.subplots()
x = range(1,1001)
y = [x**2 for x in range(1,1001)]
ax.scatter(x,y,c=y,cmap=plt.cm.Greens,s=1)
# 将c设置成一个y列表并用cmap告诉pyplot使用哪个颜色映射
ax.set_title("平方数",fontsize = 20)
ax.set_xlabel("值",fontsize = 10)
ax.set_ylabel("值的平方",fontsize = 10)
ax.tick_params(axis='both',which ="major",labelsize=10)
# 自动保存图表
# 第一个参数指定要以什么文件名保存图表，第二个参数指定将图表多余的空白区域裁掉
plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()


