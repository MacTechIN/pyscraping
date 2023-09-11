#!/usr/bin/env python
# coding: utf-8

# # 10장 카카오 API

# ## 10.1 카카오 API를 이용한 웹 문서와 이미지 검색

# ### 10.1.1 카카오디벨로퍼스 회원 가입 및 애플리케이션 등록

# ### 10.1.2 웹 문서 검색

# [10장: 500페이지]

# In[ ]:


import requests

url = "https://dapi.kakao.com/v2/search/web?sort=accuracy&page=1&size=3&query=python"

# 아래의 주석을 없애고 본인의 REST API 키를 입력
# REST_API_KEY = "n39i2db99b0d4c5e3132fb5d2fv981c4"   
req_headers = {"Authorization": "KakaoAK " + REST_API_KEY}

r = requests.get(url, headers=req_headers)

# print(r.status_code)
# print(r.url)
print(r.json())


# [10장: 501페이지]

# In[ ]:


import json

json_data = json.dumps(r.json(), indent=3, sort_keys=True, ensure_ascii=False)
print(json_data)


# [10장: 502페이지]

# In[ ]:


import requests
import json

web_url = "https://dapi.kakao.com/v2/search/web"
req_params = {"sort":"accuracy",
              "page":1,
              "size":3,
              "query":"python"
             }
# 아래의 주석을 없애고 본인의 REST API 키를 입력
# REST_API_KEY = "n39i2db99b0d4c5e3132fb5d2fv981c4"

req_headers = {"Authorization": "KakaoAK " + REST_API_KEY}

r = requests.get(web_url, params=req_params, headers=req_headers)

# 딕셔너리 형식의 데이터를 JSON 형식의 문자열로 변환(들여쓰기 적용)
json_data = json.dumps(r.json(), indent=3, sort_keys=True, ensure_ascii=False)

# 변환된 문자열을 출력
print(json_data)


# [10장: 503페이지]

# In[ ]:


import requests

# Daum 검색 API를 이용해 검색 결과를 가져오는 함수
def get_daum_web_search(page_num, size_num, query_str ):
    web_url = "https://dapi.kakao.com/v2/search/web"
    req_params = {"sort":"accuracy",
                  "page":page_num,
                  "size":size_num,
                  "query":query_str
                 }
    req_headers = {"Authorization": "KakaoAK " + REST_API_KEY}
    r = requests.get(web_url, params=req_params, headers=req_headers)
    return r


# [10장: 504페이지]

# In[ ]:


import json

r = get_daum_web_search(1, 3, "python") # 함수 호출
# 딕셔너리 형식의 데이터를 JSON 형식의 문자열로 변환(들여쓰기 적용)
json_data = json.dumps(r.json(), indent=3, sort_keys=True, ensure_ascii=False)
# 변환된 문자열을 출력
print(json_data)


# [10장: 505페이지]

# In[ ]:


is_end_result = r.json()['meta']['is_end']
is_end_result


# In[ ]:


documents_result = r.json()['documents']
documents_result


# [10장: 506페이지]

# In[ ]:


import requests
import json
import time
import pandas as pd

documents_results = [] # 가져온 documents의 내용을 통합하기 위한 변수

for page in range(1, 51):
    r = get_daum_web_search(page, 50, "python")
    is_end_result = r.json()['meta']['is_end']
    documents_result = r.json()['documents']
    documents_results.extend(documents_result)
    time.sleep(0.1)
    
    if(is_end_result==True): # 마지막 페이지인지 검사
        print(f"마지막 페이지는 {page} 페이지입니다.")
        break


# In[ ]:


len(documents_results)


# [10장: 507페이지]

# In[ ]:


# JSON 구조를 요소로 갖는 리스트를 DataFrame으로 변환
df_web_search = pd.json_normalize(documents_results)
df_web_search.head()


# [10장: 508페이지]

# In[ ]:


file_name = "C:/myPyScraping/data/ch10/web_search_results.json" # JSON 파일 이름 지정
result = df_web_search.to_json(file_name) # DataFrame 형식의 데이터를 JSON 파일로 쓰기

print("생성한 파일:", file_name)


# In[ ]:


df = pd.read_json(file_name) # JSON 파일을 DataFrame 형식의 데이터로 읽기
df.head()


# [10장: 509페이지]

