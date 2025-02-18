"""To run the script on local streamlit run <.py> directly on command line
Title function return a title instance
A callback function is a custom function
st.session_state: gives values of """

import streamlit as st
import function_call

todos = function_call.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function_call.write_todos(todos)

st.title("My Todo App")

st.subheader("This is my Todo App")

st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function_call.write_todos(todos)
        del  st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder= "Enter a Todo...",
              on_change=add_todo, key= 'new_todo')



