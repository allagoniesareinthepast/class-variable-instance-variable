# class variable과 instance(객체) variable 특성 이해

# class variable
# StudyRoom이라는 클래스를 선언해보자. 독립된 개인 공간이 없는, 오픈된 하나의 방만 있는 스터디카페라고 생각해보자.
# 비어있는 방에 최초로 학생 한 명이 들어오면 방의 총 인원은 1명, 두번째 학생이 들어오면 총 인원은 2명, 세번째 학생이 들어오면 총 인원은 3명이 될 것이다.


class StudyRoom:
    students = 0

    def __init__(self):
        StudyRoom.students += 1  # class variable은 class명으로 접근한다(StudyRoom.)

    def disp(self):
        print(StudyRoom.students)


student1 = StudyRoom()  # 첫번째 instance 생성
student2 = StudyRoom()  # 두번째 instance 생성
student1.disp()
student2.disp()  # 모든 instance들은 class variable을 공유한다.

# instance variable
# 각각의 instance들은 다른 네임스페이스를 갖는다.
# 이번에는 오픈된 공간이 없고, 한 명의 학생당 하나의 방을 쓴다고 생각해보자. 학생들이 계속 온다고해도, 하나의 방 안에는 한 명의 학생만 있을 수 있다.


class StudyRoom():
    def __init__(self):
        self.students = 0  # instance variable은 self로 접근(self.)
        self.students += 1

    def disp(self):
        print(id(self))  # self의 id 값은, 실행되는 instance의 id 값과 같다(같은 self를 공유)
        print(self.students)


student1 = StudyRoom()
student2 = StudyRoom()
student1.disp()
print(id(student1))
student2.disp()
print(id(student2))
