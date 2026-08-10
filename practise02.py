import matplotlib.pyplot as plt
from matplotlib.pyplot import show

# 设置支持中文的字体（Windows系统常用的黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
num = 1/2
x_value = range(1001)
y_value = [x**num for x in x_value]
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.viridis , s = 1)
ax.set_title('咕咕嘎嘎!!!', fontsize=30)
ax.set_xlabel('x', fontsize=20)
ax.set_ylabel('y', fontsize=20)
ax.set_ylabel('y')
plt.show()