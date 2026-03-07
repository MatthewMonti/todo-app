import sys
exit = False
filename = None
TO_DO_LIST = []

def get_argument(command):
    command_name, argument = command.split(" ", maxsplit=1)
    return argument

def handle_add_command(command): 
    try:
        command_name, argument = command.split(" ", maxsplit =1)
        part = command_name, argument

        if part[0].strip() != "add" and part[1].strip():
            print("add command must be seperated from todo item name")
            return 
        if  part[0]== "add" and part[1].strip() == "":
            print('Assign todo item before adding todo item')
            return
        if part[0].strip() != "add" and part[1].strip() == "":
            print("'add' command is not spelled right 02")
            return 

        if part[0] == "add" and part[1]:
            print(f"Adding task: {argument}")
            TO_DO_LIST.append(argument)
            handle_list_command()
            return 
        return argument 
    
    except ValueError:
        valid_command = ['save', 'open', 'delete', 'add', 'list']
        parts = command.split()

        valid_space = [' ']

        # print(parts[0])
        if parts and parts[0] in valid_command:
            print("Forgot to assign todo item")
            return
        elif parts and parts[0] not in valid_space:
            print("only 'add' command is valid for inserting new todo itemsß")
            return
    
def handle_delete_command(command):
    try:
        item_number = get_argument(command)
        num = int(item_number)
        print(f"Deleting task: {num}")
        TO_DO_LIST.pop(num - 1)
    except ValueError:
        print("forgot to provide a integer of todo item to delete")

def handle_list_command():
    for index, item in enumerate(TO_DO_LIST):
        print(f"{index+1}: {item}")

def handle_save_command(command):
    try:
        global filename
        filename = get_argument(command)
        with open(get_filename(filename), 'w') as f:
            for i in TO_DO_LIST:
                f.write(f'{i}\n')
        raise ValueError
    except ValueError:
        print( "forgot to provide a filename to save")
    
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
    elif command.startswith("add" ):
        handle_add_command(command)
    elif command.startswith("delete "):
        handle_delete_command(command)
    elif command.startswith("list"):
        if len(command) == 4:
            handle_list_command()
        else:
            print(command , "Print list with comamand: list")
    elif command.startswith("open "):
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