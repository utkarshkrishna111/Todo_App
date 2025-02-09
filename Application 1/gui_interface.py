import function_call
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-do")
input_box =sg.InputText(tooltip="Enter Todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function_call.get_todos(), key='todo_list',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15))
while True:
     event, values = window.read()
     print(event)
     print(values)
     print(values['todo_list'][0])
     match event:
         case "Add":
             todos = function_call.get_todos()
             new_todo = values['todo'] + "\n"
             todos.append(new_todo)
             function_call.write_todos(todos)
             window['todo_list'].update(values=todos)
         case "Edit":
             todo_to_edit = values['todo_list'][0]
             new_todo = values['todo']

             todos = function_call.get_todos()
             index = todos.index(todo_to_edit)
             todos[index] = new_todo + "\n"
             function_call.write_todos(todos)
             window['todo_list'].update(values=todos)
         case 'todo_list':
             window['todo'].update(value=values['todo_list'][0])
         case sg.WIN_CLOSED:
             break

window.close()


