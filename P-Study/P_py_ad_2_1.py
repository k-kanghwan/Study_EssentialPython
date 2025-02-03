"""
Chapter 2
Python Advanced(2) - Context Manager Annotation
Keyword - @contextlib.contextmanager, __enter__, __exit__

"""

"""

가장 대표적인 with 구문 이해
Context lib 데코레이터 사용
코드 직관적, 예외 처리 용이성

"""

import contextlib
import time

# Ex 1
# Use decorator


@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f  # __enter__
    f.close()  # __exit__


with my_file_writer("testfile4.txt", "w") as f:
    f.write("Context Manager Test4.\nContextlib Test4.")

# Ex 2
# Use decorator


@contextlib.contextmanager
def ExcuteTimeDC(msg):
    start = time.monotonic()
    try:  # __enter__
        yield start
    except BaseException as e:
        print(f"Loggin exception: {e}")
        raise
    else:  # __exit__
        print(f"{msg}: {time.monotonic() - start}")


with ExcuteTimeDC("Start Job!") as v:
    print(f"Received start monotonic2 : {v}")
    # Excute job.
    for i in range(100_000_000):
        pass
    # raise ValueError("occured.")
