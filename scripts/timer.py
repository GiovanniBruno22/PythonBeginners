import tkinter as tk
import time
import threading
import winsound

root = tk.Tk()
root.title("Timer")

error_label = tk.Label(root, text="Please enter a valid number", font=("Times",12,), fg="#f00")
entry_label = tk.Label(root, text="Enter timer duration (seconds):", font=("Times",48))
entry_label.grid(row=0, column=0, pady=10)
entry = tk.Entry(root)
entry.grid(row=1, column=0, pady=10)

timer_label = tk.Label(root, text="", font=("Times",48))

def display_timer(seconds):
    entry.delete(0,tk.END)
    while seconds >= 0:
        timer_label.config(text=f"Time left: {seconds} seconds")
        root.update()
        time.sleep(1)
        seconds -= 1

    # Play the alarm sound
    # The "*" may be changed to a file of your choice, if it is left unchanged the windows prebuilt sound will play
    winsound.PlaySound("*", winsound.SND_ALIAS)
    time.sleep(0.5)
    entry_label.grid(row=0, column=0, pady=10)
    entry.grid(row=1, column=0, pady=10)
    start_button.grid(row=2, column=0, pady=10)
    timer_label.grid_remove()

    
def start_timer():
    entry_string = entry.get()
    if(entry_string == "" or not entry_string.isdigit()):
        error_label.grid(row=3, column=0, pady=1)
        return
    else:
        error_label.grid_forget()
        timer_duration = int(entry.get())
    
    timer_label.grid(pady=20)
    entry.grid_remove()
    start_button.grid_remove()
    
    timer_thread = threading.Thread(target=display_timer, args=(timer_duration,))
    timer_thread.start()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.grid(row=2, column=0, pady=10)

root.mainloop()