#!/usr/bin/env python
# coding: utf-8

# # 9장 스트림릿으로 웹 앱(Web App) 만들기

# ## 9.1 스트림릿 둘러보기

# ### 9.1.1 데모 웹 앱으로 스트림릿 맛보기

# ### 9.1.2 웹 앱을 위한 코드 실행 방법

# ## 9.2 스트림릿 기본 사용법

# ### 9.2.1 텍스트 요소

# [9장: 426페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\text_app.py', '# 텍스트 표시 예제\n\nimport streamlit as st\n\nst.title("st.title(문자열): 제목")\nst.header("st.header(문자열): 헤더")\nst.subheader("st.subheader(문자열): 서브헤더")\nst.text("st.text(문자열): 일반 텍스트입니다.")\n\nst.text("st.code(code): 파이썬 코드 표시")\n\ncode = \'\'\'\ndef hello():\n    print("Hello, Streamlit!")\n\'\'\'\nst.code(code)\n\nst.markdown(\'스트림릿에서 **마크다운**을 사용할 수 있습니다.:sunglasses:\')\n')


# ### 9.2.2 데이터 표시 요소

# [9장: 429페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\data_app1.py', '# 데이터 표시 예제1\n\nimport streamlit as st\nimport pandas as pd\n\n# CSV 파일 경로\nfolder = \'C:/myPyScraping/data/ch09/\' # 폴더 경로를 지정\ncsv_file = folder + \'korea_rain1.csv\' # 파일 경로를 지정\n\n# CSV 파일을 읽어와서 DataFrame 데이터 생성\ndf = pd.read_csv(csv_file, encoding="utf-8")\n\nst.title("스트림릿에서 데이터 표시 (1/2)")\n\nst.subheader("st.dataframe() 이용")\nst.dataframe(df)\n\nst.subheader("st.table() 이용")\nst.table(df)\n')


# [9장: 430페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\data_app2.py', '# 데이터 표시 예제2\n\nimport streamlit as st\nimport pandas as pd\nimport json\n\n# 딕셔너리 데이터\ndict_data = {\n    "이름": "홍길동",\n    "나이": 25,\n    "거주지": "서울",\n    "신체정보": {\n        "키": 175.4,\n        "몸무게": 71.2\n    },\n    "취미": [\n        "등산",\n        "자전거타기",\n        "독서"\n    ]\n}\n\n# 딕셔너리 데이터를 JSON 데이터로 변경\njson_data = json.dumps(dict_data, indent=3, sort_keys=True, ensure_ascii=False)\n\nst.title("스트림릿에서 데이터 표시 (2/2)")\n\nst.subheader("st.json() 이용")\nst.json(json_data)\n\nst.subheader("st.metric() 이용")\nst.metric("온도", "25 °C", delta="1.5 °C")\n')


# ### 9.2.3 차트 요소

# [9장: 434페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\chart_app1.py', '# 차트 표시 예제1\n\nimport streamlit as st\nimport pandas as pd\n\ndata1 = [ -2,   5,  -3,  -3,   9,  -4,  -7,  -9,   2,   3]\ndata2 = [  3,   4,  -4,  -2,  -3,  -2,   0,   7,  -6,   6]\ndata3 = [-10,   2,   8,   6,  -7,  -1,  -4,  -1,   4,   5]\n\ndict_data = {"data1":data1, "data2":data2, "data3":data3}\ndf = pd.DataFrame(dict_data) # DataFrame\n\nst.title("스트림릿에서 차트 그리기")\n\nst.subheader("꺾은선형 차트: st.line_chart(df) 이용")\nst.line_chart(df, height=170) # 높이 지정\n\nst.subheader("영역형 차트: st.area_chart(df) 이용")\nst.area_chart(df, height=170) # 높이 지정\n\nst.subheader("세로 막대형 차트: st.bar_chart(df) 이용")\nst.bar_chart(df, height=170) # 높이 지정\n')


# [9장: 436페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\chart_app2.py', '# 차트 표시 예제2\n\nimport streamlit as st\nimport pandas as pd\nimport numpy as np\n\nbase_lat = 37.55   # 기준 위치 (위도)\nbase_lon = 126.95  # 기준 위치 (경도)\n\nrand1 = [ 0.38731831, 0.88186355, 0.73767047, 0.48262488, 0.40470396,\n          0.44718457, 0.62209526, 0.00927177, 0.45061387, 0.29512467,\n          0.03209323, 0.21555133, 0.18564942, 0.21124898, 0.56080097,\n          0.07353603, 0.96114633, 0.43632126, 0.61204948, 0.56378569 ]\n\nrand2 = [ 0.33344199, 0.60650414, 0.30760968, 0.15650897, 0.61547323,\n          0.4844213 , 0.5180108 , 0.52112468, 0.38900425, 0.71651658,\n          0.75229359, 0.31247536, 0.53251045, 0.37826329, 0.17648217,\n          0.57750034, 0.38393327, 0.34383632, 0.31099857, 0.26455346 ]\n \npos_lat = base_lat + np.array(rand1) * 0.02\npos_lon = base_lon + np.array(rand2) * 0.02\n\n# 위도(latitude)와 경도(longitude)를 지정한 DataFrame 데이터 생성\npos_data = {"lat":pos_lat, "lon":pos_lon} # 위도와 경도 데이터를 이용해 딕셔너리 데이터 생성\ndf_for_map = pd.DataFrame(pos_data) # DataFrame 데이터의 열 이름은 lat와 lon으로 지정됨\n\nst.title("스트림릿에서 차트 그리기")\nst.subheader("지도 좌표(위도, 경도)에 점 그리기: st.map(df) 이용")\nst.map(df_for_map, zoom=12) # zoom에 초기의 지도 크기를 지정\n')


