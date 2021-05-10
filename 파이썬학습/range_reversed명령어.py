# range(시작, 끝, 단계)

# a = list(range(0,11, 2))
# print(a)

# a = list(range(11))

# 원하는 횟수만큼 반복을 돌릴 수 있게 된다.

# for i in range(0, 11):
#     print(i)

# range 변수는 정수만 올 수 있다.

# for i in range(0, 11//2):
#     print(i)

# 변수가 몇 번째인지 enumerate 함수를 사용하여 찾아낼 수 있다
# array = [273, 52, 103, 32,57]
# for i, element in enumerate(array):
#     print("{}:{}".format(i, element))

# print()
# print()

# for i in range(len(array)):
#     print("{}:{}".format(i, array[i]))

# 숫자 역순으로 출력한다.

# for i in reversed(range(0,8)):
#     print(i)