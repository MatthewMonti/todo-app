import sys

exit = False
filename = None
TO_DO_LIST = []

def get_argument(command): 
    parts = command.split(" ", maxsplit=1) 

    if parts[0] != "add": 
        return None # No argument provided 
    return parts[1]


def handle_add_command(command): 
    argument = get_argument(command) 
    if argument is None: 
        print("Error: 'add' requires an argument.") 
        return
    if argument:
        print(f"Adding task: {argument}")
        TO_DO_LIST.append(argument)
    else:
        print("No task provided. Please provide a task.")

def handle_delete_command(command):
    argument = get_argument(command)
    TO_DO_LIST.pop(int(argument) -1)
    
    print(f"Updated List:")
    handle_list_command()

def handle_list_command():
    for index, item in enumerate(TO_DO_LIST):
        print(f"{index+1}: {item}")

class handle_typo(Exception):
    handle_list_command()

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
    filename = get_argument(command)
    
    if filename:
        try:
            with open(get_filename(filename), "r") as file:
                for line in file:
                   TO_DO_LIST.append(line.strip())
        except FileNotFoundError:
            print(f"File {get_filename(filename)} does not exist.")
    else:
        print("No filename provided.")

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
        handle_open_command(command)
        if len(TO_DO_LIST) > 1:
            while True: 
                print("There are existing todo items. Do you want to clear them? (y/n)")
                answer = input().lower().strip()

                if answer == "y":
                    print("clearing existing todo items")
                    TO_DO_LIST.clear()
                    handle_list_command()
                    break
                elif answer == "n":
                    print(f"{filename} file updated with new todo items")
                    handle_open_command(command)
                    handle_list_command()
                    break
                else:
                    print(f"Invalid input: '{answer}'. Please enter 'y' or 'n'.")
    elif command.startswith("save"):
        handle_save_command(command)
    else:
        print("Command not recognized")
    if exit and filename:
        handle_save_command(f"save {filename}")
        print(f"Saved tasks to file {filename} before exiting.")
    
    if len(sys.argv)> 1:
        filename = sys.argv[1]
        handle_open_command(f"open {filename}")
        handle_list_command()
    
    return exit

while not exit:
    command = input("Enter command: ")
    exit = process_command(command)