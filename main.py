import fileReader
import montecarlo
import betting
import scraper
import time

def main():
    #team1 = 'Tampa Bay Buccaneers'
    #team2 = 'Detroit Lions'

    #team1percentage, team2percentage, team1scores, team2scores = montecarlo.monteCarlo(team1, team2)

    #ml1 = betting.moneyline(team1percentage)
    #ml2 = betting.moneyline(team2percentage)
    #spread = betting.spread(team1scores, team2scores)
    #team1spread = ml1[0] + str(spread)
    #team2spread = ml2[0] + str(spread)
    #over = str(betting.overUnder(team1scores, team2scores))

    #print("My Lines:")
    #print(team1 + ' ' + ml1 + ' ' + team1spread + ' +' + over)
    #print(team2 + ' ' + ml2 + ' ' + team2spread + ' -' + over)
    #print("")

    #print("Fanduel Lines:")
    gameSlate = scraper.getLiveLines()
    #for game in gameSlate:
        #print('Teams             Spread         ML     O/U')
        #if 'over' in game:
        #if len(game) == 12:
        #print(game['away'] + '  ' + game['awaySpread'] + ' (' + game['awaySpreadOdds'] + ')  ' + game['awayMoney'] + '  ' + game['over'] + ' (' + game['overOdds'] + ')')
        #print(game['home'] + '  ' + game['homeSpread'] + ' (' + game['homeSpreadOdds'] + ')  ' + game['homeMoney'] + '  ' + game['under'] + ' (' + game['underOdds'] + ')')
        #else:
            #print(game['away'] + '  ' + game['awaySpread'] + ' (' + game['awaySpreadOdds'] + ')  ' + game['awayMoney'])
            #print(game['home'] + '  ' + game['homeSpread'] + ' (' + game['homeSpreadOdds'] + ')  ' + game['homeMoney'])
        #print("")

    betting.middlingInit(gameSlate)
    for i in range(12):
        i = i
        time.sleep(600)
        betting.middling()

main()