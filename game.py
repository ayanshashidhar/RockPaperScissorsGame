import random

hands = {
    "rock": "🪨", 
    "paper": "📄",
    "scissors": "✂️"
}

player_score = 0
computer_score = 0

print("=== ROCK-PAPER-SCISSORS BATTLE ===")

while True:
    player = input("Choose (rock/paper/scissors): ").lower()
    computer = random.choice(list(hands.keys()))
    
    print(f"\nYou: {hands[player]}  vs  Computer: {hands[computer]}")
    
    if player == computer:
        print("TIE! Try again!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("YOU WIN! 😄")
        player_score += 1
    else:
        print("Computer wins! 🤖")
        computer_score += 1
    
    print(f"SCORE - You: {player_score} | Computer: {computer_score}")
    
    if input("\nPlay again? (y/n): ") != 'y':
        break


