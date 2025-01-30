"""
Chapter 1
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals

"""

"""

전역변수는 주로 변하지 않는 고정 값에 사용
지역변수 사용 이유 : 지역변수는 함수 내에 로직 해결에 국한, 소멸주기 : 함수 실행 해제 시
전역변수를 지역내에서 수정되는 것은 권장하지 않음
"""

# Ex1
a = 10  # Global variable


def foo():
    # Read global variable
    print("Ex > ", a)


foo()

# Read global variable
print("Ex > ", a)

# Ex2
b = 20


def bar():
    b = 30  # Local variable
    print("Ex > ", b)


bar()
print("Ex2 > ", b)

# # Ex3
# c = 40


# def foobar():
#     c = c + 10
#     print("Ex3 > ", c)


# foobar()

# Ex4
d = 50


def barfoo():
    global d
    d = 60
    d += 100

    print("Ex4 > ", d)


barfoo()


# Ex 5(중요)
def outer():
    e = 70

    def inner():
        nonlocal e
        e += 10
        print("Ex 5 > ", e)

    return inner


intest = outer()
intest()


# Ex 6
def func(var):
    x = 10

    def printer():
        print("Ex6 > ", "Printer Func Inner")

    print("Func Inner", locals())


func("HI")

# Ex 7
print("Ex > ", globals())
globals()["test_variable"] = 100
test_variable = 100


# Ex 8(지역 -> 전역 변수 생성)
for i in range(1, 10):
    for k in range(1, 10):
        globals()[f"plus_{i}_{k}"] = i + k


print(globals())
print("Ex 8>", plus_5_5)
print("Ex 8>", plus_9_9)

for i in range(1, 10):
    for k in range(1, 10):
        globals()["mul_{}{}".format(i, k)] = i * k

print(mul_99)
print(globals())
