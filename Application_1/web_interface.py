import streamlit as st
import function_call

todos = function_call.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    function_call.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity")

st.checkbox("buy_grocery")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder= "Enter a Todo...",
              on_change=add_todo, key= 'new_todo')
