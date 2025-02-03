"""
Chapter 1
Python advanced(1) - Context Manager(2)
Keyword - Contextlib, __enter__, __exit__, @contextmanager  
"""

"""
Contextlib - Measure Execution(타이머) 제작
"""


# Ex1
# Use class

import time


class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg
        self._start = None

    def __enter__(self):
        self._start = time.monotonic()  # 나노초 단위의 정밀도를 제공
        return self._start

    def __exit__(self, exc_type, value, traceback):
        if exc_type:
            print(f"Logging exception {(exc_type, value, traceback)}")
        else:
            print(f"{self._msg} : {time.monotonic() - self._start}")
        return True  # 문제없이 실행됐음을 반환하기 위해


with ExcuteTimer("Something job") as v:
    print(f"Recieved start monotonic: {v}")  # __enter__ return value
    # Excute job
    for i in range(10_000_000):
        pass

    # raise Exception(
    #     "Raise Exception!"
    # )  # Logging exception (<class 'Exception'>, Exception('Raise Exception!'), <traceback object at 0x104f5cbc0>)
