import matplotlib.pyplot as plt
from random import choice
# 为模拟随机漫步，要创建一个名为RandomWalk的类，它随机地选择前进的方向
# 这个类需要三个属性，一个是存储随机漫步次数的变量，其他是两个列表，分别存储x与y坐标
# RandomWalk只包含2个方法，初始化和fill_walk(),后者计算随机漫步经过的所有点

class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points = 5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        #所有随机漫步都始于(0,0)
        self.x = [0]
        self.y = [0]
        # 选择方向
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        #不断漫步,直到列表达到指定的长度