# [9장: 437페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\chart_app3.py', '# 차트 표시 예제3\n\nimport streamlit as st\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport matplotlib\n\n# matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정\nmatplotlib.rcParams[\'font.family\'] = \'Malgun Gothic\'\nmatplotlib.rcParams[\'axes.unicode_minus\'] = False\n\n# 꺾은선형 차트 데이터\nfolder = \'C:/myPyScraping/data/ch09/\'\nfile = folder + \'공장별_생산현황.csv\'\ndf1 = pd.read_csv(file, index_col=\'year\')\n\n# 세로 막대형 차트 데이터\nfile = folder + \'영업팀별_판매현황.xlsx\'\ndf2 = pd.read_excel(file, index_col=\'월\')\n\nst.title("스트림릿에서 차트 그리기")\n\n# 꺾은선형 차트 그리기\nax = df1.plot(grid=True, figsize=(15,5))\nax.legend([\'공장 A\', \'공장 B\', \'공장 C\'], fontsize=10)\nax.set_title("공장별 생산 현황", fontsize=20) # 그래프 제목을 지정\nax.set_xlabel("연도", fontsize=15)            # x축 라벨을 지정\nax.set_ylabel("생산량", fontsize=15)          # y축 라벨을 지정\nfig1 = ax.get_figure()                        # fig 객체 가져오기\n\nst.subheader("꺾은선형 차트: Matplotlib과 st.pyplot(fig) 이용")\nst.pyplot(fig1) # 스트림릿 웹 앱에 그래프 그리기\n\n# 세로 막대형 차트 그리기\nax = df2.plot.bar(grid=True, rot=0,  figsize=(15,5))\nax.set_title("영업팀별 판매현황", fontsize=20) # 그래프 제목을 지정\nax.set_xlabel("월", fontsize=15)               # x축 라벨을 지정\nax.set_ylabel("판매현황", fontsize=15)         # y축 라벨을 지정\nfig2 = ax.get_figure()                         # fig 객체 가져오기\n\nst.subheader("세로 막대형 차트: Matplotlib과 st.pyplot(fig) 이용")\nst.pyplot(fig2) # 스트림릿 웹 앱에 그래프 그리기\n')


# ### 9.2.4 만능 함수와 마술 명령어

# [9장: 440페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\write_app.py', '# write 예제\n\nimport streamlit as st\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport matplotlib\n\nst.write("# 스트림릿의 st.write() 함수의 사용 예")\n\nst.write("#### 텍스트 출력")\nst.write("일반 텍스트로 출력할 수도 있고, **마크다운**으로 출력할 수도 있습니다. :thumbsup:")\n\nst.write("#### 데이터 출력")\nst.write("숫자 데이터 출력:", 1234)\n\ndf = pd.DataFrame({\n        \'1열\': [10, 20, 30, 40],\n        \'2열\': [50, 60, 70, 80,]})\n\nst.write("DataFrame 데이터 출력", df)\n\n# matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정\nmatplotlib.rcParams[\'font.family\'] = \'Malgun Gothic\'\nmatplotlib.rcParams[\'axes.unicode_minus\'] = False\n\n# 그래프를 위한 데이터 생성\nx = np.linspace(0, 2*np.pi, 100)\ny = np.sin(x)\ndf = pd.DataFrame(y, index=x)\n\n# 그래프 그리기\nax = df.plot(grid=True, figsize=(15,4), legend=False)\nax.set_title("sin(x) 그래프", fontsize=20) # 그래프 제목을 지정\nax.set_xlabel("x", fontsize=15)            # x축 라벨을 지정\nax.set_ylabel("y", fontsize=15)            # y축 라벨을 지정\nfig = ax.get_figure()                      # fig 객체 가져오기\n\nst.write("#### Matplotlib 차트 출력:", fig)\n')


# [9장: 442페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\magic_app.py', '# magic 예제\n\nimport streamlit as st\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport matplotlib\n\n"# 스트림릿의 magic 명령어 사용 예"\n\n"#### 텍스트 출력"\n"일반 텍스트로 출력할 수도 있고, **마크다운**으로 출력할 수도 있습니다. :thumbsup:"\n\n"#### 데이터 출력"\n"숫자 데이터 출력:", 1234\n\ndf = pd.DataFrame({\n        \'1열\': [10, 20, 30, 40],\n        \'2열\': [50, 60, 70, 80,]})\n\n"DataFrame 데이터 출력", df\n\n# matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정\nmatplotlib.rcParams[\'font.family\'] = \'Malgun Gothic\'\nmatplotlib.rcParams[\'axes.unicode_minus\'] = False\n\n# 그래프를 위한 데이터 생성\nx = np.linspace(0, 2*np.pi, 100)\ny = np.sin(x)\ndf = pd.DataFrame(y, index=x)\n\n# 그래프 그리기\nax = df.plot(grid=True, figsize=(15,4), legend=False)\nax.set_title("sin(x) 그래프", fontsize=20) # 그래프 제목을 지정\nax.set_xlabel("x", fontsize=15)            # x축 라벨을 지정\nax.set_ylabel("y", fontsize=15)            # y축 라벨을 지정\nfig = ax.get_figure()                      # fig 객체 가져오기\n\n"#### Matplotlib 차트 출력:", fig\n')


# ### 9.2.5 입력 위젯

# #### 기본 버튼

# [9장: 445페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\button_app.py', '# 기본 버튼 입력 예제\n\nimport streamlit as st\n\nst.title("스트림릿의 버튼 입력 사용 예")\n\nclicked = st.button(\'버튼 1\')\nst.write(\'버튼 1 클릭 상태:\', clicked)\n\nif clicked:\n     st.write(\'버튼 1을 클릭했습니다.\' )\nelse:\n     st.write(\'버튼 1을 클릭하지 않았습니다.\' )\n        \nclicked = st.button(\'버튼 2\')\nst.write(\'버튼 2 클릭 상태:\', clicked)\n\nif clicked:\n     st.write(\'버튼 2를 클릭했습니다.\' )\nelse:\n     st.write(\'버튼 2를 클릭하지 않았습니다.\' )\n')


