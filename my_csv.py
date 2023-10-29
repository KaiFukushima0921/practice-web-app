import csv

# with open('data.csv', 'r') as f:
#     reader = csv.reader(f)
#     print(type(reader))
#     for row in reader:
#         print(row)

# list_data = [['a','b','c','d'], [1,2,3],[4,5,6]]
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(list_data)

import re
# text = """101 CF001    コーヒー
# 102 CF002    コーヒー（お徳用）
# 201 TE01     紅茶
# 202 TE02-A   紅茶（お徳用A）
# 203 TE02-B   紅茶（お徳用B）"""
# tsv_str = re.sub(' +', '\t', text)
# print(tsv_str)

umaibo = re.split('\d+', 'chees123mentai')
print(umaibo)