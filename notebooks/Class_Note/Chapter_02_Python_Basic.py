#!/usr/bin/env python
# coding: utf-8

# # 2장 파이썬 기본 문법

# ## 2.1 변수와 자료형

# ### 2.1.1 변수

# [2장: 33페이지]

# In[ ]:


abc = 12340       # 숫자 12340을 abc 변수에 할당
print(abc + 100)  # abc 변수에 100을 더해서 결과를 출력


# In[ ]:


string1 = "Python is "
string2 = "powerful."
print(string1 + string2)


# ### 2.1.2 숫자(int, float)

# [2장: 35페이지]

# In[ ]:


type(123)


# In[ ]:


type(123.45)


# In[ ]:


5 + 2


# [2장: 36페이지]

# In[ ]:


print(5 + 2)  # 더하기
print(5 - 2)  # 빼기
print(5 * 2)  # 곱하기
print(5 / 2)  # 나누기
print(5 // 2) # 몫 구하기
print(5 % 2)  # 나머지 구하기
print(5 ** 2) # 거듭제곱


# [2장: 37페이지]

# In[ ]:


6 / 3


# In[ ]:


(10/5 + (5-2)) * (1.2+2) / 2**2


# ### 2.1.3 문자열(str)

# [2장: 37페이지]

# In[ ]:


"String"


# In[ ]:


'Test'


# [2장: 38페이지]

# In[ ]:


print("String")
print('Test')


# In[ ]:


print("It's OK.")


# In[ ]:


print('그는 "파이썬이 무엇입니까?"라고 물었습니다.')


# In[ ]:


type('Hello Python!')


# In[ ]:


"Hello" + " " + "Python " + "!"


# In[ ]:


"Python" * 3


# [2장: 39페이지]

# In[ ]:


len("Python")


# In[ ]:


len("Python ")


# In[ ]:


long_str = '''學而不思則罔 思而不學則殆
학이불사즉망 사이불학즉태
"배우기만 하고 생각하지 않으면 얻는 것이 없고, 생각만 하고 배우지 않으면 위태롭다."
(출처: 『논어』위정편 15장)'''

print(long_str)


# ### 2.1.4 불(bool)

# [2장: 40페이지]

# In[ ]:


print(True)


# In[ ]:


print(False)


# In[ ]:


type(True)


# In[ ]:


type(False)


# [2장: 41페이지]

# In[ ]:


print(True and False)
print(True or False)
print(not False)


# In[ ]:


# 숫자 자료형에 대한 비교 연산자 활용 예
print(10 == 5)  # 10과 5는 같다 --> 거짓(False)
print(10 != 5)  # 10과 5는 같지 않다 --> 참(True)
print(10 < 5)   # 10은 5보다 작다 --> 거짓(False)
print(10 > 5)   # 10은 5보다 크다 --> 참(True)
print(10 <= 5)  # 10은 5보다 작거나 같다 --> 거짓(False)
print(10 >= 5)  # 10은 5보다 크거나 같다 --> 참(True)

# 불 자료형에 대한 비교 연산자 활용 예
print(True == False) # True와 False는 같다 --> 거짓(False)
print(True != False) # True와 False는 같지 않다 --> 참(True)


# [2장: 42페이지]

# In[ ]:


1 > 0 and (5 > 10 or 3 < 5)


# ###  2.1.5 리스트(list)

# #### 리스트 만들기

# [2장: 43페이지]

# In[ ]:


list_num = [10, 20, 30, 40] # 숫자로 리스트를 구성
list_str = ['programming', 'language', 'python'] # 문자열로 리스트를 구성
list_mix1 = [1.5, 2.6, '문자열1', '문자열2'] # 숫자와 문자열로 리스트를 구성
list_mix2 = [4.0, True, 'abc', list_mix1] # 숫자, 불, 문자열, 리스트로 리스트를 구성
list_empty = [] # 요소가 없는 빈 리스트

print(list_num)
print(list_str)
print(list_mix1)
print(list_mix2)
print(list_empty)


# [2장: 44페이지]

# In[ ]:


type(list_empty)


# In[ ]:


print(len(list_num))   # 요소의 개수: 4
print(len(list_str))   # 요소의 개수: 3
print(len(list_mix1))  # 요소의 개수: 4
print(len(list_mix2))  # 요소의 개수: 4
print(len(list_empty)) # 요소의 개수: 0


# #### 리스트 연산자

# [2장: 44페이지]

# In[ ]:


list_str1 = ["기술이 ", "강한 나라 "]
list_str2 = ["우리나라 ", "대한민국 "]
list_str3 = list_str1 + list_str2 # 두 리스트의 요소를 연결해서 새로운 리스트를 생성
list_str4 = list_str2 * 2 # 리스트의 요소를 반복해서 연결한 후 새로운 리스트를 생성

print(list_str3)
print(list_str4)


# #### 리스트 인덱싱

# [2장: 45페이지]

# In[ ]:


print(list_num)    # list_num 출력
print(list_num[0]) # list_num의 첫 번째 요소를 가져옴 
print(list_num[1]) # list_num의 두 번째 요소를 가져옴
print(list_num[2]) # list_num의 세 번째 요소를 가져옴
print(list_num[3]) # list_num의 네 번째 요소를 가져옴


# [2장: 46페이지]

# In[ ]:


print(list_num[-1]) # list_num의 마지막 요소를 가져옴
print(list_num[-2]) # list_num의 마지막 요소 앞의 요소를 가져옴


# In[ ]:


print(list_mix2)       # list_mix2 출력
print(list_mix2[3])    # list_mix2에서 네 번째 요소를 가져옴
print(list_mix2[3][2]) # 네 번째 요소인 리스트에서 세 번째 요소를 가져옴


# In[ ]:


list_num1 = [100, 200, 300, 400] # 리스트 생성
print(list_num1) 

list_num1[1] = 500 # 두 번째 요소에 새로운 데이터를 할당
print(list_num1)


# [2장: 47페이지]

# In[ ]:


list_num2 = [0, 10, 20, 30, 40, 50] # 숫자로 리스트를 구성
print(list_num2)

del list_num2[2] # 리스트에서 인덱스가 2인 요소를 제거
print(list_num2)


# #### 리스트 슬라이싱

# [2장: 48페이지]

# In[ ]:


list_num3 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] # 리스트 생성

