#!/usr/bin/env python
# coding: utf-8

# # 4장 파일 읽고 쓰기와 문자열 처리

# ## 4.1 파일 읽고 쓰기

# ### 4.1.1 파일 읽고 쓰기 위한 기본 구조

# ### 4.1.2 파일 읽기

# [4장: 130페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\data\\ch04\\read_test.txt', 'All grown-up\nwere once children,\nalthough few of them\nremember it.\n')


# [4장: 131페이지]

# In[ ]:


f = open('C:/myPyScraping/data/ch04/read_test.txt', 'r') # 파일 열기(읽기 모드)
data = f.read() # 파일의 내용 전체를 읽어서 변수에 할당
f.close()       # 파일 닫기

print(data)     # 읽어온 파일 내용 출력


# In[ ]:


# cp949로 인코딩된 한글 텍스트 파일 읽기 
file_name='C:/myPyScraping/data/ch04/헌법_cp949.txt' # 파일 경로를 변수에 할당

f = open(file_name, 'r', encoding='cp949') # 파일 열기(읽기 모드)
# f = open(file_name)
data = f.read() # 파일의 내용 전체를 읽어서 변수에 할당
f.close()       # 파일 닫기

print(data)     # 읽어온 파일 내용 출력


# [4장: 132페이지]

# In[ ]:


# utf-8로 인코딩된 한글 텍스트 파일 읽기 
file_name = 'C:/myPyScraping/data/ch04/헌법_utf8.txt' # 파일 경로를 변수에 할당

f = open(file_name, 'r', encoding='utf-8') # 파일 열기(읽기 모드)
data = f.read() # 파일의 내용 전체를 읽어서 변수에 할당
f.close()       # 파일 닫기

print(data)     # 읽어온 파일 내용 출력


# ### 4.1.3 파일을 한 줄씩 읽어 처리하기

# #### 한 줄씩 읽어오기: `readline()`

# [4장: 133페이지]

# In[ ]:


file_name = 'C:/myPyScraping/data/ch04/read_test.txt' # 파일 경로를 변수에 할당

f = open(file_name, 'r') # 파일 열기(읽기 모드)

line1 = f.readline() # 파일의 내용을 한 줄씩 읽어서 변수에 할당
line2 = f.readline() # 파일의 내용을 한 줄씩 읽어서 변수에 할당
f.close()  # 파일 닫기

print(line1, end='') # print 자체의 개행문자는 출력하지 않고 내용 출력
print(line2, end='')


# In[ ]:


file_name = 'C:/myPyScraping/data/ch04/read_test.txt' # 파일 경로를 변수에 할당

f = open(file_name, 'r')  # 파일 열기(읽기 모드)
line_num = 0 # 줄 수 표시를 위한 변수 초기화

while True:              
    line = f.readline()      # 파일의 내용을 한 줄씩 읽어서 변수에 할당
    if (line == ''):         # line이 빈 문자열인지 검사 
        break                # 빈 문자열이면 while문을 빠져나감
    line_num = line_num + 1  # line_num 을 1씩 증가 
    print("{0}: {1}".format(line_num, line), end='') # 줄 수와 읽은 문자열 출력
    
f.close() # 파일 닫기


# #### 한 줄씩을 요소로 갖는 리스트로 읽어오기:  `readlines()`

# [4장: 134페이지]

# In[ ]:


file_name = 'C:/myPyScraping/data/ch04/read_test.txt' # 파일 경로를 변수에 할당

f = open(file_name, 'r') # 파일 열기(읽기 모드)
lines = f.readlines()    # 파일 전체의 내용을 읽어서 변수에 할당
f.close()                # 파일 닫기

print(lines)


# In[ ]:


file_name = 'C:/myPyScraping/data/ch04/read_test.txt' # 파일 경로를 변수에 할당

f = open(file_name, 'r') # 파일 열기(읽기 모드)
lines = f.readlines()    # 파일 전체의 내용을 읽어서 변수에 할당
f.close() # 파일 닫기

line_num = 0 # 줄 수 표시를 위한 변수 초기화
for line in lines:
    line_num = line_num + 1  # line_num 을 1씩 증가 
    print("{0}: {1}".format(line_num, line), end='') # 줄 수와 읽은 문자열 출력


# ### 4.1.4 파일 쓰기

# [4장: 135페이지]

# In[ ]:


file_name = 'C:/myPyScraping/data/ch04/write_test.txt' # 파일 경로를 변수에 할당

f = open(file_name, 'w') # 파일 열기(쓰기 모드)
f.write("Python is powerful... and fast;\n") # 문자열을 파일에 쓰기
f.write("plays well with others;\n")
f.write("runs everywhere;\n")
f.write("is friendly & easy to learn;\n")
f.write("is Open.\n")
f.close() # 파일 닫기

