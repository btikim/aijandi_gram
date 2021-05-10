# while <불 표현식>
#      명령어

# i =0
# while i < 10 :
#     print(i)
#     i += 1

# numbers =[1,3,1,5,18,1,0]
# while 1 in numbers:
#     numbers.remove(1)
#     print(numbers)

# 특정 시간 동안 대기하는 프로그램 작성

# import time
# fi = time.time()
# while fi + 3 >= time.time():
#     pass

# print("3초가 지났습니다.")


# import time
# fi = time.time()
# while fi + 1 >= time.time():
#     print("xyz", end="")

# print("1초가 지났습니다.")
# i=0
# while True:
#     print("{}번째 실행하고 있습니다.".format(i))
#     i += 1
#     input_text = input("> 종료하시겠습니까? y, n")
#     if input_text.lower()=="y":
#         print("반복을 종료합니다")
#         break

# continue 현재 반복을 중지하고, 다음 반복으로 넘어간다.

treeHit =0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무가 넘어갔습니다.ㅎㅎㅎ")



