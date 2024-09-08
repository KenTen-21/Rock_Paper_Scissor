import random
import tkinter as tk
from tkinter import messagebox

# Initialize variables
wins = 0
losses = 0
ties = 0
total_games = 0

# Game logic functions
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    global wins, losses, ties
    if player_choice == computer_choice:
        ties += 1
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        wins += 1
        return "You win!"
    else:
        losses += 1
        return "You lose!"

def update_stats():
    global total_games
    total_games = wins + losses + ties
    stats_label.config(text=f"Games Played: {total_games}\nWins: {wins}\nLosses: {losses}\nTies: {ties}")

def play_game(player_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    update_stats()

def end_game():
    messagebox.showinfo("Game Over", f"Final Stats:\nGames Played: {total_games}\nWins: {wins}\nLosses: {losses}\nTies: {ties}")
    root.destroy()

def restart_game():
    global wins, losses, ties, total_games
    wins = 0
    losses = 0
    ties = 0
    total_games = 0
    result_label.config(text="")
    computer_choice_label.config(text="")
    update_stats()

# Create GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

instructions = tk.Label(root, text="Choose Rock 🪨, Paper 📄, or Scissors ✂️.", fg="black", bg="aqua", font=("Helvetica", 16, "underline"))
instructions.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

rock_button = tk.Button(buttons_frame, text="Rock 🪨", font=("Helvetica", 16), bg="gray", fg="white", command=lambda: play_game('rock'))
rock_button.grid(row=0, column=0)

paper_button = tk.Button(buttons_frame, text="Paper 📄", font=("Helvetica", 16), bg="white", fg="black", command=lambda: play_game('paper'))
paper_button.grid(row=0, column=1)

scissors_button = tk.Button(buttons_frame, text="Scissors ✂️", font=("Helvetica", 16), bg="red", fg="white", command=lambda: play_game('scissors'))
scissors_button.grid(row=0, column=2)

computer_choice_label = tk.Label(root, text="", font=("Helvetica", 16))
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()

stats_label = tk.Label(root, text="Games Played: 0\nWins: 0\nLosses: 0\nTies: 0", font=("Helvetica", 16), bd=1, relief="solid", bg="yellow", fg="black")
stats_label.pack()

end_button = tk.Button(root, text="End Game", font=("Helvetica", 16), bg="black", fg="white", command=end_game)
end_button.pack()

restart_button = tk.Button(root, text="Restart Game", font=("Helvetica", 16), bg="blue", fg="white", command=restart_game)
restart_button.pack()

# Run the main loop
root.mainloop()