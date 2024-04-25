import streamlit as st
from modules import functions

todos = functions.return_todos()

st.title("My Todo App.")

st.text("This app is for increasing your Productivity.")


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.text_input(label='', placeholder="Add a todo...",
              key="new_todo", on_change=add_todo)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# var = st.button(label= "Hello")
# var2 = st.button(label="Hero")
# st.sidebar(var, var2)

st.session_state