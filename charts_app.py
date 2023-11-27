
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import platform
import seaborn as sb



# import platform
# from matplotlib import font_manager, rc
# plt.rcParams['axes.unicode_minus'] = False
# if platform.system() == 'Linux':
#     rc('font', family='NanumGothic')

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

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




def run_app_charts() :


    st.title('차트를 통한 전체적인 분석')

    st.title('')
    st.title('')
    st.title('')

    fig = plt.figure()
    df_total = df.groupby('건물용도')['물건금액(만원)'].max()
    plt.pie(df_total, labels=df_total.index, autopct='%.2f' , startangle= 90 ,wedgeprops={'width' : 0.7} )
    plt.title('서울시 건물용도별 거래 비율')
    
    st.pyplot(fig)
    df_count = df['건물용도'].value_counts().to_frame()
    df_count = df_count.rename(columns={ 'count' : '건 수'})
    st.write(df_count)