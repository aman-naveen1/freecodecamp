import random

def player(prev_play, opponent_history = []):
    # If it's the first round, return a random choice
    if not prev_play:
        return random.choice(["R", "P", "S"])

    # Append the previous move to the opponent's history
    opponent_history.append(prev_play)
    
    # Count the frequency of the opponent's previous moves
    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        move_counts[move] += 1
    
    # Find the most frequent move of the opponent
    most_frequent_move = max(move_counts, key=move_counts.get)
    
    # Return the move that counters the most frequent opponent's move
    if most_frequent_move == "R":
        return "P"  # Paper beats Rock
    elif most_frequent_move == "P":
        return "S"  # Scissors beats Paper
    else:
        return "R"  # Rock beats Scissors
