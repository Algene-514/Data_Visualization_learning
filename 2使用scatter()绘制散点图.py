# 绘制散点图
import matplotlib.pyplot as plt
# 设置支持中文的字体（Windows系统常用的黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
fig, ax = plt.subplots()
x = [1,2,3,4,5,6,7,8,9]
y = [1,4,9,16,25,36,49,64,81]
ax.scatter(x,y,s=50) # 与plot()绘制折线图功能相对，scatter()用来绘制单个点,s参数表示点的尺寸

#如果对plot()传递单个点不会绘制任何图像

# 设置图表标题并给坐标轴添加上标签
ax.set_title("平方数",fontsize = 20)
ax.set_xlabel("值",fontsize = 10)
ax.set_ylabel("值的平方",fontsize = 10)
ax.tick_params(axis='both',which ="major",labelsize=10)
# 'both'：同时应用到 X 轴和 Y 轴。
# 'major'：仅调整主刻度
plt.show()

# 要绘制一系列点，可以想scatter()传递包含x值和y值的列表
# x = [1,2,3,4,5,6,7,8,9]
# y = [1,4,9,16,25,36,49,64,81]
