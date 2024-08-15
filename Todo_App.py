import functions
import FreeSimpleGUI as gui 
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", 'w') as file:
        pass

#file= 'Projects/Todo_project/todo.txt'
a = "todo.txt"
clock = gui.Text('', key = 'clock')
label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todo(a), key ='todos', 
                        enable_events=False , size=[45, 10])
edit_button = gui.Button("Edit")
comp_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window= gui.Window('My To-Do App', 
                    layout=[[clock], 
                            [label], 
                            [input_box, add_button], 
                            [list_box, edit_button, comp_button],
                            [exit_button]], 
                            font = ('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todo(a) 
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todo( todos, a)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todo(a)  
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos, a)
                window['todos'].update(values=todos)
            except IndexError:
                print("Index Error Found!")
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todo(a)
            todos.remove(todo_to_complete)
            functions.write_todo(todos,a)
            window['todos'].update(values= todos)
            window['todo'].update(value='')
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'])
        case gui.WIN_CLOSED:
            break
window.close()