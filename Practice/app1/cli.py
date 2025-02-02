
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:].strip()+"\n"
        
        
        todos = functions.get_todos()

        todos.append(todo)
        
        functions.write_todos(todos)
    
    elif user_action.startswith('show'):

        todos = functions.get_todos()
        
        for index,item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}.{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:].strip())
            number -=1
            new_todo = input("Enter new todo: ") + "\n"

            todos = functions.get_todos()

            todos[number] = new_todo
            
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:].strip())

            todos = functions.get_todos()

            remove = todos.pop(number-1)
            remove = remove.strip('\n')

            functions.write_todos(todos)

            message = f"Todo {remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    if 'exit' in user_action:
        break

print('Bye!')