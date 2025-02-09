import function_call
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-do")
input_box =sg.InputText(tooltip="Enter Todo", key = "todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label, add_button], [input_box]],
                   font=('Helvetica', 10))
while True:
     event, values = window.read()
     print(event)
     print(values)
     match event:
         case "Add":
             todos = function_call.get_todos()
             new_todo = values['todo'] + "\n"
             todos.append(new_todo)
             function_call.write_todos(todos)
         case sg.WIN_CLOSED:
             break

window.close()


