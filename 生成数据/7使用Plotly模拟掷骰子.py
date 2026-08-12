from random import randint

class Die:
    """表示一共骰子的类"""

    def __init__(self,num_sides = 6):
        """骰子面数为6"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子之间的随机值"""
        return randint(1,self.num_sides)

# 投骰子！
die = Die()
# 投几次骰子并将结果储存在一个列表中
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

