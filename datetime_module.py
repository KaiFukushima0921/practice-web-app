from datetime import datetime, date

# dt_obj = datetime(2018,1,2,3,4,5)
# print(dt_obj)

# dt_obj_now = datetime.now()
# print(dt_obj_now)

d = date(2017, 1, 2)
# print(d)

today = date.today()
print(today)
dt_obj_now = datetime.now()
today = dt_obj_now.date()