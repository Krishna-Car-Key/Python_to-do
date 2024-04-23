import PySimpleGUI as sg
from modules import functions

user_input_title = sg.Text("To-Do Box ")
user_input_box = sg.Input(tooltip="Enter todo", key='todo')
add_box = sg.Button("add")

window = sg.Window('My To-Do Lists',
                   layout=[[user_input_title], [user_input_box, add_box]],
                   font=('Helvetica', 16))

while True:
   event,value = window.read()
   print(event,value)
   match event:
       case 'add':
           todos = functions.return_todos()

           new_todo = value['todo'].title() + '\n'
           todos.append(new_todo)

           functions.write_todos(todos)

       case sg.WIN_CLOSED:
           break


window.close()
