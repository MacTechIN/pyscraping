#!/usr/bin/env python
# coding: utf-8

# # 8장 웹 API

# ## 8.1 웹 API의 이해

# ### 8.1.1 웹 API의 데이터 획득 과정

# ### 8.1.2 웹 API의 인증 방식

# ### 8.1.3 응답 데이터의 형식 및 처리

# #### JSON 데이터 형식

# #### JSON 데이터 변환 및 데이터 추출

# [8장: 341페이지]

# In[ ]:


import json

python_dict = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}
type(python_dict)


# In[ ]:


json_data = json.dumps(python_dict)
type(json_data)


# [8장: 342페이지]

# In[ ]:


print(json_data)


# In[ ]:


json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
print(json_data)


# In[ ]:


dict_data = json.loads(json_data) # JSON 데이터를 파이썬의 딕셔너리 타입으로 변환
type(dict_data)


# [8장: 343페이지]

# In[ ]:


dict_data['신체정보']['몸무게']


# In[ ]:


dict_data['취미']


# In[ ]:


dict_data['취미'][0]


# ## 8.2 API 키 없이 시간 관련 데이터 가져오기 

# ### 8.2.1 시간대 리스트와 현재 시각 데이터 가져오기

# [8장: 345페이지]

# In[ ]:


import requests  
import json

url = "https://timeapi.io/api/TimeZone/AvailableTimeZones"

r = requests.get(url)
r.text[:70] # 문자열 중 앞의 일부만 출력
# r.text    # 문자열 전체를 출력


# [8장: 346페이지]

# In[ ]:


import requests  
import json

url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"

r = requests.get(url)
print(r.text) 


# In[ ]:


url = "https://timeapi.io/api/Time/current/zone" # 요청 주소
parameters = {"timeZone": "Asia/Seoul"}          # 요청 매개 변수 생성

r = requests.get(url, params=parameters)
print(r.text) 


# In[ ]:


json_to_dict = json.loads(r.text)
type(json_to_dict)


# [8장: 347페이지]

# In[ ]:


json_to_dict = r.json() #JSON 형태의 데이터를 파이썬의 딕셔너리 타입으로 변환
type(json_to_dict)


# In[ ]:


import requests
import json

url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"

date_time_dict = requests.get(url).json()
type(date_time_dict)


# In[ ]:


date_time_dict


# [8장: 348페이지]

# In[ ]:


date_time_dict["dateTime"], date_time_dict["timeZone"], date_time_dict["dayOfWeek"]


# ### 8.2.2 시간대 변환 데이터 가져오기

# [8장: 349페이지]

# In[ ]:


import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2022-10-03 10:03:00"
to_time_zone = "UTC" # GMT로 지정해도 결과는 동일

headers = {"Content-Type": "application/json"}

json_data = json.dumps({"fromTimeZone": from_time_zone,
                        "dateTime": from_date_time,
                        "toTimeZone": to_time_zone})

r = requests.post(url, headers=headers, data=json_data) # POST 방법으로 요청해 응답받음
ctz_json_to_dict = r.json()
ctz_json_to_dict


# [8장: 350페이지]

# In[ ]:


import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2022-10-03 10:03:00"
to_time_zone = "GMT" # UTC로 지정해도 결과는 동일

dict_data = {"fromTimeZone": from_time_zone,
              "dateTime": from_date_time,
              "toTimeZone": to_time_zone}

r = requests.post(url, json=dict_data) # POST 방법으로 요청해 응답받음
ctz_json_to_dict = r.json()
ctz_json_to_dict


# [8장: 351페이지]

# In[ ]:


dateTime = ctz_json_to_dict['conversionResult']['dateTime'] # 변환된 날짜와 시각 데이터를 추출
to_date_time = f"{dateTime.split('T')[0]} {dateTime.split('T')[1]}"
from_date_time, to_date_time


# ## 8.3 RSS 피드 데이터 가져오기

# ### 8.3.1 RSS 문서의 구조 및 데이터 추출

# [8장: 353페이지]

# In[ ]:


