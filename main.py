import fileReader

def main():
    titans = fileReader.teamToFile('season-data.csv', 'Tennessee Titans')
    print(titans)

main()