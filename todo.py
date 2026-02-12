exit = False

def get_argument(command):
    command_name, argument = command.split(" ", maxsplit=1)
    return argument 
while not exit:
    command = input("Enter command: ")

    if command.startswith("exit"):
        exit = True
    elif command.startswith("add"):
        # add task
        argument = get_argument(command)
        print(f"Adding task: {argument}")
    elif command.startswith("delete"):
        # delete task
        argument = get_argument(command)
        print(f"Deleting task: {argument}")
    else:
        print("Command not recognized")