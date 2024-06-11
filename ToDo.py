from tkinter import *
from tkinter import messagebox


tasks_list = []
completed_tasks = []

# global variable for counting the task
counter = 1


def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty!")
        return 0
    return 1


def clear_taskNumberField():
    taskNumberField.delete(0, END)

def clear_taskField():
    enterTaskField.delete(0, END)


def insertTask():
    global counter
    value = inputError()
    if value == 0:
        return
    content = enterTaskField.get()
    tasks_list.append(content)
    TextArea.insert(END, f"[ {counter} ] {content}\n")
    counter += 1
    clear_taskField()


def deleteTask():
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("No task", "No task to delete!")
        return
    number = taskNumberField.get()
    if number == "":
        messagebox.showerror("Input Error", "Task number cannot be empty!")
        return
    try:
        task_no = int(number)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid task number!")
        return
    if task_no < 1 or task_no > len(tasks_list):
        messagebox.showerror("Input Error", "Task number out of range!")
        return
    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert(END, f"[ {i + 1} ] {tasks_list[i]}\n")


def completeTask():
    if len(tasks_list) == 0:
        messagebox.showerror("No task", "No task to complete!")
        return
    number = taskNumberField.get()
    if number == "":
        messagebox.showerror("Input Error", "Task number cannot be empty!")
        return
    try:
        task_no = int(number)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid task number!")
        return
    if task_no < 1 or task_no > len(tasks_list):
        messagebox.showerror("Input Error", "Task number out of range!")
        return
    clear_taskNumberField()
    completed_tasks.append(tasks_list[task_no - 1])
    tasks_list.pop(task_no - 1)
    updateTextArea()

def updateTextArea():
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert(END, f"[ {i + 1} ] {tasks_list[i]}\n")
    for i in range(len(completed_tasks)):
        TextArea.insert(END, f"[COMPLETED] {completed_tasks[i]}\n")


def searchTask():
    search_term = searchField.get()
    if search_term == "":
        messagebox.showerror("Input Error", "Search field cannot be empty!")
        return
    TextArea.delete(1.0, END)
    found = False
    for i in range(len(tasks_list)):
        if search_term.lower() in tasks_list[i].lower():
            TextArea.insert(END, f"[ {i + 1} ] {tasks_list[i]}\n")
            found = True
    if not found:
        TextArea.insert(END, "No tasks found!\n")
    searchField.delete(0, END)


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("ToDo App")
    gui.geometry("400x500")

    enterTask = Label(gui, text="Enter Your Task", bg="light green")
    enterTaskField = Entry(gui, width=30)
    Submit = Button(gui, text="Submit", fg="Black", bg="Grey", command=insertTask)
    TextArea = Text(gui, height=10, width=40, font="lucida 13")
    taskNumber = Label(gui, text="Task Number", bg="Grey")
    taskNumberField = Entry(gui, width=5, font="lucida 13")
    delete = Button(gui, text="Delete", fg="Black", bg="Grey", command=deleteTask)
    complete = Button(gui, text="Complete", fg="Black", bg="Grey", command=completeTask)
    searchLabel = Label(gui, text="Search Task", bg="light green")
    searchField = Entry(gui, width=30)
    searchButton = Button(gui, text="Search", fg="Black", bg="Grey", command=searchTask)
    Exit = Button(gui, text="Exit", fg="Black", bg="Grey", command=exit)

    enterTask.grid(row=0, column=0, padx=10, pady=5)
    enterTaskField.grid(row=0, column=1, ipadx=50, pady=5)
    Submit.grid(row=0, column=2, padx=10)
    TextArea.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    taskNumber.grid(row=2, column=0, pady=5)
    taskNumberField.grid(row=2, column=1, pady=5)
    delete.grid(row=2, column=2, pady=5)
    complete.grid(row=3, column=2, pady=5)
    searchLabel.grid(row=4, column=0, padx=10, pady=5)
    searchField.grid(row=4, column=1, ipadx=50, pady=5)
    searchButton.grid(row=4, column=2, padx=10)
    Exit.grid(row=5, column=1, pady=20)

    gui.mainloop()
