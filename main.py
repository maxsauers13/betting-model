import fileReader
import montecarlo
import betting
import scraper
import time

# FILENAME = 'nba-games.txt'
FILENAME = 'nfl-games.txt'

def main():
    lines = []
    lines.append(betting.makeLines(FILENAME, 'Los Angeles Rams', 'Green Bay Packers'))
    lines.append(betting.makeLines(FILENAME, 'Baltimore Ravens', 'Buffalo Bills'))
    lines.append(betting.makeLines(FILENAME, 'Cleveland Browns', 'Kansas City Chiefs'))
    lines.append(betting.makeLines(FILENAME, 'Tampa Bay Buccaneers', 'New Orleans Saints'))
    print("My Lines:")
    for game in lines:
        print('Teams           Spread  ML  O/U')
        print(game[0][0] + '  ' + game[0][1] + '  ' + game[0][2] + '  ' + game[0][3])
        print(game[1][0] + '  ' + game[1][1] + '  ' + game[1][2] + '  ' + game[1][3])
        print("")

    print("Fanduel Lines:")
    gameSlate = scraper.getLiveLines()
    for game in gameSlate:
        print('Teams           Spread  ML  O/U')
        print(game['away'] + '  ' + game['awaySpread'] + '  ' + game['awayMoney'] + '  ' + game['over'])
        print(game['home'] + '  ' + game['homeSpread'] + '  ' + game['homeMoney'] + '  ' + game['under'])
        print("")

    # UNCOMMENT BELOW FOR MIDDLING FUNCTIONALITY
    #betting.middlingInit(gameSlate)
    #for i in range(60):
    #    print(i)
    #    time.sleep(60)
    #    betting.middling()

main()