# #### 다운로드 버튼

# [9장: 448페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\download_button_app.py', '# 다운로드 버튼 사용 예제\n\nimport streamlit as st\nimport pandas as pd\nfrom io import BytesIO\n\nKTX_data = {\'경부선 KTX\': [43621, 41702, 41266, 32427],\n            \'호남선 KTX\': [6626, 8675, 10622, 9228],\n            \'경전선 KTX\': [4424, 4606, 4984, 5570],\n            \'전라선 KTX\': [2244, 3146, 3945, 5766]}\ncol_list = [\'경부선 KTX\',\'호남선 KTX\',\'경전선 KTX\',\'전라선 KTX\']\nindex_list = [\'2014\', \'2015\', \'2016\', \'2017\']\n\ndf = pd.DataFrame(KTX_data, columns = col_list, index = index_list)\n\n# DataFrame 데이터를 CSV 데이터(csv_data)로 변환\ncsv_data = df.to_csv()\n\n# DataFrame 데이터를 엑셀 데이터(excel_data)로 변환\nexcel_data = BytesIO() # 메모리 버퍼에 바이너리 객체 생성\ndf.to_excel(excel_data) # DataFrame 데이터를 엑셀 형식으로 버퍼에 쓰기\n\n# 스트림릿 화면 구성\nst.title("스트림릿의 다운로드 버튼 사용 예")\n\nst.subheader("DataFrame 데이터")\nst.dataframe(df)\n             \nst.subheader("CSV 파일로 다운로드")\nst.download_button("CSV 파일 다운로드", csv_data, file_name=\'KTX_users.csv\')\n\nst.subheader("엑셀 파일로 다운로드")\nst.download_button("엑셀 파일 다운로드", excel_data, file_name=\'KTX_users.xlsx\')\n')


# #### 체크박스

# [9장: 450페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\check_box_app.py', '# 체크박스 사용 예제\n\nimport streamlit as st\n\nst.title("스트림릿의 체크박스 사용 예")\n\nchecked1 = st.checkbox(\'체크박스 1\')\nst.write(\'체크박스 1 상태:\', checked1)\n       \nif checked1:\n     st.write(\'체크박스 1을 체크했습니다.\' )\nelse:\n     st.write(\'체크박스 1을 체크하지 않았습니다.\' )\n        \nchecked2 = st.checkbox(\'체크 박스 2\', value=True)\nst.write(\'체크박스 2 상태:\', checked2)\n\nif checked2:\n     st.write(\'체크박스 2를 체크했습니다.\' )\nelse:\n     st.write(\'체크박스 2를 체크하지 않았습니다.\' )\n')


# #### 라디오 버튼

# [9장: 452페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\radio_button_app.py', '# 라디오 버튼 사용 예제\n\nimport streamlit as st\nimport pandas as pd\n\nst.title("스트림릿의 라디오 버튼 사용 예")\n\nradio1_options = [\'10\', \'20\', \'30\', \'40\']\nradio1_selected = st.radio(\'1. (5 x 5 + 5)은 얼마인가요?\', radio1_options)\nst.write(\'**선택한 답**:\', radio1_selected)\n        \nradio2_options = [\'마라톤\', \'축구\', \'수영\', \'승마\']\nradio2_selected = st.radio(\'2. 당신이 좋아하는 운동은?\', radio2_options, index=2)\nst.write(\'**당신의 선택**:\', radio2_selected)\n')


# #### 셀렉트박스

# [9장: 453페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\selectbox_app.py', '# 셀렉트박스 사용 예제\n\nimport streamlit as st\n\nst.title("스트림릿의 셀렉트박스 사용 예")\n\nselectbox1_options = [\'하이든\', \'모짜르트\', \'베토벤\', \'슈만\']\nyour_option1 = st.selectbox(\'1. 좋아하는 음악가는?\', selectbox1_options)\nst.write(\'**당신의 선택**:\', your_option1)\n\nselectbox2_options = [\'보티첼리\', \'램브란트\', \'피카소\', \'뭉크\']\nyour_option2 = st.selectbox(\'2. 좋아하는 화가는?\', selectbox2_options)\nst.write(\'**당신의 선택**:\', your_option2)\n')


# #### 텍스트 입력

# [9장: 454페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\text_input_app.py', '# 텍스트 입력의 사용 예제\n\nimport streamlit as st\n\nst.title("스트림릿의 텍스트 입력 사용 예")\n\nuser_id = st.text_input(\'아이디(ID) 입력\', value="streamlit", max_chars=15)\nuser_password = st.text_input(\'패스워드(Password) 입력\', value="abcd", type="password")\n\nif user_id == "streamlit":\n    if user_password == "1234":\n        st.write(\'로그인 됐습니다. 서비스를 이용할 수 있습니다.\')\n    else:\n        st.write(\'잘못된 패스워드입니다. 다시 입력하세요.\')\nelse:\n    st.write(\'없는 ID 입니다. 회원 가입을 하거나 올바른 ID를 입력하세요.\')\n')


# #### 숫자 입력

# [9장: 456페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\number_input_app.py', '# 숫자 입력의 사용 예제\n\nimport streamlit as st\n\nst.title("스트림릿의 숫자 입력 사용 예")\n\nnumber1 = st.number_input(\'20 이상의 두 자리 숫자를 입력하세요\', min_value=20, max_value=99)\nst.write(\'**입력한 숫자**\', number1)\n\nheight = st.number_input(\'키(cm)를 입력하세요\', min_value=1.0, value=170.0, step=0.1)\nweight = st.number_input(\'몸무게(kg)를 입력하세요\', min_value=1.0, value=65.5)\nBMI = weight/((height/100)**2)\nst.write(\'**신체질량지수(BMI):**\', BMI )\n')


