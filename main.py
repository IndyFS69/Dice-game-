from random import randint




def RollDice():
    # rolls a dice -- generates a random number between 1 and 6
    x = randint(1, 6)
    return x


def winnersScore(y):
    y = str(y)
    f = open("WINNERS.txt", "a")
    f.write("\n")
    f.write(y)
    f.close()
x = 0
counter = 0
while x == 0:

    print("please enter a valid username and password below")
    username = input("Username: ")
    password = input("Password: ")
    f = open("AUTHENTICATION.txt", "r")
    y = f.read()
    listofUsernames = y.split(" ")
    for i in range(0, len(listofUsernames)):
       if username == listofUsernames[i] and password == listofUsernames[i + 1]:
        print("valid")
        # need to close the file.
        x = 1
    #this is to stop brute forcing
    #so after 5 failed atempts of entering a valid username and password the program will stop:
    counter += 1
    if counter == 5:
        raise ValueError("you have tried and failed too many times.")
try: x == 1
except ValueError(e):
    print(e)
p1FinalScore = 0
p2FinalScore = 0
#generates the random number:
for i in range(1, 5):
    p1Roll3 = 0
    p2Roll3 = 0
    p1Roll1 = RollDice()
    p1Roll2 = RollDice()
    p2Roll1 = RollDice()
    p2Roll2 = RollDice()
    if p1Roll1 == p1Roll2:
        p1Roll3 = RollDice()
    if p2Roll1 == p2Roll2:
        p2Roll3 = RollDice()
    p1Score = p1Roll1 + p1Roll2 + p1Roll3
    p2Score = p2Roll1 + p2Roll2 + p2Roll3
    if p1Score % 2 == 0:
        p1Score += 10
    else:
        p1Score -= 5
    if p2Score % 2 == 0:
        p2Score += 10
    else:
        p2Score -= 5

    # stops the score going below 0
    if p1Score < 0:
        p1Score = 0
    if p2Score < 0:
        p2Score = 0

    print("Player 1's score is currently: ", p1Score)
    print("Player 2's score is currently: ", p2Score)
    p1FinalScore += p1Score
    p2FinalScore += p2Score
while p1FinalScore == p2FinalScore:
    print("\nYour scores are the same so lets roll again\n")
    p1FinalScore += RollDice()
    p2FinalScore += RollDice()
print("\nPlayer 1's final score is", p1FinalScore)
print("Player 2's final score is", p2FinalScore)

if p1FinalScore > p2FinalScore:
    winnersScore(username)
    winnersScore(p1FinalScore)
else:
    winnersScore(username)
    winnersScore(p2FinalScore)

winnerLinesRaw = open("WINNERS.txt", "r").readlines()
winnerLines = []
for i in winnerLinesRaw:
    winnerLines.append(i.strip())
del winnerLinesRaw, winnerLines[0]

best = [-1, "no", -1]
for i in range(1, len(winnerLines) + 1, 2):
    if int(winnerLines[i]) > best[0]: best = [int(winnerLines[i]), winnerLines[i - 1], i]

list_a = []
f = open("WINNERS.txt", 'r').readlines()
for line in f:
    list_a.append(line.strip())
del list_a[0], f, line

list_paired = []
for i in range(0, len(list_a), 2):
    list_paired.append([list_a[i], list_a[i + 1]])

list_paired.sort(key=lambda x: int(x[1]), reverse=True)

print("\nThe top 5 highest previous scores are:\n")
for i in range(0, 5):
    print(str(i + 1) + ". " + str(list_paired[i]))
