#from pip._internal.operations.prepare import File

FILEPATH='todo.txt'

#To read Todos from file
def read_txt_file(filepath=FILEPATH):    #default argument
    """Reads todos.txt file in FIles folder and returns list with todos
    Default param: string-->'FIles/todo.txt'
    return: list
    """
    with open(filepath,'r') as file:
        list_var=file.readlines()

    return list_var

    # file=open('FIles/todo.txt', 'r')
    # list_var=file.readlines()
    # file.close()
    # return list_var



#Write todo list in file
def write_txt(list_var):
    """For Writing text file with list_var list"""
    with open(FILEPATH, 'w') as file:
        file.writelines(list_var)


    # file = open('FIles/todo.txt', 'w', )  # create file object with todo.txt in write mode
    # file.writelines(list_var)
    # file.close()

#Show or display List
def show_list(list_var):
    for x in range(len(list_var)):  # for items in todo_list  does same
        print(f"{str(x + 1)}. {list_var[x][:-1]}")

#Mention number of reamianing todos
def remaining_todos(list_var):
    print(f"ToDos Remaining: {len(list_var)}!!")

#Print Invalid command when words used instead of numbers
def Print_Invalid_Command():
    print("Invalid Command.Specify the todo number")

def Print_Todo_Invalid():
    print("The Todo number is invalid!! Please try again")

# To print or do only in this file, and not run it in other files that import this file
if __name__=="__main__":
    print("In Functions.py")
