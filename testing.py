agenda = []

while True:
    user_input = input("What is your Agenda? Type add, show, edit, completed or exit: ").strip()
    if user_input == 'add':
        add_agenda = input("Add your todo\'s: ")
        agenda.append(add_agenda)
    elif user_input == 'exit':
        break

    elif user_input == 'edit':
        num_ind = int(input("WHICH number? "))
        existing_num = num_ind - 1
        new_input = input("replace with: ")
        agenda[existing_num] = new_input
        print(agenda)
    elif user_input == 'completed':
        which_task = int(input("Which task have been completed? "))
        del_task = which_task - 1
        agenda.pop(del_task)

    elif user_input == 'show' or 'display':
        for item in agenda:
            item = item.title()
            print(item)

































