# 绘制散点图
import matplotlib.pyplot as plt
# 设置支持中文的字体（Windows系统常用的黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
fig, ax = plt.subplots()

# 可以利用循环来自动生成并计算数据
# 对于python，生成1000个点像生成5个点一样简单
x = range(1,1001)
y = [x**2 for x in range(1,1001)]

# ax.scatter(x,y,c="green",s=1)
ax.scatter(x,y,c=(0,0.8,0),s=1)
# 也可以用参数c自定义颜色：直接输入颜色名或者用RGB自定义颜色,数值越靠近1，颜色越浅
ax.set_title("平方数",fontsize = 20)
ax.set_xlabel("值",fontsize = 10)
ax.set_ylabel("值的平方",fontsize = 10)
ax.tick_params(axis='both',which ="major",labelsize=10)
plt.show()


