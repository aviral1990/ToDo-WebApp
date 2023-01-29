import streamlit as st
from Modules import functions



completed_todo_list=functions.read_txt_file('completed.txt')

st.title("Completed ToDos List")
if(len(completed_todo_list)==0):
    st.write("Completed ToDos is Empty!!")
else:
    for item in completed_todo_list:
        st.write("--> "+item)

    button=st.button("Delete all")
    if(button):     #If Button Pressed
        completed_todo_list.clear()
        functions.write_txt(completed_todo_list,'completed.txt')
        st.experimental_rerun()  # rerun the webpage script

