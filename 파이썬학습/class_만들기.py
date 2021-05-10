class FourCal:
    pass

a = FourCal()
print(a)

class Student:
    def __init__(self, name, age):
        print("객체가 생성되었습니다")

        self.name = name
        self.age = age

    def printf(self):
        print(self.name, self.age)

stu = Student("김진환 님", 53)
stu.printf()

# student = Student()

# 클래스는 변수와 함수를 만들어놓은 틀이다. 
# 클래스(틀) : 학생은 이름이라는 속성을 갖고 있어!
# 객체(실체화 된 것) : 학생 이름은 "윤인성"이야
# 실체화 한 객체 = "인스턴스"

#생성자는 __init__ 을 이용해서 만든다. 반드시 self를 매개변수로 가져야 한다. 

# 이전에 계산한 결괏값을 유지하기 위해서 result 전역 변수(global)를 사용한다. 
# 프로그램을 실행하면 예상한 대로 다음과 같은 결괏값이 출력된다.
