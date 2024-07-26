
'''
에러와 예외
문법 에러 : Syntax Error : 문법오류나 잘못된 할당. 소괄호문제 등 코딩 문제
예외 : Exception : 내장 예외_파이썬에서 이미 정의된 상황에 대한 처리.
    ZeroDivisonError : 나누기 또는 모듈 연산의 두번째 인자가 0일 때.
    NameError : 지역 또는 전역 이름을 찾을 수 없을 때
    TypeError : 타입 불일치 또는 인자 누락, 인자 초과, 인자 타입 불일치
    ValueError : 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받음
    IndexError : 시퀀스 인덱스가 범위를 벗어날 때 발생
    KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우
    ModuleNotFoundError : 모듈을 찾을 수 없을 때 발생
    ImportError : import 이름을 찾을 수 없을 때 발생
    KeyboardInterrupt : 사용자가 ctrl-C또는 del을 누를 때 발생. 무한루프 강제종료
    IndentationError : 잘못된 들여쓰기 등 문법 오류
예외처리 : Exception Handling : 예외 발생 시에 적절하게 처리되도록 하는 방법. 복수처리 가능_하위 예외클래스부터 확인하도록 
    try : 예외 발생 가능 코드
    except : 예외 발생 시 실행 코드
    else : 예외 발생하지 않을 시 실행 코드
    finally : 예외발생여부에 무관하게 항상 실행할 코드
'''
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
# 0으로 나눌 수 없습니다.


try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')
"""
숫자입력 : a
숫자가 아닙니다.
"""


try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')


try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')
