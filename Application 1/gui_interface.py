import function_call
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-do")
input_box =sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label, add_button], [input_box]])
window.read()
window.close()
