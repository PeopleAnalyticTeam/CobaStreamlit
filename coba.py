import pickle
import streamlit as st
st.title('coba hitung luas persegi panjang')

panjang = st.number_input("input panjang",0)
lebar = st.number_input(" input lebar",0)
hitung = st.button("Hitung Luas")

if hitung :
    luas = panjang * lebar
    st.write ("Luas Persegi Panjang Adalah= ", luas)
    st.success (f"Luas Persegi Panjang Adalah = {luas}")