# In[ ]:


from IPython.display import HTML

df_html = df_web_search.head().iloc[:,2:4] # 필요한 부분만 선택해 변수에 할당
# df_html = df_web_search # 전체를 선택해 변수에 할당

# DataFrame 데이터를 HTML 코드로 변환
html_table = df_html.to_html(escape=False, render_links=True) # 앞의 일부 변환
HTML(html_table) # HTML 코드의 내용을 웹 브라우저처럼 보여줌


# In[ ]:


import datetime

now = datetime.datetime.now() # 현재의 날짜 및 시각을 가져와 할당

# HTML 기본 구조를 갖는 HTML 코드
html_code = '''
<!DOCTYPE html>
<html>
  <head>
    <title>웹 문서 검색 결과</title>
  </head>
  <body>
    <h1> 웹 문서 검색 결과 (다음) </h1>
    <h3> * 데이터 추출 날짜: {0:%Y-%m-%d}</h3>
    {1}
  </body>
</html>    
'''.format(now, html_table)

# HTML(html_code) # HTML 코드의 내용을 웹 브라우저처럼 보여줌


# [10장: 510페이지]

# In[ ]:


# 생성할 HTML 파일 이름 지정
file_name = "C:/myPyScraping/data/ch10/daum_web_search_results.html" 

with open(file_name, 'w', encoding="utf-8") as f:
    f.write(html_code)
    
print("생성한 파일:", file_name)


# ### 10.1.3 이미지 검색

# [10장: 513페이지]

# In[ ]:


import requests

# Daum 검색 API를 이용해 검색 결과를 가져오는 함수
def get_daum_image_search(page_num, size_num, query_str ):
    image_url = "https://dapi.kakao.com/v2/search/image"
    req_params = {"sort":"accuracy",
                  "page":page_num,
                  "size":size_num,
                  "query":query_str
                 }
    req_headers = {"Authorization": "KakaoAK " +  REST_API_KEY}

    r = requests.get(image_url, params=req_params, headers=req_headers)
    
    return r


# [10장: 514페이지]

# In[ ]:


import json

r = get_daum_image_search(1, 3, "고양이") # 함수 호출

# 딕셔너리 형식의 데이터를 JSON 형식의 문자열로 변환(들여쓰기 적용)
json_data = json.dumps(r.json(), indent=3, sort_keys=True, ensure_ascii=False)

# 변환된 문자열을 출력
print(json_data)


# [10장: 515페이지]

# In[ ]:


documents_result = r.json()['documents']
documents_result


# [10장: 516페이지]

# In[ ]:


import pandas as pd 

# JSON 구조를 요소로 갖는 리스트를 DataFrame으로 변환
df_image_search = pd.json_normalize(documents_result)

# df_image_search # 전체 출력
df_image_search.iloc[:, 2:6] # 일부분 출력


# [10장: 517페이지]

# In[ ]:


from pathlib import Path

def find_image_file_extension(image_url):
    path = Path(image_url)           # path 객체 생성
    suffix = path.suffix             # 전체 경로에서 파일의 확장자 부분만 선택
    extension = suffix.split("?")[0] # 매개변수가 있으면 분리해 확장자만 선택
    extension = extension.lower()    # 확장자가 대문자이면 소문자로 변경
    
    # 확장자가 없거나 확장자 길이가 4보다 크면 jpg로 지정
    if(extension == '') or (len(extension) > 5): 
        extension = '.jpg'

    return extension


# [10장: 518페이지]

# In[ ]:


import pandas as pd 


# [인수]
#  - s_img_urls: Series 데이터 (값과 index가 있음)
#  - query_str: 검색어
#  - folder: 이미지 파일을 다운로드할 폴더

# [반환]
#  - file_names: 이미지 파일 이름 리스트
#  - extensions: 이미지 파일의 확장자 리스트

