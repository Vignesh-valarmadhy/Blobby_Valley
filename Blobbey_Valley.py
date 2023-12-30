def find_scores(game_results):
    alice_score = 0
    bob_score = 0
    is_alice_serving = True

    for result in game_results:
        if is_alice_serving:
            if result == 'A':
                alice_score += 1
            else:
                is_alice_serving = False  # Switch roles
        else:
            is_alice_serving = True  # Switch roles

    return alice_score, bob_score

# Example usage:
game_results = "ABAABBA"
alice_score, bob_score = find_scores(game_results)
print("Alice's score:", alice_score)
print("Bob's score:", bob_score)
