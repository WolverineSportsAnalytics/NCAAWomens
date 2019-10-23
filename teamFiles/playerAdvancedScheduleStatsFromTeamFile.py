import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
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

def playerAdvancedAverages(soup, cursor, cnx, teamName):

    tables = soup.find_all("table")

    i = 18
    j = 19

    for table in tables[52:56]:
        print ("________________________________________________________________________________________________________________________")
        print ("Player Advanced Average Stats: ", i,"/",j," season")

        rows = table.find_all("tr")
        for row in rows[1:]:
            points = row.find_all("td")
            team = teamName

            fullName = points[0].text
            gamesPlayed = points[2].text
            minutes = points[3].text


            usagePercent = float(points[4].text)
            pointsPerScoringAttempt = points[5].text
            effectiveFieldGoalPercent = float(points[6].text)
            print effectiveFieldGoalPercent
            threePointRate = float(points[7].text)
            freeThrowRate = float(points[8].text)
            offensiveReboundPercent = float(points[9].text)
            defensiveReboundPercent = float(points[10].text)
            totalReboundPercent = float(points[11].text)
            assistPercent = float(points[12].text)
            turnoverPercent = float(points[13].text)
            assistsPerTurnover = points[14].text
            stealPercent = float(points[15].text)
            blockPercent = float(points[16].text)
            personalFoulPercent = float(points[17].text)
            season = (i + "/" + j)

            inserts = (team, fullName, gamesPlayed, fieldGoalsMade, fieldGoalsAttempt)

            insertStats = "INSERT INTO _______ (team, fullName, gamesPlayed, fieldGoalsAttempt,...there should be the same num of percent s's as variables created above) VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            # inserts the stats into whatever table is designated
            #cursor.execute(insertStats, inserts)
            #cnx.commit()
            print "Finished inserting data for: ", fullName

        i-=1
        j-=1

    return

def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    #html = open('herHoopStatsMichigan.htm').read()
    #soup = BeautifulSoup(html, 'html.parser')
<<<<<<< HEAD:Scrapers/playerAdvancedScheduleStatsFromTeamFile
    teams = ("Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin")
    
    open('teamFiles/herHoopStatsMichigan.htm').read()
    for team in teams:
        fileName = ("herHoopStats" + team + ".htm")
        print fileName
=======
>>>>>>> a861a1269ce46c91d5fc55e598882e439ad2a63a:teamFiles/playerAdvancedScheduleStatsFromTeamFile.py


    for subdir, dirs, files in os.walk("/Users/cindygu/Sports/WSA/NCAAWomens/teamFiles/NonConference"):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')
                teamName = getTeam(soup, cursor, cnx)
                playerAdvancedAverages(soup, cursor, cnx, teamName)
                print (filepath)
                # print(path_in_str)

        #fill in functions that want to be done for every team

    #playerBoxScores("Nicole MungerMichiganHerHoopsStats.htm", cursor, cnx, "Michigan", "Nicole Munger")


    return




if __name__=="__main__":
    main()
