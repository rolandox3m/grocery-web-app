FILEPATH = 'todo_list.txt'


def get_todos(filepath=FILEPATH):
    """ Opens and reads files to set a list """
    with open(filepath, 'r') as file_local:
        to_dos_local = file_local.readlines()
    return to_dos_local


def write_todos(my_list, filepath=FILEPATH):
    with open(filepath, 'w') as file:
       file.writelines(my_list)

if __name__ == '__main__':
    print('Hello from functions')