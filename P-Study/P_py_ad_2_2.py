"""
Chapter 2
Python advanced(2) - Property(1) - Underscore

Keyword - access modifier(접근지정자), undersocre

"""

"""
다양한 언더스코어 활용
파이선 접근지정자 설명

"""


# Ex1
# Use underscore
# 1. 인터프리터
# 2. 값 무시
# 3. 네이밍(국제화, 자릿수)

# Unpacking
x, _, y = (1, 2, 3)

a, *_, b = (1, 2, 3, 4, 5)


print("Ex1 > ", x, y, a, b)

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass

# Ex 2
# 접근지정자 self.변수명
# name : public  # 읽기 쓰기 허용
# _name : protected
# __name : private  # 캡슐화
# 파이썬 -> Public 강제X, 약속된 규약에 따라 코딩 장려(자유도, 책임감 장려)
# 타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 장려 안함) -> Naming mangling
# 타 클래스 __ 접근하지 않는 것이 원칙

# No use Property


class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        self._z = 0


a = SampleA()
a.x = 1

print(f"Ex2 > x : {a.x}")
# print(f"Ex2 > y : {a.__y}")

print(f"Ex2 > z : {a._z}")

print(f"Ex2 > ", dir(a))

a._SampleA__y = 2  # 수정 가능

print(f"Ex2 > y : {a._SampleA__y}")

# Ex3
# 메소드 활용 Getter, Setter


class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0  # _SampleB__y
        self._z = 0

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value


b = SampleB()
b.x = 1
b.set_y(2000)

print(f"Ex3 > x : {b.x}")
print(f"Ex3 > y : {b.get_y()}")

# 변수 접근 후 수정 부분에서 일관성 및 가독성이 하락
b._SampleB__y = 343

print("Ex3 > ", dir(b))
