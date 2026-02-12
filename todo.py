exit = False

TO_DO_LIST = []

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
        TO_DO_LIST.append(argument)
        print(f"Adding task: {argument}")
    elif command.startswith("delete"):
        # delete task
        argument = get_argument(command)
        # specific pop over del (accident whole list) or remove (less specific)
        ## integer convert string to number - 1 (index value minus 1)
        TO_DO_LIST.pop(int(argument) -1)
        ## int converts string to number
        print(f"Deleting task: {argument}")
    elif command.startswith("list"):
        index = 0
        for todo_item in TO_DO_LIST:
            index+=1
            print(f"{index}. {todo_item}")
        for index, item in enumerate(TO_DO_LIST):
            print(f"{index}: {item}")
    else:
        print("Command not recognized")
