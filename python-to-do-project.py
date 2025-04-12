# The user menu where they'll pick what they want to do
def user_menu():
    print("\nWelcome to my To-Do List App!")
    print("Please choose an option:")
    print("1. Add a new task")
    print("2. View current tasks")
    print("3. Delete a current task")
    print("4. Quit")
    print("5. Clear all tasks")

# Add task using .append and then relay a success message back to the user
def add_task(tasks):
    try:
        task = input("Enter the task you want to add: ").strip()
        if not task:
            raise ValueError("Task cannot be empty.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        tasks.append(task)
        print(f"'{task}' added to your list!")
    finally:
        print("Returning to main menu...\n")

# View tasks using a for loop to iterate through the list
def view_tasks(tasks):
    try:
        if not tasks:
            raise Exception("No tasks left to do, yay!")
    except Exception as e:
        print(e)
    else:
        print("Your current tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    finally:
        print("Done showing tasks.\n")

# To delete a task, use pop to remove it from the list
def delete_task(tasks):
    try:
        if not tasks:
            raise Exception("No tasks available to delete.")
        view_tasks(tasks)
        task_number = int(input("Enter the task number you want to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
        else:
            raise IndexError("Oh no, that task number doesn't exist!")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError as ie:
        print(f"Error: {ie}")
    except Exception as e:
        print(e)
    else:
        print(f"Your task: '{removed_task}' was deleted successfully!")
    finally:
        print("Returning to main menu...\n")

# Clear all tasks
def clear_tasks(tasks):
    try:
        if not tasks:
            raise Exception("The list is already empty, congrats!")
        tasks.clear()
    except Exception as e:
        print(e)
    else:
        print("All tasks cleared successfully!")
    finally:
        print("Returning to main menu...\n")

# Goes with the user menu, tells Python which input means which function to use
def main():
    tasks = []
    while True:
        user_menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
            if choice not in {'1', '2', '3', '4', '5'}:
                raise ValueError("That's not a valid, recognized response. Please try again.")
        except ValueError as ve:
            print(f"Error: {ve}")
        else:
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                delete_task(tasks)
            elif choice == '4':
                print("Thank you for using the To-Do app! Hope you got your chores done. Goodbye!")
                break
            elif choice == '5':
                clear_tasks(tasks)

# Using the if __name__ == "__main__": guard to ensure that the main function runs only when the program is run directly.
if __name__ == "__main__":
    main()