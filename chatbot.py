import re
from datetime import datetime

tasks = []

def add_task(task_description, due_date=None):
    task = {"description": task_description.strip(), "due_date": due_date}
    tasks.append(task)
    return f"Task '{task_description}' has been added."

def view_tasks():
    if not tasks:
        return "You have no tasks."
    response = "Here are your tasks:\n"
    for idx, task in enumerate(tasks, start=1):
        due_date = task["due_date"].strftime("%Y-%m-%d %H:%M") if task["due_date"] else "No due date"
        response += f"{idx}. {task['description']} - Due: {due_date}\n"
    return response

def delete_task(task_number):
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            return f"Task '{removed_task['description']}' has been deleted."
        else:
            return "Invalid task number."
    except ValueError:
        return "Please provide a valid task number."

def set_reminder(task_number, reminder_time):
    try:
        task_number = int(task_number) - 1
        reminder_datetime = datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")
        if 0 <= task_number < len(tasks):
            tasks[task_number]["due_date"] = reminder_datetime
            return f"Reminder set for task '{tasks[task_number]['description']}' at {reminder_time}."
        else:
            return "Invalid task number."
    except ValueError:
        return "Please provide a valid task number and reminder time in 'YYYY-MM-DD HH:MM' format."

# ✅ Make sure this is defined BEFORE it's called
def show_help():
    return (
        "\n📌 Available Commands:\n"
        "1. add task <task description>\n"
        "   ➤ Example: add task Buy groceries\n"
        "2. view tasks\n"
        "3. delete task <task number>\n"
        "4. set reminder <task number> <YYYY-MM-DD HH:MM>\n"
        "5. help\n"
        "6. exit or quit\n"
    )

def process_input(user_input):
    user_input = user_input.strip()

    add_match = re.fullmatch(r"(?i)add task (.+)", user_input)
    view_match = re.fullmatch(r"(?i)view tasks", user_input)
    delete_match = re.fullmatch(r"(?i)delete task (\d+)", user_input)
    reminder_match = re.fullmatch(r"(?i)set reminder (\d+) (.+)", user_input)
    help_match = re.fullmatch(r"(?i)help", user_input)

    if add_match:
        return add_task(add_match.group(1))
    elif view_match:
        return view_tasks()
    elif delete_match:
        return delete_task(delete_match.group(1))
    elif reminder_match:
        return set_reminder(reminder_match.group(1), reminder_match.group(2))
    elif help_match:
        return show_help()
    else:
        return "Sorry, I didn't understand that. Type 'help' to see the list of commands."

def chatbot():
    print("👋 Hello! I'm your personal assistant bot.")
    print("I can help you manage your tasks and reminders.")
    print("Type 'help' to see a list of commands.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Goodbye! Have a great day! ✨")
            break
        response = process_input(user_input)
        print(f"Bot: {response}")

chatbot()
