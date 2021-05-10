# try:
#     # 오류가 발생할 수 있는 구문
# except Exception as e:
#     # 오류가 발생했을 때
# else:
#     # 오류가 발생하지 않았을 경우
# finally:
#     # 무조건 마지막에 실행한다. 

# try:
#     4/ 0
# except ZeroDivisionError as e:
#     print(e)

# print("이 줄이 나타날 수 있습니다.")


try:
    f = open('./robot_210116.txt', "r")
except FileNotFoundError as e:     # 만약 파일이 없어서 에러가 나면 메시지를 보여준다.
    print(str(e))
else:
    data = f.read()     # 만약 파일이 있으면 읽어들여서 보여준다.
    print(data)
    f.close

# f = open("c://이천PC/Python학습/PY_개발/robot_210116.txt", "r")
# data = f.read()     # 만약 파일이 있으면 읽어들여서 보여준다.
# print(data)
# f.close
