def input_text(option):
    if option == '7':
        user_description_input = input("Enter description: ")
        user_time_taken_input = int(input("Enter time taken: "))
        return user_description_input, user_time_taken_input

    elif option == '5':
        task_duration = input("Enter task duration: ")
        return task_duration

    elif option == '6' or '4':
        user_description_input = input("Enter task description to search for: ")
        return user_description_input

    else:
        return "An error has occured."