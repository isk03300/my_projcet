
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import platform
import seaborn as sb



import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


df = pd.read_csv('./data/dev.csv')
df = df.drop( [ '법정동코드','자치구코드' ,'지번구분' ,'권리구분','취소일'] , axis=1)
# df = df.fillna('NoData')
df['계약일'] = pd.to_datetime(df['계약일'].astype(str))
df['접수연도'] = df['접수연도'].astype(str)

menu = ['용도 선택','오피스텔','아파트','연립다세대','단독다가구']

def run_app_trade() :

    

    st.header('2023년도 서울특별시 부동산 실거래가')

    if st.checkbox('전체 실거래 보기') :
        st.warning('출처 : https://data.seoul.go.kr/dataList/OA-21275/S/1/datasetView.do')
        st.text('*기준은 계약일이 아닌 접수연도를 기준으로 한다*')
        st.dataframe(df)
        
        
        st.text(' ')
        st.text(' ')
        st.text(' ')
        st.text(' ')
        
        fig = plt.figure()
        color_set = sb.color_palette()[9]
        order_set = df['자치구명'].value_counts().index
        sb.countplot(data = df , y ='자치구명',color=color_set,order=order_set)
        plt.title('서울시 전체 실거래 건 수')
        plt.xlabel('거래 건 수')
        st.pyplot(fig)

        st.text(' ')
        st.text(' ')
        st.text(' ')
        st.text(' ')

        fig2 = plt.figure()
        df2 = df.loc[df['건물명'].notna() , ]
        df2 = df2['건물명'].value_counts().head()
        df2_amounts = df2.to_frame().rename(columns={'count' : '건 수'})
        plt.pie(df2 , labels=df2.index, autopct='%.2f',wedgeprops={'width':0.7})
        plt.title('서울시 전체 실거래량 Top5 건물 ')
        st.pyplot(fig2)
        st.dataframe(df2_amounts)
        print(df2)


        
        
        st.text('')
    
    st.text(' ')
    st.text(' ')

        

    choice = st.selectbox('건물의 용도를 선택하시오', menu )


    if choice == menu[1] :
         df_apt = df.loc[ df['건물용도'] =='오피스텔' ,].set_index('건물용도')

         st.dataframe(df_apt) 
        

         st.text(' ')
         st.text(' ')
         st.text(' ')
         st.text(' ')
        
         apt_order = df_apt['자치구명'].value_counts().index
         apt_color = sb.color_palette()[0]
         
         fig = plt.figure()

         sb.countplot( data = df_apt , y = df_apt['자치구명'] , color=apt_color ,order=apt_order )
         plt.title('자치구별 오피스텔 거래 건 수')
         plt.xlabel('거래 건 수( 단위 : 회 )')
         st.pyplot(fig)

         st.text(' ')
         st.text(' ')
         st.text(' ')
         st.text(' ')
         
         fig2 = plt.figure()
         df_apt_pie = df_apt['건물명'].value_counts().head()
         plt.pie(df_apt_pie ,labels= df_apt_pie.index, autopct='%.2f' , wedgeprops={'width' : 0.8} )
         plt.title('서울시 자치구 오피스텔 거래량 Top5') 
         st.pyplot(fig2)

         df_apt_amounts = df_apt['건물명'].value_counts().to_frame().head()
         df_apt_amounts = df_apt_amounts.rename(columns={'count' : '건 수'})
         st.write(df_apt_amounts)

        


    
    elif choice == menu[2]:

         df_apt = df.loc[ df['건물용도'] =='아파트' ,].set_index('건물용도')

         st.dataframe(df_apt) 
        
         apt_order = df_apt['자치구명'].value_counts().index
         apt_color = sb.color_palette()[1]
         
         fig = plt.figure()

         sb.countplot( data = df_apt , y = df_apt['자치구명'] , color=apt_color ,order=apt_order )
         plt.title('자치구별 아파트 거래 건 수')
         plt.xlabel('거래 건 수( 단위 : 회 )')
         st.pyplot(fig)
         
         fig2 = plt.figure()
         df_apt_pie = df_apt['건물명'].value_counts().head()
         plt.pie(df_apt_pie ,labels= df_apt_pie.index, autopct='%.2f' , wedgeprops={'width' : 0.8} )
         plt.title('서울시 자치구 아파트 거래량 Top5')
         st.pyplot(fig2)
         df_apt_amounts = df_apt['건물명'].value_counts().to_frame().head()
         df_apt_amounts = df_apt_amounts.rename(columns={'count' : '건 수'})
         st.write(df_apt_amounts)


    elif choice == menu[3]:

         df_apt = df.loc[ df['건물용도'] =='연립다세대' ,].set_index('건물용도')

         st.dataframe(df_apt) 
        
         apt_order = df_apt['자치구명'].value_counts().index
         apt_color = sb.color_palette()[2]
         
         fig = plt.figure()

         sb.countplot( data = df_apt , y = df_apt['자치구명'] , color=apt_color ,order=apt_order )
         plt.title('자치구별 연립다세대 거래 건 수')
         plt.xlabel('거래 건 수( 단위 : 회 )')
         st.pyplot(fig)
         
         fig2 = plt.figure()
         df_apt_pie = df_apt['건물명'].value_counts().head()
         plt.pie(df_apt_pie ,labels= df_apt_pie.index, autopct='%.2f' , wedgeprops={'width' : 0.8} )
         plt.title('서울시 자치구 연립다세대 거래량 Top5')
        
         st.pyplot(fig2)

         df_apt_amounts = df_apt['건물명'].value_counts().to_frame().head()
         df_apt_amounts = df_apt_amounts.rename(columns={'count' : '건 수'})
         st.write(df_apt_amounts)

    elif choice == menu[4]:

         df_apt = df.loc[ df['건물용도'] =='단독다가구' ,].set_index('건물용도')

         st.dataframe(df_apt) 
        
         apt_order = df_apt['자치구명'].value_counts().index
         apt_color = sb.color_palette()[3]
         
         fig = plt.figure()

         sb.countplot( data = df_apt , y = df_apt['자치구명'] , color=apt_color ,order=apt_order )
         plt.title('자치구별 단독다가구 거래 건 수')
         plt.xlabel('거래 건 수( 단위 : 회 )')
         st.pyplot(fig)
         
         fig2 = plt.figure()
         df_apt_pie = df_apt['법정동명'].value_counts().head()
         plt.pie(df_apt_pie ,labels= df_apt_pie.index, autopct='%.2f' , wedgeprops={'width' : 0.8} )
         plt.title('서울시 자치구 단독다가구 거래량 Top5')
        
         st.pyplot(fig2)

         st.info('단독다가구는 상세 주소가 없는 관계로 법정동명으로 집계 하였습니다.')
         
         df_apt_amounts = df_apt['법정동명'].value_counts().to_frame().head()
         df_apt_amounts = df_apt_amounts.rename(columns={'count' : '건 수'})
         st.write(df_apt_amounts)
    