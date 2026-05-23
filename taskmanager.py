c=0
list_tasks={}
print("Welcome to Task Manager:\n")
prev_work=input("Do you want to use a previously used file(Yes/No):\n")
if prev_work=="Yes":
    prev_file=input("Enter file name:\n")
    try:
        with open(prev_file,"r") as f:
            for l in f:
                task,status=l.strip().split("-")
                list_tasks[task]=status
    except FileNotFoundError:
        print("File Not Found,proceeding with empty list")
while True:
    c=input("\n1.View Tasks\n2.Add Tasks\n3.Task Updation\n4.Delete Task\n5.Exit\n")
    match(c):
        case "1":
            for i,j in list_tasks.items():
                print(f"Title:{i}\nStatus:{j}\n")
            if len(list_tasks)==0:
                print("Task list is empty\n")
        case "2":
            task_name=input("Enter Task Name:\n")
            list_tasks[task_name]="Incomplete"
        case "3":
            task_upd=input("Enter Task Name to be updated:\n")
            if task_upd in list_tasks:
                list_tasks[task_upd]="Complete"
            else:
                print("Task Not in List")
        case "4":
            task_del=input("Enter task you want to delete:\n")
            if task_del in list_tasks:
                del list_tasks[task_del]
            else:
                print("Enter valid task")
        case "5":
            print("Thank You")
            with open("output.txt","w") as fo:
                for i,j in list_tasks.items():
                    fo.write(f"{i}-{j}\n")
            break
        case _:
            print("Invalid Choice")