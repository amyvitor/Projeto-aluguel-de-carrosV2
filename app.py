import pandas as pd 
import streamlit as st 

#python -m streamlit run app.py

#------------------------------------------------Sidebar
st.sidebar.image("logo.png")
st.sidebar.title("CarXANA")

carros = ['Rolls-Royce','Bentley','Porsche', 'Aston Martin', 'Toro']

opcao = st.sidebar.selectbox("Escolha o carro que foi alugado", carros)

#-------------------------------------------------Principal
st.title('CarXana - Aluguel de Carros' )


st.image(f'{opcao}.png')
st.markdown(f'## Você Alugou o Modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

###Copia aqui agora

if opcao == 'Rolls-Royce':
        diaria = 1012
elif opcao == 'Bentley':
        diaria = 450
elif opcao == 'Porsche':
        diaria = 390
elif opcao == 'Aston Martin':
        diaria = 600
elif opcao == 'Toro':
        diaria = 666
        
        
if st.button('calcular'):
        dias = int(dias)
        km = float(km)

        total_dias = dias * diaria
        total_km = km * 0.15
        aluguel_total = total_dias+total_km

        st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km . O valor total a pagar é R${aluguel_total:.2f}')