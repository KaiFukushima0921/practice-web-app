import datetime

def print_datetime(f):
    def wrapper():
        print(f'開始:{datetime.datetime.now()}')
        f()
        print(f'終了:{datetime.datetime.now()}')
    return wrapper

@print_datetime
def calc():
    print(3**5)

calc()
