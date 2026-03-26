from datetime import datetime, timedelta
import emoji

# 1. 내가 태어난지 얼마나 됐는지 확인 => 13009일이라니 오래살았구나 (26.3.26일 기준)

now = datetime.now()
my_birthday = datetime(1990, 8, 13)
my_birthdays = now - my_birthday

print(f"내가 태어난지 {my_birthdays.days}일 째 입니다")

# 2. 1년 중에 100일, 200일, 300일 되는 날 확인해보자 

year = 2026
start_day = datetime(year, 1, 1)

the_day_100 = start_day + timedelta(days=99)
the_day_200 = start_day + timedelta(days=199)
the_day_300 = start_day + timedelta(days=299)

print("2026년에 100일이 되는 날은 " ,the_day_100.strftime("%Y-%m-%d"))
print("2026년에 200일이 되는 날은 " ,the_day_200.strftime("%Y-%m-%d"))
print("2026년에 300일이 되는 날은 " ,the_day_300.strftime("%Y-%m-%d"))

#  2-1 반복문으로 작성 
year = 2026
start_date = datetime(year, 1, 1)

days = [100, 200, 300]

for d in days:
    target_date = start_date + timedelta(days=d - 1)
    print(f"{year}년 {d}일째 되는 날: {target_date.strftime('%Y-%m-%d')}")

# 2-2 함수로 작성
def get_day_of_year(year, day):
    from datetime import datetime, timedelta
    start = datetime(year, 1, 1)
    return start + timedelta(days=day - 1)

print(get_day_of_year(2026, 100))
print(get_day_of_year(2026, 200))
print(get_day_of_year(2026, 300))