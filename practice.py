# # 주석 넣는법
# 1. #
# 2. ''' 문장 '''
# 3. 여러 문장 선택 후 ctrl + /

'''
print("야호"*9)

############ 참 / 거짓 ############
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not 5>10)
'''

'''
############ 변수 활용 ############
# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는" + str(age) + " 살이며, " + hobby + "을 아주 좋아해요")
#print(name, "는" , str(age) , " 살이며, " , hobby , "을 아주 좋아해요")
# "+" 대신 "," 도 사용 가능 단, ","는 띄워쓰기 포함 
print(name + "는 어른일까요? " + str(is_adult))

############ 변수 활용 퀴즈1 ############
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
'''

'''
############ 연산자 ############
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 몫 구하기 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # 두 값이 같은지 비교하는 연산 = True
print(4 == 2) # False
print(3 + 4 == 7) #True

print(1 != 3) # 두 값이 같지 않은 지 비교하는 연산 = True
print(not(1 != 3)) # True의 not이기 때문에 False

print((3 > 0) and (3 < 5)) # 앞 항과 뒷 항이 모두 만족해야 True = True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False
'''

'''
############ 수식 ############
from tkinter import N


print(2 + 3 * 4) # 14
print((2+3) * 4) # 20
number = 2 + 3 * 4 #14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 5 # 1
print(number)
'''

'''
############ 숫자 처리 함수 ############
print(abs(-5)) # 절댓값 = 5
print(pow(4, 2)) # 제곱 4의 2제곱 = 16
print(max(5, 12)) # 최대값 = 12
print(min(5, 12)) # 최소값 = 5
print(round(3.14)) # 반올림 = 3
print(round(4.99)) # 5

# math 라이브러리 이용
from math import *
print(floor(4.99)) # 내림 = 4
print(ceil(3.14)) # 올림 = 4
print(sqrt(16)) # 제곱근 = 4
'''

'''
############ 랜덤 함수 ############
# 랜덤 라이브러리 이용
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값 생성

# 로또
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성 
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

############ 랜덤 함수 활용 퀴즈 2 ############
# 내 풀이
from random import *
print("오프라인 스터디 모임 날짜는 매월 " + str(randrange(4, 28)) + " 일로 선정되었습니다.")

# 강의 풀이
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")
'''

############ 문자열 ############
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)