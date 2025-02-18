def get_todos(filepath = r"C:\Users\utkar\PycharmProjects\PythonProject1\Application_1\todo.txt"):
    """ Read a text file and return a list of
    to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = r"C:\Users\utkar\PycharmProjects\PythonProject1\Application_1\todo.txt"):
    """ Write the To-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")