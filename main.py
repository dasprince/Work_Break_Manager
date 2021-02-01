import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    reset_button.config(state="disabled")
    start_button.config(state="normal")
    window.after_cancel(timer)
    canvas.itemconfig(count_timer, text="00:00")
    up_label.config(text="Timer")
    check.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        up_label.config(text="Break", fg=RED)
        count_mechanism(long_break_sec)
    elif reps % 2 == 0:
        up_label.config(text="Break", fg=PINK)
        count_mechanism(short_break_sec)
    else:
        up_label.config(text="Work", fg=GREEN)
        count_mechanism(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_mechanism(count):
    # def_count = count
    count_min = math.floor(count / 60)
    count_second = count % 60
    global timer

    if count_second < 10:
        canvas.itemconfig(count_timer, text=f"{count_min}:0{count_second}")
    else:
        canvas.itemconfig(count_timer, text=f"{count_min}:{count_second}")
    if count > 0:
        timer = window.after(1000, count_mechanism, count - 1)
    else:
        start_timer()
        mark = ""
        count_mark = math.floor(reps / 2)
        for m in range(count_mark):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Tomato Positioning


window = tkinter.Tk()

window.title("Work Time Manager")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# TIMER
up_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"), padx=10, pady=10)
up_label.grid(row=0, column=1)

# Start button
start_button = tkinter.Button(text="START", state="normal", highlightthickness=0, padx=5, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = tkinter.Button(text="RESET", state="disabled", highlightthickness=0, padx=5, command=reset)
reset_button.grid(row=2, column=2)

# Check Mark
check = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), padx=5)
check.grid(row=3, column=1)

window.mainloop()
