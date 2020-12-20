import fileReader
import montecarlo
import betting

def main():
    team1 = 'Chicago Bears'
    team2 = 'Minnesota Vikings'

    team1percentage, team2percentage, team1scores, team2scores = montecarlo.monteCarlo(team1, team2)

    ml1 = betting.moneyline(team1percentage)
    ml2 = betting.moneyline(team2percentage)
    spread = betting.spread(team1scores, team2scores)
    team1spread = ml1[0] + str(spread)
    team2spread = ml2[0] + str(spread)
    over = str(betting.over(team1scores, team2scores))

    print(team1 + ' ' + ml1 + ' ' + team1spread + ' +' + over)
    print(team2 + ' ' + ml2 + ' ' + team2spread + ' -' + over)

main()