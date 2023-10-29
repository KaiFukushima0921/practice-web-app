def my_decorator(func):
    def wrapper():
        print("デコレータの前処理")
        func()
        print("デコレータの後処理")
    return wrapper

@my_decorator
def say_hello():
    print('こんにちは')

say_hello()