print(list_num3)      # 리스트 출력
print(list_num3[0:4]) # 인덱스 범위: 0~3
print(list_num3[5:10]) # 인덱스 범위: 5~9


# In[ ]:


print(list_num3[:4]) # start를 생략. 인덱스 범위: 0~3
print(list_num3[5:]) # end를 생략. 인덱스 범위: 5~끝(9)
print(list_num3[:])  # start와 end 둘 다 생략. 인덱스 범위: 모든 인덱스


# #### 리스트 요소의 존재 여부 확인

# [2장: 49페이지]

# In[ ]:


list_num6 = [0, 1, 2, 3] # 리스트 생성

print(2 in list_num6) # 2는 리스트에 있음: True 반환
print(5 in list_num6) # 5는 리스트에 없음: False 반환


# #### 리스트 메서드

# [2장: 50페이지]

# In[ ]:


friends = ['토마스'] # 리스트를 생성
print(friends)

friends.append('고든') # 리스트의 끝에 요소('고든')를 추가
print(friends)

friends.append('에드워드') # 리스트의 끝에 요소('에드워드')를 추가
print(friends)


# ### 2.1.6 튜플(tuple)

# #### 튜플 만들기

# [2장: 51페이지]

# In[ ]:


tuple_num1 = (0, 1, 2, 3, 4) # 소괄호로 튜플을 생성
tuple_num2 =  5, 6, 7, 8, 9  # 괄호 없이 튜플을 생성

