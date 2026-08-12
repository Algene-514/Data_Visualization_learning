from itertools import count
from random import randint
from plotly.graph_objs import Bar,Layout
from plotly import offline
class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)
num_sides = int(input('输入骰子面数,默认面数为6'))
die = Die(num_sides)
results = []
for i in range(10001):
    result = die.roll()
    results.append(result)
frequency = []
num = list(range(1,num_sides+1))
for j in num:
    total = results.count(j)
    frequency.append(total)
print(frequency)

