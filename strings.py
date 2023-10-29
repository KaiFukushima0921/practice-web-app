# data = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
# csv = ','.join(data)
# print(csv)

# data2 = "aaa bbb ccc"
# data2_list = data2.split(' ')
# print(data2_list)

# item = "apple"
# text = f"there is an {item}."
# print(text)

# item1 = "apple"
# item2 = "banana"

# text1 = "There are {} and {}"
# print(text1.format(item1,item2))

text = "There are %s, %s, and %s"
f_text = text % ('apple', 'bananas', 'oranges',)
print(f_text)