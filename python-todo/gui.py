import PySimpleGUI as sg
from modules import functions

user_input_title = sg.Text("To-Do Box ")
user_input_box = sg.Input(tooltip="Enter todo", key='todo')
add_box = sg.Button("Add")

# in Listbox we can use the value to store the list-
# -like Listbox(value=functions.return_todos())
# however i am not applying this because my function is running normally

list_box = sg.Listbox(functions.return_todos(),
                      enable_events=True,
                      size=(45, 10), key='todos')
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

layout = [[user_input_title], [user_input_box, add_box], [list_box, edit_button,complete_button]]

window = sg.Window('My To-Do Lists',
                   layout=layout,
                   font=('Helvetica', 16))

while True:
    event, value = window.read()
    print(event, value)
    match event:
        case 'Add':
            todos = functions.return_todos()

            new_todo = value['todo'].title() + '\n'
            todos.append(new_todo)

            functions.write_todos(todos)
            window['todos'].update(todos)
        case 'Edit':
            print(value['todos'])
            todos = functions.return_todos()
            index = todos.index(value['todos'][0])
            todos[index] = value['todo'] + '\n'
            functions.write_todos(todos)
            window['todos'].update(todos)
        case 'Complete':
            todo_to_complete = value['todos'][0]
            todos = functions.return_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(todos)
            window['todo'].update('')

        case 'todos':
            value['todo'] = value['todos'][0]
            print(value['todo'])
            window['todo'].update(value['todo'])

        case sg.WIN_CLOSED:
            break

window.close()
