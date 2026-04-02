# 필요한 라이브러리 불러오기 
import time
import webbrowser
from datetime import datetime

start_date = datetime(2024, 11,15)  # 만난 날짜 설정
now = datetime.now() # 현재 날짜 
days_in_love = now - start_date # 만난 기간 설정

# 메시지를 리스트로 저장
message_list = ["안녕, 현준아. \n",
                "너를 안지 어느새 " + str(days_in_love) + "일이 되었네. \n",
                "너를 만난 후 난 완전 다른 사람이 되었어. \n",
                "너가 아니면 도파민이 돌지 않아. \n",
                "앞으로도 너의 선수생활을 계속 보고 싶어. 그러니까 4월 4일날 잘하자. \n" 
]

# 반복문으로 3초간의 여유를 두고 문자열이 출력되게 하기
for message in message_list : 
    print(message)
    time.sleep(3)

# while 무한루프
while True:
    # 대답 요청하기 
    answer = input("[선택] 4월 4일날 POM 받겠다는 Y, 거절은 N을 입력 >> ")
    # 대답에 따른 url 브라우저 설정
    if answer in ["Y", 'y'] :
        url1 = 'https://www.youtube.com/watch?v=ZoYuWpun3co'
        webbrowser.open(url1)
        break
    
    elif answer in ['N', 'n']:
        url2 = 'https://www.youtube.com/watch?v=v_NenHiCqXQ'
        webbrowser.open(url2)
        break
    
    else : 
        print('\n[경고] 제발 Y 또는 N을 입력해줘...그렇지 않으면 이 프로그램은 끝나지 않아')