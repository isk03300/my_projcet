
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import platform
import seaborn as sb
import numpy as np

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')

elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')




df = pd.read_csv('./data/dev.csv')
df = df.drop( [ '법정동코드','자치구코드' ,'지번구분' ,'권리구분','취소일'] , axis=1)
df = df.fillna('NoData')
df['계약일'] = pd.to_datetime(df['계약일'].astype(str))
df['접수연도'] = df['접수연도'].astype(str)
df2 = pd.read_csv('./data/dev2.csv') 

menu = ['오피스텔','아파트','연립다세대','단독다가구','종합']
 

def run_app_charts() :


    st.title('차트를 통한 전체적인 분석')

    st.title('')
    st.title('')
    st.title('')


 
    fig2 = px.line(df2,x='거래일자',y='거래량',title='2023년 서울시 부동산 실거래 변동(월별)')
    fig2.update_xaxes(dtick='M1')
    fig2.update_layout(title={'text': '2023년 서울시 부동산 실거래 변동(월별)', 'font': {'size': 40}}, width=800, height=600)
    st.plotly_chart(fig2)
  

    st.title('')
    st.title('')
    st.title('')
    st.title('')
    st.title('')
    st.title('')

    fig = plt.figure()
    df_total = df['건물용도'].value_counts()
    plt.pie(df_total, labels=df_total.index, autopct='%.2f' , startangle= 90 ,wedgeprops={'width' : 0.7} )
    plt.title('서울시 건물용도별 거래 비율') 
    st.pyplot(fig)

    df_count = df['건물용도'].value_counts().to_frame()
    df_count = df_count.rename(columns={ 'count' : '건 수'})
    df_max_price = df.groupby('건물용도')['물건금액(만원)'].agg([np.max , np.min])
    df_max_price = df_max_price.rename(columns={'max' : '최고가(만원)' , 'min' : '최저가(만원)'})
    df_sum_dataframe = pd.concat([df_count,df_max_price],axis = 1)
    st.write(df_sum_dataframe)

    