# #### 날짜 입력

# [9장: 458페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\date_input_app.py', '# 날짜 입력의 사용 예제\n\nimport streamlit as st\nimport datetime\n\nst.title("스트림릿의 날짜 입력 사용 예")\n\n# 날짜 지정\nbirthday = st.date_input("1. 당신의 생일은 언제입니까?", \n                          value=datetime.date(2000, 1, 1))\nst.write("당신의 생일: ", birthday)\n\n# 날짜의 범위 지정\ndate_range = st.date_input("2. 시작과 끝 날짜를 선택해 주세요", \n                           value=[datetime.date(2022, 1, 10), datetime.date(2022, 2, 1)],\n                           min_value=datetime.date(2022, 1, 5),\n                           max_value=datetime.date(2022, 2, 20))\nst.write("당신이 선택한 날짜의 범위: ", date_range)\n')


# #### 시각 입력

# [9장: 460페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\time_input_app.py', '# 시각 입력의 사용 예제\n\nimport streamlit as st\nimport datetime\n\nst.title("스트림릿의 시각 입력 사용 예")\n\nalarm_time = st.time_input("알람 시각을 설정하세요", value=datetime.time(7, 30)) # 오전 7시 30분\nst.write("**알람 설정 시각:** ", alarm_time)\n\nwork_start_time = st.time_input("업무 시작 시각을 설정하세요", value=datetime.time(9)) # 오전 9시\nst.write("**업무 시작 시각:** ", work_start_time)\n')


# ### 9.2.6 미디어 요소

# [9장: 462페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\image_app.py', '# 이미지 표시 사용 예제\n\nimport streamlit as st\nfrom PIL import Image\n\nst.title("스트림릿의 이미지 표시 사용 예")\n\n# 1) 컴퓨터 내에 있는 이미지 파일을 열어서 표시\nst.subheader("1. 컴퓨터 내의 이미지 파일을 표시")\nimage_file = \'C:/myPyScraping/data/ch09/avenue.jpg\' # 이미지 파일 경로\nimage_local = Image.open(image_file)                # PIL 라이브러리의 Image.open() 함수로 이미지 파일 열기\nst.image(image_local, width=350, caption=\'컴퓨터 내의 이미지 파일을 열어서 표시한 이미지\') # 이미지 표시\n\n# 2) 웹상에 있는 이미지의 주소(URL)를 이용해 이미지 표시\nst.subheader("2. 웹상에 있는 이미지 파일을 표시")\nimage_url = "https://cdn.pixabay.com/photo/2015/05/04/10/16/vegetables-752153_960_720.jpg" # 이미지 URL\nst.image(image_url, width=350, caption=\'웹상에 있는 이미지의 주소(URL)를 지정해 표시한 이미지\') # 이미지 표시\n')


# ### 9.2.7 레이아웃과 컨테이너

# #### 사이드바에 표시

# [9장: 464페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\sidebar_app.py', '# 이미지 표시 사용 예제\n\nimport streamlit as st\nfrom PIL import Image\n\n# 사이드바 화면\nst.sidebar.title("사이드바 ")\nst.sidebar.header("텍스트 입력 사용 예")\nuser_id = st.sidebar.text_input(\'아이디(ID) 입력\', value="streamlit", max_chars=15)\nuser_password = st.sidebar.text_input(\'패스워드(Password) 입력\', value="abcd", type="password")\n\nst.sidebar.header("셀렉트박스 사용 예")\nselectbox_options = [\'진주 귀걸이를 한 소녀\', \'별이 빛나는 밤\', \'절규\', \'월하정인\'] # 셀렉트 박스의 선택 항목\nyour_option = st.sidebar.selectbox(\'좋아하는 작품은?\', selectbox_options, index=3) # 셀렉트박스의 항목 선택 결과\nst.sidebar.write(\'**당신의 선택**:\', your_option)\n\n# 메인(Main) 화면\nst.title("스트림릿의 사이드바 사용 예")\n\nfolder = \'C:/myPyScraping/data/ch09/\'\n\n# selectbox_options의 요소에 따라서 보여줄 이미지 파일 리스트 (selectbox_options의 요소와 순서를 일치시킴)\nimage_files = [\'Vermeer.png\', \'Gogh.png\', \'Munch.png\', \'ShinYoonbok.png\'] # 이미지 파일 리스트\n\n# 셀렉트박스에서 선택한 항목에 따라 이미지 표시\nselectbox_options_index = selectbox_options.index(your_option) # selectbox_options의 리스트 인덱스 찾기\nimage_file = image_files[selectbox_options_index] # 선택한 항목에 맞는 이미지 파일 지정\nimage_local = Image.open(folder + image_file)     # PIL 라이브러리의 Image.open() 함수로 이미지 파일 열기\nst.image(image_local, caption=your_option)        # 이미지 표시\n')


# #### 컬럼으로 화면 분할

