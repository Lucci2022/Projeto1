import pandas as pd 
import streamlit as st 
import numpy as np 
import altair as alt 

st.write("Iron Maiden")


df = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a','b','c'])

c = alt.Chart(df).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a','b','c'])

st.write(df)
st.write(c)


"Cria um texto na tela"

st.title('Iron Maiden')
st.header('Melhor banda')
