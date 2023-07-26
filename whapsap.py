import tkinter as tk
import pyautogui as pg
import time

# Global variable to track whether the writing should continue or stop
continue_writing = True

def start_writing():
    global continue_writing

    time_input = int(entry_times.get())
    text_input = entry_text.get()
    start_time = int(entry_start_time.get())

    print("Starting in", start_time, "seconds...")
    time.sleep(start_time)

    label_text.config(fg="red")  # Set text color to red

    for _ in range(time_input):
        if not continue_writing:
            break

        pg.write(text_input)
        pg.press("enter")

def stop_writing():
    global continue_writing
    continue_writing = False

def exit_program():
    window.quit()

# Create the application window
window = tk.Tk()
window.title("Auto Writer")
window.geometry("300x400")
window.configure(bg="lightgray")

# Create labels and pack them into the window
label_times = tk.Label(window, text="How many times do you want to write the text?", bg="lightgray")
label_times.pack()

# Create entry for times input
entry_times = tk.Entry(window)
entry_times.pack()

# Create label and pack it into the window
label_text = tk.Label(window, text="What text do you want to write?", bg="lightgray")
label_text.pack()

# Create entry for text input
entry_text = tk.Entry(window)
entry_text.pack()

# Create label and pack it into the window
label_start_time = tk.Label(window, text="Set the starting time in seconds:", bg="lightgray")
label_start_time.pack()

# Create entry for start time input
entry_start_time = tk.Entry(window)
entry_start_time.pack()

# Create start button and pack it into the window
button_start = tk.Button(window, text="Start", command=start_writing)
button_start.pack(pady=10)

# Create stop button and pack it into the window
button_stop = tk.Button(window, text="Stop", command=stop_writing)
button_stop.pack(pady=10)

# Create exit button and pack it into the window
button_exit = tk.Button(window, text="Exit", command=exit_program)
button_exit.pack(pady=10)

# Run the application
window.mainloop()
