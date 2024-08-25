user_input = "Type add or show: "

todos = [] #Create the empty list

while True:
    user_action = input("Type add, show, edit, complete or exit: ") # User input action
    # If user misstype 'add', 'show' or 'exit' as 'add ', 'show ' or 'exit '
    # user_action.strip() gonna match it with the right one
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo) # When user input text collect all text in empty list todos

        # User can see what to do
        # print(todos) -> return as a list with [] and ,
        # Use for-loop for showing user every data user has input as to do
        # Use enumerate to print out index with number
        # Instead of have space in the middle of number and index in the list use 'fstring'
        # FString help to fix the middle space from 1 - [index-value] to 1-[index-value]
        # Ex: 1 - Eating to 1-Eating
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}" # Fstring. Instead of - can use anything like .(dot) or ,(comma)
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: ")) # This number is in the list of todo
            number = number - 1 # User List start from 1
            # After user choose what they want to edit
            print("Number of the to do you what to edit " + str(todos[number])) # Show the text what they want to edit
            edit_todo = input("Enter new todo: ") # Let the user enter new to do
            todos[number] = edit_todo # Tell the program that the new input is the same as old one before edited
            existing_todo = todos[number]
            print(existing_todo) # Print new to do
            print("Got it!")
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case whatever: # Or can use _ instead whatever variable
            print("Hey, you entered an unknown command")
print("Bye!")






