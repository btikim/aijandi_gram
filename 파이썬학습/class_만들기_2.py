class FourCal:       # FourCal 이라는 클래스를 만든다.
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result=self.first + self.second
        return result

a = FourCal()     # FourCal 클래스를 a 라는 변수에 넣는다.
a.setdata(4,2)    # 클래스를 불러들이는 점 앞의 변수를 위해 self라고 함수에 넣는 것이다.
print(a.add())






# class FourCal:       # FourCal 이라는 클래스를 만든다.
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

# a = FourCal()     # FourCal 클래스를 a 라는 변수에 넣는다.
# a.setdata(1,2)    # 클래스를 불러들이는 점 앞의 변수를 위해 self라고 함수에 넣는 것이다.
# print(a.first)
# print(a.second)

# student = Student()

# 클래스는 변수와 함수를 만들어놓은 틀이다. 
# 클래스(틀) : 학생은 이름이라는 속성을 갖고 있어!
# 객체(실체화 된 것) : 학생 이름은 "윤인성"이야
# 실체화 한 객체 = "인스턴스"

#생성자는 __init__ 을 이용해서 만든다. 반드시 self를 매개변수로 가져야 한다. 


