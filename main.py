import streamlit as st
st.write("Time series forecasting demo")

st.title('Time series forecasting demo')
st.markdown('Using differentiation and LSTM to predict time series')

model = st.selectbox('Chose feature engineering', ('include moving features', 'time series only'))

_num_hidden_layers = 50
_dropout_rate = 3
_num_epochs = 20

col1, col2, col3 = st.columns(3)
_num_hidden_layers = col1.number_input("num_hidden_layers", value=_num_hidden_layers)
_dropout_rate = col2.number_input("dropout_rate", value=_dropout_rate)
_num_epochs = col3.number_input("num_epochs", value=_num_epochs)