player1_score= 250
player2_score=300

print("Player 1 scores:", player1_score)
print("Player 2 scores:", player2_score)

print("Did player 1 win?", player1_score>player2_score)

print("Leaderboard Before Update:")
print("Rank 1", player1_score)
print("Rank 2", player2_score)

temp=player1_score
player1_score=player2_score
player2_score=temp

print("Leaderboard After Update:")
print("Rank 1:", player1_score)
print("Rank 2:", player2_score)