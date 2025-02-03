"""
Chapter 1
Python advanced(1) - 
"""

"""

컨텍스트 매니저 : 원하는 타이밍에 정확하게 리소스를 할당, 제공 및 반환하는 역할
가장 대표적인 with 구문 이해
정확한 이해 후 사용이 프로그래밍 개발에 중요(문제 발생 요소 인식)

"""

# Ex 1
file = open("./testfile1.txt", "w")  # 운영체제로부터 리소스를 할당
try:
    file.write("Context Manger Test1\nContextlib Test1.")
finally:
    file.close()

# Ex 2
with open("./testfile2.txt", "w") as f:
    f.write("Context Manger Test1\nContextlib Test2.")


# Ex 3
# Use class -> Context Manager with exception handling.
class MyFileWriter:
    def __init__(self, file_name, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print("MyFileWriter started : __enter__")
        return self.file_obj

    def __exit__(self, exe_type, value, trace_back):
        print("MyFileWriter started : __exit__")
        if exe_type:
            print(f"Logging exception {(exe_type, value, trace_back)}")
        self.file_obj.close()


with MyFileWriter("./testfile3.txt", "w") as f:
    f.write("Context Manger Test3\nContextlib Test3.")
