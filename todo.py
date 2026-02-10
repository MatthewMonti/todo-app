exit = False

while not exit:
    command = input("Enter command: ")

    if command.startswith("exit"):
        exit = True
    elif command.startswith("add"):
        pass
    elif command.startswith("delete"):
        pass
    else:
        print("Command not recognized")