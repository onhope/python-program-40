import random
numbers = list(range(1,46))
print(numbers)

selected_numbers = random.sample(numbers, 6) # random 라이브러리의 sample 함수를 사용하여 1~45까지의 숫자 리스트에서 6개의 숫자를 무작위로 선택 
print(selected_numbers)

selected_numbers.sort(); # 오름차순으로 정렬