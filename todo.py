exit = False

TO_DO_LIST = []

def get_argument(command):
    command_name, argument = command.split(" ", maxsplit=1)
    return argument 


def handle_add_command(command):
    argument = get_argument(command)
    TO_DO_LIST.append(argument)
    print(f"Adding task: {argument}")

def handle_delete_command(command):
    argument = get_argument(command)
    TO_DO_LIST.pop(int(argument) -1)
    print(f"Deleting task: {argument}")

def handle_list_command():
    for index, item in enumerate(TO_DO_LIST):
        print(f"{index+1}: {item}")

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
    else:
        print("Command not recognized")
