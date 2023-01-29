import streamlit as st
from Modules import functions
#Hellooooooooooooooooooooo
#read Todos from text file
todos=functions.read_txt_file()
todos_len=len(todos)
completed_todos=functions.read_txt_file('completed.txt')
def add_todo():
    new_todo=st.session_state["new_todo"]+'\n'
    todos.append(new_todo)
    functions.write_txt(todos)
    st.session_state["new_todo"]=""     #Update Text box to Blank

st.title("My To-Do App")
st.write("Add, Modify or mark To-Dos complete")
if(todos_len==0):
    st.write("<b>No More ToDos!!</b>",unsafe_allow_html=True)

st.text_input(label="",placeholder="Add a To-Do",on_change=add_todo,key="new_todo")

i=0
for item in todos:
    checkbox=st.checkbox(item,key=item)
    if(checkbox):
        deleted_item=todos.pop(i)
        completed_todos.append(deleted_item)
        functions.write_txt(todos)  #Update Todos.txt
        functions.write_txt(completed_todos,'completed.txt')
        del st.session_state[item]  #delete checkbox
        st.experimental_rerun()     #rerun the webpage script
    i=i+1




#To Print the session for debugging
#st.session_state