# [9장: 467페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\columns_app.py', '# 세로단(컬럼) 분할 사용 예제\n\nimport streamlit as st\nfrom PIL import Image\nimport pandas as pd\nimport numpy as np\n\nst.title("스트림릿에서 화면 분할 사용 예")\n\n# 1) 2개로 세로단 분할 (예제 1)\nfolder = \'C:/myPyScraping/data/ch09/\'    # 폴더 지정\nfile = folder + \'공장별_생산현황2.csv\'   # 데이터 파일 지정\ndf = pd.read_csv(file, index_col=\'year\') # CSV 파일을 DataFrame 데이터로 읽기\n\n[col1, col2] = st.columns(2) # 너비가 같은 2개의 세로단으로 구성\n\nwith col1: # 첫 번째 세로단(컬럼)\n    st.subheader("DataFrame 데이터")\n    st.dataframe(df)  # DataFrame 데이터 표시\n\nwith col2: # 두 번째 세로단(컬럼)\n    st.subheader("꺾은 선 차트")\n    st.line_chart(df) # 꺾은 선 차트 표시\n\n# 2) 3개로 세로단 분할 (예제 2)\ncolumns = st.columns([1.1, 1.0, 0.9]) # 너비가 다른 3개의 세로단으로 구성\n\nimage_files = [\'dog.png\', \'cat.png\', \'bird.png\'] # 이미지 파일명 리스트\nimage_cations = [\'강아지\', \'고양이\', \'새\']       # 이미지 파일명 리스트\n\nfor k in range(len(columns)):\n    with columns[k]: # 세로단(컬럼) 지정\n        st.subheader(image_cations[k])                    # 세로단 별로 subheader 표시\n        image_local = Image.open(folder + image_files[k]) # 세로단 별로 이미지 열기\n        st.image(image_local,caption=image_cations[k])    # 세로단 별로 이미지 표시\n')


# ## 9.3 스트림릿을 활용해 웹 앱 만들기

# ### 9.3.1 주식 데이터 대시보드

# [9장: 469페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\stock_info_app.py', '# 주식 데이터를 가져오는 웹 앱\n\nimport streamlit as st\nimport pandas as pd\nimport yfinance as yf\nimport datetime\nimport matplotlib.pyplot as plt\nimport matplotlib\nfrom io import BytesIO\n\n#----------------------------------------\n# 한국 주식 종목 코드를 가져오는 함수\n#----------------------------------------\ndef get_stock_info(maket_type=None):\n    # 한국거래소(KRX)에서 전체 상장법인 목록 가져오기\n    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"\n    method = "download"\n    if maket_type == \'kospi\':\n        marketType = "stockMkt"  # 주식 종목이 코스피인 경우\n    elif maket_type == \'kosdaq\':\n        marketType = "kosdaqMkt" # 주식 종목이 코스닥인 경우\n    elif maket_type == None:\n        marketType = ""\n    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)\n\n    df = pd.read_html(url, header=0)[0]\n    \n    # 종목코드 열을 6자리 숫자로 표시된 문자열로 변환\n    df[\'종목코드\']= df[\'종목코드\'].apply(lambda x: f"{x:06d}")\n    \n    # 회사명과 종목코드 열 데이터만 남김\n    df = df[[\'회사명\',\'종목코드\']]\n    \n    return df\n#----------------------------------------------------\n# yfinance에 이용할 Ticker 심볼을 반환하는 함수\n#----------------------------------------------------\ndef get_ticker_symbol(company_name, maket_type):\n    df = get_stock_info(maket_type)\n    code = df[df[\'회사명\']==company_name][\'종목코드\'].values\n    code = code[0]\n    \n    if maket_type == \'kospi\':\n        ticker_symbol = code +".KS" # 코스피 주식의 심볼\n    elif maket_type == \'kosdaq\':\n        ticker_symbol = code +".KQ" # 코스닥 주식의 심볼\n    \n    return ticker_symbol\n#---------------------------------------------------------\n\nst.title("주식 정보를 가져오는 웹 앱")\n\n# 사이드바의 폭을 조절. {width:250px;}로 지정하면 폭을 250픽셀로 지정\nst.markdown(\n    """\n    <style>\n    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width:250px;}\n    </style>\n    """, unsafe_allow_html=True\n)\n\nst.sidebar.header("회사 이름과 기간 입력")\n\n# 주식 종목 이름을 입력 받아서 지정\nstock_name = st.sidebar.text_input(\'회사 이름\', value="NAVER")\n# 기간을 입력 받아서 지정\ndate_range = st.sidebar.date_input("시작일과 종료일",\n                 [datetime.date(2019, 1, 1), datetime.date(2021, 12, 31)])\n\nclicked = st.sidebar.button("주가 데이터 가져오기")\n\nif(clicked == True):\n    # 주식 종목과 종류 지정해 ticker 심볼 획득\n    ticker_symbol = get_ticker_symbol(stock_name, "kospi")\n    ticker_data = yf.Ticker(ticker_symbol)\n    \n    start_p = date_range[0]                            # 시작일\n    end_p = date_range[1] + datetime.timedelta(days=1) # 종료일(지정된 날짜에 하루를 더함)\n    # 시작일과 종료일 지정해 주가 데이터 가져오기\n    df = ticker_data.history(start=start_p, end=end_p)\n    \n    # 1) 주식 데이터 표시\n    st.subheader(f"[{stock_name}] 주가 데이터")\n    st.dataframe(df.head())  # 주가 데이터 표시(앞의 일부만 표시)\n    \n    # 2) 차트 그리기\n    # matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정\n    matplotlib.rcParams[\'font.family\'] = \'Malgun Gothic\'\n    matplotlib.rcParams[\'axes.unicode_minus\'] = False\n    \n    # 선 그래프 그리기\n    ax = df[\'Close\'].plot(grid=True, figsize=(15, 5))\n    ax.set_title("주가(종가) 그래프", fontsize=30) # 그래프 제목을 지정\n    ax.set_xlabel("기간", fontsize=20)             # x축 라벨을 지정\n    ax.set_ylabel("주가(원)", fontsize=20)         # y축 라벨을 지정\n    plt.xticks(fontsize=15)                        # X축 눈금값의 폰트 크기 지정\n    plt.yticks(fontsize=15)                        # Y축 눈금값의 폰트 크기 지정    \n    fig = ax.get_figure()                          # fig 객체 가져오기    \n    st.pyplot(fig)                                 # 스트림릿 웹 앱에 그래프 그리기\n    \n    # 3) 파일 다운로드\n    st.markdown("**주가 데이터 파일 다운로드**")\n    # DataFrame 데이터를 CSV 데이터(csv_data)로 변환\n    csv_data = df.to_csv()  # DataFrame 데이터를 CSV 데이터로 변환해 반환\n\n    # DataFrame 데이터를 엑셀 데이터(excel_data)로 변환\n    excel_data = BytesIO()  # 메모리 버퍼에 바이너리 객체 생성\n    df.to_excel(excel_data) # DataFrame 데이터를 엑셀 형식으로 버퍼에 쓰기\n\n    columns = st.columns(2) # 2개의 세로단으로 구성\n    with columns[0]:\n        st.download_button("CSV 파일 다운로드", csv_data, file_name=\'stock_data.csv\')\n    with columns[1]:\n        st.download_button("엑셀 파일 다운로드", excel_data, file_name=\'stock_data.xlsx\')\n')


