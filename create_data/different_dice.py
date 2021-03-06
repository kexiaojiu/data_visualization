#coding=utf-8
import pygal
from die import Die

# 创建一个D6和D10
die_1 = Die()
die_2 = Die(10)

# 投掷骰子多次并记录结果
results = []

for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
numbers = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    numbers.append(value)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = numbers
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')
