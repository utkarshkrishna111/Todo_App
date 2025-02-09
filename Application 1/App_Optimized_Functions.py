from function_call import get_todos, write_todos
import time

today_time = time.strftime("%d-%m-%Y %H:%M:%S")
print(f"It is", today_time)

while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith('Add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('Show'):

        todos = get_todos()

        new_todos = []
        for i in todos:
            new_todo = i.strip('\n')
            new_todos.append(new_todo)

        for index, item in enumerate(new_todos):
            print(f"{index + 1}:{item.capitalize()}")

    elif user_action.startswith('Edit'):
        try:
            i = int(user_action[5:])
            todos = get_todos()

            i=i-1
            todo_edited = todos[i].strip('\n')
            todos[i] = input("Enter New Todo: ") + "\n"

            write_todos(todos)

            print(f"Existing Todo: {todo_edited} \nReplaced with: {todos[i]}")
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('Complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)

            message = f"ToDo {todo_to_remove} was removed from the list. "
            print(message)
        except IndexError:
            print("There is no item with that number.\n")
            continue
        except ValueError:
            print("Please enter the Todo to mark as complete in format: Complete 10")

    elif user_action.startswith('Exit'):
        break
    else:
        print("You have entered unknown command")
print('Bye')



