import streamlit as st
import pandas as pd
from charts_app import run_app_charts
from home_app import run_app_home
from trade_app import run_app_trade




def main() :

    df = pd.read_csv('./data/dev.csv')
    df = df.drop( [ '법정동코드','자치구코드' ,'지번구분' ,'권리구분','취소일'] , axis=1)
    df = df.fillna('NoData')
    df['계약일'] = pd.to_datetime(df['계약일'].astype(str))
    df['접수연도'] = df['접수연도'].astype(str)
    print(df['계약일'])
    

    menu = ['Home','실거래가','차트/그래프 분석']
    
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == menu[0] :

        run_app_home()

    
    if choice == menu[1] :

        run_app_trade()


    if choice == menu[2] :

        run_app_charts()







if __name__ == '__main__' :
    main()
