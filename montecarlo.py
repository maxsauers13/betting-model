import fileReader
import math
import statistics
import random
from scipy.stats import norm

TEAMS = ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets', 'Pittsburgh Steelers', 'Cleveland Browns', 'Baltimore Ravens', 'Cincinnati Bengals', 'Indianapolis Colts', 'Tennessee Titans', 'Houston Texans', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Denver Broncos', 'Los Angeles Chargers', 'Washington Football Team', 'New York Giants', 'Philadelphia Eagles', 'Dallas Cowboys', 'Green Bay Packers', 'Minnesota Vikings', 'Chicago Bears', 'Detroit Lions', 'New Orleans Saints', 'Tampa Bay Buccaneers', 'Atlanta Falcons', 'Carolina Panthers', 'Los Angeles Rams', 'Seattle Seahawks', 'Arizona Cardinals', 'San Francisco 49ers']

def getAverages(teamName):
    totals = fileReader.getTotalsTeam('season-data.csv', teamName)
    averagePF = totals[1] / totals[0]
    averagePA = totals[2] / totals[0]
    
    return averagePF, averagePA

def getAdjPoints(team1, team2):
    team1avgPF, team1avgPA = getAverages(team1)
    team2avgPF, team2avgPA = getAverages(team2)
    adjPoints1 = math.sqrt(team1avgPF * team2avgPA)
    adjPoints2 = math.sqrt(team2avgPF * team1avgPA)

    return adjPoints1, adjPoints2

def getStDevPoints(teamName):
    scores = fileReader.getScoresTeam('games-data.csv', teamName)
    stDev = statistics.stdev(scores)

    return stDev

def getNorms(team1, team2):
    team1adj, team2adj = getAdjPoints(team1, team2)
    print(team1adj, team2adj)

    std1 = getStDevPoints(team1)
    std2 = getStDevPoints(team2)
    print(std1, std2)

    rand1 = random.random()
    rand2 = random.random()

    norm1 = 1 / norm.cdf(rand1)
    norm2 = 1 / norm.cdf(rand2)
    
    return norm1, norm2

a, b = getNorms('Jacksonville Jaguars', 'Tennessee Titans')
print(a, b)