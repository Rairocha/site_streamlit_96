import streamlit as st
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
def filtro(df):
    coluna = st.selectbox('Qual é a coluna do filtro?'
                        ,df.columns)
    if df.dtypes[coluna]=='object':
        valor = st.multiselect('Qual é o valor do filtro?'
                        ,df[coluna].unique())
        st.write(df.loc[df[coluna].isin(valor)])
    else:
        valor1 = st.number_input("escolha o valor minimo",
                                df[coluna].min(),df[coluna].max())
        valor2 = st.number_input("escolha o valor maximo",
                                df[coluna].min(),df[coluna].max())
        st.write(df[df[coluna].between(valor1,valor2)])

def grafico(df):
    categorica=st.selectbox('Qual é a coluna categorica?'
                        ,df.select_dtypes('object').columns)
    numerica= st.selectbox('Qual é a coluna number?'
                        ,df.select_dtypes('number').columns)
    fig,ax = plt.subplots(1,1)
    sns.barplot(data=df,x=categorica,y=numerica)
    st.pyplot(fig)