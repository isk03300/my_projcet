
import streamlit as st
import pandas as pd

df = pd.read_csv('./data/dev.csv')
df = df.drop( [ '법정동코드','자치구코드' ,'지번구분' ,'권리구분','취소일'] , axis=1)
df = df.fillna('NoData')
df['계약일'] = pd.to_datetime(df['계약일'].astype(str))
df['접수연도'] = df['접수연도'].astype(str)

menu = ['오피스텔','아파트','다세대연립','다가구주택']

def run_app_trade() :

    

    st.header('2023년도 서울특별시 부동산 실거래가')

    if st.checkbox('전체 실거래 보기') :
        st.dataframe(df)
       
        st.text('출처 : https://data.seoul.go.kr/dataList/OA-21275/S/1/datasetView.do')
    st.text(' ')
    st.text(' ')

        

    choice = st.selectbox('건물의 종류를 선택하시오',menu)

    if choice == menu[0] :
         #st.text('sdsd')
         st.dataframe(df.loc[ df['건물용도'] =='오피스텔' , ].set_index('건물용도'))
         
    
    elif choice == menu[1]:

        st.dataframe(df.loc[ df['건물용도'] =='아파트' , ].set_index('건물용도'))
     
    elif choice == menu[2]:

        st.dataframe(df.loc[ df['건물용도'] =='연립다세대' , ].set_index('건물용도'))

    elif choice == menu[3]:

        st.dataframe(df.loc[ df['건물용도'] =='단독다가구' , ].set_index('건물용도'))

    