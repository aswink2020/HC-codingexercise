import logging
from task import TaskBuilder
from todolist import ToDoListManager

logging.basicConfig(filename='todolist.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def print_menu():
    print("\n===== To-Do List Manager =====")
    print("1. Add Task")
    print("2. Mark Completed")
    print("3. View Tasks")
    print("4. Quit")

def get_user_input():
    return input("Enter your choice (1-4): ")

def add_task(todo_manager):
    try:
        description = input("Enter task description: ")
        due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
        tags = input("Enter tags (optional, separated by commas): ").split(',')

        task = TaskBuilder(description).set_due_date(due_date.strip()).add_tags(tags).build()
        todo_manager.add_task(task)
        logging.info(f"Task added: {description}")
        print("Task added successfully!")
    except Exception as e:
        logging.error(f"Error adding task: {str(e)}")
        print(f"Error adding task: {str(e)}")

def mark_completed(todo_manager):
    try:
        task_description = input("Enter the task to mark as completed: ")
        success = todo_manager.mark_completed(task_description)
        if success:
            logging.info(f"Task marked as completed: {task_description}")
            print(f"Task '{task_description}' marked as completed.")
        else:
            logging.warning(f"Task not found: {task_description}")
            print(f"Task '{task_description}' not found.")
    except Exception as e:
        logging.error(f"Error marking task as completed: {str(e)}")
        print(f"Error marking task as completed: {str(e)}")

def view_tasks(todo_manager):
    try:
        view_choice = input("Select view option (1. Show all, 2. Show completed, 3. Show pending): ")
        if view_choice == "1":
            tasks = todo_manager.view_tasks()
        elif view_choice == "2":
            tasks = todo_manager.view_tasks("completed")
        elif view_choice == "3":
            tasks = todo_manager.view_tasks("pending")
        else:
            logging.warning("Invalid view choice. Showing all tasks.")
            print("Invalid choice. Showing all tasks.")
            tasks = todo_manager.view_tasks()

        print("\n===== Tasks =====")
        for task in tasks:
            print(task)

    except Exception as e:
        logging.error(f"Error viewing tasks: {str(e)}")
        print(f"Error viewing tasks: {str(e)}")

def main():
    try:
        todo_manager = ToDoListManager()

        while True:
            print_menu()
            choice = get_user_input()

            if choice == "1":
                add_task(todo_manager)

            elif choice == "2":
                mark_completed(todo_manager)

            elif choice == "3":
                view_tasks(todo_manager)

            elif choice == "4":
                print("Exiting the To-Do List Manager. Goodbye!")
                break

            else:
                logging.warning("Invalid choice entered.")
                print("Invalid choice. Please enter a number between 1 and 4.")

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
