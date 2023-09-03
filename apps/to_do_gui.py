import sqlite3 as sql
from tkinter import *
from tkinter import messagebox


"""
    To Do App with Tkinter
"""
connector = sql.connect("todo.db")
cursor = connector.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS Todo_List (S_NO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, TASK TEXT, DETAIL TEXT)"
)


app = Tk()
app.title("To Do App GUI")
app.geometry("750x500")
app.resizable(0, 0)

# color and font variables
left_frame_bg = "Gray70"
center_frame_bg = "Gray57"
right_frame_bg = "Gray35"
frame_font = ("Garamond", 14)

# StringVar variables
task_name_str = StringVar()
search_str = StringVar()

# the functions
# add a task to database
def submit_task():
    global task_name_str, task_detail_entry
    global cursor
    task = task_name_str.get()
    detail = task_detail_entry.get(1.0, END)
    print(task)
    print(detail)

    if task == '':
        messagebox.showerror('Error!', 'Please fill all the fields')
    else:
        cursor.execute(
            "INSERT INTO Todo_List (TASK, DETAIL) VALUES (?, ?)", (task, detail)
        )
        connector.commit()
        messagebox.showinfo('Task added', 'New Task Added')
        listbox.delete(0, END)
        list_tasks()
        clear_fields()


# list all tasks
def list_tasks():
    curr = connector.execute("SELECT TASK FROM Todo_List")
    fetch = curr.fetchall()
    for data in fetch:
        listbox.insert(END, data[0])


# delete a task
def delete_task():
    global listbox, connector, cursor

    if not listbox.get(ACTIVE):
        messagebox.showerror("No item selected, you have not selected any item")

    cursor.execute("DELETE FROM Todo_List WHERE TASK= ?", (listbox.get(ACTIVE),))
    connector.commit()

    messagebox.showinfo("Task Deleted", "Task Deleted")
    listbox.delete(0, END)
    list_tasks()
    clear_fields()


# delete all tasks
def delete_all_tasks():
    cursor.execute("DELETE FROM Todo_list")
    connector.commit()

    messagebox.showinfo("All Tasks Deleted", "All Tasks Deleted")
    listbox.delete(0, END)
    list_tasks()


# view selected task details
def view_task():
    global task_name_str, task_detail_entry, listbox

    curr = cursor.execute("SELECT * FROM Todo_List WHERE TASK=?", (listbox.get(ACTIVE),))

    values = curr.fetchall()[0]

    task_name_str.set(values[1])
    task_detail_entry.delete(1.0, END)
    task_detail_entry.insert(END, values[2])


# clear input fields
def clear_fields():
    global task_name_str, task_detail_entry, listbox

    listbox.select_clear(0, END)

    task_name_str.set("")
    search_str.set("")
    task_detail_entry.delete(1.0, END)


# search a task
def search_task():
    global task_name_str, task_detail_entry, listbox

    query = str(search_str.get())

    if query != "":
        curr = connector.execute(
            "SELECT * FROM Todo_List WHERE TASK LIKE ?", ("%" + query + "%",)
        )
        check = curr.fetchall()

        for data in check:
            listbox.delete(0, END)
            listbox.insert(END, data[1])
        
    else:
        messagebox.showinfo("Error", "Enter search query")


Label(app, text="To Do App", font=("Roboto", 15, "bold"), bg="Black", fg="White").pack(
    side=TOP, fill=X
)

# Create left frame
left_frame = Frame(app, bg=left_frame_bg, width=80)
left_frame.place(relx=0, relheight=1, y=30, relwidth=0.3)

# create center frame
center_frame = Frame(app, bg=center_frame_bg)
center_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)

# create right frame
right_frame = Frame(app, bg=right_frame_bg)
right_frame.place(relx=0.6, relwidth=0.4, relheight=1, y=30)


# left frame components
Label(left_frame, text="Add Task", bg=left_frame_bg, font=frame_font).place(
    relx=0.3, rely=0.05
)

task_name_entry = Entry(left_frame, width=20, font=("Verdana", 11), textvariable=task_name_str)
task_name_entry.place(relx=0.1, rely=0.1)

Label(left_frame, text="Detail", bg=left_frame_bg, font=frame_font).place(
    relx=0.28, rely=0.2
)

task_detail_entry = Text(left_frame, width=20, font=("Verdana", 11), height=5)
task_detail_entry.place(relx=0.1, rely=0.25)

# middle frame components
Label(center_frame, text="Search", font=frame_font, bg=center_frame_bg).place(relx=0.3, rely=0.04)
search_entry = Entry(
    center_frame, width=18, font=("Verdana", 12), textvariable=search_str
).place(relx=0.06, rely=0.1)

Button(
    center_frame, text="Search", font=frame_font, width=13, command=search_task
).place(relx=0.05, rely=0.17)
Button(
    center_frame, text="Add Task", font=frame_font, width=13, command=submit_task
).place(relx=0.05, rely=0.3)
Button(
    center_frame, text="View Task", font=frame_font, width=13, command=view_task
).place(relx=0.05, rely=0.4)
Button(
    center_frame, text="Clear Fields", font=frame_font, width=13, command=clear_fields
).place(relx=0.05, rely=0.5)
Button(
    center_frame, text="Delete Task", font=frame_font, width=13, command=delete_task
).place(relx=0.05, rely=0.7)
Button(
    center_frame,
    text="Delete All Tasks",
    font=frame_font,
    width=14,
    command=delete_all_tasks,
).place(relx=0.04, rely=0.8)

# right frame components
Label(right_frame, text="Task List", font=("Roboto", 14), bg=right_frame_bg).place(
    relx=0.25, rely=0.09
)

listbox = Listbox(
    right_frame,
    selectbackground="SkyBlue",
    bg="green",
    font=("Helvetica", 12),
    height=20,
    width=25,
)
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.93, rely=0, relheight=1)
listbox.config(yscrollcommand=scroller.set)
listbox.place(relx=0.1, rely=0.15)

list_tasks()


app.mainloop()
