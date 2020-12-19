
# parse the file and get the stats for the wanted team
# stats are GP, PF, PA respectively in the returned list
def teamToFile(filename, teamname):
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