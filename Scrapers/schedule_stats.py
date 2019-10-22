import mysql.connector
import requests
from bs4 import BeautifulSoup
import os

def getTeam(soup,cursor,cnx):
    i = 18
    j = 19

    print "________________________________________________________________________________________________________________________"
    print "Team Info: " + str(i) + "/" + str(j) + " season"
    list = soup.find('ul', {"class": "list-unstyled"})
    # puts the list items into an array
    list_items = list.findAll('li')
    # print list_items
    teamName = list_items[0].text
    return teamName

def scheduleStats(soup, cursor, cnx, teamName):

    #table 56 18/19 schedule
    #table 57 17/18 schedule
    #table 58 16/17 schedule
    #table 59 15/16 schedule

    tables = soup.find_all("table")

    i = 18
    j = 19
    for table in tables[56:60]:

        print "________________________________________________________________________________________________________________________"
        print "Schedule Stats: ", i,"/",j," season"
        rows = table.find_all("tr")
        for row in rows[1:]:

            points = row.find_all("td")
            date = points[0].text
            team = teamName
            if points[1].text == "H":
                home = 1
            else:
                home = 0
            opponent = points[3].text
            if points[5].text == "W":
                win = 1
            else:
                win = 0
            pointsScored = int(points[7].text)
            # print("Points Scored:" + str(pointsScored))
            pointsAllowed = int(points[8].text)
            # print("Points Allowed:" + str(pointsAllowed))
            margin = int(points[9].text)
            # print("Margin:" + str(margin))
            simpleRPI = int(points[12].text)
            # print("Simple RPI:" + str(simpleRPI))
            #inserts = (team, opponent, home,)

            #insertStats = "INSERT INTO _______ (fullName, gamesPlayed, fieldGoalsAttempt,...there should be the same num of percent s's as variables created above) VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            # inserts the stats into whatever table is designated
            #cursor.execute(insertStats, inserts)
            #cnx.commit()
            print "Finished inserting data for: ", teamName, " vs. ", opponent

        i-=1
        j-=1

    return

def teamStats(soup,cursor,cnx):
    i = 18
    j = 19

    print "________________________________________________________________________________________________________________________"
    print "Team Stats: " + str(i) + "/" + str(j) + " season"

    #finish filling in the inserts list with all the variables
    #inserts = (playerName, team, season, position, height, jerseyNum)

    #insertStats = "INSERT INTO playerReference (fullName, teamName, season, position, height, jerseyNumber) VALUES(%s, %s, %s, %s, %s, %s)"

    # inserts the stats into whatever table is designated
    #cursor.execute(insertStats, inserts)
    #cnx.commit()
    print "Finished inserting data for: "

    '''
    cleanUp = "DELETE FROM _____ WHERE blocks IS NULL"
    cursor.execute(cleanUp)
    cnx.commit()
    '''
    return



def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    for subdir, dirs, files in os.walk("/Users/cindygu/Sports/WSA/NCAAWomens/teamFiles"):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')
                teamName = getTeam(soup, cursor, cnx)
                scheduleStats(soup, cursor, cnx, teamName)
                print (filepath)
                # print(path_in_str)
    '''fileName = 'lakenwairau.htm'
    print fileName
    html = open(fileName).read()
    soup = BeautifulSoup(html, 'html.parser')
    teamStats(soup, cursor, cnx)
    cursor.close()
    cnx.commit()
    cnx.close()
    '''

    return



if __name__=="__main__":
    main()
