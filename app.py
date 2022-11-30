import streamlit as st

st.title("Greater of Three Numbers:")

a=st.number_input("Enter First Number:")

b=st.number_input("Enter Second Number:")

c=st.number_input("Enter Third Number:")

if (a>b) and (a>c):

  st.write("1st is greater")

elif (b>a) and (b>c):

  st.write("2nd is greater")

else:

  st.write("3rd is greater")
