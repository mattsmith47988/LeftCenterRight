import random
import time
start_time = time.time()
players = []
times_won = []
dice_rolls = 0
total_players = 20
total_iterations = 100000.0

total_rounds = 0.0

for x in range(total_players):
    players.append(3)
    times_won.append(0.0)
    #print "Player " + str(x + 1) + " has 3 chips\n"
iterations = 0

#Simulates specified number of games
while iterations < total_iterations:
    #print "BEGINNING GAME #" + str(iterations + 1)
    game_won = False
    empty_players = 0
    rounds = 0

    #Reinitialize chip counts
    for x in range (total_players):
        players[x] = 3

    #Runs a single game
    while (game_won == False):
        rounds = rounds + 1
        for x in range(total_players):
            #Check if player has any chips and determine how many times they should roll
            if players[x] > 0:
                if players[x] > 3:
                    times_to_roll = 3
                else:
                    times_to_roll = players[x]
                #for n in range (total_players):
                    #print "\t\t\tPlayer " + str(n + 1) + " has " + str(players[n]) + " chips"

                for y in range(times_to_roll):
                    roll = random.randrange(1,7)
                    if roll <= 3:
                        #print "Player " + str(x + 1) + " rolled a dot"
                        dice_rolls = dice_rolls + 1
                        continue
                    #Roll of 'C'
                    elif roll == 4:
                        players[x] = players[x] - 1
                        #print "Player " + str(x+1) + " rolled a C"
                        dice_rolls = dice_rolls + 1
                    #Roll of 'L'
                    elif roll == 5:
                        players[x] = players[x] - 1
                        if x == 0:
                            players[(total_players-1)] = players[(total_players-1)] + 1
                        else:
                            players[x-1] = players[x-1] + 1
                        dice_rolls = dice_rolls + 1
                        #print "Player " + str(x + 1) + " rolled an L"
                    #Roll of 'R'
                    elif roll == 6:
                        players[x] = players[x] - 1
                        if x == (total_players-1):
                            players[0] = players[0] + 1
                        else:
                            players[x + 1] = players[x + 1] + 1
                        #print "Player " + str(x + 1) + " rolled an R"
                        dice_rolls = dice_rolls + 1
            #Check to see whether chips belong to one player
            for z in range(total_players):
                if players[z] == 0:
                    empty_players = empty_players + 1
            if empty_players == (total_players-1):
                for a in range(total_players):
                    if players[a] > 0:
                        #print "Player " + str(a+1) + " won!"
                        times_won[a] = times_won[a] + 1
                game_won = True
                iterations = iterations + 1
                total_rounds = total_rounds + rounds
                #print "Game won in " + str(rounds) + " rounds!"
                break
            else:
                empty_players = 0
print "\nSimulation over.\n"

end_time = time.time()
total_time = end_time - start_time

text_file = open("Output.txt", "w")
for x in range(total_players):
    percent_won = 100.0*((times_won[x])/total_iterations)
    print "Times won for Player " + str(x+1) + ": " + str(times_won[x]) + "(" + str(percent_won) + "%)"
    text_file.write(str(x+1) + "\t" + str(times_won[x]) + "\n")
text_file.close()

print "\nExecuted in " + str(total_time) + " seconds " + "(" + str(total_iterations/total_time) + " games per second)"
print "\nAverage rounds per game: " + str(total_rounds / total_iterations)
print "\nAverage dice rolls per game: " + str(dice_rolls/total_iterations)