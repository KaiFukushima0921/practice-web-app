x = 1000
y = 0

# try:
#     z = x / y
#     print(z)
# except:
#     print('除数に0が指定されました')

# try:
#     z = x / y
#     print(z)
# except ZeroDivisionError as e:
#     print('除数に0が指定されました')
#     print(type(e), str(e))
    


# param = {'x' : 1000, 'z' : "a"}
# try:
#     x = param['x']
#     y = param['z']
#     z = x / y
#     print(z)

# except KeyError as e:
#     print('処理に必要なデータが存在しません')
# except ZeroDivisionError as e:
#     print('除数に0が指定されました')
# except:
#     print('原因不明のエラーが発生しました')


# def sample(num):
#     if type(num)!=int:
#         raise TypeError('パラメータが不正です')
    
#     return num * 10

# result = sample("a")
# print(result)]


try:
    z = x / y
    print(z)
except ZeroDivisionError as e:
    print('除数に0が指定されました')
    raise e