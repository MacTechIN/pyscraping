#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:55:21 2023

@author: sam
"""

import pandas as pd
#UTF-8 인코딩 환율 = "%ED%99%98%EC%9C%A8"

u#rl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=환율'


url_finish = urlx.encode('utf-8')

print(url_finish)


# url에서 표 데이터를 추출해 DataFrame 데이터의 리스트로 반환
dfs = pd.read_html(url)

print('dfs', type(dfs), dfs)

#%%
#Hesh code 
won = "ED9998EC9CA8"
print(hex('0xED9998EC9CA8'))

#%%
print(len(dfs))


#%%

won = u"환율"
won_list  = ["0x{:02x}".format(ord(x)) for x in won]

# won_list2 = [x.encode("utf-8").encode("hex") for x in won)
# print(won_list2) 

u8_won = won.encode("utf-8")
print(u8_won) # b'\xed\x99\x98\xec\x9c\xa8'

for x in u8_won:
	print(f"0x{x:02x}", end = ' ') # 0xed 0x99 0x98 0xec 0x9c 0xa8 