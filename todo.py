exit = False

def get_argument(command):
    command_name, argument = command.split(" ", maxsplit=1)
    return argument

while not exit:
    command = input("Enter command: ")

    if command.startswith("exit"):
        exit = True
    elif command.startswith("add"):
        argument = get_argument(command)
        print(f"Adding task: {argument}")
    elif command.startswith("delete"):
        argument = get_argument(command)
    else:
        print("Command not recognized")