import matplotlib.pyplot as plt
from fontTools.varLib import plot
from matplotlib.pyplot import scatter, show

# 设置支持中文的字体（Windows系统常用的黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
x_value = range(1,9001)
y_value = [x**50 for x in x_value]
fig, ax = plt.subplots()
ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.rainbow,s=1)
ax.set_title('吼吼吼')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.tick_params(axis='x',labelrotation=90)
plt.show()