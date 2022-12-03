## Task 1 &  Task 2

#A - rock           Y-rock
#B - paper          X-paper
#C - scissors       Z-scissors

# Total score is the sum of your scores for each round
# Plus the score of the outcome of the round (0 if lost, 3 for draw , 6 for win)

# Rock == 1, paper == 2 , scissors == 3

def mapValues(play):
    play = play.strip()
    if play == 'A' or play == 'X':
        value = 1
    if play == 'B' or play == 'Y':
        value = 2
    if play == 'C' or play == 'Z':
        value = 3
    return value


def gameResult(line):
    line = line.split(" ")

    opponent = line[0]
    opponentResult = mapValues(opponent)
    you = line[1]
    youResult = mapValues(you)

    ## These are all the play situations covered (basically a matrix of conditions)
    if youResult == 1 and opponentResult == 3:
        # Score for the round + the shape i selected
        score = 6 + youResult
    elif youResult == 3 and opponentResult == 1:
        score = 0 + youResult
    elif opponentResult == youResult:
        score = 3 + youResult
    elif opponentResult > youResult:
        score = 0 + youResult
    elif opponentResult < youResult:
        score = 6 + youResult
    return score



def task1():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
        total = []
        # Start parsing -
        for line in lines:
            #print(line.strip())

            # Calculate win or loss
            score = gameResult(line)
            print(score)
            total.append(score)
            #print(score)
        print("Total: ",sum(total))

## Correct 13682


## Task 2

# The round needs to end X - lose Y - draw Z -win

def gameResult2(line):
    line = line.split(" ")

    opponent = line[0]
    opponentResult = mapValues(opponent)
    youExpected = mapValues(line[1].strip())

    ## Here check whats the expected result, then think of the appropriate moves that would deliver the win/lose/draw/ then play out scoring
    # Y = lose
    print(youExpected)
    if youExpected == 1: #lose
        if opponentResult == 1:
            youResult = 3
        if opponentResult == 2:
            youResult = 1
        if opponentResult == 3:
            youResult = 2

    if youExpected == 2: #draw
        youResult = opponentResult

    if youExpected == 3: #win
        if opponentResult == 1:
            youResult = 2
        if opponentResult == 2:
            youResult = 3
        if opponentResult == 3:
            youResult = 1
    print(youResult)

    ## These are all the play situations covered (basically a matrix of conditions)
    if youResult == 1 and opponentResult == 3:
        # Score for the round + the shape i selected
        score = 6 + youResult
    elif youResult == 3 and opponentResult == 1:
        score = 0 + youResult
    elif opponentResult == youResult:
        score = 3 + youResult
    elif opponentResult > youResult:
        score = 0 + youResult
    elif opponentResult < youResult:
        score = 6 + youResult
    return score

def task2():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
        total = []
        # Start parsing -
        for line in lines:
            #print(line.strip())

            # Calculate win or loss
            score = gameResult2(line)
            print(score)
            total.append(score)
            #print(score)
    print("Total: ",sum(total))

    return

if __name__ == '__main__':
    #task1()
    task2()