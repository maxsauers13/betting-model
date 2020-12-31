import montecarlo
import scraper

# determine moneyline odds from a winning percentage
def moneyline(percentage):
    output = 0

    if percentage > 50:
        output = int((percentage / (100 - percentage)) * -100)
        return str(output)
    else:
        output = int(((100 - percentage) / percentage) * 100)
        return '+'+str(output)
    

# determine the spread using past scores for each team
def spread(scores1, scores2):
    differences = []

    for i in range(len(scores1)):
        differences.append(abs(scores1[i] - scores2[i]))
    
    return sum(differences) // len(differences)

# determine the over/under line using past scores
def overUnder(scores1, scores2):
    avg1 = sum(scores1) / len(scores1)
    avg2 = sum(scores2) / len(scores2)

    return int(avg1 + avg2)

def middlingInit(games):
    f = open('bets.txt', 'w')
    for game in games:
        #bet initially on all the favorite lines and overs and write them to bets.txt
        awaySpread = game['awaySpread']
        homeSpread = game['homeSpread']
        if awaySpread[0] == '-':
            f.write(game['away'] + ',' + awaySpread + ',' + game['awaySpreadOdds'])
            f.write('\n')
        else:
            f.write(game['home'] + ',' + homeSpread + ',' + game['homeSpreadOdds'])
            f.write('\n')
        
        f.write(game['away'] + ',' + game['home'] + ',' + game['over'] + ',' + game['overOdds'])
        f.write('\n')

def middling():
    games = scraper.getLiveLines()
    fr = open('bets.txt', 'r')
    lines = fr.readlines()
    for i in range(len(games)):
        #check if the lines in each game allows for a middle bet
        game = games[i]
        initGame = lines[i * 2].split(',')
        initSpread = initGame[1]
        #check if the betted team is home or away and if they are favorites or underdogs
        if game['away'] == initGame[0]:
            print('away')
            if initSpread[0] == '-':
                print('favorite')
                if float(game['awaySpread']) < float(initSpread):
                    print('test')
                    fw = open('bets.txt', 'a')
                    fw.write(game['away'] + ',' + game['awaySpread'] + ',' + game['awaySpreadOdds'])
                    fw.write('\n')
            else:
                print('underdog')
                initSpread = float(initSpread[1:])
                if float(game['awaySpread']) > initSpread:
                    print('test')
                    fw = open('bets.txt', 'a')
                    fw.write(game['away'] + ',' + game['awaySpread'] + ',' + game['awaySpreadOdds'])
                    fw.write('\n')

        else:
            print('home')
            if initSpread[0] == '-':
                print('favorite')
                if float(game['homeSpread']) < float(initSpread):
                    print('test')
                    fw = open('bets.txt', 'a')
                    fw.write(game['home'] + ',' + game['homeSpread'] + ',' + game['homeSpreadOdds'])
                    fw.write('\n')
            else:
                print('underdog')
                initSpread = float(initSpread[1:])
                if float(game['homeSpread']) > initSpread:
                    print('test')
                    fw = open('bets.txt', 'a')
                    fw.write(game['home'] + ',' + game['homeSpread'] + ',' + game['homeSpreadOdds'])
                    fw.write('\n')

        #check if the over/under bet allows for middling
        initGame = lines[(i * 2) + 1].split(',')
        initOU = initGame[2]
        if initOU[0] == '+':
            print('over')
            initOU = float(initOU[1:])
            over = game['over']
            if float(over[1:]) > initOU:
                print('test')
                fw = open('bets.txt', 'a')
                fw.write(game['away'] + ',' + game['home'] + ',' + game['under'] + ',' + game['underOdds'])
                fw.write('\n')
        else:
            print('under')
            initOU = float(initOU[1:])
            under = game['under']
            if float(under[1:]) < initOU:
                print('test')
                fw = open('bets.txt', 'a')
                fw.write(game['away'] + ',' + game['home'] + ',' + game['over'] + ',' + game['overOdds'])
                fw.write('\n')