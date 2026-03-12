import sys
import os
exit = False
filename = None
TO_DO_LIST = []

def get_argument(command):
    command_name, argument = command.split(" ", maxsplit=1)
    return argument

def get_command_name(command):
    command_name, argument = command.split(" ", maxsplit=1)
    return command_name

def handle_add_command(command):
    try:
        name = get_command_name(command)
        task = get_argument(command)
        if name == "add" and task.strip() == "":
            print("Forgot to assign task name to add")
        if name == "add" and task:
            print(f"Adding task: {task}")
            TO_DO_LIST.append(task)
            handle_list_command()
        if name != "add" and task:
            print("Command not recognized")
            print("Type 'help' to see available command")
    except ValueError:
        if command == "add":
            print("Forgot to assign task name to add")
        else: 
            print("Command not recognized")
            print("Type 'help' to see available command")
    

def handle_remove_command(command):
    try:
        name = get_command_name(command)
        item_number = get_argument(command)

        if item_number.strip() == "":
            print("Forgot to assign todo item number of item you want to remove")
            return
        if not item_number.isdigit():
            print("Please assign number not name")
            return

        num = int(item_number)

        if name == "remove":
            print(f"Removing task: {num}")
            try:
                TO_DO_LIST.pop(num - 1)
                handle_list_command()
            except IndexError:
                print("Invalid index")
    except ValueError:
        print("Command not recognized")
        print("Type 'help' to see available command")
def delete_filename_command():
    try:
        name = get_command_name(command)
        command_filename = get_argument(command)
        full_filename = get_filename(command_filename)
        if name == "delete" and command_filename:
            if os.path.exists(full_filename):
                os.remove(full_filename)
                print(f"'{full_filename}' deleted")
            else:
                print(f"{full_filename} does not exist")
        elif name != "delete" and command_filename:
            print("Command not recognized")
            print("Type 'help' to see available command")
        elif name == "delete" and command_filename.strip() == "":
            print("Did not assign filename to delete")
    except ValueError:
        if command == "delete":
            print("Did not assign filename to delete")
        else:
            print("Command not recognized")
            print("Type 'help' to see available command")
    

def handle_list_command():
    for index, item in enumerate(TO_DO_LIST):
        print(f"{index+1}: {item}")


def handle_save_command(command):
    try:
        filename = get_argument(command)
        name = get_command_name(command)
        if name == "save" and filename.strip() == "":
            print("Forgot to assign filename to save")
        elif name == "save" and filename:
            with open(get_filename(filename), 'w') as f:
                for i in TO_DO_LIST:
                    f.write(f'{i}\n')
        elif name != "save" and filename:
            print("Command not recognized")
            print("Type 'help' to see available command")
            
    except ValueError:
        if command == "save":
            print("Forgot to assign filename to save")
        else:
            print("Command not recognized")
            print("Type 'help' to see available command")
    
def get_filename(filename):
    return filename + ".todo.txt"

def handle_open_command(command):
    try:
        global filename
        filename = get_argument(command)
        name = get_command_name(command)
        if name == "open" and filename.strip() == "":
            print("Forgot to assign filenname to open")
        elif name == "open" and filename:
            with open(get_filename(filename), "r") as file:
                for line in file:
                    TO_DO_LIST.append(line.strip())
        elif name != "open" and filename:
            print("Command not recognized")
            print("Type 'help' to see available command")
    except ValueError:
        if command == "open":
            print("Forgot to assign filename to open")
        else:
            print("Command not recognized")
            print("Type 'help' to see available command")
    except FileNotFoundError:
        print(f"File {get_filename(filename)} does not exist.")


def handle_help_command():
    base = os.path.dirname(__file__)
    path = os.path.join(base, "documentation/documentation_todo_app.txt")

    try:
        with open(path, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Help file not found at {path}")

def process_command(command):
    global filename
    exit = False

    if command.startswith("exit"):
        exit = True
    elif command.startswith("add"):
        handle_add_command(command)
    elif command.startswith("remove"):
        handle_remove_command(command)
    elif command.startswith("list"):
        if command == "list":
            handle_list_command()
        elif command != "list":
            print("Command not recognized")
    elif command.startswith("open"):
        if len(TO_DO_LIST) == 0:
            handle_open_command(command)
            handle_list_command()
            return
        if len(TO_DO_LIST) > 0:
            while True: 
                print("There are existing todo items. Do you want to clear them? (y/n)")
                answer = input()

                if answer.lower() == "y":
                    print("clearing existing todo items")
                    TO_DO_LIST.clear()
                    handle_list_command()
                    break
                elif answer.lower() == "n":
                    print(f"{filename} file updated with new todo items")
                    handle_open_command(command)
                    handle_list_command()
                    break
                else:
                    print(f"Invalid input: '{answer}'. Please enter (y/n).")
    elif command.startswith("save"):
        try:
            command_file_name = get_argument(command)
            full_file_name = get_filename(command_file_name)
            file_name_exist = os.path.exists(full_file_name)
            if file_name_exist is True:
                while True:
                    print("Filename already exists do you want to override it? (y/n)")
                    answer = input()

                    if answer.lower() == "y":
                        print(f"yes override and clear {full_file_name} file")
                        handle_save_command(command)
                        handle_list_command()
                        break
                    elif answer.lower() == "n":
                        print(f"{filename} file updated")
                        break
                    else:
                        print(f"Invalid input: Open'{full_file_name}' or override?. Please enter (y/n).")
            elif file_name_exist is False:
                print(f"Creating new file named: {full_file_name}")
                handle_save_command(command)
        except ValueError:
            print("failed to provide filename to save")
    elif command.startswith("delete"):
        try:
            command_file_name = get_argument(command)
            full_file_name = get_filename(command_file_name)
            file_name_exist = os.path.exists(full_file_name)
            if file_name_exist is True:
                while True:
                    print(f"Do you want to delete this file: '{full_file_name}' Please enter (y/n)")
                    answer= input()

                    if answer.lower() == "y":
                        print(f"{command_file_name} has been deleted")
                        delete_filename_command()
                        break
                    elif answer.lower() == "n":
                        print(f"{command_file_name} not been deleted")
                        break
                    else:
                        print(f"Invalid input: Delete {full_file_name}? Please enter (y/n)")
            elif file_name_exist is False:
                print(f"{full_file_name} not exist please check filename")
        except ValueError:
            print("failed to provide filename to delete")
                        
    elif command.startswith("help"):
        handle_help_command()
    else:
        print("Command not recognized")
        print("Type 'help' to see available command")

    if exit:
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