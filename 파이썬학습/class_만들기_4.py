# 클래스 상속
# 부모의 클래스를 그대로 받아서 내용을 추가한다.

class FourCal:       # FourCal 이라는 클래스를 만든다.
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result=self.first + self.second
        return result

class MoreFourCal(FourCal):      # 클래스 이름에 괄호를 하고 다른 클래스 이름을 넣어주면     
                                 # 해당 클래스를 상속받는다는 것이다.
    def pow(self):
        result2 = self.first ** self.second
        return result2

a = MoreFourCal(3,8)
print(a.pow())


# 부모 클래스와 자식 클래스에 동일한 함수가 있을 경우 자식 클래스의 함수가 실행된다.
#   --> 이를 메서드 오버라이딩 이라고 한다.

# 클래스 변수는 클래스에 미리 선언해놓은 변수이다.