def download_image_file(s_img_urls, query_str, folder):
    file_names = []
    extensions = []
    for image_index, image_url in zip(s_img_urls.index, s_img_urls.values):
        # 이미지 파일 URL에서 이미지 가져와서 이미지 데이터 생성
        
        try:
            r = requests.get(image_url) # 응답 객체

            if(r.status_code==200):
                image_data = r.content  # 응답 객체에서 이미지 데이터 생성

                # 파일이름 생성
                # 1) 이미지 파일 확장자 추출
                extension = find_image_file_extension(image_url)
                # 2) 이미지 파일 번호 생성
                image_num = image_index
                # 3) 저장할 이미지 파일 이름 생성
                file_name = f"{folder}{query_str}_{image_num:04d}{extension}"

                file_names.append(file_name)
                extensions.append(extension)
                with open(file_name, 'wb') as f: # 이미지 데이터를 파일로 저장
                    f.write(image_data)
        except:
            print(f"인덱스 {image_index}를 위한 이미지 주소 연결에 실패했습니다.")
        
            
    return file_names, extensions


# [10장: 519페이지]

# In[ ]:


s_image_urls = df_image_search['image_url']
s_image_urls


# In[ ]:


from pathlib import Path

folder = "C:/myPyScraping/data/ch10/download/" # 다운로드할 폴더 지정
dir_path = Path(folder) # 디렉터리 경로를 입력해 dir_path 객체 생성

if dir_path.exists()==False:
    dir_path.mkdir()

query_str = "cat"

image_file_names, extensions = download_image_file(s_image_urls, query_str, folder)
image_file_names


# [10장: 520페이지]

# In[ ]:


import requests
import json
import time
import pandas as pd

documents_results = [] # 가져온 documents의 내용을 통합하기 위한 변수

for page in range(1, 3):     # page의 범위를 1~2로 지정
# for page in range(1, 51):   # 최대한 많은 이미지를 다운로드하기 위한 page 범위 지정
    r = get_daum_image_search(page, 80, "강아지")
    is_end_result = r.json()['meta']['is_end']
    documents_result = r.json()['documents']
    documents_results.extend(documents_result)
    time.sleep(0.5)
    
    if(is_end_result==True): # 마지막 페이지인지 검사
        print(f"마지막 페이지는 {page} 페이지입니다.")
        break
        
df_image_search2 = pd.json_normalize(documents_results) # 리스트의 JSON 요소를 DataFrame으로 변환
s_image_urls2 = df_image_search2['image_url']

print("다운로드할 이미지 파일 개수:", len(s_image_urls2))


# In[ ]:


df_image_search2.tail().iloc[:, 2:6] # 일부분 출력


# [10장: 521페이지]

# In[ ]:


print(df_image_search2[0:37]['image_url'][35])


# In[ ]:


from pathlib import Path

folder = "C:/myPyScraping/data/ch10/download2/" # 다운로드할 폴더 지정
dir_path = Path(folder) # 디렉터리 경로를 입력해 dir_path 객체 생성

if dir_path.exists()==False:
    dir_path.mkdir()
    
query_str = "cat"

image_file_names, extensions = download_image_file(s_image_urls2, query_str, folder)
image_file_names

print("[다운로드 완료]")


# [10장: 522페이지]

# In[ ]:


df_extension = pd.DataFrame(extensions, columns=['확장자'])
df_extension['확장자'].value_counts()


# In[ ]:


set(extensions)


# ## 10.2 카카오 API를 이용한 카카오톡 메시지 전송

# ### 10.2.1 카카오 로그인 관련 설정

# ### 10.2.2 액세스 토큰 생성

# [10장: 533페이지]

# In[ ]:


import requests

url = "https://kauth.kakao.com/oauth/token" # 카카오 메시지 API를 위한 토큰 생성 URL

# 아래의 주석을 없애고 본인의 REST API 키를 입력
# REST_API_KEY = "n39i2db99b0d4c5e3132fb5d2fv981c4" 

# 아래의 주석을 없애고 본인의 인가 코드를 입력
# CODE = "nNmD6KK6hVoXx ~~ b7kAAAGArmTQ8g"

req_data = {"grant_type" : "authorization_code",
            "client_id" : REST_API_KEY,
            "redirect_url" : "https://localhost:5000",
            "code" : CODE }

r = requests.post(url, data=req_data)
token_info = r.json()
token_info


# [10장: 534페이지]

# In[ ]:


token_info['access_token']


# In[ ]:


from selenium.webdriver import Chrome
import time 
from selenium.webdriver.common.by import By

driver = Chrome()                # 크롬 드라이버 객체 생성
time.sleep(1)

driver.set_window_size(700, 800) # 웹 브라우저의 창 크기 설정

Redirect_URI = "https://localhost:5000"

