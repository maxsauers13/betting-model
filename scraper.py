import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

GAME_LENTH = 16000
URL = 'https://il.sportsbook.fanduel.com/sports/navigation/6227.1/13348.3'

#open driver and get html as a string
def getHtml(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    driver.close()

    soup = BeautifulSoup(html, "html.parser")
    html_soup = soup.prettify()
    return html_soup

#get the starting index for each game on the page
#and get each game as a string
def getGamesHtml(html_soup):
    game_indices = [i.start() for i in re.finditer('class="event"', html_soup)]
    game_last = [i.start() for i in re.finditer('class="event last"', html_soup)]
    for  i in game_last:
        game_indices.append(i)

    game_strings = []
    for i in range(len(game_indices) - 1):
        game_strings.append(html_soup[game_indices[i]:game_indices[i + 1]])
    game_strings.append(html_soup[game_indices[len(game_indices) - 1]:game_indices[len(game_indices) - 1] + GAME_LENTH])
    return game_strings


#write to the games file
#f = open('games.txt', 'w')
#for game in game_strings:
#    f.write(game)
#f.close()

#create a list of dictionaries to hold all game odds and print them
def getLiveLines():
    game_slate = []
    game_strings = getGamesHtml(getHtml(URL))
    for game in game_strings:
        game_dict = {}

        f = open('game.txt', 'w')
        f.write(game)
        f.close()

        f = open('game.txt', 'r')
        lines = f.readlines()
        isAway = True
        for i in range(len(lines)):
            if 'class="name"' in lines[i]:
                i += 1
                if isAway:
                    game_dict['away'] = lines[i].strip()
                    isAway = False
                else:
                    game_dict['home'] = lines[i].strip()
                    isAway = True
            if 'class="currenthandicap"' in lines[i] and '!--' not in lines[i + 1] and 'had-value' not in lines[i + 1]:
                i += 1
                if isAway:
                    game_dict['awaySpread'] = lines[i].strip()
                    isAway = False
                    #find the odds line under the spread/over line
                    while 'class="selectionprice"' not in lines[i]:
                        i += 1
                    i += 1
                    game_dict['awaySpreadOdds'] = lines[i].strip()
                else:
                    game_dict['homeSpread'] = lines[i].strip()
                    isAway = True
                    while 'class="selectionprice"' not in lines[i]:
                        i += 1
                    i += 1
                    game_dict['homeSpreadOdds'] = lines[i].strip()
            if 'class="uo-currenthandicap"' in lines[i]:
                i += 1
                if isAway:
                    game_dict['over'] = '+' + lines[i].strip()
                    isAway = False
                    while 'class="selectionprice"' not in lines[i]:
                        i += 1
                    i += 1
                    game_dict['overOdds'] = lines[i].strip()
                else:
                    game_dict['under'] = '-' + lines[i].strip()
                    isAway = True
                    while 'class="selectionprice"' not in lines[i]:
                        i += 1
                    i += 1
                    game_dict['underOdds'] = lines[i].strip()
            if 'class="selectionprice"' in lines[i] and '!--' in lines[i - 1]:
                i += 1
                if isAway:
                    game_dict['awayMoney'] = lines[i].strip()
                    isAway = False
                else:
                    game_dict['homeMoney'] = lines[i].strip()
                    isAway = True

        game_slate.append(game_dict)
    return game_slate