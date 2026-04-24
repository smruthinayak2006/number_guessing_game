import random
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- GAME LOGIC ---------------- #

def start_game():
    global number, attempts_left, max_attempts

    difficulty = difficulty_var.get()

    if difficulty == "Easy":
        low, high, max_attempts = 1, 50, 10
    elif difficulty == "Medium":
        low, high, max_attempts = 1, 100, 7
    else:
        low, high, max_attempts = 1, 200, 5

    number = random.randint(low, high)
    attempts_left = max_attempts

    result_label.configure(
        text=f"Guess between {low} and {high}",
        text_color="white"
    )
    attempts_label.configure(text=f"Attempts Left: {attempts_left}")

    entry.configure(state="normal")
    entry.delete(0, "end")

def check_guess():
    global attempts_left

    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")
        return

    attempts_left -= 1
    entry.delete(0, "end")

    # ✅ WIN CONDITION
    if guess == number:
        score = max_attempts - attempts_left
        result_label.configure(
            text=f"🎉 Correct! Score: {score}",
            text_color="green"
        )
        entry.configure(state="disabled")
        messagebox.showinfo("Win", "You guessed it right!")
        return

    # ✅ HINT SYSTEM WITH COLORS
    diff = abs(number - guess)
    hint = "⬆ Higher" if guess < number else "⬇ Lower"

    if diff <= 5:
        proximity = " (Very Close!)"
        color = "green"
    elif diff <= 10:
        proximity = " (Close!)"
        color = "orange"
    else:
        proximity = " (Far!)"
        color = "red"

    result_label.configure(
        text=hint + proximity,
        text_color=color
    )

    attempts_label.configure(text=f"Attempts Left: {attempts_left}")

    # ✅ GAME OVER
    if attempts_left == 0:
        entry.configure(state="disabled")
        messagebox.showinfo("Game Over", f"Number was {number}")

# ---------------- UI ---------------- #

app = ctk.CTk()
app.title("🎯 Number Guessing Game")

# Window size + center
width, height = 700, 500
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

app.geometry(f"{width}x{height}+{x}+{y}")

# Main frame
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(expand=True, fill="both", padx=40, pady=40)

# Title
title = ctk.CTkLabel(
    frame,
    text="🎯 Number Guessing Game",
    font=("Arial", 26, "bold")
)
title.pack(pady=20)

difficulty_var = ctk.StringVar(value="Medium")

dropdown = ctk.CTkOptionMenu(
    frame,
    values=["Easy", "Medium", "Hard"],
    variable=difficulty_var
)
dropdown.pack(pady=10)

# Start button
start_btn = ctk.CTkButton(
    frame,
    text="Start Game",
    width=200,
    height=40,
    command=start_game
)
start_btn.pack(pady=10)

# Entry (disabled initially)
entry = ctk.CTkEntry(
    frame,
    placeholder_text="Enter your guess",
    width=250,
    height=40,
    font=("Arial", 14)
)
entry.pack(pady=15)
entry.configure(state="disabled")

# Guess button
guess_btn = ctk.CTkButton(
    frame,
    text="Submit Guess",
    width=200,
    height=40,
    command=check_guess
)
guess_btn.pack(pady=10)

# Restart button (NEW)
restart_btn = ctk.CTkButton(
    frame,
    text="Restart Game",
    width=200,
    height=35,
    command=start_game
)
restart_btn.pack(pady=5)

# Result label
result_label = ctk.CTkLabel(
    frame,
    text="Click Start to begin",
    font=("Arial", 14)
)
result_label.pack(pady=15)

# Attempts label (bigger + visible)
attempts_label = ctk.CTkLabel(
    frame,
    text="",
    font=("Arial", 16, "bold")
)
attempts_label.pack()

app.mainloop()