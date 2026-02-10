exit = False

while not exit:
    command = input("Enter command: ")

    if command.startswith("exit"):
        exit = True