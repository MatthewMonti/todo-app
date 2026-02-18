exit = False

TO_DO_LIST = []

def get_argument(command):
    command_name, argument = command.split(" ", maxsplit=1)
    return argument 


def handle_add_command(command):
    argument = get_argument(command)
    TO_DO_LIST.append(argument)
    
    print(f"Updated List:")
    handle_list_command()

def handle_delete_command(command):
    argument = get_argument(command)
    TO_DO_LIST.pop(int(argument) -1)
    
    print(f"Updated List:")
    handle_list_command()

def handle_list_command():
    for index, item in enumerate(TO_DO_LIST):
        print(f"{index+1}: {item}")

def handle_save_command(command):
    filename = get_argument(command)
    filename += ".todo.txt"
    with open(filename, 'w') as f:
        for i in TO_DO_LIST:
            f.write(f'{i}\n')

def handle_open_command(command):
    # Read a list of todo items from a file
    filename = get_argument(command)
    filename += ".todo.txt"

    with open(filename, "r") as f:
        for line in f:
            TO_DO_LIST.append(line.strip())

while not exit:
    command = input("Enter command: ")

    if command.startswith("exit"):
        exit = True
    elif command.startswith("add"):
        handle_add_command(command)
    elif command.startswith("delete"):
        handle_delete_command(command)
        # NOTE: 
        # User input is always a string, so the delete command receives the index as a # numeric string (e.g., "3"). We convert that numeric string to an integer using # int(argument) so we can delete the correct item by its index. 
        # This matters because list values can repeat (e.g., two "walk" tasks), but 
        # indexes are unique. Deleting by index ensures we remove the exact item the # user intended, not just the first or last matching value.
    elif command.startswith("list"):
        handle_list_command()
    elif command.startswith("save"):
        handle_save_command(command)
    elif command.startswith("open"):
        handle_open_command(command)
    else:
        print("Command not recognized")