rss_simple_document = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>파이썬 웹 스크레이핑 홈페이지</title>
  <link>https://www.python_web_scraping.com</link>
  <description>파이썬 웹 스크레이핑 설명</description>
  <pubDate>Sat, 30 Apr 2022 15:39:19 GMT</pubDate>
  <lastBuildDate>Sat, 30 Apr 2022 17:50:21 GMT</lastBuildDate>
  <item>
    <title>1장. 웹 스크레이핑</title>
    <link>https://www.python_web_scraping.com/web_scraping.html</link>
    <description>웹 스크레이핑 기본에 관한 교육</description>
    <pubDate>Sat, 30 Apr 2022 00:30:00 GMT</pubDate>
  </item>
  <item>
    <title>2장. 웹 API 교육</title>
    <link>https://www.python_web_scraping.com/web_api.html</link>
    <description>웹 API에 관한 교육</description>
    <pubDate>Sat, 30 Apr 2022 09:45:12 GMT</pubDate>
  </item>
</channel>

</rss>"""


# [8장: 355페이지]

# In[ ]:


import feedparser

d = feedparser.parse(rss_simple_document) # RSS 형식의 데이터를 파싱

d.feed.title, d.feed.link, d.feed.description, d.feed.published, d.feed.updated


# In[ ]:


d["feed"]["title"], d["feed"]["link"], d["feed"]["description"], d["feed"]["published"], d["feed"]["updated"]


# [8장: 356페이지]

# In[ ]:


d.entries[0].title, d.entries[0].link, d.entries[0].description, d.entries[0].published


# In[ ]:


d.entries[1].title, d.entries[1].link, d.entries[1].description, d.entries[1].published


# ### 8.3.2 구글 뉴스의 검색 기사 가져오기

# [8장: 358페이지]

# In[ ]:


import feedparser

query = "머신러닝"
# RSS 서비스 주소
rss_url = f'https://news.google.com/rss/search?q={query}&&hl=ko&gl=KR&ceid=KR:ko'
rss_news = feedparser.parse(rss_url) # RSS 형식의 데이터를 파싱

title = rss_news['feed']['title']
updated = rss_news['feed']['updated']

print("['구글 뉴스' RSS 피드 제목]", title)
print("['구글 뉴스' RSS 피드 제공 일시]", updated)


# In[ ]:


from datetime import datetime, timedelta

# RSS 피드 제공 일시를 한국 날짜와 시간으로 변경 하는 함수
def get_local_datetime(rss_datetime):
    # 전체 값 중에서 날짜와 시간만 문자열로 추출
    date_time_str = ' '.join(rss_datetime.split()[1:5])
    
    # 문자열의 각 자리에 의미를 부여해 datetime 객체로 변경
    date_time_GMT = datetime.strptime(date_time_str, '%d %b %Y %H:%M:%S')
    
    # GMT에 9시간을 더해 한국 시간대로 변경
    date_time_KST = date_time_GMT + timedelta(hours=9)
    
    return date_time_KST # 변경된 시간대의 날짜와 시각 반환


# [8장: 359페이지]

# In[ ]:


print("['구글 뉴스' RSS 피드 제공 일시]", get_local_datetime(updated))


# In[ ]:


import feedparser
import pandas as pd

df_gnews = pd.DataFrame(rss_news.entries) # 구글 뉴스 아이템을 판다스 DataFrame으로 변환

selected_columns = ['title', 'published', 'link'] # 관심있는 열만 선택
df_gnews2 = df_gnews[selected_columns].copy()     # 선택한 열만 다른 DataFrame으로 복사

# published 열의 작성 일시를 한국 시간대로 변경
df_gnews2['published'] = df_gnews2['published'].apply(get_local_datetime) 

df_gnews2.columns = ['제목', '제공 일시', '링크'] # 열 이름 변경
df_gnews2.head(3)                                 # 앞의 일부만 출력


# [8장: 360페이지]

# In[ ]:


from IPython.display import HTML

df = df_gnews2.head(3) # DataFrame 데이터의 일부 열과 행을 선택
# df = df_gnews2       # DataFrame 데이터 전체를 선택

html_table = df.to_html(escape=False, render_links=True) # DataFrame 데이터를 HTML 코드로 변환
HTML(html_table)  # HTML 코드의 내용을 웹 브라우저처럼 보여줌


# [8장: 361페이지]

# In[ ]:


from datetime import datetime, timedelta

google_news_datetime_KST = get_local_datetime(updated) # 한국 날짜와 시간으로 변경 

df = df_gnews2.head() # DataFrame 데이터 앞의 일부
# df = df_gnews2 # DataFrame 데이터 전체

# DataFrame 데이터를 HTML 코드로 변환 (justify='center' 옵션을 이용해 열 제목을 중간에 배치)
html_table = df.to_html(justify='center', escape=False, render_links=True) 

# HTML 기본 구조를 갖는 HTML 코드
html_code = '''
<!DOCTYPE html>
<html>
  <head>
    <title>구글 뉴스 검색</title>
  </head>
  <body>
    <h1>{0}</h1>
    <h3> *검색 날짜 및 시각: {1}</h3>
    {2}
  </body>
</html>    
'''.format(title, google_news_datetime_KST, html_table)

file_name = "C:/myPyScraping/data/ch08/google_news.html" # 생성할 HTML 파일 이름 지정
with open(file_name, 'w', encoding="utf-8") as f:
    f.write(html_code)
    
print("생성한 파일:", file_name)


# ## 8.4 스포티파이를 이용한 노래 데이터 가져오기

# ### 8.4.1 앱 만들고 액세스 토큰 생성

# #### 개발자 웹 사이트에서 앱 만들기

# #### 액세스 토큰 생성

# [8장: 368페이지]

# In[ ]:


import requests

## 자신의 Client ID와 Client Secret 입력
# CLIENT_ID = '5df50a2c54ab3b1987b03bd42af2ac09'
# CLIENT_SECRET = '81ca98ebh0b74231b9c2c06269e9647d'

url = 'https://accounts.spotify.com/api/token'

auth_data = {'grant_type': 'client_credentials',
              'client_id': CLIENT_ID,
              'client_secret': CLIENT_SECRET}

r = requests.post(url, data=auth_data) # POST 방법으로 응답을 요청
r_token = r.json() # 응답 객체의 JSON 형식의 데이터를 딕셔너리 타입으로 변환
r_token


# In[ ]:


def get_spotify_access_token(client_id, client_secret):
    
    url = 'https://accounts.spotify.com/api/token'

    auth_data = {'grant_type': 'client_credentials',
                  'client_id': client_id,
                  'client_secret': client_secret}
        
    r = requests.post(url, data=auth_data) # POST 방법으로 응답을 요청
    r_token = r.json() # 응답 객체의 text 부분을 JSON 형식으로 변환
    
    return r_token['access_token']


# [8장: 369페이지]

# In[ ]:


ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
ACCESS_TOKEN


# ### 8.4.2 아티스트 API로 아티스트 관련 정보 가져오기

# #### 아티스트 정보 가져오기

# [8장: 374페이지]

# In[ ]:


import requests

def get_spotify_artist_info(artist_id):
    url = "https://api.spotify.com/v1/artists/{id}".format(id=artist_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}

    r = requests.get(url, headers=headers)

    return r.json()


# [8장: 375페이지]

# In[ ]:


artist_id = "3HqSLMAZ3g3d5poNaI7GOU" # 아이유의 아티스트 ID
artist_data = get_spotify_artist_info(artist_id)

print("[아티스트 관련 정보]")
print("- 이름:", artist_data['name'])
print("- ID:", artist_data['id'])
print("- 장르:", artist_data['genres'])
print("- 인기도:", artist_data['popularity'])


# In[ ]:


artist_id = "3Nrfpe0tUJi4K4DXYWgMUX" # 방탄소년단(BTS)의 아티스트 ID
artist_data = get_spotify_artist_info(artist_id)

print("[아티스트 관련 정보]")
print("- 이름:", artist_data['name'])
print("- ID:", artist_data['id'])
print("- 장르:", artist_data['genres'])
print("- 인기도:", artist_data['popularity'])


# #### 아티스트의 인기곡 정보 가져오기

# [8장: 379페이지]

# In[ ]:


url = "https://api.spotify.com/v1/markets"

ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
headers = {"Authorization": "Bearer " + ACCESS_TOKEN}

r = requests.get(url, headers=headers)
r.text[:50] # 앞의 일부만 표시
# r.text     # 전체 표시


# In[ ]:


def get_spotify_artist_top_tracks(artist_id, country_code):

    url = "https://api.spotify.com/v1/artists/{id}/top-tracks".format(id=artist_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}
    parameters = {"market": country_code}
    r = requests.get(url, params=parameters, headers=headers)

    return r.json()


# [8장: 380페이지]

# In[ ]:


import pandas as pd

artist_id = "3HqSLMAZ3g3d5poNaI7GOU" # 아이유의 아티스트 ID
country_code = "KR" # 대한민국의 국가 코드

# 인기곡 정보 JSON 객체 받기
artist_top_tracks_data = get_spotify_artist_top_tracks(artist_id, country_code)
# 인기곡 정보 JSON 데이터에서 곡 정보 객체 리스트 추출
top_tracks = artist_top_tracks_data['tracks']

[type(top_tracks), len(top_tracks)] # top_tracks의 타입과 개수 출력


# In[ ]:


top_tracks[0].keys() # 리스트의 첫 번째 요소로 있는 딕셔너리에서 키만 추출


# In[ ]:


# 리스트를 DataFrame 데이터로 변환
df_artist_top_track = pd.DataFrame(top_tracks)
# DataFrame 데이터에서 열 선택
df_artist_top_track2 = df_artist_top_track[['artists', 'name', 'duration_ms', 'id', 'popularity']]

df_artist_top_track2.head()


# [8장: 381페이지]

# In[ ]:


def get_artists(artists_info):
    artists_name = []
    for artist_info in artists_info:
        name = artist_info['name'] # 아티스트 정보 중 이름만 추출
        artists_name.append(name)  # 아티스트 이름을 리스트로 묶음
    
    artists_name_str = ", ".join(artists_name) # 리스트로 된 아티스트 이름을 문자열로 변환 
    return artists_name_str


# In[ ]:


df_artist_top_track3 = df_artist_top_track2.copy() # DataFrame 데이터 복사

# get_artists() 함수를 artists 열의 각 항목에 적용
df_artist_top_track3['artists'] = df_artist_top_track3['artists'].apply(get_artists)
df_artist_top_track3.head()


# In[ ]:


def convert_msec(msec):
    milliseconds = (msec%1000)
    seconds = (msec/1000) % 60
    seconds = int(seconds)
    minutes = (msec/(1000*60)) % 60
    minutes = int(minutes)
    hours = (msec/(1000*60*60)) % 60
    hours = int(hours)
    
    hms_str = "{0:02d}:{1:02d}:{2:02d}.{3:03d}".format(hours, minutes, seconds, milliseconds)
    return hms_str


# [8장: 383페이지]

# In[ ]:


df_IU_top_track = df_artist_top_track3.copy() # DataFrame 데이터 복사

# convert_msec() 함수를 duration_ms 열의 각 항목에 적용
df_IU_top_track['duration_ms'] = df_IU_top_track['duration_ms'].apply(convert_msec) 

# duration_ms 열 이름을 duration로 변경
df_IU_top_track.rename(columns={'duration_ms':'duration'}, inplace=True)
df_IU_top_track.head()


# In[ ]:


df_IU_top_track.columns = ["아티스트", "곡 제목", "곡의 길이", "곡 ID", "인기도"] # 열 제목을 변경
df_IU_top_track.head()


# [8장: 384페이지]

# In[ ]:


import pandas as pd

def get_artist_top_track(artist_id, country_code):
    # 인기곡 정보 JSON 객체 받기
    artist_top_tracks_data = get_spotify_artist_top_tracks(artist_id, country_code)
    # 인기곡 정보 JSON 데이터에서 곡 정보 객체 리스트 추출
    top_tracks = artist_top_tracks_data['tracks']

    # 리스트를 DataFrame 데이터로 변환
    df_artist_top_track = pd.DataFrame(top_tracks)
    # DataFrame 데이터에서 열 선택
    df_artist_top_track2 = df_artist_top_track[['artists','name', 'duration_ms', 'id', 'popularity']]
    
    df_artist_top_track3 = df_artist_top_track2.copy() # DataFrame 데이터 복사
    # get_artists() 함수를 artists 열의 각 항목에 적용
    df_artist_top_track3['artists'] = df_artist_top_track3['artists'].apply(get_artists)

    df_artist_top_track4 = df_artist_top_track3.copy() # DataFrame 데이터 복사
    # convert_msec() 함수를 duration_ms 열의 각 항목에 적용
    df_artist_top_track4['duration_ms'] = df_artist_top_track4['duration_ms'].apply(convert_msec)
    
    # duration_ms 열 이름을 duration로 변경
    df_artist_top_track4.rename(columns={'duration_ms':'duration'}, inplace=True)

    # 열 제목을 변경
    df_artist_top_track4.columns = ["아티스트", "곡 제목", "곡의 길이", "곡 ID", "인기도"]
    
    return df_artist_top_track4


# [8장: 385페이지]

# In[ ]:


artist_id = "3Nrfpe0tUJi4K4DXYWgMUX" # 방탄소년단(BTS)의 아티스트 ID  
country_code = "US" # 미국의 국가 코드

df_BTS_top_track = get_artist_top_track(artist_id, country_code)
df_BTS_top_track.head()


# #### 아티스트의 앨범 정보 가져오기

# [8장: 387페이지]

# In[ ]:


def get_spotify_artist_albums_tracks(artist_id, include_groups=None):

    url = "https://api.spotify.com/v1/artists/{id}/albums".format(id=artist_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    parameters = {"include_groups": include_groups}
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}
      
    if(include_groups==None): # 앨범 타입을 지정하지 않을 경우 params 인수 없이 호출
        r = requests.get(url, headers=headers)
    else:                     # 앨범 타입을 지정할 경우 params 인수 호출
        r = requests.get(url, params=parameters, headers=headers)

    return r.json()


# [8장: 388페이지]

# In[ ]:


import pandas as pd

artist_id = "3HqSLMAZ3g3d5poNaI7GOU" # 아이유의 아티스트 ID

# album, single, appears_on, compilation
include_groups = "album,single"

artist_albums_data = get_spotify_artist_albums_tracks(artist_id, include_groups)
# artist_albums_data = get_sptoify_artist_albums_tracks(artist_id)
artist_albums = artist_albums_data['items']

albums_info = []
for album in artist_albums:
    albums_name_release_date = {"name":album['name'],
                                "album_type":album['album_type'],
                                "release_date":album['release_date'],
                                "album_id":album['id'],}
    albums_info.append(albums_name_release_date)

df_albums = pd.DataFrame(albums_info)
df_albums[0:10]


# [8장: 389페이지]

# In[ ]:


df_albums[df_albums['album_type']=='album']


# In[ ]:


import pandas as pd

def get_artist_albums(artist_id, include_groups=None):
    
    artist_albums_data = get_spotify_artist_albums_tracks(artist_id, include_groups)
    artist_albums = artist_albums_data['items']

    albums_info = []
    for album in artist_albums:
        albums_name_release_date = {"name":album['name'],
                                    "album_type":album['album_type'],
                                    "release_date":album['release_date'],
                                    "album_id":album['id'],}
        albums_info.append(albums_name_release_date)

    df_albums = pd.DataFrame(albums_info)
    return df_albums


# [8장: 390페이지]

# In[ ]:


artist_id = "6OwKE9Ez6ALxpTaKcT5ayv" # 악동뮤지션(악뮤)의 아티스트 ID

df_AKMU_albums = get_artist_albums(artist_id)
df_AKMU_albums.head()


# ### 8.4.3 트랙 API로 곡 관련 정보 가져오기

# #### 트랙(곡) 정보 가져오기

# [8장: 393페이지]

# In[ ]:


import requests

def get_spotify_track_info(track_id):
    url = "https://api.spotify.com/v1/tracks/{id}".format(id=track_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    headers = {"Authorization": "Bearer " + ACCESS_TOKEN} # 헤더 생성
    r = requests.get(url, headers=headers) # GET 방법으로 요청해 응답받음

    return r.json()


# In[ ]:


track_id = "2bgTY4UwhfBYhGT4HUYStN" # 트랙 ID(방탄소년단 Butter)
track_data = get_spotify_track_info(track_id)

print("[트랙(곡) 정보]")
print("- 아티스트:", get_artists(track_data['artists'])) # get_artists() 함수 이용
print("- 트랙(곡) 제목:", track_data['name'])
print("- 발표일:", track_data['album']['release_date'])
print("- 트랙(곡) 길이:", convert_msec(track_data['duration_ms'])) # convert_msec() 함수 이용
print("- 트랙 ID:", track_data['id'])
print("- 인기도:", track_data['popularity'])


# #### 트랙(곡)의 오디오 특징 정보 가져오기

# [8장: 396페이지]

# In[ ]:


import requests

def get_spotify_audio_features(track_id):
    url = "https://api.spotify.com/v1/audio-features/{id}".format(id=track_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    headers = {"Authorization": "Bearer " + ACCESS_TOKEN} # 헤더 생성
    r = requests.get(url, headers=headers) # GET 방법으로 요청해 응답받음

    return r.json()


# In[ ]:


track_id = "2bgTY4UwhfBYhGT4HUYStN" # 트랙 ID(방탄소년단 Butter)
audio_features_data = get_spotify_audio_features(track_id)
audio_features_data


# [8장: 397페이지]

# In[ ]:


import pandas as pd 

track_IDs = ["2bgTY4UwhfBYhGT4HUYStN", # 방탄소년단 Butter
             "3P3UA61WRQqwCXaoFOTENd", # 아이유 밤편지
             "5FKdWT5A7vDTEnPiHrruFY", # 김동률 출발
             "4ribiWWnI451QMRdOgByIP", # 이무진 비와 당신
             "1s6GWG2BrEWLE8sbd1lXME", # 악뮤 오랜 날 오랜 밤
             "4t2FIqZJORKZGSKg30SShr", # 악뮤(with IU) 낙하
             "1iIhGHzzrzqQfuNkFI2qAn", # 지코 아무 노래
             "4XaG9IpCXklOcuau1sIrUX", # 퀸(Queen) We Are The Champions
             "7vd1j4IDTU0koES9M8dvBQ", # 이루마 Kiss The Rain
             "3L1Ssz5HaOV3ZG9eJnV8UY"] # 피아노 캐논 변주곡
 
tracks_audio_features = [] # 여러 곡의 오디오 특징 리스트

for track_ID in track_IDs:
    # 아티스트와 트랙 이름 가져오기
    track_info = get_spotify_track_info(track_ID)
    
    # 트랙의 오디오 특징을 가져오기
    audio_features = get_spotify_audio_features(track_ID)
    
    # 아티스트와 트랙 정보와 오디오 특징 통합
    track_audio_features = {"artists":get_artists(track_info['artists']), 
                            "title":track_info['name'], 
                            "danceability":audio_features['danceability'],
                            "energy":audio_features['energy'],
                            "valence":audio_features['valence'],
                            "acousticness":audio_features['acousticness'],
                            "speechiness":audio_features['speechiness'],
                            "instrumentalness":audio_features['instrumentalness'],
                            "liveness":audio_features['liveness']}
    
    # 트랙의 오디오 특징 정보를 리스트에 담기
    tracks_audio_features.append(track_audio_features)
    
# DataFrame 데이터로 변환
df_tracks_audio_features = pd.DataFrame(tracks_audio_features)
df_tracks_audio_features


# [8장: 399페이지]

# In[ ]:


import matplotlib as mpl

mpl.rcParams['font.family'] = 'Malgun Gothic' # '맑은 고딕'으로 폰트 설정 
mpl.rcParams['axes.unicode_minus'] = False   # 마이너스(-) 폰트 깨짐 방지


# [8장: 400페이지]

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 이제 오디오 특징 중 몇 가지를 선택해 막대 그래프로 비교해 보겠습니다.

# In[ ]:


import matplotlib.pyplot as plt

selected_columns = ["danceability", "energy", "valence", "acousticness",
                    "speechiness", "instrumentalness", "liveness"]
df_tracks_audio_features2 = df_tracks_audio_features[selected_columns]

ax = df_tracks_audio_features2.T.plot.bar(figsize=(15,4))
ax.legend(df_tracks_audio_features["title"],  bbox_to_anchor=(0.55, 0.2))

# x축 라벨, y축 라벨, title 지정 
ax.set_xlabel('오디오 특징', fontsize = 15)
ax.set_ylabel('값', fontsize = 15)
ax.set_title('트랙별 오디오 특징 비교', fontsize = 18)

plt.show()


# ### 8.4.4  앨범 API로 앨범 관련 정보 가져오기

# #### 앨범 정보 가져오기 

# [8장: 404페이지]

# In[ ]:


def get_spotify_album_info(album_id):
    url = "https://api.spotify.com/v1/albums/{id}".format(id=album_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    headers = {"Authorization": "Bearer " + ACCESS_TOKEN} # 헤더 생성

    r = requests.get(url, headers=headers) # GET 방법으로 응답을 요청

    return r.json()


# In[ ]:


album_id = "01dPJcwyht77brL4JQiR8R" # 앨범 ID(아이유 IU 5th Album 'LILAC' 앨범)

album_data = get_spotify_album_info(album_id)
album_data.keys()


# [8장: 405페이지]

# In[ ]:


print("[앨범 정보]")
print("- 아티스트:", get_artists(album_data['artists'])) # get_artists() 함수 이용
print("- 앨범 제목:", album_data['name'])
print("- 앨범 발표일:", album_data['release_date'])
print("- 앨범의 곡 개수:", album_data['total_tracks']) 
print("- 앨범 ID:", album_data['id'])
print("- 앨범 인기도:", album_data['popularity'])
print("- 앨범 Label:", album_data['label'])


# #### 앨범의 트랙(곡) 정보 가져오기 

# [8장: 407페이지]

# In[ ]:


def get_spotify_album_tracks(album_id):
    url = "https://api.spotify.com/v1/albums/{id}/tracks".format(id=album_id)
    ACCESS_TOKEN = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)

    headers = {"Authorization": "Bearer " + ACCESS_TOKEN} # 헤더 생성

    r = requests.get(url, headers=headers) # GET 방법으로 요청해 응답받음

    return r.json()


# In[ ]:


album_id = "01dPJcwyht77brL4JQiR8R" # 앨범 ID(아이유 IU 5th Album 'LILAC' 앨범)

album_tracks_data = get_spotify_album_tracks(album_id)

print("[앨범 트랙 정보]")
print("- 앨범 트랙 API URL:", album_tracks_data['href'])
print("- 설정한 트랙 수 :", album_tracks_data['limit']) 
print("- 설정한 트랙 오프셋:", album_tracks_data['offset']) 
print("- 앨범의 곡 개수:", album_tracks_data['total']) 
print("- 다음 트랙 API URL:", album_tracks_data['next']) 


# [8장: 408페이지]

# In[ ]:


import pandas as pd

def get_album_track(album_id):    
    album_tracks_data = get_spotify_album_tracks(album_id)
    album_tracks = album_tracks_data['items']

    df_album_tracks = pd.DataFrame(album_tracks) # DataFrame 데이터로 변환
    
    df_album_tracks2 = df_album_tracks[['artists', 'name', 'duration_ms', 'id']] # DataFrame 데이터에서 열 선택
    
    df_album_tracks3 = df_album_tracks2.copy() # DataFrame 데이터 복사
    df_album_tracks3['artists'] = df_album_tracks3['artists'].apply(get_artists) # 함수를 artists 열의 각 항목에 적용

    df_album_tracks4 = df_album_tracks3.copy() # DataFrame 데이터 복사
    df_album_tracks4['duration_ms'] = df_album_tracks4['duration_ms'].apply(convert_msec) # 함수를 artists 열의 각 항목에 적용
    df_album_tracks4.rename(columns = {'duration_ms' : 'duration'}, inplace = True) # duration_ms 열 이름을 duration로 변경

    df_album_tracks4.columns = ["아티스트", "곡 제목", "곡의 길이", "곡 ID"] # 열 제목을 변경
    
    return df_album_tracks4


# In[ ]:


album_id = "01dPJcwyht77brL4JQiR8R" # 앨범 ID(아이유 IU 5th Album 'LILAC' 앨범)

df_IU_album_tracks = get_album_track(album_id)
df_IU_album_tracks.head()


# ## 8.5 야후 파이낸스에서 주식 데이터 가져오기

# ### 8.5.1 설치 및 기본 사용법

# ### 8.5.2 미국 주식 데이터 가져오기

# [8장: 411페이지]

# In[ ]:


import yfinance as yf

ticker_symbol = "TSLA" # 테슬라 주식 심볼
ticker_data = yf.Ticker(ticker_symbol)

# 해당 종목의 정보 가져오기
# ticker_data.info

df = ticker_data.history(period='5d')
df


# [8장: 412페이지]

# In[ ]:


df = ticker_data.history(period='1mo', interval='1d',start='2022-04-18', end='2022-04-22')
df


# [8장: 413페이지]

# In[ ]:


df = ticker_data.history(start='2022-04-18', end='2022-04-23') # start와 end 모두 지정
# df = ticker_data.history(start='2022-04-18') # start만 지정
df


# In[ ]:


import datetime

start_p = datetime.datetime(2021,5,24) # 시작일 지정
end_p = datetime.datetime(2021,5,29)   # 종료일 지정

df = ticker_data.history(start=start_p, end=end_p) # start와 end 모두 지정
df


# ### 8.5.3 국내 주식 데이터 가져오기

# [8장: 414페이지]

# In[ ]:


import pandas as pd

#----------------------------------------------------
# 한국 주식의 종목 이름과 종목 코드를 가져오는 함수
#----------------------------------------------------
def get_stock_info(maket_type=None):
    # 한국거래소(KRX)에서 전체 상장법인 목록 가져오기
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"
    method = "download"
    if maket_type == 'kospi':
        marketType = "stockMkt"  # 주식 종목이 코스피인 경우
    elif maket_type == 'kosdaq':
        marketType = "kosdaqMkt" # 주식 종목이 코스닥인 경우
    elif maket_type == None:
        marketType = ""
    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)

    df = pd.read_html(url, header=0)[0]
    
    # 종목코드 열을 6자리 숫자로 표시된 문자열로 변환
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}") 
    
    # 회사명과 종목코드 열 데이터만 남김
    df = df[['회사명','종목코드']]
    
    return df


# [8장: 415페이지]

# In[ ]:


def get_ticker_symbol(company_name, maket_type):
    """
    ----------------------------------------------------
      yfinance에 이용할 Ticker 심볼을 반환하는 함수
    ----------------------------------------------------
    """
    df = get_stock_info(maket_type)
    code = df[df['회사명']==company_name]['종목코드'].values
    code = code[0]
    
    if maket_type == 'kospi':
        ticker_symbol = code +".KS" # 코스피 주식의 심볼
    elif maket_type == 'kosdaq':
        ticker_symbol = code +".KQ" # 코스닥 주식의 심볼
    
    return ticker_symbol


# In[ ]:


import yfinance as yf

ticker_symbol = get_ticker_symbol("삼성전자", "kospi") # 삼성전자, 주식 종류는 코스피로 지정
ticker_data = yf.Ticker(ticker_symbol)

df = ticker_data.history(start='2022-06-13', end='2022-06-18') # 시작일과 종료일 지정
# df = ticker_data.history(period='5d') # 기간을 지정

df


# [8장: 416페이지]

# In[ ]:


excel_file_name = "C:/myPyScraping/data/ch08/삼성전자_주가_데이터.xlsx" # 엑셀 파일 이름 지정
df.to_excel(excel_file_name)

print("생성 파일:", excel_file_name)


# ### 8.5.4 여러 주식 데이터 가져오기

# [8장: 417페이지]

# In[ ]:


ticker_symbols = "MSFT" # 마이크로소프트 주식 심볼
# ticker_symbols = ["MSFT"] # 리스트도 지정해도 됨
df = yf.download(ticker_symbols, start="2020-01-01", end="2022-01-01")
df.tail()


# In[ ]:


# 그래프 그리기
import matplotlib.pyplot as plt

df['Close'].plot(grid=True, figsize=(15, 5), title="Microsoft")
plt.show()


# [8장: 418페이지]

# In[ ]:


ticker_symbols = ["GOOG", "AAPL"] # 주식 심볼 리스트(구글, 애플)
df = yf.download(ticker_symbols,  start="2020-01-01", end="2022-01-01")
df.tail()


# In[ ]:


# 그래프 그리기
import matplotlib.pyplot as plt

df['Close'].plot(grid=True, figsize=(15, 5))
plt.show()


# [8장: 419페이지]

# In[ ]:


# 그래프 그리기
df['Close'].plot(grid=True, figsize=(15, 5), subplots=True, layout=(2,1))
plt.show()


# ## 8.6 정리