print(tuple_num1)
print(tuple_num2)


# In[ ]:


type(tuple_num1)


# In[ ]:


type(tuple_num2)


# [2장: 52페이지]

# In[ ]:


tuple_num3 = (10, )      # 소괄호로 하나의 요소를 갖는 튜플 생성
tuple_num4 =  "데이터1", # 괄호 없이 하나의 요소를 갖는 튜플 생성 

print(tuple_num3)
print(tuple_num4)


# #### 튜플 다루기

# [2장: 52페이지]

# In[ ]:


tuple_mixed1 = ('programming', 'language', 'python', 1, 2, 3) # 튜플 생성
print(tuple_mixed1[0])   # 튜플 인덱싱
print(tuple_mixed1[0:4]) # 튜플 슬라이싱(인덱스 0~3까지의 요소를 선택) 


# In[ ]:


tuple_mixed1[3] = 10 # 튜플의 요소를 변경할 수 없어서 오류가 발생


# ### 2.1.7 세트(set)

# #### 세트 만들기

# [2장: 53페이지]

# In[ ]:


set_num = {10, 100, 2, 3, 4, 4, 5}
set_str = {"사과", "배", "오렌지", "귤", "귤"}

print(set_num)
print(set_str)


# [2장: 54페이지]

# In[ ]:


type(set_str)


# In[ ]:


set_num[0]


# #### 세트의 교집합, 합집합, 차집합

# [2장: 54페이지]

# In[ ]:


set_A = {0, 1, 2, 3, 4} # 세트(집합) A
set_B = {3, 4, 5, 6, 7} # 세트(집합) B

# &, |, - 연산자 사용
print(set_A & set_B)    # 집합 A와 B의 교집합(A∩B)
print(set_A | set_B)    # 집합 A와 B의 합집합(A∪B)
print(set_A - set_B)    # 집합 A와 B의 차집합(A―B)

# intersection(), union(), difference() 메서드 사용
print(set_A.intersection(set_B)) # 집합 A와 B의 교집합(A∩B)
print(set_A.union(set_B))        # 집합 A와 B의 합집합(A∪B)
print(set_A.difference(set_B))   # 집합 A와 B의 차집합(A―B)


# ### 2.1.8 딕셔너리(dict)

# #### 딕셔너리 만들기

# [2장: 55페이지]

# In[ ]:


dict_ex1 = {1:'사과', 2:'배', 3:'복숭아', 4:'딸기'}     # 키는 숫자, 값은 문자열
dict_ex2 = {1:1234, 5:5678, 7:7890}                     # 키와 값이 모두 숫자
dict_ex3 = {True: '맞습니다.', False:'아닙니다.'}      # 키는 불, 값은 문자열 
dict_ex4 = {'ID_101':['민준',24], 'ID_102':['서연',27]} # 키는 문자열, 값은 리스트

print(dict_ex1)
print(dict_ex2)
print(dict_ex3)
print(dict_ex4)


# [2장: 56페이지]

# In[ ]:


type(dict_ex4)


# In[ ]:


dict_ex5 = dict(a=10, b=2.0,  c='string', d=True, abc=[1,2,3])
dict_ex5


# #### 딕셔너리 키로 값 선택, 변경, 추가, 삭제하기

# [2장: 57페이지]

# In[ ]:


print(dict_ex1[1])
print(dict_ex2[7])
print(dict_ex3[True])
print(dict_ex4['ID_102'])
print(dict_ex5['b'])


# In[ ]:


dict_user = {"이름": "박재민", "나이": 24} # 딕셔너리 생성
print(dict_user)

dict_user["나이"] = 25 # 기존 키로 값을 변경
print(dict_user)

dict_user["취미"] = ["게임", "농구"] # 새로운 키와 값의 쌍을 추가
print(dict_user)


# [2장: 58페이지]

