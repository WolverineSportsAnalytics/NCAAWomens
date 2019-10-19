import mysql.connector
import requests
from bs4 import BeautifulSoup



def get_combine_data(soup):
    i = 1
    tables = soup.find_all("table")
    for table in tables:
        print "table number", i

        rows = table.find_all("tr")
        print rows[0].text
        print "________________________________________________________________________________________________________________________"
        i+=1
        

    return

def variousTeamStats(soup):
    
    tables = soup.find_all("table")

    rows = tables[1].find_all("tr")
    for row in rows:
        print row.text

def playerAverages(soup,curosr,cnx, teamName):

    tables = soup.find_all("table")

    i = 18
    j = 19

    for table in tables[48:52]:
        print "________________________________________________________________________________________________________________________"
        print "Player Average Stats: ", i,"/",j," season"

        rows = table.find_all("tr")
        for row in rows[1:]:
            points = row.find_all("td")
            team = teamName
            
            fullName = points[0].text
            gamesPlayed = points[2].text
            minutes = points[3].text
            fieldGoalsMade = points[4].text
            # can someone increment the rest?
            # we also need to figure out what to do if a player has empty categories aka are bench players that never played
            '''
            fieldGoalsAttempt = 
            fieldGoalPercent = 
            twoPointMade = 
            twoPointAttempt = 
            twoPointPercent = 
            threePointMade = 
            threePointAttempt = 
            threePointPercent = 
            freeThrowMade = 
            freeThrowAttempt = 
            freeThrowPercent = 
            offensiveRebound = 
            defensiveRebound = 
            totalRebound = 
            assist = 
            turnover = 
            steal = 
            block = 
            personalFoul = 
            pointsScored = 
            season = (i + "/" + j)
            '''
            #finish filling in the inserts list with all the variables
            inserts = (team, fullName, gamesPlayed, fieldGoalsMade, fieldGoalsAttempt)

            insertStats = "INSERT INTO _______ (team, fullName, gamesPlayed, fieldGoalsAttempt,...there should be twenty six variables) VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            # inserts the stats into whatever table is designated
            cursor.execute(insertStats, inserts) 
            cnx.commit()
            print "Finished inserting data for: ", fullName

        i-=1
        j-=1
    '''
    cleanUp = "DELETE FROM _____ WHERE blocks IS NULL"
    cursor.execute(cleanUp)
    cnx.commit()
    '''
    return

def playerBoxScores(fileName, cursor, cnx, teamName, playerName):

    html = open(fileName).read()
    soup = BeautifulSoup(html, 'html.parser')

    i = 18
    j = 19
    tables = soup.find_all("table")
    for table in tables[24:28]:
        rows = table.find_all("tr")
        for row in rows[1:]:
            point = row.find_all("td")
            fullName = playerName
            team = teamName
            season = (str(i) + "/" + str(j))
            date = point[0].text
            opponent = point[2].text
            if point[3] == "H":
                home = 1
            else:
                home = 0
            minutes = point[5].text
            pointsScored = point[6].text
            fieldGoalMade = point[7].text
            fieldGoalAttempt = point[8].text
            fieldGoalPercent = point[9].text
            threePointMade = point[10].text
            threePointAttempt = point[11].text
            threePointPercent = point[12].text
            freeThrowMade = point[13].text
            freeThrowAttempt = point[14].text
            freeThrowPercent = point[15].text
            offensiveRebound = point[16].text
            defensiveRebound = point[17].text
            totalRebound = point[18].text
            assist = point[19].text
            turnover = point[20].text
            steal = point[21].text
            block = point[22].text
            personalFoul = point[23].text

            inserts = (fullName,team,date,season,opponent,home, minutes, pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threePointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,turnover,steal,block,personalFoul)

            insertStats = "INSERT INTO performancePlayer (fullName,team,date,season,opponent,home, minutes, pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threePointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,turnover,steal,block,personalFoul) VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
            
            print fieldGoalPercent
            
            print "Right before insert statement"
            cursor.execute(insertStats, inserts) 
            cnx.commit()
            print "Finished inserting data for: ", fullName
    
        i-= 1
        j-=1


    return

