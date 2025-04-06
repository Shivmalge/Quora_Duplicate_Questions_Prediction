import streamlit as st
import helper
import pickle
import gzip

with gzip.open('model.pkl.gz', 'rb') as f:
    model = pickle.load(f)

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter Question 1: ')
q2 = st.text_input('Enter Question 2: ')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)

    if(result):
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
