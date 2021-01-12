import fileReader
import math
import statistics
import random
from scipy.stats import norm

MONTE_CARLO_ITERATIONS = 2000

# get the average points forced and against for a team
def getAverages(fileName, teamName):
    points = fileReader.getScoresTeam(fileName, teamName)
    averagePF = sum(points[0]) / len(points[0])
    averagePA = sum(points[1]) / len(points[1])
    
    return averagePF, averagePA

# get the adjusted points scored for two opposing teams
def getAdjPoints(fileName, team1, team2):
    team1avgPF, team1avgPA = getAverages(fileName, team1)
    team2avgPF, team2avgPA = getAverages(fileName, team2)
    adjPoints1 = math.sqrt(team1avgPF * team2avgPA)
    adjPoints2 = math.sqrt(team2avgPF * team1avgPA)

    return adjPoints1, adjPoints2

# get the standard deviation for the scores of a team
def getStDevPoints(fileName, teamName):
    scores = fileReader.getScoresTeam(fileName, teamName)
    stDev = statistics.stdev(scores[0])

    return stDev

# get the probability density function for opposing teams
def getNorms(fileName, team1, team2):
    team1adj, team2adj = getAdjPoints(fileName, team1, team2)

    std1 = getStDevPoints(fileName, team1)
    std2 = getStDevPoints(fileName, team2)

    rand1 = random.random()
    rand2 = random.random()

    norm1 = norm.ppf(rand1, team1adj, std1)
    norm2 = norm.ppf(rand2, team2adj, std2)
    
    return norm1, norm2

# perform monte carlo machine learning method
def monteCarlo(fileName, team1, team2):
    team1wins = 0
    team1scores = []
    team2wins = 0
    team2scores = []

    count = 0
    while count < MONTE_CARLO_ITERATIONS:
        team1score, team2score = getNorms(fileName, team1, team2)

        if team1score > team2score:
            team1wins += 1
        else:
            team2wins += 1
        
        team1scores.append(team1score)
        team2scores.append(team2score)
        count += 1
    
    return (team1wins / MONTE_CARLO_ITERATIONS) * 100, (team2wins / MONTE_CARLO_ITERATIONS) * 100, team1scores, team2scores