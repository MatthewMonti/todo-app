exit = False
filename = None
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
    global filename
    filename = get_argument(command)
    with open(get_filename(filename), 'w') as f:
        for i in TO_DO_LIST:
            f.write(f'{i}\n')

def get_filename(filename):
    return filename + ".todo.txt"

def handle_open_command(command):
    global filename
    # Read a list of todo items from a file
    filename = get_argument(command)
    with open(get_filename(filename), "r") as f:
        for line in f:
            TO_DO_LIST.append(line.strip())

def process_command(command):
    global filename
    exit = False

    if command.startswith("exit"):
        exit = True
    elif command.startswith("add"):
        handle_add_command(command)
    elif command.startswith("delete"):
        handle_delete_command(command)
    elif command.startswith("list"):
        handle_list_command()
    elif command.startswith("open"):
        if len(TO_DO_LIST) > 0:
            print("There are existing todo items. Do you want to clear them?")
    elif command.startswith("save"):
        handle_save_command(command)
    else:
        print("Command not recognized")
    if exit and filename:
        handle_save_command(f"save {filename}")
        print(f"Saved tasks to file {filename} before exiting.")
    
    return exit

while not exit:
    command = input("Enter command: ")
    exit = process_command(command)