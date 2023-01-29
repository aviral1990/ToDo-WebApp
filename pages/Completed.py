import streamlit as st
from Modules import functions



completed_todo_list=functions.read_txt_file('completed.txt')

for item in completed_todo_list:
    st.write(item)