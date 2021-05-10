# 이미지 인식 후 자동 저장하는 기능

import pyautogui
import schedule
import time

def job():
    try:
        location = pyautogui.locateCenterOnScreen('save_img.png',confidence=0.8)  # 정확도를 80%로 지정한다
        print(location)
        time.sleep(0.5)
        x,y = location
        pyautogui.doubleClick(x,y)
        print("저장하기 버튼을 눌렀습니다.")
    
    except:
        print("프로그램 창이 비활성화 중입니다")

schedule.every(5).seconds.do(job)

while 1:
        schedule.run_pending()
        time.sleep(1)
