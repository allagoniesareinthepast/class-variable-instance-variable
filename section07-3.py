# self의 이해
# method에 self가 있으면 instance method
# method에 self가 없으면 class method


class Self:
    def class_method():
        print("method")

    def instance_method(self):
        print("instance")


example = Self()
# example.class_method # instance는 class method를 실행할 수 없음
example.instance_method()
Self.class_method()
# Self.instance_method() # class는 instance method를 실행할 수 없음
# function2에 instance를 넣어줌으로써 해결 (instance안의 self를 사용한 것으로 추측)
Self.instance_method(example)
