import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval


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

def parseFloat(str):

    try:
        return float(str)
    except:
        if str == "":
            return 
        str = str.strip()
        if str.endswith("%"):
            return float(str.strip("%").strip())
        raise Exception("Don't know how to parse %s" % str)


def playerAdvancedAverages(soup, cursor, cnx, teamName):

    tables = soup.find_all("table")

    i = 18
    j = 19
    q = 4

    for table in tables[52:56]:
        print ("________________________________________________________________________________________________________________________")
        print ("Player Advanced Average Stats: ", i,"/",j," season")

        rows = table.find_all("tr")
        for row in rows[1:]:
            points = row.find_all("td")
            team = teamName

            player = points[0].text
            player = player.encode()
            gamesPlayed = points[2].text
            gamesPlayed = gamesPlayed.encode()
            minutes = points[3].text
            minutes = minutes.encode()
            print minutes
            if gamesPlayed == "" or (minutes == 0):
                print "Player did not play in a game"
            else:

                usagePercent = parseFloat(points[4].text)
                pointsPerScoringAttempt = points[5].text
                pointsPerScoringAttempt = pointsPerScoringAttempt.encode()
                effectiveFieldGoalPercent = parseFloat(points[6].text)
                
                threePointRate = parseFloat(points[7].text)
                if threePointRate == "":
                    threePointRate = -111
                freeThrowRate = parseFloat(points[8].text)
                if freeThrowRate == "":
                    freeThrowRate = -111
                offensiveReboundPercent = parseFloat(points[9].text)
                defensiveReboundPercent = parseFloat(points[10].text)
                totalReboundPercent = parseFloat(points[11].text)
                assistPercent = parseFloat(points[12].text)
                turnoverPercent = parseFloat(points[13].text)
                assistsPerTurnover = points[14].text
                assistsPerTurnover = assistsPerTurnover.encode()
                if assistsPerTurnover == "":
                    assistsPerTurnover = -111
                stealPercent = parseFloat(points[15].text)
                blockPercent = parseFloat(points[16].text)
                personalFoulPercent = parseFloat(points[17].text)
                season = (str(i) + "/" + str(j))
                seasonID = q

                inserts = (team,defensiveReboundPercent,seasonID,blockPercent,season,personalFoulPercent,assistsPerTurnover,stealPercent,totalReboundPercent,turnoverPercent,assistPercent,player,gamesPlayed,minutes,usagePercent,pointsPerScoringAttempt,effectiveFieldGoalPercent,threePointRate,freeThrowRate,offensiveReboundPercent)
                print len(inserts)
                insertStats = "INSERT INTO playerAdvancedAverages (team,defensiveReboundPercent,seasonID,blockPercent,season,personalFoulPercent,assistsPerTurnover,stealPercent,totalReboundPercent,turnoverPercent,assistPercent,player,gamesPlayed,minutes,usagePercent,pointsPerScoringAttempt,effectiveFieldGoalPercent,threePointRate,freeThrowRate,offensiveReboundPercent) VALUES(%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s)"
                # inserts the stats into whatever table is designated
                cursor.execute(insertStats, inserts)
                cnx.commit()
            print "Finished inserting data for: ", player

        i-=1
        j-=1
        q-=1

    return

def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    #html = open('herHoopStatsMichigan.htm').read()
    #soup = BeautifulSoup(html, 'html.parser')

    teams = ("Michigan", "MichiganSt", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "OhioSt", "PennSt", "Purdue", "Rutgers", "Wisconsin")
    
    open('herHoopStatsMichigan.htm').read()
    
    for team in teams:
        fileName = ("herHoopStats" + team + ".htm")

        teamFile = open(fileName).read()
        teamSoup = BeautifulSoup(teamFile, 'html.parser')
        playerAdvancedAverages(teamSoup, cursor, cnx, team)

    '''


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

    '''
    return




if __name__=="__main__":
    main()