# In[ ]:


dict_user2 = {'이름': '조수빈', '나이': 28, '취미': ['독서', '영화']}
print(dict_user2)

del dict_user2['취미'] # del을 이용해 딕셔너리의 특정 키와 값의 쌍을 삭제  
print(dict_user2)


# #### 딕셔너리 키의 존재 여부 확인

# [2장: 58페이지]

# In[ ]:


dict_vehicle = {'버스':1, '기차':2, '배':3, '비행기':4} # 딕셔너리 생성

print('기차' in dict_vehicle) # dict_vehicle의 키에 '기차'는 있음
print('택시' in dict_vehicle) # dict_vehicle의 키에 '택시'는 없음


# #### 딕셔너리 메서드

# [2장: 59페이지]

# In[ ]:


dict_num_alpha = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'} # 딕셔너리 생성
print(dict_num_alpha)          # dict_num_alpha 출력
print(dict_num_alpha.keys())   # 딕셔너리의 키를 가져옴
print(dict_num_alpha.values()) # 딕셔너리의 값을 가져옴
print(dict_num_alpha.items())  # 딕셔너리의 키와 값의 쌍을 가져옴


# [2장: 60페이지]

# In[ ]:


print(list(dict_num_alpha.keys()))   # 딕셔너리 키의 반환 결과를 리스트로 변환
print(list(dict_num_alpha.values())) # 딕셔너리 값의 반환 결과를 리스트로 변환
print(list(dict_num_alpha.items()))  # 딕셔너리 키와 값의 쌍 반환 결과를 리스트로 변환


# In[ ]:


print(dict_num_alpha)             # 기존 딕셔너리 출력

dict_new = {5: 'f', 6: 'g'}       # 딕셔너리 생성
dict_num_alpha.update(dict_new)   # 기존 딕셔너리에 새로운 딕셔너리의 키와 값의 쌍을 추가
print(dict_num_alpha)             # 새로운 딕셔너리 추가 후 딕셔너리 출력


# In[ ]:


print(dict_num_alpha.get(1)) # 입력값이 딕셔너리 키에 있으면 대응하는 값을 반환 
print(dict_num_alpha.get(7)) # 입력값이 딕셔너리 키에 없으면 None을 반환


# [2장: 61페이지]

# In[ ]:


dict_num_eng = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}
print(dict_num_eng)

dict_num_eng.clear() # 딕셔너리의 모든 키와 값의 쌍을 삭제
print(dict_num_eng)


# ## 2.2 제어문

# ### 2.2.1 조건문

# #### 단일 조건에 따른 분기: if

# [2장: 62페이지]

# In[ ]:


x = 95           # x에 95를 할당

if x >= 90:      # <조건>
    print("합격") # <조건>이 참이면 <코드 블록>을 수행


# #### 단일 조건과 그 외에 따른 분기: if ~ else

# [2장: 63페이지]

# In[ ]:


x = 85                            # x에 85를 할당

if x >= 90:                      # <조건>
    print("축하합니다.")          # <코드 블록 1>
    print("당신은 합격입니다.")   # <조건>이 참이면 <코드 블록 1>을 수행
else:
    print("죄송합니다.")          # <코드 블록 2>
    print("당신은 불합격입니다.") # <조건>이 참이 아니면 <코드 블록 2>를 수행


# #### 여러 조건에 따른 분기: if ~ elif ~ else

# [2장: 64페이지]

# In[ ]:


x = 75                # x에 75를 할당

if x >= 90:           # <조건1>
    print("학점: A")  # <코드 블록 1>
elif  80 <= x < 90:  # <조건2>: 80 <= x < 90는 (x >= 80) and (x < 90)과 같음  
    print("학점: B")  # <코드 블록 2>
elif  70 <= x < 80:  # <조건3>
    print("학점: C")  # <코드 블록 3>
else:
    print("학점: D")  # <코드 블록 4>


