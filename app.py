import streamlit as st
import pandas as pd 


from funcoes import filtro,grafico

st.write('Titulo do meu site')
arquivo = st.file_uploader('Coloque um csv')

if arquivo:
    df = pd.read_csv(arquivo)

    if st.checkbox('Ver filtro'):
       filtro(df)
  
    if st.checkbox('Ver gráfico'):
        grafico(df)
else:
    st.write('Coloque o arquivo!')