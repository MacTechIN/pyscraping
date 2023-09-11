#!/usr/bin/env python
# coding: utf-8

# # 3장 함수, 클래스, 모듈

# ## 3.1 함수

# ### 3.1.1 함수의 정의와 호출

# #### 함수의 기본 구조

# #### 함수의 다양한 예

# [3장: 84페이지]

# In[ ]:


# 함수의 정의(이모티콘 출력)
def my_emoticon():
    print("=======")
    print(" (^o^)")
    print("=======")
    
# 함수의 호출
my_emoticon()


# In[ ]:


# 함수의 정의(게임 정보 출력)
def game_info_display(name, version, genre): # 3개의 매개변수를 갖는 함수
    print("--- 게임 정보 ----")
    print("이름:", name)
    print("버전:", version)
    print("장르:", genre)

# 함수의 호출(매개변수의 개수와 같은 순서로 인수를 입력)
game_info_display("고독한 방랑자", "2.02", "MMORPG")


# In[ ]:


# 함수의 정의(y = 2*x + 1)
def my_func(x):
    y = 2*x + 1
    return y

# 함수의 호출(함수의 인수는 숫자로 입력)
my_func(3)


# [3장: 85페이지]

# In[ ]:


result = my_func(5)
result


# In[ ]:


# 함수의 정의(리스트를 입력 받아서 합계와 평균 반환) 
def calc_sum_mean(list_data):
    e_count = 0  # 요소 개수(초기화)
    e_sum = 0    # 요소 합계(초기화)
    
    for element in list_data:
        e_count = e_count + 1    # 요소 개수 계산
        e_sum = e_sum + element  # 요소 합계 계산
    e_mean = e_sum / e_count     # 평균 = 합계/개수
    
    return e_sum, e_mean  # 계산 합계와 평균을 반환(자료형은 튜플)

# 함수의 호출(인수는 리스트로 입력)
calc_sum_mean([1, 2, 3, 4, 5, 6, 7, 8, 9])


# [3장: 86페이지]

# In[ ]:


