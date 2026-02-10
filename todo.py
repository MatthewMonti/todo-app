exit = False

while not exit:
    command = input("Enter command: ")

    if command.startswith("exit"):
        exit = True
    else:
        print("Command not recognized")