base_url = "https://kauth.kakao.com/oauth/authorize"
param1 = f"client_id={REST_API_KEY}"
param2 = f"redirect_uri={Redirect_URI}"
param3 = "response_type=code"
param4 = "scope=talk_message"

parameters = f"{param1}&{param2}&{param3}&{param4}"
url = base_url + "?" + parameters

driver.get(url) # 웹 브라우저를 실행해 지정한 URL에 접속


# [10장: 536페이지]

# In[ ]:


from selenium.webdriver import Chrome
import time 
from selenium.webdriver.common.by import By

def get_kakao_auth_code(rest_api_key, redirect_uri):
    driver = Chrome()                # 크롬 드라이버 객체 생성
    time.sleep(1)

    driver.set_window_size(800, 600) # 웹 브라우저의 창 크기 설정  

    base_url = "https://kauth.kakao.com/oauth/authorize"
    param1 = f"client_id={rest_api_key}"
    param2 = f"redirect_uri={redirect_uri}"
    param3 = "response_type=code"
    param4 = "scope=talk_message"
    
    parameters = f"{param1}&{param2}&{param3}&{param4}"
    url = base_url + "?" + parameters

    driver.get(url) # 웹 브라우저를 실행해 지정한 URL에 접속
    driver.implicitly_wait(5)
    
    # 로그인(ID 입력)
    user_email = "test@abc.com"                             # 자신의 email 주소 입력
    user_id = driver.find_element(By.NAME, "email")         # name 속성으로 아이디(ID) 입력창 찾기
    # user_id = driver.find_element(By.ID, "id_email_2")    # ID 속성으로 아이디(ID) 입력창 찾기
    user_id.send_keys(user_email)                           # email 주소 입력

    # 로그인(PW 입력)
    user_password = "test1234"                              # 자신의 암호 입력
    user_pw = driver.find_element(By.NAME, "password")      # name 속성으로 패스워드(비밀번호) 입력창 찾기
    # user_pw = driver.find_element(By.ID, "id_password_3") # id 속성으로 패스워드(비밀번호) 입력창 찾기
    user_pw.send_keys(user_password)                        # 암호 입력
    time.sleep(1)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[8]/button[1]')
    login_button.click()
    time.sleep(3) # 다른 URL로 넘어갈 때까지 명시적으로 기다림

    redirect_url =  driver.current_url # 인가 코드가 포함된 URL을 가져옴
    auth_code = redirect_url.split("code=")[-1] # 인가 코드만 추출
    
    return auth_code


# [10장: 537페이지]

# In[ ]:


import requests

def get_kakao_access_token(rest_api_key, redirect_uri, auth_code):

    url = "https://kauth.kakao.com/oauth/token" # 카카오 메시지 API를 위한 토큰 생성 URL

    req_data = {"grant_type" : "authorization_code",
                "client_id" : rest_api_key,
                "redirect_url" : redirect_uri,
                "code" : auth_code }

    r = requests.post(url, data=req_data)
    token_info = r.json()
    
    return token_info['access_token']


# [10장: 538페이지]

# In[ ]:


# 아래의 주석을 없애고 본인의 REST API 키를 입력
# REST_API_KEY = "n39i2db99b0d4c5e3132fb5d2fv981c4" 
Redirect_URI = "https://localhost:5000"

AUTH_CODE = get_kakao_auth_code(REST_API_KEY, Redirect_URI)
ACCESS_TOKEN = get_kakao_access_token(REST_API_KEY, Redirect_URI, AUTH_CODE)

print("카카오 인가 코드:", AUTH_CODE)
print("카카오 액세스 토큰:", ACCESS_TOKEN)


# ### 10.2.3 카카오톡 메시지 보내기

# [10장: 540페이지]

# In[ ]:


import requests
import json

def send_kakaotalk_message(access_token, text_message):
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send' # URL 생성
    headers = {"Authorization": "Bearer " + access_token}
    json_data = json.dumps({"object_type" : "text",
                          "text" : text_message,
                          "link" : {} })
    data = {"template_object": json_data} 
    r = requests.post(url, headers=headers, data=data) # POST 방법으로 요청해 응답받음

    if r.json()['result_code'] == 0:
        print('카카오톡 메시지 보내기 성공')
    else:
        print('카카오톡 메시지 보내기 실패')


