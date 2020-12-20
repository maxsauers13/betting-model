import fileReader

def main():
    titans = fileReader.getScoresTeam('games-data.csv', 'Tennessee Titans')
    print(titans)
    nfl = fileReader.getTotalsLeague('season-data.csv')
    print(len(nfl))

main()