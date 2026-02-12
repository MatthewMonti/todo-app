exit = False

while not exit:
    command = input("Enter command: ")

    if command.startswith("exit"):
        exit = True
    elif command.startswith("add"):
        # add task
        command, argument = command.split(" ", maxsplit = 1)
        print(f"Adding task: {argument}")
    elif command.startswith("delete"):
        pass
    else:
        print("Command not recognized")