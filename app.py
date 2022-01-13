from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *


import_task_list(tasks)

while (True):
    print_menu()
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = input_text(option) #
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = int(input_text(option))
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = input_text(option)
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description, time_taken = input_text(option)
        task = create_task(description, time_taken)
        tasks.append(task)
    elif option == "8":
        clear_task_list(tasks)
    else:
        print("Invalid Input - choose another option")