import fileReader
import math
import statistics
import random
from scipy.stats import norm

TEAMS = ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets', 'Pittsburgh Steelers', 'Cleveland Browns', 'Baltimore Ravens', 'Cincinnati Bengals', 'Indianapolis Colts', 'Tennessee Titans', 'Houston Texans', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Denver Broncos', 'Los Angeles Chargers', 'Washington Football Team', 'New York Giants', 'Philadelphia Eagles', 'Dallas Cowboys', 'Green Bay Packers', 'Minnesota Vikings', 'Chicago Bears', 'Detroit Lions', 'New Orleans Saints', 'Tampa Bay Buccaneers', 'Atlanta Falcons', 'Carolina Panthers', 'Los Angeles Rams', 'Seattle Seahawks', 'Arizona Cardinals', 'San Francisco 49ers']
MONTE_CARLO_ITERATIONS = 10000

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

    std1 = getStDevPoints(team1)
    std2 = getStDevPoints(team2)

    rand1 = random.random()
    rand2 = random.random()

    norm1 = norm.ppf(rand1, team1adj, std1)
    norm2 = norm.ppf(rand2, team2adj, std2)
    
    return norm1, norm2

def monteCarlo(team1, team2):
    team1wins = 0
    team1scores = []
    team2wins = 0
    team2scores = []

    count = 0
    while count < MONTE_CARLO_ITERATIONS:
        team1score, team2score = getNorms(team1, team2)

        if team1score > team2score:
            team1wins += 1
        else:
            team2wins += 1
        
        team1scores.append(team1score)
        team2scores.append(team2score)
        count += 1
    
    return (team1wins / MONTE_CARLO_ITERATIONS) * 100, (team2wins / MONTE_CARLO_ITERATIONS) * 100, team1scores, team2scores