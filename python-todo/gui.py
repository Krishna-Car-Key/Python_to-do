import PySimpleGUI as sg
from modules import functions

user_input_title = sg.Text("To-Do Box ")
user_input_box = sg.Input(tooltip="Enter todo", key='todo')
add_box = sg.Button("add")
list_box = sg.Listbox(functions.return_todos(),
                      enable_events=True,
                      size=(45, 10), key='todos')
edit_button = sg.Button("edit")

window = sg.Window('My To-Do Lists',
                   layout=[[user_input_title], [user_input_box, add_box], [list_box, edit_button]],
                   font=('Helvetica', 16))

while True:
    event, value = window.read()
    print(event, value)
    match event:
        case 'add':
            todos = functions.return_todos()

            new_todo = value['todo'].title() + '\n'
            todos.append(new_todo)

            functions.write_todos(todos)
            window['todos'].update(todos)
        case 'edit':
            print(value['todos'])
            todos = functions.return_todos()
            index = todos.index(value['todos'][0])
            todos[index] = value['todo'] + '\n'
            functions.write_todos(todos)
            window['todos'].update(todos)
        case 'todos':
            value['todo'] = value['todos'][0]
            print(value['todo'])
            window['todo'].update(value['todo'])

        case sg.WIN_CLOSED:
            break

window.close()