# In[ ]:


x = 100

if x >= 90:
    if x == 100:
        print("만점으로 합격")
    else:
        print("합격")
else:
    print("불합격")


# ### 2.2.2 반복문

# #### for 반복문

# [2장: 65페이지]

# In[ ]:


for num in [0, 1, 2, 3, 4, 5]:
    print(num)


# [2장: 66페이지]

# In[ ]:


list(range(0, 10, 1))


# In[ ]:


list(range(10))


# In[ ]:


for num in range(6):
    print(num)


# [2장: 67페이지]

# In[ ]:


list_num = [10, 20, 30, 40]

for index, value in enumerate(list_num):
     print(index, value)


# In[ ]:


names = ["남온조", "이청산", "최남라", "이수혁", "이나연", "양대수"] # 이름
scores = [96, 85, 100, 70, 80, 75] # 시험점수


# In[ ]:


for k in range(len(names)):
    print(names[k], scores[k])


# [2장: 68페이지]

# In[ ]:


for name, score in zip(names, scores):
    print(name, score)


# #### while 반복문

# [2장: 69페이지]

# In[ ]:


list_num = []   # 빈 리스트 생성
count = 0       # count를 0으로 초기화

while (count < 10):        # <조건> count가 10보다 작은지 검사 
    list_num.append(count)  # <코드 블록> list_num에 count 추가
    count = count + 1       # <코드 블록> count를 1씩 증가
    
print(list_num) # 리스트 list_num의 내용을 출력


# #### 반복의 흐름을 바꾸는 break와 continue

# [2장: 69페이지]

# In[ ]:


num = [1, 2, 3, 4, 5, 6]
num_sum = 0 # 숫자의 합계를 0으로 초기화
count = 0 # count를 0으로 초기화

while True:
    num_sum = num_sum + num[count] # 리스트 num의 요소를 하나씩 더함
    print(num_sum)
    if (num_sum >= 10): # 합계(num_sum)가 10 이상인지 검사
        print("while 문을 끝냅니다.")
        break # while 문을 끝냄
    
    count = count + 1 # count를 1씩 증가


# [2장: 70페이지]

# In[ ]:


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months_data = [15, 21, 33, 17, 19, 22, 16, 25, 27, 18, 13, 14]
data_sum = 0 # 숫자 합계를 초기화

for month, data in zip(months, months_data):
    if(month == 5):
        print('해당 월의 데이터를 제외합니다.')
        continue # 이후 코드는 실행하지 않고 다음 반복으로 넘어감
    data_sum = data_sum + data # 월별 데이터의 합계를 구함
    
print(data_sum) # for 문에서 계산된 전체 합계를 출력


# #### 한 줄 for 반목문

# [2장: 71페이지]

# In[ ]:


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 리스트 생성

# 리스트의 각 요소에 2*x+1 연산을 수행해서 새로운 리스트 생성
result = [2*x+1 for x in numbers]

print(result) # 생성한 리스트 출력


# In[ ]:


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 리스트 생성

# x >=3 조건을 만족할 때만 2*x+1 연산을 수행
result = [2*x+1 for x in numbers if x>=3]

print(result) # 생성한 리스트 출력


# ## 2.3 데이터의 출력 

# ### 2.3.1 기본 출력

# [2장: 72페이지]

# In[ ]:


print(1, 2, 3, 4, 5) # 숫자 출력
print('a', 'b', 'c', 'd', 'e') # 문자 출력
print(123, "abc", True) # 숫자, 문자, 불 출력
print(['abc', 123, 'def'], {"a": 1, "b": 2}) # 리스트와 딕셔너리 출력


# [2장: 73페이지]

# In[ ]:


print("합계:") # end 옵션이 없으면 개행문자가 들어가서 줄 바꿈 수행
print(90)
print("합계:", end='') # end 옵션에 빈 문자열을 입력해 줄 바꿈이 없도록 함
print(90)