print("생성한 파일:", file_name) # 생성한 파일 이름 출력


# [4장: 136페이지]

# In[ ]:


get_ipython().system('type C:\\myPyScraping\\data\\ch04\\write_test.txt')


# In[ ]:


file_name = 'C:/myPyScraping/data/ch04/two_times.txt' # 파일 경로를 변수에 할당

f = open(file_name, 'w') # 파일 열기(쓰기 모드)
f.write("[구구단 2단의 일부]\n")
for num in range(1, 6): # for문: num이 1~5까지 반복
    format_string = "2 x {0} = {1}\n".format(num, 2 * num) # 저장할 문자열 생성
    f.write(format_string) # 파일에 문자열 쓰기
f.close() # 파일 닫기

print("생성한 파일:", file_name) # 생성한 파일 이름 출력


# In[ ]:


get_ipython().system('type C:\\myPyScraping\\data\\ch04\\two_times.txt')


# ### 4.1.5 with 문으로 파일 읽고 쓰기 

# [4장: 137페이지]

# In[ ]:


file_name = 'C:/myPyScraping/data/ch04/three_times.txt' # 파일 경로를 변수에 할당

with open(file_name, 'w') as f:       # 파일 열기(쓰기 모드)
    f.write("[구구단 3단의 일부]\n")   
    for num in range(1, 6):            # for문: num이 1~5까지 반복
        format_string = "3 x {0} = {1}\n".format(num, 3 * num) # 저장할 문자열 생성
        f.write(format_string)        # 파일에 문자열 쓰기


# In[ ]:


with open(file_name, 'r') as f:  # 파일 열기(읽기 모드)
    data = f.read()               # 파일에서 문자열 읽기
    print(data)


# ## 4.2 문자열 처리

# ### 4.2.1 문자열 분리하기: `split()`

# [4장: 138페이지]

# In[ ]:


"에스프레소,아메리카노,카페라테,카푸치노".split(',')


# In[ ]:


"  에스프레소 아메리카노   카페라테      카푸치노\n".split()


# ### 4.2.2 불필요한 문자열 삭제하기: `strip()`

# [4장: 139페이지]

# In[ ]:


"aaaaPythonaaa".strip('a')


# In[ ]:


"\n  Python  \n\n".strip()


# ### 4.2.3 문자열 연결하기: `join()`

# [4장: 140페이지]

# In[ ]:


" ".join(["서울시","서초구","반포대로","201(반포동)"])


# In[ ]:


"****".join(["서울시","서초구","반포대로","201(반포동)"])


# In[ ]:


joined_str = "\n".join(["서울시","서초구","반포대로","201(반포동)"])
joined_str


# In[ ]:


print(joined_str)


# ### 4.2.4 문자열 찾기: `find()`, `count()`, `startswith()`, `endswith()`

# [4장: 141페이지]

# In[ ]:


str_p = "Python is powerful. Python is easy."

print(str_p.find("Python"))         # 전체 범위
print(str_p.find("Python", 10, 30)) # 시작과 끝 범위 지정
print(str_p.find("easy"))           # 전체 범위
print(str_p.find("Python", 21))     # 시작 범위 지정. 일치하는 문자열 없음
print(str_p.find("Jupyter"))        # 전체 범위. 일치하는 문자열 없음


# [4장: 142페이지]

# In[ ]:


print(str_p.count("Python"))         # 전체 범위
print(str_p.count("Python", 10, 30)) # 시작과 끝 범위 지정
print(str_p.count("easy"))           # 전체 범위
print(str_p.count("Python", 21))     # 시작 범위 지정. 일치하는 문자열 없음
print(str_p.count("Jupyter"))        # 전체 범위. 일치하는 문자열 없음


# [4장: 143페이지]

# In[ ]:


print("- 문자열이 'Python'으로 시작?", str_p.startswith("Python"))
print("- 문자열이 'powerful'로 시작?", str_p.startswith("powerful"))
print("- 지정 범위에서 'powerful'로 시작?", str_p.startswith("powerful",10))
print("- 문자열이 'easy.'으로 끝?", str_p.endswith("easy."))


# ### 4.2.5 문자열 바꾸기: `replace()`

# [4장: 143페이지]

# In[ ]:


str_o = "Python is powerful. Python is easy. Python is open."
print(str_o.replace("Python", "IPython"))    # 전체 범위
print(str_o.replace("Python", "IPython", 2)) # 횟수 지정


# ### 4.2.6 대소문자 변경하기: `lower()`, `upper()`

# [4장: 144페이지]

# In[ ]:


str_lu = "Python is powerful. PYTHON IS EASY."
print(str_lu.lower()) # 문자열을 모두 소문자로 바꾸기
print(str_lu.upper()) # 문자열을 모두 대문자로 바꾸기


# ## 4.3 정리
