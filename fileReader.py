TEAMS = ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets', 'Pittsburgh Steelers', 'Cleveland Browns', 'Baltimore Ravens', 'Cincinnati Bengals', 'Indianapolis Colts', 'Tennessee Titans', 'Houston Texans', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Denver Broncos', 'Los Angeles Chargers', 'Washington Football Team', 'New York Giants', 'Philadelphia Eagles', 'Dallas Cowboys', 'Green Bay Packers', 'Minnesota Vikings', 'Chicago Bears', 'Detroit Lions', 'New Orleans Saints', 'Tampa Bay Buccaneers', 'Atlanta Falcons', 'Carolina Panthers', 'Los Angeles Rams', 'Seattle Seahawks', 'Arizona Cardinals', 'San Francisco 49ers']

# parse the file and get the stats for the wanted team
# stats are GP, PF, PA respectively in the returned list
def getTotalsTeam(filename, teamname):
    output = []
    file = open(filename, 'r')
    lines = file.readlines()

    for line in lines:
        spl_line = line.split(',')
        if spl_line[0] == teamname:
            output.append(int(spl_line[1]) + int(spl_line[2]) + int(spl_line[3]))
            output.append(int(spl_line[5]))
            output.append(int(spl_line[6]))
    
    return output

# use the getTotalsTeam function to get the stats
# for every team in the league and returns a 2D list
def getTotalsLeague(filename):
    output = []

    for team in TEAMS:
        output.append(getTotalsTeam(filename, team))

    return output

# get a list of all the scores for a team
def getScoresTeam(filename, teamname):
    output = []
    file = open(filename, 'r')
    lines = file.readlines()

    for line in lines:
        spl_line = line.split(',')
        if spl_line[0] == teamname:
            output.append(int(spl_line[1]))
    
    return output