# ### 9.3.2 환율 데이터 대시보드

# [9장: 473페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\exchange_rate_app.py', '# 환율 데이터를 가져오는 웹 앱\n\nimport streamlit as st\nimport pandas as pd\nimport datetime\nimport time\nimport matplotlib.pyplot as plt\nimport matplotlib\nfrom io import BytesIO\n\n# -----------------------------------------------------------------------------\n# 날짜별 환율 데이터를 반환하는 함수\n# - 입력 인수: currency_code(통화코드), last_page_num(페이지 수)\n# - 반환: 환율 데이터\n# -----------------------------------------------------------------------------\ndef get_exchange_rate_data(currency_code, last_page_num):\n    base_url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn"\n    df = pd.DataFrame()\n    \n    for page_num in range(1, last_page_num+1):\n        url = f"{base_url}?marketindexCd={currency_code}&page={page_num}"\n        dfs = pd.read_html(url, header=1)\n        \n        # 통화 코드가 잘못 지정됐거나 마지막 페이지의 경우 for 문을 빠져나옴\n        if dfs[0].empty:\n            if (page_num==1):\n                print(f"통화 코드({currency_code})가 잘못 지정됐습니다.")\n            else:\n                print(f"{page_num}가 마지막 페이지입니다.")\n            break\n            \n        # page별로 가져온 DataFrame 데이터 연결\n        df = pd.concat([df, dfs[0]], ignore_index=True)\n        time.sleep(0.1) # 0.1초간 멈춤\n        \n    return df\n# -----------------------------------------------------------------------------\n  \nst.title("환율 정보를 가져오는 웹 앱")\n\n# 사이드바의 폭을 조절. {width:250px;}로 지정하면 폭을 250픽셀로 지정\nst.markdown(\n    """\n    <style>\n    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width:250px;}\n    </style>\n    """, unsafe_allow_html=True\n)\n\ncurrency_name_symbols = {"미국 달러":"USD", "유럽연합 유로":"EUR",\n                         "일본 엔(100)":"JPY", "중국 위안":"CNY"}\ncurrency_name = st.sidebar.selectbox(\'통화 선택\', currency_name_symbols.keys())\n\nclicked = st.sidebar.button("환율 데이터 가져오기")\n\nif(clicked==True):\n\n    currency_symbol = currency_name_symbols[currency_name] # 환율 심볼 선택\n    currency_code = f"FX_{currency_symbol}KRW"\n\n    last_page_num = 20 # 네이버 금융에서 가져올 최대 페이지 번호 지정\n    \n    # 지정한 환율 코드를 이용해 환율 데이터 가져오기\n    df_exchange_rate = get_exchange_rate_data(currency_code, last_page_num)\n    \n    # 원하는 열만 선택\n    df_exchange_rate = df_exchange_rate[[\'날짜\', \'매매기준율\',\'사실 때\',\n                                         \'파실 때\', \'보내실 때\', \'받으실 때\']]\n    \n    # 최신 데이터와 과거 데이터의 순서를 바꿔 df_exchange_rate2에 할당\n    df_exchange_rate2 = df_exchange_rate[::-1].reset_index(drop=True)\n\n    # df_exchange_rate2의 index를 날짜 열의 데이터로 변경\n    df_exchange_rate2 = df_exchange_rate2.set_index(\'날짜\')\n\n    # df_exchange_rate2의 index를 datetime 형식으로 변환\n    df_exchange_rate2.index = pd.to_datetime(df_exchange_rate2.index,\n                                             format=\'%Y-%m-%d\')\n\n    # 1) 환율 데이터 표시\n    st.subheader(f"[{currency_name}] 환율 데이터")\n    st.dataframe(df_exchange_rate.head())  # 환율 데이터 표시(앞의 일부만 표시)\n    \n    # 2) 차트 그리기\n    # matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정\n    matplotlib.rcParams[\'font.family\'] = \'Malgun Gothic\'\n    matplotlib.rcParams[\'axes.unicode_minus\'] = False\n    \n    # 선 그래프 그리기 (df_exchange_rate2 이용)\n    ax = df_exchange_rate2[\'매매기준율\'].plot(grid=True, figsize=(15, 5))\n    ax.set_title("환율(매매기준율) 그래프", fontsize=30) # 그래프 제목을 지정\n    ax.set_xlabel("기간", fontsize=20)                   # x축 라벨을 지정\n    ax.set_ylabel(f"원화/{currency_name}", fontsize=20)  # y축 라벨을 지정\n    plt.xticks(fontsize=15)             # X축 눈금값의 폰트 크기 지정\n    plt.yticks(fontsize=15)             # Y축 눈금값의 폰트 크기 지정\n    fig = ax.get_figure()               # fig 객체 가져오기\n    st.pyplot(fig)                      # 스트림릿 웹 앱에 그래프 그리기\n    \n    # 3) 파일 다운로드\n    st.markdown("**환율 데이터 파일 다운로드**")\n    # DataFrame 데이터를 CSV 데이터(csv_data)로 변환\n    csv_data = df_exchange_rate.to_csv()\n\n    # DataFrame 데이터를 엑셀 데이터(excel_data)로 변환\n    excel_data = BytesIO() # 메모리 버퍼에 바이너리 객체 생성\n    df_exchange_rate.to_excel(excel_data) # 엑셀 형식으로 버퍼에 쓰기\n\n    columns = st.columns(2) # 2개의 세로단으로 구성\n    with columns[0]:\n        st.download_button("CSV 파일 다운로드", csv_data,\n                           file_name=\'exchange_rate_data.csv\')\n    with columns[1]:\n        st.download_button("엑셀 파일 다운로드", excel_data,\n                           file_name=\'exchange_rate_data.xlsx\')\n')


