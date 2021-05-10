# global 변수 만들어 적용하기

a = 5 

def vartest():
    global a
    a = a + 4

vartest()
print(a)