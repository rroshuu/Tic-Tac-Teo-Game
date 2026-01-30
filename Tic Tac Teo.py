import tkinter as tk
import math

# Initialize board
board = [" " for _ in range(9)]
buttons = []

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"
    buttons[move].config(text="O", fg="red", state="disabled")

    if check_winner("O"):
        status_label.config(text="🤖 AI Wins!", fg="red")
        disable_all()
    elif is_draw():
        status_label.config(text="😐 It's a Draw!", fg="orange")

# Human move
def human_move(i):
    board[i] = "X"
    buttons[i].config(text="X", fg="blue", state="disabled")

    if check_winner("X"):
        status_label.config(text="🎉 You Win!", fg="green")
        disable_all()
        return
    elif is_draw():
        status_label.config(text="😐 It's a Draw!", fg="orange")
        return

    ai_move()

# Disable buttons
def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

# Reset game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")
    status_label.config(text="Your Turn (X)", fg="black")

# GUI window
root = tk.Tk()
root.title("🎮 Tic Tac Toe – Human vs AI")
root.geometry("350x450")
root.resizable(False, False)

# Heading
title = tk.Label(root, text="TIC TAC TOE", font=("Arial", 20, "bold"))
title.pack(pady=10)

status_label = tk.Label(root, text="Your Turn (X)", font=("Arial", 14))
status_label.pack(pady=5)

# Game frame
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(
        frame,
        text=" ",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        command=lambda i=i: human_move(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Arial", 12),
    command=reset_game
)
reset_btn.pack(pady=15)

root.mainloop()