def playerAdvancedAverages(soup, cursor, cnx, teamName):

    tables = soup.find_all("table")

    i = 18
    j = 19

    for table in tables[52:56]:
        print "________________________________________________________________________________________________________________________"
        print "Player Advanced Average Stats: ", i,"/",j," season"

        rows = table.find_all("tr")
        for row in rows[1:]:
            points = row.find_all("td")
            team = teamName

            fullName = points[0].text
            gamesPlayed = points[2].text
            minutes = points[3].text
            fieldGoalsMade = points[4].text
            '''
            usagePercent = 
            pointsPerScoringAttempt = 
            effectiveFieldGoalPercent = 
            threePointRate = 
            freeThrowRate = 
            offensiveReboundPercent = 
            defensiveReboundPercent = 
            totalReboundPercent = 
            assistPercent = 
            turnoverPercent = 
            assistsPerTurnover = 
            stealPercent = 
            blockPercent = 
            personalFoulPercent = 
            season = (i + "/" + j)
            '''
            inserts = (team, fullName, gamesPlayed, fieldGoalsMade, fieldGoalsAttempt)

            insertStats = "INSERT INTO _______ (team, fullName, gamesPlayed, fieldGoalsAttempt,...there should be the same num of percent s's as variables created above) VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            # inserts the stats into whatever table is designated
            cursor.execute(insertStats, inserts) 
            cnx.commit()
            print "Finished inserting data for: ", fullName

        i-=1
        j-=1

    return
def playersOnTeam (soup, cursor, cnx, teamName):
    tables = soup.find_all("table")

    i = 18
    j = 19

    for table in tables[52:56]:
        print "________________________________________________________________________________________________________________________"
        print "Players on team for ", i,"/",j," season"

        rows = table.find_all("tr")
        for row in rows[1:]:
            points = row.find_all("td")

            team = teamName
            fullName = points[0].text
            season = (str(i) + "/" + str(j))

            inserts = (fullName, team, season)

            insertStats = "INSERT INTO playerReference (fullName, teamName, season) VALUES (%s, %s, %s)"
            # inserts the stats into whatever table is designated
            cursor.execute(insertStats, inserts) 
            cnx.commit()
            print "Finished inserting data for: ", fullName
        i-=1
        j-=1


    return

def advancedScheduleStats(soup, cursor, cnx, teamName):

    #table 60 18/19 advanced
    #table 61 17/18 advanced
    #table 62 16/17 advanced
    #table 63 15/16 advanced

    tables = soup.find_all("table")

    i = 18
    j = 19

    for table in tables[60:64]:
        print "________________________________________________________________________________________________________________________"
        print "Advanced Schedule Stats: ", i,"/",j," season"
        
        rows = table.find_all("tr")
        for row in rows[1:]:

            points = row.find_all("td")
            opponent = points[4].text
            if points[2].text == "H":
                    home = 1
            else:
                home = 0
            team = teanName
            offensiveRating = points[5].text
            defensiveRating = points[6].text
            netRating = points[7].text
            pace = points[8].text
            pointsPerScoringAttempt = points[9].text
            freeThrowPercent = points[10].text
            twoPointPercent = points[11].text
            threePointPercent = points[12].text
            offensiveReboundPercent = points[13].text
            defensiveReboundPercent = points[14].text
            assistPercent = points[15].text
            blockPercent = points[16].text
            date = points[0].text

            inserts = (team, opponent, home,)

            insertStats = "INSERT INTO _______ (fullName, gamesPlayed, fieldGoalsAttempt,...there should be the same num of percent s's as variables created above) VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            # inserts the stats into whatever table is designated
            cursor.execute(insertStats, inserts) 
            cnx.commit()
            print "Finished inserting data for: ", teamName, " vs. ", opponent

        i-=1
        j-=1



    return

def scheduleStats(soup, cursor, cnx,teamName):

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
            pointsScored = points[7].text
            pointsAllowed = points[8].text
            margin = points[9].text
            opponentRPI = points[12].text

            inserts = (team, opponent, home,)

            insertStats = "INSERT INTO _______ (fullName, gamesPlayed, fieldGoalsAttempt,...there should be the same num of percent s's as variables created above) VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            # inserts the stats into whatever table is designated
            cursor.execute(insertStats, inserts) 
            cnx.commit()
            print "Finished inserting data for: ", teamName, " vs. ", opponent
             
        i-=1
        j-=1

    return 

def main():
    
    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    html = open('herHoopStatsMichigan.htm').read()
    soup = BeautifulSoup(html, 'html.parser')
    teams = ("Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin")
    
    for team in teams:
        fileName = ("herHoopStats" + team + ".htm")
        
        #teamFile = open(fileName).read()
        #teamSoup = BeautifulSoup(teamFile, 'html.parser')

        #fill in functions that want to be done for every team
    
    playerBoxScores("Nicole MungerMichiganHerHoopsStats.htm", cursor, cnx, "Michigan", "Nicole Munger")
    

    return




if __name__=="__main__":
    main()
