#!/usr/bin/env python
# coding: utf-8

# # 7장 셀레니움을 이용한 웹 스크레이핑

# ## 7.1 셀레니움 소개 및 설치

# ## 7.2 셀레니움으로 웹 브라우저 제어

# ### 7.2.1 웹 사이트 접속


# [7장: 319페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import pandas as pd
driver = Chrome() # 크롬 드라이버 객체 생성

url = "https://coinmarketcap.com/ko/" # URL 지정
driver.get(url)  # 웹 브라우저를 실행해 지정한 URL에 접속

# 웹 사이트 문서 높이 가져오기
scroll_height = driver.execute_script("return document.body.scrollHeight")

y = 0          # Y축 좌표의 초깃값
y_step = 1000  # Y축 아래로 이동하는 단계
while (True):
    y = y + y_step
    script =  "window.scrollTo(0,{0})".format(y)
    driver.execute_script(script) # 스크립트 실행
    driver.implicitly_wait(5)     # 스크롤 수행 후 데이터를 받아올 때까지 기다림
    
    # 수식 스크롤 위치가 문서 끝보다 크거나 같으면 while 문 빠져나가기
    if (y >= scroll_height):
        break
    
html = driver.page_source # HTML 코드를 가져옴
dfs = pd.read_html(html)  # HTML 소스에서 table의 내용을 DataFrame 리스트로 변환

df = dfs[0]         # 리스트의 첫 번째 요소를 선택
df.iloc[95:100,1:6] # DataFrame 데이터에서 행과 열을 선택해 출력


# [7장: 320페이지]

# In[ ]:


df.iloc[0:5,1:6]


# In[ ]:


df['이름'] = [name.replace(str(num), " ") for num, name in zip(df['#'], df['이름'])]
df['이름'] = [name.replace("구매하기", "") for name in df['이름']]
df.iloc[0:5,1:6]
## 


# [7장: 321페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

def get_coin_info(page_num):
    driver = Chrome() # 크롬 드라이버 객체 생성
    
    # page 추가해 URL 지정
    url = f"https://coinmarketcap.com/ko/?page={page_num}"
    driver.get(url)  # 웹 브라우저를 실행해 지정한 URL에 접속

    # 웹 사이트 문서 높이 가져오기
    scroll_height = driver.execute_script("return document.body.scrollHeight")

    y = 0           # Y축 좌표의 초깃값
    y_step = 1000   # Y축 아래로 이동하는 단계
    while (True):
        y = y + y_step
        script =  "window.scrollTo(0,{0})".format(y)
        driver.execute_script(script) # 스크립트 실행
        driver.implicitly_wait(5) # 스크롤 수행 후 데이터를 받아올 때까지 기다림

        # 수식 스크롤 위치가 문서 끝보다 크거나 같으면 while 문 빠져나가기
        if (y >= scroll_height):
            break

    html = driver.page_source # HTML 코드를 가져옴
    dfs = pd.read_html(html)  # HTML 소스에서 table의 내용을 DataFrame 리스트로 변환

    df = dfs[0] # 리스트의 첫 번째 요소를 선택
    
    # '이름' 열의 내용 변경
    df['이름'] = [name.replace(str(num), " ") for num, name in zip(df['#'], df['이름'])]
    df['이름'] = [name.replace("구매하기", "") for name in df['이름']]
    
    driver.quit() # 웹 브라우저를 종료함

    return df.iloc[:,1:9]


# [7장: 322페이지]

# In[ ]:
import display

page_num = 1 # page 지정
df_coin = get_coin_info(page_num) # 함수 호출

# DataFrame 데이터에서 행과 열을 선택해 출력
with pd.option_context('display.max_rows',6):
    pd.set_option("show_dimensions", False) # DataFrame의 행과 열 개수 출력 안 하기
    display(df_coin.iloc[:,0:6])

print(df_coin.head(6).iloc[:,0:6])


# ### 7.3.3 유튜브 검색 결과 가져오기

# [7장: 324페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time

driver = Chrome() # 크롬 드라이버 객체 생성

base_url = "https://www.youtube.com" # 유튜브의 기본 URL
search_word = '/results?search_query=' + '방탄소년단' # 검색어23QWWWWW
url = base_url +  search_word        # 접속하고자 하는 웹 사이트

driver.get(url) # 웹 브라우저를 실행해 지정한 URL에 접속
time.sleep(3)   # 웹 브라우저를 실행하고 URL에 접속할 때까지 기다림

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력


# In[ ]:


driver = Chrome()

base_url = "https://www.youtube.com"
search_word = '/results?search_query=' + '방탄소년단'
search_option = "&sp=CAMSAhAB" # 조회수로 정렬

url = base_url +  search_word + search_option # 접속하고자 하는 웹 사이트
driver.get(url)
time.sleep(3) # 웹 브라우저를 실행하고 URL에 접속할 때까지 기다림


