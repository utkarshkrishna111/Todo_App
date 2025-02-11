import function_call
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", 'w') as file:
        pass

sg.theme("Black")

clock = sg.Text('',key="clock")
label = sg.Text("Type in a To-do")
input_box =sg.InputText(tooltip="Enter Todo", key = "todo")
add_button = sg.Button("Add")
"""add_button = sg.Button(size=2, image_source= "add.png",
                       mouseover_colors="LightBlue2", tooltip="Add todo",
                       key="Add")"""
list_box = sg.Listbox(values=function_call.get_todos(), key='todo_list',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout_1 = layout=[[clock],
                   [label],
                   [input_box, add_button],
                   [list_box, edit_button, complete_button],
                   [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout_1,
                   font=('Helvetica', 15))
while True:
     event, values = window.read(timeout=200)
     window["clock"].update(value=time.strftime("%d-%m-%Y %H:%M:%S"))
     match event:
         case "Add":
             todos = function_call.get_todos()
             new_todo = values['todo'] + "\n"
             todos.append(new_todo)
             function_call.write_todos(todos)
             window['todo_list'].update(values=todos)
         case "Edit":
             try:
                 todo_to_edit = values['todo_list'][0]
                 new_todo = values['todo']
                 todos = function_call.get_todos()
                 index = todos.index(todo_to_edit)
                 todos[index] = new_todo + "\n"
                 function_call.write_todos(todos)
                 window['todo_list'].update(values=todos)
             except IndexError:
                 sg.popup('Please select an item first',font=("Helvetica", 20))
         case "Complete":
              try:
                 todo_to_complete = values['todo_list'][0]
                 todos = function_call.get_todos()
                 todos.remove(todo_to_complete)
                 function_call.write_todos(todos)
                 window['todo_list'].update(values=todos)
                 window['todo'].update(value='')
              except IndexError:
                  sg.popup('Please select an item first', font=("Helvetica", 20))
         case "Exit":
             break
         case 'todo_list':
             window['todo'].update(value=values['todo_list'][0])
         case sg.WIN_CLOSED:
             break

window.close()


