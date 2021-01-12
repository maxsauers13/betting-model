# parse the file and get the stats for the entire league
# stats are GP, PF, PA respectively for each team in
# the 2D list returned
def getTotalsLeague(fileName):
    output = []
    file = open(fileName, 'r')
    teams = file.read().split('}}')
    teams.pop(len(teams) - 1)
    
    for team in teams:
        team_data = []
        team_list = team.split(',')
        passed = False
        # parse through each team's data and gather all the necessary parts
        for data in team_list:
            data_split = data.split(':')
            if '"Team"' == data_split[0] and data_split[1][1:len(data_split[1]) - 1] not in team_data:
                team_data.append(data_split[1][1:len(data_split[1]) - 1])
            elif '"Wins"' == data_split[0] and not passed:
                team_data.append(float(data_split[1]))
            elif '"Losses"' == data_split[0] and not passed:
                team_data[1] += float(data_split[1])
                passed = True
            elif '"Points"' == data_split[0]:
                team_data.append(float(data_split[1]))

        output.append(team_data)
    return output

# use the getTotalsLeague function to get the stats
# for a certain team and returns a 1D list
# stats are GP, PF, PA respectively in the returned list
def getTotalsTeam(fileName, teamName):
    league_stats = getTotalsLeague(fileName)
    for team in league_stats:
        if teamName in team:
            return team[1:]

# get a 2D list of all the scores for a team
# points for and points against respectively
def getScoresTeam(filename, teamname):
    points_for = []
    points_against = []
    file = open(filename, 'r')
    lines = file.readlines()
    
    teamindex = 0
    opponentindex = 0
    if filename == 'nba-games.txt':
        teamindex = 1
        opponentindex = 3
    else:
        teamindex = 3
        opponentindex = 4

    for line in lines:
        line_list = line.split(',')
        # add part for nfl file
        if line_list[0] == teamname:
            points_for.append(int(line_list[teamindex]))
            points_against.append(int(line_list[opponentindex]))
        if line_list[2] == teamname:
            points_for.append(int(line_list[opponentindex]))
            points_against.append(int(line_list[teamindex]))
    
    output = []
    output.append(points_for)
    output.append(points_against)
    return output