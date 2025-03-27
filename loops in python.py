# loops in python
# while loops
# ask user to enter correct password
# password="hello"
# guess=" "
# while guess!= password:
#     guess= input ("enter the password:")
# print("correct password!:")



# print number from 1to5 
# num=1
# while num<=5:  #condition
#     print(num)
#     num+=1  #increase num by 1


# # print number from 1to5
# for num in range(1,6):
#     print(num)


# stop loop with break

# a=int(input("enter a value:"))
# if 40<=a:
#     print("distinction")
# elif 75<=a:
#     print("pass")
# else:
#     print("fail")






# # Input: Role of the person
# role = input("Enter the role (Boss/Manager/Supervisor/Salesman/Fresher): ")

# # Using if-elif-else or nested if to determine access
# if role == "Boss":
#     print("Boss has full access to company data.")
# else:
#     if role == "Manager":
#         print("Manager has limited access compared to Boss.")
#     elif role == "Supervisor":
#         print("Supervisor has access to employee details.")
#     elif role == "Salesman":
#         print("Salesman has access to product details.")
#     elif role == "Fresher":
#         print("Fresher can only read their details, no write access.")
#     else:
#         print("Role not recognized. No access granted.")



   
import os

# Function to load tasks from a file
def load_tasks():
    tasks = []
    if os.path.exists("todo_list.txt"):
        with open("todo_list.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                title, status = line.strip().split(" | ")
                tasks.append({"title": title, "status": status})
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open("todo_list.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['title']} | {task['status']}\n")

# Function to display the task list
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    print("\nTask List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {'Completed' if task['status'] == 'done' else 'Pending'}")

# Function to add a new task
def add_task(tasks):
    title = input("\nEnter the task title: ")
    tasks.append({"title": title, "status": "pending"})
    print(f"Task '{title}' added!")

# Function to mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks) and tasks[task_index]['status'] == 'pending':
            tasks[task_index]['status'] = 'done'
            print(f"Task '{tasks[task_index]['title']}' marked as completed!")
        else:
            print("Invalid task number or task already completed.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main function to run the To-Do list app
def todo_list_app():
    tasks = load_tasks()  # Load existing tasks from file at the start
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Exit")
        choice = input("\nChoose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            save_tasks(tasks)  # Save tasks to file when exiting
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list_app()