# [10장: 541페이지]

# In[ ]:


sample_message = "파이썬을 이용한 카카오톡 메시지입니다."
send_kakaotalk_message(ACCESS_TOKEN, sample_message)


# In[ ]:


sample_message2 = "아래 링크를 클릭하면 해당 링크로 연결됩니다.\nwww.google.com"
send_kakaotalk_message(ACCESS_TOKEN, sample_message2)


# ## 10.3 웹 스크레이핑 결과를 카카오톡으로 보내기

# ### 10.3.1 날씨 정보 보내기

# [10장: 543페이지]

# In[ ]:


import requests  
from bs4 import BeautifulSoup 
import time

def get_weather_daum_for_kakaotalk(location):
    search_query = location + " 날씨"
    search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
    url = search_url + search_query
    html_weather = requests.get(url).text
    time.sleep(2)    
    soup_weather = BeautifulSoup(html_weather, "lxml")
    
    txt_temp = soup_weather.select_one('strong.txt_temp').get_text()
    txt_weather = soup_weather.select_one('span.txt_weather').get_text()

    dl_weather_dds = soup_weather.select('dl.dl_weather dd')
    [wind_speed, humidity, pm10] = [x.get_text() for x in dl_weather_dds]

    today_weather = "[오늘의 날씨 정보]\n"
    weather_info1 = f"- 설정 지역: {location}\n"
    weather_info2 = f"- 기온: {txt_temp}\n"
    weather_info3 = f"- 날씨 정보: {txt_weather}\n"
    weather_info4 = f"- 현재 풍속: {wind_speed}\n"
    weather_info5 = f"- 현재 습도: {humidity}\n"
    weather_info6 = f"- 미세 먼지: {pm10}"
    
    weather_message = today_weather + weather_info1 + weather_info2 + \
                      weather_info3 +  weather_info4 + weather_info5 + \
                      weather_info6

    return weather_message


# [10장: 544페이지]

# In[ ]:


location = "경기도 수원시" # 날씨를 알고 싶은 지역
weather_message = get_weather_daum_for_kakaotalk(location)
print(weather_message)


# In[ ]:


# 아래의 주석을 없애고 본인의 REST API 키를 입력
# REST_API_KEY = "n39i2db99b0d4c5e3132fb5d2fv981c4" 
Redirect_URI = "https://localhost:5000"

AUTH_CODE = get_kakao_auth_code(REST_API_KEY, Redirect_URI)
ACCESS_TOKEN = get_kakao_access_token(REST_API_KEY, Redirect_URI, AUTH_CODE)

print("카카오 인가 코드:", AUTH_CODE)
print("카카오 액세스 토큰:", ACCESS_TOKEN)


# [10장: 545페이지]

# In[ ]:


location = "경기도 수원시" # 날씨를 알고 싶은 지역 
weather_message = get_weather_daum_for_kakaotalk(location) # 날씨 정보 문자열 가져오기
send_kakaotalk_message(ACCESS_TOKEN, weather_message)      # 카카오톡 메시지 보내기


# ### 10.3.2 환율 정보 보내기

# [10장: 546페이지]

# In[ ]:


import pandas as pd

# 네이버 금융의 환율 정보 웹 사이트 주소
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'

# 웹 사이트의 표 데이터에서 두 번째 줄을 DataFrame 데이터의 columns로 선택
dfs = pd.read_html(url, header=1)

exchange_rate_df = dfs[0].head(4) # 전체 데이터 중 앞의 일부분만 표시
exchange_rate_df


# In[ ]:


exchange_rate_list = exchange_rate_df[['통화명','매매기준율']].values.tolist()
exchange_rate_list


# In[ ]:


exchange_rate_message = "★ 주요 통화의 환율 정보 ★\n" # 전송할 문자열 변수

for exchange_rate in exchange_rate_list:
    string = f"▶ {exchange_rate[0]}: {exchange_rate[1]}원"
    exchange_rate_message = exchange_rate_message + "\n" + string # 하나의 문자열로 만들기
    
send_kakaotalk_message(ACCESS_TOKEN, exchange_rate_message) # 카카오톡 메시지 보내기


# ### 10.3.3 가상 화폐 정보 보내기

# [10장: 547페이지]

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
        driver.implicitly_wait(5)     # 스크롤 수행 후 데이터를 받아올 때까지 기다림 

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


