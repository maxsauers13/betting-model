import montecarlo

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