import random

numbers = list(range(1,46))

for i in range(1,6) : # 반목문으로 5천원어치 로또 번호 출력
    selected_number  = random.sample(numbers, 6)
    selected_number.sort()
    print(str(i) + "게임: " , selected_number)