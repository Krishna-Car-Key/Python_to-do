import streamlit as st
from modules import functions

todos = functions.return_todos()
st.title("My Todo App.")

st.text("This app is for increasing your Productivity.")

for todo in todos:
    st.checkbox(todo)

# var = st.button(label= "Hello")
# var2 = st.button(label="Hero")
# st.sidebar(var, var2)
st.text_input(label='', placeholder="Add a todo...")

