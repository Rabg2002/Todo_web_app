import streamlit as str
import functions

todos = functions.get_todo("todo.txt")
def add_todo():
    todo = str.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todo(todos, "todo.txt")

    
str.title("My Todo Web App")
str.subheader("This is my Todo App")
str.write("This is to increase your productivity")

for index , todo in enumerate(todos):
    checkbox = str.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos, "todo.txt")
        del str.session_state[todo]
        str.rerun()
        
str.text_input(label="", placeholder="Enter new Todo..",
                on_change=add_todo, key='new_todo')

str.session_state