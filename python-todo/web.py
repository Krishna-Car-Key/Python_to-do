import streamlit as st
from modules import functions

todos = functions.return_todos()

st.title("My Todo App.")

st.text("This app is for increasing your Productivity.")


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


def remove_todo():
    todo_to_remove = st.session_state["to_remove"]
    todos.remove(todo_to_remove)
    functions.write_todos(todos)


for index, todo in enumerate(todos):
    st.checkbox(todo, key=todo)
#     if True:
#         todos.remove(todo)
#         functions.write_todos(todos)

# var = st.button(label= "Hello")
# var2 = st.button(label="Hero")
# st.sidebar(var, var2)
st.text_input(label='', placeholder="Add a todo...",
              key="new_todo", on_change=add_todo)