# ### 9.3.3 부동산 데이터 대시보드

# [9장: 478페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\land_info_app.py', '# 부동산 데이터를 가져오는 웹 앱\n\nimport streamlit as st\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport matplotlib\n\n# 원본 DataFrame의 제목 열에 있는 문자열을 분리해\n# 전국, 서울, 수도권의 매매가 변화율 열이 있는 DataFrame 반환하는 함수\n#----------------------------------------------------------------------------------\ndef split_title_to_rates(df_org):\n    df_new = df_org.copy()\n\n    df_temp = df_new[\'제목\'].str.replace(\'%\', \'\') # 제목 문자열에서 % 제거\n    df_temp = df_temp.str.replace(\'보합\', \'0\')    # 제목 문자열에서 보합을 0으로 바꿈\n    df_temp = df_temp.str.replace(\'보합세\', \'0\')  # 제목 문자열에서 보합세를 0으로 바꿈\n    \n    regions = [\'전국\', \'서울\', \'수도권\']\n    for region in regions:\n        df_temp = df_temp.str.replace(region, \'\') # 문자열에서 전국, 서울, 수도권 제거\n\n    df_temp = df_temp.str.split(\']\', expand=True) # ]를 기준으로 열 분리\n    df_temp = df_temp[1].str.split(\',\', expand=True) # ,를 기준으로 열 분리\n    \n    df_temp = df_temp.astype(float)\n    \n    df_new[regions] = df_temp # 전국, 서울, 수도권 순서대로 DataFrame 데이터에 할당\n\n    return df_new[[\'등록일\'] + regions + [\'번호\']] # DataFrame에서 필요한 열만 반환\n#----------------------------------------------------------------------------------\n\nst.title("부동산 정보를 가져오는 웹 앱")\n\n# 사이드바의 폭을 조절. {width:250px;} 으로 지정하면 폭을 250픽셀로 지정함\nst.markdown(\n    """\n    <style>\n    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width:250px;}\n    </style>\n    """, unsafe_allow_html=True\n)\n\n# 선택을 위한 체크박스를 생성\nchecked_1 = st.sidebar.checkbox(\'전국\')\nchecked_2 = st.sidebar.checkbox(\'서울\')\nchecked_3 = st.sidebar.checkbox(\'수도권\')\n\nclicked = st.sidebar.button("부동산 데이터 가져오기") # 버튼 생성\n      \nif(clicked==True):\n    st.subheader("아파트의 매매가 변화율 데이터")\n    \n    base_url = "https://land.naver.com/news/trendReport.naver"\n\n    df_rates = pd.DataFrame() # 전체 데이터가 담길 DataFrame 데이터\n    last_page_num = 2 # 가져올 데이터의 마지막 페이지\n\n    for page_num in range(1, last_page_num+1):\n\n        url = f"{base_url}?page={page_num}"\n        dfs = pd.read_html(url)\n\n        df_page = dfs[0] # 리스트의 첫 번째 항목에 동향 보고서 제목 데이터가 있음\n        df_rate = split_title_to_rates(df_page)\n\n        # 세로 방향으로 연결 (기존 index를 무시)\n        df_rates = pd.concat([df_rates, df_rate], ignore_index=True)\n\n    # 최신 데이터와 과거 데이터의 순서를 바꿈. index도 초기화함\n    df_rates_for_chart = df_rates[::-1].reset_index(drop=True)\n    \n    selected_regions = []\n    \n    if(checked_1==True):\n        selected_regions.append("전국")\n    if(checked_2==True):\n        selected_regions.append("서울")\n    if(checked_3==True):\n        selected_regions.append("수도권")\n\n    if(selected_regions == []):\n        st.subheader("지역을 선택하세요.")\n    else:\n        # 1) 매매가 변화율 표시. 환율 데이터를 앞의 일부만 표시\n        st.dataframe(df_rates[[\'등록일\']+selected_regions].head())\n    \n        # 2) 차트 그리기\n        # matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정\n        matplotlib.rcParams[\'font.family\'] = \'Malgun Gothic\'\n        matplotlib.rcParams[\'axes.unicode_minus\'] = False\n\n        # 선 그래프 그리기 (df_exchange_rate2 이용)\n        ax = df_rates_for_chart.plot(x=\'등록일\', y=selected_regions, figsize=(15, 6),\n                                     style = \'-o\', grid=True) # 그래프 그리기\n        \n        ax.set_title("아파트 매매가 변화율", fontsize=30) # 그래프 제목을 지정\n        ax.set_xlabel("날짜", fontsize=20)                # x축 라벨을 지정\n        ax.set_ylabel("변화율(%)", fontsize=20)           # y축 라벨을 지정\n        plt.xticks(fontsize=15)             # X축 눈금값의 폰트 크기 지정\n        plt.yticks(fontsize=15)             # Y축 눈금값의 폰트 크기 지정\n        fig = ax.get_figure()               # fig 객체 가져오기\n        st.pyplot(fig)                      # 스트림릿 웹 앱에 그래프 그리기\n')


