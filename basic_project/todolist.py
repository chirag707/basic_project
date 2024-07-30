tasks = []
def addtask():
    newtask = input(print("enter a new task:"))
    tasks.append(newtask)
    print(f"'{newtask}' has been added")
    print("~~~~~~~~~~~~~~~~~~~~~")
    return 
def deletetask():
    listtask()
    deltask = int(input(print("choose the # to delete")))
    if deltask < len(tasks) and deltask >0 :
        tasks.pop(deltask-1)
        print("~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("invalid input , please try again " )
        print("~~~~~~~~~~~~~~~~~~~~~")
def listtask():
    if not tasks:
        print("no tasks currently")
    else :
        print("current tasks on the list ---->")
        for index , task in enumerate(tasks) :
          
          print(f"{index+1}. {task}")

print("welcome to your to do list !")
while 1 :
    print("-------------------")
    print("1. Add a new task")
    print("2. delete a task")
    print("3. list tasks")
    print("4. quit")
    choice = int (input("what do you want to do today:"))
    if choice == 1 :
        addtask()
    elif choice == 2:
        deletetask() 
    elif choice == 3:
        listtask() 
    elif choice == 4:
        break 
    else :
        print("invalid input")
    
    