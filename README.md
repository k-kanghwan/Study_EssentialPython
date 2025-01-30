<!-- *NOTE* for write markdown -->
<!-- 
  ## => seciton
  ### => chapter in section 
  #### => contents in lecture(chapter)
1. => number in chapter

★☆☆ : Importance


-->

# 파이썬 필수문법

## Table of Contents
- [파이썬 필수문법](#파이썬-필수문법)
  - [Table of Contents](#table-of-contents)
  - [1. Python Acvanced(1)](#1-python-acvanced1)
    - [Variable Scope](#variable-scope)

## 1. Python Acvanced(1)
### Variable Scope
> [py_ad_1_1.py](Material/SourceCode/py_ad_1_1.py "py_ad_1_1.py")
> - [x] Scope
> - [x] Global 
> - [x] Nonlocal
> - [x] Locals
> - [x] Globals

1. Vairable Scope
    - **Global** : Global Variable
    - **Local** : Local Variable

    ```python
    a = 10  # Global Variable
    b = 20  # Global Variable
    def foo():
        a = 20  # Local Variable
        b = b + 10  # UnboundLocalError: local variable 'b' referenced before assignment
        print(a)
    
    def bar():
        global a
        a = a + 10
        print(a)
    ```

    **<u>Output</u>**
    ```
    20
    30
    ```

2. Nonlocal
    - **Nonlocal** : Local Variable in Nested Function

    ```python
    def outer():
        a = 10
        def inner():
            nonlocal a  # Nonlocal Variable
            a += 20
            print(a)
        return inner
    
    foo = outer()
    foo()
    ```

    **<u>Output</u>**
    ```
    30
    ```

3. Locals, Globals
    - `locals()` : 로컬 변수들의 상태를 딕셔너리 형태로 반환
    - `globals()` : 글로벌 변수들의 상태를 딕셔너리 형태로 반환

    ```python
    test_variable = 100
    print("Ex > ", globals())
    globals()["test_variable"] = 100  # 변수 선언 원리
    ```

    **<u>Output</u>**
    ```
    Ex >  {...,  'test_variable': 100}
    ```

4. 지역 -> 전역 변수 생성
    ```python
    for i in range(1, 10):
        for k in range(1, 10):
            globals()['mul_{}{}'.format(i, k)] = i * k  # 동적으로 전역 변수 생성

    print(mul_99)
    print(globals())
    ```

    **<u>Output</u>**
    ```
    81
    {..., 'mul_99': 81, ...}
    ```

> #### 📖 Summary
>       ✅ 전역변수는 주로 변하지 않는 고정 값에 사용  
>       ✅ 지역변수 사용 이유 : 지역변수는 함수 내에 로직 해결에 국한, 소멸주기 : 함수 실행 해제 시  
>       ✅ 전역변수를 지역 내에서 수정되는 것은 권장하지 않음  
>       ✅ 전역변수는 주로 변하지 않는 고정 값에 사용  

