import matplotlib.pyplot as plt
# 设置支持中文的字体（Windows系统常用的黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
x_values = range(1,10001)
y_values = [x**3 for x in x_values]
ax.scatter(x_values,y_values,c=y_values,cmap = plt.cm.rainbow,s=1)
plt.show()