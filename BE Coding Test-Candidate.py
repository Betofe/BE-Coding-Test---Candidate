# stored team names in a list

teams = ["tarantulas", "lions", "fc awesome", "snakes", "grouches"]

# initialized variable to store points of each team, both start with 0 points
tarantulas = 0
lions = 0
fcawesome = 0
snakes = 0
grouches = 0

# creating a list to be storing points
points = []

# creating a two dimensional list to store both teams and points respectively

matches = [teams, points]

# loping through for the user to enter the team names and scores

i = 1
while i < 6:
    print("Match" + str(i))
    team1 = input("Enter first team: ")
    score1 = input("Enter first score: ")
    team2 = input("Enter second team: ")
    score2 = input("Enter second score: ")

    print("-----------------------------")

# all matches have three conditions in which a win is 3 points, null 1 point, and loss 0 point

    if team1 == 'lions' and team2 == 'snakes':
        if score1 > score2:
            lions = lions + 3
        elif score1 == score2:
            lions = lions + 1
            snakes = snakes + 1
        elif score1 < score2:
            snakes = snakes + 3
    elif team1 == 'lions' and team2 == 'fc awesome':
        if score1 > score2:
            lions = lions + 3
        elif score1 == score2:
            lions = lions + 1
            fcawesome = fcawesome + 1
        elif score1 < score2:
            fcawesome = fcawesome + 3
    elif team1 == 'lions' and team2 == 'grouches':
        if score1 > score2:
            lions = lions + 3
        elif score1 == score2:
            lions = lions + 1
            grouches = grouches + 1
        elif score1 < score2:
            grouches = grouches + 1
    elif team1 == 'tarantulas' and team2 == 'fc awesome':
        if score1 > score2:
            tarantulas = tarantulas + 3
        elif score1 == score2:
            tarantulas = tarantulas + 1
            fcawesome = fcawesome + 1
        elif score1 < score2:
            fcawesome = fcawesome + 3
    elif team1 == 'tarantulas' and team2 == 'snakes':
        if score1 > score2:
            tarantulas = tarantulas + 3
        elif score1 == score2:
            tarantulas = tarantulas + 1
            snakes = snakes + 1
        elif score1 < score2:
            snakes = snakes + 3
    else:
        print("Incorrect value")
    i = i + 1

# adding the points in the list variable initialized above

points.append(tarantulas)
points.append(lions)
points.append(snakes)
points.append(fcawesome)
points.append(grouches)
points.sort(reverse=True)

# loop through the teams and scores to display the final output

for k in range(len(teams)):
    print(f"{matches[0][k]} , {matches[1][k]} pts")