# [7장: 326페이지]

# In[ ]:


html = driver.page_source # 접속 후에 해당 page의 HTML 코드를 가져옴
# driver.quit() # 웹 브라우저를 종료함

soup = BeautifulSoup(html, 'lxml')

title_hrefs = soup.select('a#video-title')

title_hrefs[0] # 첫 번째 항목 출력


# In[ ]:


title_hrefs[0].get('title') # title_hrefs[0]['title'] 도 동일


# In[ ]:


title_hrefs[0]['href'] # title_hrefs[0].get('href')도 동일


# [7장: 327페이지]

# In[ ]:


base_url = "https://www.youtube.com"
titles = []
urls = []
for title_href in title_hrefs[0:5]:
    title = title_href['title']         # 태그 안에서 title 속성의 값을 가져오기
    url = base_url + title_href['href'] # href 속성의 값 가져와 기본 url과 합치기
    titles.append(title)
    urls.append(url)
    print("{0}, {1}".format(title, url))


# [7장: 328페이지]

# In[ ]:


view_uploads = soup.select('span.style-scope.ytd-video-meta-block')

view_uploads[0:6]


# [7장: 329페이지]

# In[ ]:


view_numbers = view_uploads[0::2] # 인덱스가 짝수인 요소 선택
upload_times = view_uploads[1::2] # 인덱스가 홀수인 요소 선택

[view_numbers[0:3], upload_times[0:3]]


# In[ ]:


[view_numbers[0].get_text(), upload_times[0].get_text()]


# In[ ]:


[view_numbers[0].get_text().split(" ")[-1], upload_times[0].get_text()]


# [7장: 330페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
import pandas as pd
import time

def get_data_from_youtube(word, scroll=False):
    driver = Chrome()

    base_url = "https://www.youtube.com"
    search_word = '/results?search_query=' + word
    search_option = "&sp=CAMSAhAB" # 조회수로 정렬

    url = base_url +  search_word + search_option # 접속하고자 하는 웹 사이트
    driver.get(url) # URL에 접속
    time.sleep(3) # 웹 브라우저를 실행하고 URL에 접속할 때까지 기다림  
    
    if(scroll==True):
        # 수직(Y축 방향)으로 스크롤 동작하기 
        y = 0 # Y축 방향으로 스크롤 이동할 거리 초기화
        y_step = 1000
        for k in range(1, 5): # 반복 횟수 지정
            y = y + y_step  # 반복할 때마다 Y축 방향으로 더해지는 거리를 지정
            script = "window.scrollTo({0},{1})".format(0, y)
            driver.execute_script(script) # Y축 방향으로 스크롤
            time.sleep(3) # 결과를 받아올 때까지 잠시 기다림

    html = driver.page_source # 접속 후에 해당 page의 HTML 코드를 가져옴
    # driver.quit() # 웹 브라우저를 종료함
    
    soup = BeautifulSoup(html, 'lxml')
    
    # 동영상 제목과 URL 추출하기
    title_hrefs = soup.select('a#video-title')
    
    titles = []
    urls = []    
    for title_href in title_hrefs:
        title = title_href['title']         # 태그 안에서 title 속성의 값을 가져오기
        url = base_url + title_href['href'] # href 속성의 값 가져와 기본 url과 합치기        
        titles.append(title)
        urls.append(url)

    # 조회수와 업로드 시기 추출하기
    view_uploads = soup.select('span.style-scope.ytd-video-meta-block')
    
    view_numbers = view_uploads[0::2] # 인덱스가 짝수인 요소 선택
    upload_times = view_uploads[1::2] # 인덱스가 홀수인 요소 선택

    views = []
    uploads = [] 
    for view_number, upload_time in zip(view_numbers, upload_times):
        view = view_number.get_text().split(" ")[-1] # 조회수 추출
        upload = upload_time.get_text()              # 업로드 시기 추출
        views.append(view)
        uploads.append(upload)
        
    # 추출된 정보를 모으기
    search_results = []
    for title, url, view, upload in zip(titles, urls, views, uploads):
        search_result = [title, url, view, upload]
        search_results.append(search_result)
    
    # 추출 결과를 판다스 DataFrame 데이터 형식으로 변환
    df = pd.DataFrame(search_results, columns=["제목", "링크", "조회수", "업로드"])
    
    return df


# [7장: 331페이지]

# In[ ]:


df = get_data_from_youtube('방탄소년단') # get_data_from_youtube('방탄소년단', False) 도 가능
df.tail()
# df # 전체를 다 출력하려면 df.tail() 대신 df를 이용


# [7장: 333페이지]

# In[ ]:


df = get_data_from_youtube('방탄소년단', True)
df.tail() # 전체 중 끝 부분만 확인
# df # 전체를 다 출력하려면 df.tail() 대신 df를 이용


# ## 7.4 정리