list_sum, list_mean = calc_sum_mean([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list_sum)
print(list_mean)


# #### 매개변수에 기본값을 할당한 함수

# In[ ]:


def my_add(a=1, b=2, c=3):
    y = a + b + c
    print("{0} + {1} + {2} = {3}".format(a, b, c, y))


# [3장: 87페이지]

# In[ ]:


# 모든 매개변수가 기본값을 사용
my_add()     

# 첫 번째 매개변수는 입력한 인수를 사용하고 나머지는 기본값을 사용
my_add(11)      

# 첫 번째와 두 번째 매개변수는 입력한 인수를 사용하고 나머지는 기본값을 사용
my_add(11, 12) 

# 모든 매개변수가 입력한 인수를 사용
my_add(11, 12, 13) 


# In[ ]:


# 첫 번째와 세 번째 매개변수는 입력한 인수를 사용하고 두 번째는 기본값을 사용 
my_add(11, c=13) # 인수 입력이 매개변수에 의한 입력보다 먼저 와야 함 

# 두 번째와 세 번째 매개변수는 입력한 인수를 사용하고 첫 번째는 기본값 사용 
my_add(c=13, b=12) # 매개변수에 의한 입력끼리는 순서가 중요하지 않음


# In[ ]:


def my_add2(a, b, c=3, d=4):
    y = a + b + c + d
    print("{0} + {1} + {2} + {3} = {4}".format(a, b, c, d, y))


# [3장: 88페이지]

# In[ ]:


my_add2(1, 2)         # 기본값 없는 매개변수는 반드시 인수 필요. c와 d에는 기본값 입력
my_add2(1, 2, 13)     # d에는 기본값이 입력됨
my_add2(1, 2, 13, 14) # c와 d에 모두 인수로 지정한 값 입력
my_add2(1, 2, d=14)   # c에는 기본값이 입력됨


# #### 지역 변수와 전역 변수

# [3장: 88페이지]

# In[ ]:


a = 10 # 전역 변수. 어디서나 사용

def func1():
    a = 1 # 지역 변수. 함수 func1 내에서만 사용
    print("[func1()] 지역 변수 a =", a)
    
def func2():
    a = 2 # 지역 변수. 함수 func2 내에서만 사용
    print("[func2()] 지역 변수 a =", a)    
    
def func3():
    print("[func3()] 전역 변수 a =", a) # 전역 변수를 변경 없이 사용
    
def func4():
    global a # 함수 내에서 전역 변수를 변경하려면 반드시 'global 전역변수명' 선언 필요
    a = 20    # 전역 변수의 값 변경
    print("[func4()] 전역 변수 a =", a)


# [3장: 89페이지]

# In[ ]:


func1()
func2()


# In[ ]:


print("전역 변수 a = ", a)


# In[ ]:


func3() # 함수 내에서 전역 변수 a를 호출
func4() # 함수 내에서 전역 변수 a의 값을 변경
func3() # 함수 내에서 전역 변수 a를 호출


# ### 3.1.2 내장 함수

# #### 자료형 변환 함수

# [3장: 90페이지]

# In[ ]:


print("정수로 변환:", [int(12.34), int("1234"), int(0.56), int(-56.78)])
print("실수로 변환:", [float(12), float("12.34"), float("56"), float(-98)])
print("문자열로 변환:", [str(12), str(12.34)])


# [3장: 91페이지]

# In[ ]:


print("튜플/세트 -> 리스트로 변환:", list((1,2,3)), list({1,2,3})) 
print("리스트/세트 -> 튜플로 변환:", tuple([1,2,3]), tuple({1,2,3}))
print("리스트/튜플 -> 세트로 변환:", set([1,2,3]), set((1,2,3)))


# In[ ]:


list_data = [100, 2, 3, 4, 5, 5, 5] # 리스트 데이터

print(list_data)
print(set(list_data))   # 리스트 데이터를 세트로 변환


# #### 최솟값, 최댓값,  합계를 구하는 함수

# [3장: 92페이지]

# In[ ]:


list_data = [-2, -1, 0, 1, 2, 3, 4, 5] # 리스트 데이터

print("최소:", min(list_data)) # 리스트 요소의 최솟값
print("최대:", max(list_data)) # 리스트 요소의 최댓값
print("합계:", sum(list_data)) # 리스트 요소의 합


# In[ ]:


mean = sum(list_data) / len(list_data) # 요소의 평균 = 요소의 합 / 요소의 개수

print("평균:", mean)


# In[ ]:


set_data = {-2, -1, 0, 1, 2, 3, 3, 3} # 중복 요소는 제거하고 세트 생성

print("세트 데이터:", set_data)
print("최소: {}, 최대: {}".format(min(set_data), max(set_data)))
print("합계: {}, 데이터 개수: {}".format(sum(set_data), len(set_data)))


# ## 3.2 클래스

# ### 3.2.1 클래스와 객체

# ### 3.2.2 클래스 선언

# [3장: 95페이지]

# In[ ]:


class Robot():
    def __init__(self, name, position):    # 초기화 함수
        self.name = name                   # 인스턴스 변수(로봇 객체의 이름) 초기화
        self.position = position           # 인스턴스 변수(로봇 객체의 초기 위치) 초기화 
       
    def move(self):                        # 앞으로 한 칸 이동을 위한 함수
        self.position = self.position + 1  # 이전 위치에서 앞으로 한 칸 이동
        print(f"{self.name}의 현재 위치: {self.position}")


# ### 3.2.3 객체 생성과 활용

# [3장: 96페이지]

# In[ ]:


robot1 = Robot('R1', 0)  # 클래스에서 객체 생성


# In[ ]:


print(f"로봇의 이름: {robot1.name}, 초기 위치: {robot1.position}")


# [3장: 97페이지]

# In[ ]:


robot1.move() # 객체의 메서드 move 호출


# In[ ]:


robot2 = Robot('R2', 10) # 클래스에서 객체 생성
# 객체의 속성에 접근해 로봇의 이름과 초기 위치 출력 
print(f"로봇의 이름: {robot2.name}, 초기 위치: {robot2.position}") 

robot2.move() # 객체의 메서드 move 호출(호출할 때마다 한 칸씩 이동)
robot2.move() # 객체의 메서드 move 호출(호출할 때마다 한 칸씩 이동)


# ## 3.3 모듈

# ### 3.3.1 모듈 만들고 불러오기

# #### 모듈 만들기

# [3장: 98페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch03\\calc_area.py', '# File name: calc_area.py\nPI = 3.14\ndef rectangle(l, w): # 직사각형(가로: l, 세로: w)의 넓이를 반환\n    return l * w\n\ndef circle(r): # 원(반지름: r)의 넓이를 반환\n    return PI * r ** 2\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/code/ch03/car.py', '# File name: car.py\nclass Car(): # 클래스 선언\n    def __init__(self, size, color):\n        self.size = size    # 인스턴스 변수 생성 및 초기화\n        self.color = color  # 인스턴스 변수 생성 및 초기화\n        \n    def move(self):\n        print("자동차({0} & {1})가 움직입니다.".format(self.size, self.color))\n')


# #### 모듈 불러오기

# [3장: 99페이지]

# In[ ]:


cd C:\myPyScraping\code\ch03


# In[ ]:


import calc_area                # 모듈 임포트
 
pi = calc_area.PI                # 임포트한 모듈의 변수를 사용
rect = calc_area.rectangle(5, 2) # 임포트한 모듈의 함수를 호출
circ = calc_area.circle(3)       # 임포트한 모듈의 함수를 호출

print(f"원주율:{pi}, 직사각형 넓이: {rect}, 원의 넓이: {circ}")    


# In[ ]:


import car                        # 모듈 임포트

my_car = car.Car("중형", "검은색") # 임포트한 모듈의 클래스에서 객체를 생성
my_car.move()                      # 객체의 메서드를 호출


# [3장: 100페이지]

# In[ ]:


from calc_area import PI, rectangle, circle # 모듈의 변수, 함수를 임포트

pi = PI                # 모듈명 없이 바로 변수를 사용
rect = rectangle(5, 2) # 모듈명 없이 바로 함수를 호출
circ = circle(3)       # 모듈명 없이 바로 함수를 호출

print(f"원주율:{pi}, 직사각형 넓이: {rect}, 원의 넓이: {circ}")    


# [3장: 101페이지]

# In[ ]:


import calc_area as area   # 모듈을 불러와서 별명으로 지정

pi = area.PI                # 임포트한 모듈의 별명과 함께 변수를 사용
rect = area.rectangle(5, 2) # 임포트한 모듈의 별명과 함께 함수를 호출
circ = area.circle(3)       # 임포트한 모듈의 별명과 함께 함수를 호출

print(f"원주율:{pi}, 직사각형 넓이: {rect}, 원의 넓이: {circ}")   


# In[ ]:


from calc_area import PI as pi          # 모듈의 변수를 별명으로 지정
from calc_area import rectangle as rect # 모듈의 함수를 별명으로 지정
from calc_area import circle as circ    # 모듈의 함수를 별명으로 지정

p = pi          # 모듈의 변수를 별명으로 사용
r = rect(5, 2)  # 모듈의 함수를 별명으로 호출
c = circ(3)     # 모듈의 함수를 별명으로 호출

print(f"원주율:{p}, 직사각형 넓이: {r}, 원의 넓이: {c}")   


# ### 3.3.2 내장 모듈

# #### 파일과 경로 처리 모듈

# [3장: 104페이지]

# In[ ]:


from pathlib import Path

# 파일의 경로 입력해 Path 클래스에서 file_path 객체 생성
file_path = Path('C:/myPyScraping/code/ch03/car.py')

print("- 파일의 전체 경로:", file_path)          # 파일의 전체 경로 출력
print("- 파일의 디렉터리:", file_path.parent)    # 파일의 디렉터리 출력
print("- 파일명:", file_path.name)               # 파일의 이름 출력
print("- 파일의 확장자:", file_path.suffix)      # 파일의 확장자 출력
print("- 확장자 제외한 파일명:", file_path.stem) # 확장자를 제외한 파일명 출력


# In[ ]:


from pathlib import Path

dir_path = Path('C:/myPyScraping/code/ch03') # 디렉터리 경로를 입력해 dir_path 객체 생성

print("- 지정한 경로:", dir_path)
print("- 경로 존재 여부 확인:", dir_path.exists())
print("- 경로가 디렉터리(폴더)인지 확인:", dir_path.is_dir())
print("- 경로가 파일인지 확인:", dir_path.is_file())
print("- 홈 디렉터리:", dir_path.home())


# [3장: 105페이지]

# In[ ]:


print("- 파일의 전체 경로:", file_path)  
print("- 경로 존재 여부 확인:", file_path.exists())
print("- 경로가 디렉터리(폴더)인지 확인:", file_path.is_dir())
print("- 경로가 파일인지 확인:", file_path.is_file()) 


# #### 날짜와 시간 처리 모듈

# [3장: 106페이지]

# In[ ]:


from datetime import date, time, datetime, timedelta

date_obj = date(2020, 10, 9)
time_obj = time(15, 23, 21)
datetime_obj = datetime(2021, 8, 15, 20, 19, 45)

print("[date 클래스로 날짜 지정]", date_obj)
print("[date 클래스의 속성 이용] {0}/{1}/{2}".format(date_obj.year, 
                                                     date_obj.month, 
                                                     date_obj.day))

print("[time 클래스로 시각 지정]", time_obj)
print("[time 클래스의 속성 지정] {0}/{1}/{2}".format(time_obj.hour, 
                                                     time_obj.minute, 
                                                     time_obj.second))

print("[datetime 클래스로 날짜와 시각 지정]", datetime_obj)


# [3장: 107페이지]

# In[ ]:


date_obj2 = date(2020, 10, 15)   # 날짜 지정
diff_date = date_obj2 - date_obj # date 객체의 날짜 차이를 연산
diff_date


# In[ ]:


print("두 날짜의 차이: {}일".format(diff_date.days))


# In[ ]:


date_org = date(2022, 5, 15) # 날짜 지정
date_result = date_org - timedelta(weeks=1) # 일주일 전의 날짜 계산
print("지정 날짜: {0}, 일주일 전 날짜: {1}".format(date_org, date_result))


# [3장: 108페이지]

# In[ ]:


# 날짜 및 시간 지정
datetime_org = datetime(2021, 11, 14, 23, 0, 0) 

# 1시간 30분 후 날짜 및 시각 계산
datetime_result = datetime_org + timedelta(hours=1, minutes=30) 

print(datetime_result)


# In[ ]:


today = date.today()
now = datetime.now()

print("- 오늘의 날짜: {0}-{1}-{2}".format(today.year, today.month, today.day))
print("- 현재의 날짜 및 시각(전체 표시):", now)
print("- 현재의 날짜: {0}-{1}-{2}".format(now.year, now.month, now.day))
print("- 현재의 시각: {0}:{1}:{2}".format(now.hour, now.minute, now.second))


# In[ ]:


special_day = datetime(2021, 4, 8, 13, 30, 0)

print("- 날짜 표시: {0:%Y}년 {0:%m}월 {0:%d}일".format(special_day))
print("- 날짜 표시(다른 표현): {:%Y-%m-%d}".format(special_day))
print("- 시각 표시: {0:%H}시 {0:%M}분 {0:%S}초 ({0:%p})".format(special_day))
print("- 시각 표시(다른 표현): {:%H/%M/%S (%p)}".format(special_day))
print("- 요일 표시: {0:%A}, {0:%a}, {0:%w}".format(special_day))
print("- 월 표시: {0:%B}, {0:%b}".format(special_day))


# [3장: 109페이지]

# In[ ]:


import locale

# 한글, 한국, UTF-8 인코딩을 로케일로 지정
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')  

print("* 설정한 로케일: ", locale.getlocale())  # 설정한 로케일 가져오기
print("- 요일 표시(한글/한국): {0:%A}, {0:%a}".format(special_day))
print("- 월 표시(한글/한국): {0:%B}, {0:%b}".format(special_day))

# 영어, 미국, UTF-8 인코딩을 로케일로 지정
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 

print("* 설정한 로케일: ", locale.getlocale()) # 설정한 로케일 가져오기
print("- 요일 표시(영어/미국): {0:%A}, {0:%a}".format(special_day))
print("- 월 표시(한글/한국): {0:%B}, {0:%b}".format(special_day))


# [3장: 110페이지]

# In[ ]:


# 한글, 한국, UTF-8 인코딩을 로케일로 지정
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')  
print(special_day.strftime("[날짜] %Y-%m-%d, %A [시간] %H:%M:%S (%p)"))

# 영어, 미국, UTF-8 인코딩을 로케일로 지정
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 
print(special_day.strftime("[Date] %Y-%m-%d, %A [Time] %H:%M:%S (%p)"))


# ### 3.3.3 패키지

# #### 패키지 구조

# #### 패키지 작성

# [3장: 111페이지]

# In[ ]:


from pathlib import Path

# 디렉터리 경로를 입력해 path 객체를 생성
dir_path = Path('C:/myPyScraping/code/ch03/image/io_file')          

# 디렉터리가 없다면 생성
dir_path.mkdir(parents=True, exist_ok=True)

# 생성한 디렉터리의 존재 여부 확인
print("{0} 디렉터리의 존재 여부: {1}".format(dir_path, dir_path.exists()))


# [3장: 112페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/code/ch03/image/io_file/img_read.py', '# File name: img_read.py\n\ndefault_image = "=> variable \'default_imag\' in img_read module"\n\ndef png_read():\n    print("- png_read() in img_read module")\n    \ndef jpg_read():\n    print("- jpg_read() in img_read module")    \n')


# #### 패키지 사용

# [3장: 113페이지]

# In[ ]:


cd C:\myPyScraping\code\ch03


# In[ ]:


# image 패키지 내에 io_file 폴더에 있는 img_read 모듈 임포트
import image.io_file.img_read  

# '패키지명.하위폴더명.모듈명.함수()' 형식으로 함수 호출
image.io_file.img_read.png_read() 
image.io_file.img_read.jpg_read()

# '패키지명.하위폴더명.모듈명.변수' 형식으로 변수를 사용
print(image.io_file.img_read.default_image)


# [3장: 114페이지]

# In[ ]:


from image.io_file import img_read

# 모듈명.함수() 형식으로 함수를 호출
img_read.png_read() 
img_read.jpg_read()

# 모듈명.변수 형식으로 변수를 사용
print(img_read.default_image)


# In[ ]:


from image.io_file.img_read import png_read, jpg_read, default_image

# 모듈의 함수를 바로 호출
png_read() 
jpg_read()

# 모듈의 변수를 바로 사용
print(default_image)


# [3장: 115페이지]

# In[ ]:


# 'import 패키지명[.하위폴더명].모듈명 as 별명'
import image.io_file.img_read as i_read

# 모듈 별명으로 함수를 호출
i_read.png_read() 


# In[ ]:


# 'from 패키지명[.하위폴더명] import 모듈명 as 별명'
from image.io_file import img_read as img_r

# 모듈 별명으로 함수를 호출
img_r.jpg_read() 


# [3장: 116페이지]

# In[ ]:


# 'from 패키지명[.하위폴더명].모듈명 import 변수명/함수명/클래스명 as 별명'
from image.io_file.img_read import png_read as p_read
from image.io_file.img_read import jpg_read as j_read
from image.io_file.img_read import default_image as d_image

# 별명으로 모듈의 함수를 바로 호출
p_read() 
j_read()

# 별명으로 모듈의 변수를 바로 사용
print(d_image)


# ### 3.3.4 스케줄러 패키지

# #### 설치 및 기본 활용

# [3장: 119페이지]

# In[ ]:


import schedule
import time
from datetime import datetime

def job():
    now = datetime.now()
    print("[작업 수행 시각] {:%H:%M:%S}".format(now))

schedule.every(2).seconds.do(job)  # 2초(second)마다 job() 함수 실행

while True:
    schedule.run_pending()
    time.sleep(1)


# [3장: 120페이지]

# In[ ]:


schedule.clear() # 기본 스케줄러 객체를 제거


# In[ ]:


import schedule
import time
from datetime import datetime

def job():
    now = datetime.now()
    print("[작업 수행 시각] {:%H:%M:%S}".format(now))

schedule.every(2).seconds.do(job)  # 2초(second)마다 job() 함수 실행

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거          
        break            # while 문을 빠져나옴


# [3장: 121페이지]

# In[ ]:


def job():
    now = datetime.now()
    print("[작업 수행 시각] {:%H:%M:%S}".format(now))

# --------- 스케줄 추가 -----------
schedule.every().minute.at(":15").do(job) # 매분 15초에 job() 함수 실행
schedule.every(2).minutes.do(job)         # 2분마다 job() 함수 실행

now = datetime.now()
print("[**작업 시작 시각**] {:%H:%M:%S}".format(now))

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거
        break            # while 문을 빠져나옴


# [3장: 123페이지]

# In[ ]:


import schedule
import time
from datetime import datetime

# 작업을 위한 함수 지정
def send_message(district): # 매개 변수(district)가 있는 함수를 지정
    now = datetime.now()
    if(district == '서울'):
        weather = "맑음"
        print("**{}의 날씨: {} [현재 시각] {:%H:%M:%S}".format(district, weather, now))
    elif(district == '부산'):
        weather = "흐림"
        print("  >>{}의 날씨: {} [현재 시각] {:%H:%M:%S}".format(district, weather, now))
    else:
        print("--> {}의 날씨: 없음. [현재 시각] {:%H:%M:%S}".format(district, now))

# --------- 스케줄 추가 -----------        
# 함수의 매개 변수(district)에 값을 지정
schedule.every(2).seconds.do(send_message, district='서울') 
schedule.every(4).seconds.do(send_message, district='부산')

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거
        break            # while 문을 빠져나옴


# [3장: 123페이지]

# In[ ]:


def job():
    now = datetime.now()
    print("[작업 수행 시각] {:%H:%M:%S}".format(now))

# 스케줄 지정    
schedule.every().minute.at(":17").do(job) # 매분 17초에 job() 함수 실행

now = datetime.now()
print("[**작업 시작 시각**] {:%H:%M:%S}".format(now))

schedule.run_all() # 스케줄러의 모든 작업을 바로 수행

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거          
        break            # while 문을 빠져나옴


# #### 다중 작업과 다중 스케줄러 만들기

# [3장: 124페이지]

# In[ ]:


import schedule
import time

# 다중 작업을 위한 함수 지정
def job1():
    now = datetime.now()
    print("[** 작업1] {:%H:%M:%S}".format(now))
    
def job2():
    now = datetime.now()
    print("   [>> 작업2] {:%H:%M:%S}".format(now))

# --------- 스케줄 추가 -----------
schedule.every(1).seconds.do(job1) # 매초마다 job1() 함수 실행
schedule.every(3).seconds.do(job2) # 3초마다 job2() 함수 실행

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거          
        break            # while 문을 빠져나옴


# [3장: 125페이지]

# In[ ]:


import time
import schedule

# 다중 작업을 위한 함수 지정
def job1():
    now = datetime.now()
    print("[** 작업1] {:%H:%M:%S}".format(now))

def job2():
    now = datetime.now()
    print("   [>> 작업2] {:%H:%M:%S}".format(now))  

def job3():
    now = datetime.now()
    print("      [$$ 작업3] {:%H:%M:%S}".format(now))
        
# 스케줄러 생성
scheduler1 = schedule.Scheduler() # 스케줄러 객체(scheduler1) 생성
scheduler2 = schedule.Scheduler() # 스케줄러 객체(scheduler2) 생성

# --------- 스케줄 추가 -----------
scheduler1.every().second.do(job1)   # 매초마다 job1() 함수 실행
scheduler1.every().second.do(job2)   # 매초마다 job2() 함수 실행
scheduler2.every(3).seconds.do(job3) # 3초마다 job3() 함수 실행

while True:
    try:
        # 각 스케줄러 객체마다 run_pending()를 실행
        scheduler1.run_pending() # scheduler1 객체에 대해 run_pending() 실행
        scheduler2.run_pending() # scheduler2 객체에 대해 run_pending() 실행
        time.sleep(1)
    except:
        print("작업 강제 종료")
        scheduler1.clear()  # 스케줄러 객체(scheduler1)를 제거  
        scheduler2.clear()  # 스케줄러 객체(scheduler2)를 제거
        break              # while 문을 빠져나옴    


# ## 3.4 정리