# [10장: 548페이지]

# In[ ]:


page_num = 1                      # page 지정
df_coin = get_coin_info(page_num) # 함수 호출
df_coin.iloc[0:5,1:3] # 원하는 행(0~4)과 열(1~2)을 선택해 출력


# [10장: 549페이지]

# In[ ]:


df_coin_selected = df_coin.iloc[0:5,1:3] # 행(0~4)과 열(1~2)을 선택
coin_info_list = df_coin_selected.values.tolist() # DataFrame 데이터의 값을 리스트로 변환

coin_info_message = "★ 주요 가상 화폐 가격 정보 ★\n" # 전송할 문자열 변수

for coin_info in coin_info_list:
    string = f"▶ {coin_info[0]}: {coin_info[1]}"
    coin_info_message = coin_info_message + "\n" + string # 하나의 문자열로 만들기
    
print(coin_info_message) # 카카오톡 메시지 출력
print("------------------------------")
send_kakaotalk_message(ACCESS_TOKEN, coin_info_message) # 카카오톡 메시지 보내기   


# ### 10.3.4 주식 정보 보내기

# [10장: 550페이지]

# In[ ]:


import requests
from bs4 import BeautifulSoup

def get_current_stock_price(stock_code):
    
    base_url = 'https://finance.naver.com/item/main.nhn'
    url = base_url + "?code=" + stock_code
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    stock_price = soup.select_one('p.no_today span.blind').get_text()
    
    return stock_price


# In[ ]:


company_stock_codes = {"삼성전자": "005930", "현대차":"005380", "NAVER":"035420"}

stock_price_message = "★ 관심 종목 주가 정보 ★\n" # 전송할 문자열 변수

for company, stock_code in company_stock_codes.items():
    current_stock_price = get_current_stock_price(stock_code)
    string = (f"▶ {company}: {current_stock_price}원")
    stock_price_message = stock_price_message + "\n" + string # 하나의 문자열로 만들기
    
print(stock_price_message) # 카카오톡 메시지 출력
print("------------------------------")
send_kakaotalk_message(ACCESS_TOKEN, stock_price_message) # 카카오톡 메시지 보내기 


# ### 10.3.5 스케줄에 따라 카카오톡 메시지 보내기

# [10장: 552페이지]

# In[ ]:


import schedule
import time
from datetime import datetime

# 작업을 위한 함수 지정
count = 0    
def job():
    global count
    count = count + 1
    
    now = datetime.now()
    print("[메시지 보내기 작업 수행 시각] {:%H:%M:%S}".format(now))
    
    # 아래의 주석을 없애고 본인의 REST API 키를 입력
    # REST_API_KEY = "n39i2db99b0d4c5e3132fb5d2fv981c4"
    Redirect_URI = "https://localhost:5000"

    CODE = get_kakao_auth_code(REST_API_KEY, Redirect_URI)
    ACCESS_TOKEN = get_kakao_access_token(REST_API_KEY, Redirect_URI, CODE)

    location = "경기도 수원시" # 날씨를 알고 싶은 지역
    weather_message = get_weather_daum_for_kakaotalk(location) # 날씨 정보 문자열 가져오기
    weather_message = "◆(스케줄러 이용)◆\n" + weather_message
    send_kakaotalk_message(ACCESS_TOKEN, weather_message)      # 카카오톡 메시지 보내기
    
# 코드 테스트를 위해 매분마다 날씨 정보 가져와 메시지 보내기 위한 스케줄 설정
schedule.every(1).minutes.at(":00").do(job)  # 매분 0초마다 job() 함수 실행

# -- 매일 지정한 시각에 날씨 정보 가져와 출력하기 위한 스케줄 설정
# schedule.every().day.at("07:00").do(job) # 매일 07시에 job() 함수 실행
# schedule.every().day.at("12:00").do(job) # 매일 12시에 job() 함수 실행
# schedule.every().day.at("18:00").do(job) # 매일 18시에 job() 함수 실행

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
        if(count == 3): # count가 정해진 횟수까지 도달하면 while 문 빠져나옴
            schedule.clear()
            print("스케줄러 종료. 총 전송 횟수:", count)
            break
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거  
        break            # while 문을 빠져나옴


# ## 10.4 정리