# ### 9.3.4 구글 뉴스에서 기사 검색 

# [9장: 481페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\gnews_search_app.py', '# 구글 뉴스에서 기사를 검색하는 웹 앱\n\nfrom datetime import datetime, timedelta\nimport streamlit as st\nimport pandas as pd\nimport feedparser\n\n# RSS 피드 제공 일시를 한국 날짜와 시간으로 변경하는 함수\ndef get_local_datetime(rss_datetime):    \n    # 전체 값 중에서 날짜와 시간만 문자열로 추출 \n    date_time_str = \' \'.join(rss_datetime.split()[1:5])\n    \n    # 문자열의 각 자리에 의미를 부여해 datetime 객체로 변경 \n    date_time_GMT = datetime.strptime(date_time_str, \'%d %b %Y %H:%M:%S\') \n    \n    # GMT에 9시간을 더해 한국 시간대로 변경\n    date_time_KST = date_time_GMT + timedelta(hours=9) \n    \n    return date_time_KST # 변경된 시간대의 날짜와 시각 반환 \n#---------------------------------------------------------\n\n# 구글 뉴스 RSS 피드에서 검색 결과를 가져와 DataFrame 데이터로 반환하는 함수 \ndef get_gnews(query):\n    # RSS 서비스 주소\n    rss_url = f\'https://news.google.com/rss/search?q={query}&&hl=ko&gl=KR&ceid=KR:ko\' \n    rss_news = feedparser.parse(rss_url) # RSS 형식의 데이터를 파싱\n    \n    title = rss_news[\'feed\'][\'title\']\n    updated = rss_news[\'feed\'][\'updated\']\n    updated_KST = get_local_datetime(updated) # 한국 날짜와 시각으로 변경   \n    \n    df_gnews = pd.DataFrame(rss_news.entries) # 구글 뉴스 아이템을 판다스 DataFrame으로 변환\n\n    selected_columns = [\'title\', \'published\', \'link\'] # 관심있는 열만 선택\n    df_gnews2 = df_gnews[selected_columns].copy()     # 선택한 열만 다른 DataFrame으로 복사\n\n    # published 열의 작성 일시를 한국 시간대로 변경\n    df_gnews2[\'published\'] = df_gnews2[\'published\'].apply(get_local_datetime) \n\n    df_gnews2.columns = [\'제목\', \'제공 일시\', \'링크\'] # 열 이름 변경\n    \n    return title, updated_KST, df_gnews2\n#---------------------------------------------------------\n\n# 구글 뉴스 검색 결과를 Table로 정리한 HTML 코드를 반환하는 함수\ndef create_gnews_html_code(title, updated_KST, df):\n    # DataFrame 데이터를 HTML 코드로 변환 (justify=\'center\' 옵션을 이용해 열 제목을 중간에 배치)\n    html_table = df.to_html(justify=\'center\', escape=False, render_links=True) \n\n    # HTML 기본 구조를 갖는 HTML 코드\n    html_code = \'\'\'\n    <!DOCTYPE html>\n    <html>\n      <head>\n        <title>구글 뉴스 검색</title>\n      </head>\n      <body>\n        <h1>{0}</h1>\n        <h3> *검색 날짜 및 시각: {1}</h3>\n        {2}\n      </body>\n    </html>    \n    \'\'\'.format(title, updated_KST, html_table)\n    \n    return html_code\n# -----------------------------------\n\nst.title("구글 뉴스 기사를 검색하는 웹 앱")\n\nquery = st.text_input(\'검색어 입력\', value="메타버스")\n\n# 구글 뉴스 검색 결과 가져오기\n[title_gnews, updated_KST_gnews, df_gnews] = get_gnews(query)\n\n# 웹 앱에 표시할 HTML 테이블 생성 (DataFrame 데이터 중 처음 일부만 HTML 테이블로 생성)\nhtml_table = df_gnews.head().to_html(justify=\'center\', escape=False, render_links=True)\n\n# HTML 파일 다운로드를 위한 HTML code 생성\ngnews_html_code = create_gnews_html_code(title_gnews, updated_KST_gnews, df_gnews)\n\nst.markdown("**기사 검색 결과**")\nst.write(html_table, unsafe_allow_html=True) # HTML 테이블 표시\nst.markdown("") # 빈 줄 생성\n\ncolumns = st.columns(3) # 3개의 세로단으로 구성 (2개의 세로단에만 필요한 내용 표시)\nwith columns[0]:        \n    st.markdown("**HTML 파일 다운로드**")\nwith columns[1]:\n    st.download_button("다운로드", gnews_html_code, file_name=\'gnews_search_results.html\')\n')


# ### 9.3.5 멀티페이지 웹 앱

# [9장: 487페이지]

# In[ ]:


get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\code\\ch09\\my_app\\Multipage_Home.py', '# 멀티페이지 웹 앱\n\nimport streamlit as st\n\nst.title("경제 정보를 가져오는 웹 앱")\n\nst.subheader("사이드바에서 페이지를 선택하세요.")\nst.subheader("- Multipage Home: 경제 정보 홈 페이지")\nst.subheader("- Stock Info: 주식 정보 페이지")\nst.subheader("- Exchange Rate: 환율 정보 페이지")\nst.subheader("- Land Info: 부동산 정보 페이지")\n\n# 사이드바의 폭을 조절. {width:250px;} 으로 지정하면 폭을 250픽셀로 지정함\nst.markdown(\n    """\n    <style>\n    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width:250px;}\n    </style>\n    """, unsafe_allow_html=True\n)\n')


# ### 9.3.6 스트림릿 클라우드에 웹 앱 배포

# ## 9.4 정리