# In[ ]:


print("나는 파이썬을 이용해 \n많은 업무를 \n자동화합니다.")


# ### 2.3.2 형식 지정 출력

# [2장: 73페이지]

# In[ ]:


fruit_0 = "Banana"
fruit_1 = "Apple"
fruit_2 = "Orange"

print("문자열 출력: {0}, {1}, {2}".format(fruit_0, fruit_1, fruit_2))
print("문자열 출력: {2}, {0}, {1}".format(fruit_0, fruit_1, fruit_2))


# [2장: 74페이지]

# In[ ]:


print("문자열 출력: {}, {}, {}".format(fruit_0, fruit_1, fruit_2))


# In[ ]:


num_int = 123
num_float= 3.14159265358979323846 

print("숫자 출력: {0}, {1}".format(num_int, num_float))


# [2장: 75페이지]

# In[ ]:


list_num_ints = [1, 12, 123, 1234, 12345] # 리스트 생성

print("[숫자(정수)의 출력 형식을 지정하지 않고 출력]")
for list_num_int in list_num_ints:
    print("{0}".format(list_num_int)) # 출력 형식 미지정
    
print("\n[숫자(정수)의 출력 형식을 지정해 출력]")
for list_num_int in list_num_ints:
    print("{0:6d}".format(list_num_int)) # 출력 형식(정수의 출력 자리 개수) 지정


# In[ ]:


print("[숫자(실수)의 출력 형식을 지정해 출력]")
print("{0:.2f}, {0:.5f}, {0:.0f}".format(num_float))


# [2장: 76페이지]

# In[ ]:


temp_c = 10.5 # 섭씨 온도
temp_f = (temp_c * 9/5) + 32 # 변환된 화씨 온도로 변환

# string.format() 의 결과를 변수에 할당
format_str = "변환 결과: 섭씨 {0:.1f}도 → 화씨 {1:.1f}도".format(temp_c, temp_f)

print(format_str) # 변수의 내용을 출력


# In[ ]:


user_name = "홍길동" 
user_number = "1234-5678"

print("고객 이름:{name}, 고객 번호:{number}".format(name=user_name, number=user_number))


# [2장: 77페이지]

# In[ ]:


name = "최서희"
phone_number = "010-xyz-1234"

print(f"이름: {name}, 전화번호: {phone_number}") # f-문자열 방식을 이용한 출력


# In[ ]:


r = 2 # 반지름 
pi = 3.141592 # 파이

print(f"제품 가격: {57250000:,}원") # {표현내용}에 값을 직접 입력
print(f"파이(소수점 6자리까지): {pi:.6f}") # {표현내용}에 변수를 입력
print(F"반지름이 {r}인 원의 넓이: {pi*r**2:.2f}") # {표현내용}에 계산식을 입력


# ## 2.4 예외 처리

# ### 2.4.1 try ~ except 사용

# [2장: 78페이지]

# In[ ]:


10/0


# [2장: 79페이지]

# In[ ]:


try:
    10/0
except:
    print("실행 중 오류가 발생했습니다.")


# In[ ]:


try:
    10/0
except ZeroDivisionError:
    print("실행 중 숫자를 0으로 나누었습니다.")


# In[ ]:


try:
    for k in [1,2,3]:
        if(k==3):
            print("k = {0}. 일부러 오류 발생".format(k))
            raise
        else:
            print("k = {0}".format(k))
except:
    print("실행 중 오류가 발생했습니다.")


# ### 2.4.2 try ~ finally 사용

# [2장: 80페이지]

# In[ ]:


tuple_num = (1,2,3) # 튜플 데이터

try:
    tuple_num[0] = 4 # 튜플의 요소를 변경할 수 없어 오류 발생
except:
    print("오류가 발생했습니다.")
finally:
    print("tuple_num = {0}".format(tuple_num))


# ## 2.5 정리
