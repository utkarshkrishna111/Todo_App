import streamlit as st
import function_call

todos = function_call.get_todos()

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity")

st.checkbox("buy_grocery")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder= "Enter a Todo...")