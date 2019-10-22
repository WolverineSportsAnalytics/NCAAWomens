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
            team = teamName
            offensiveRating = float(points[5].text)
            # print("Offensive Rating:" + str(offensiveRating))

            defensiveRating = float(points[6].text)
            # print("Defensive Rating:" + str(defensiveRating))

            netRating = float(points[7].text)
            # print("Net Rating:" + str(netRating))

            pace = float(points[8].text)
            # print("Pace:" + str(pace))

            pointsPerScoringAttempt = float(points[9].text)

            freeThrowPercent = float(points[10].text.strip('%'))
            # print("Free Throw Percent:" + str(freeThrowPercent))
            twoPointPercent = float(points[11].text.strip('%'))
            # print("Two Point Percent:" + str(twoPointPercent))

            threePointPercent = float(points[12].text.strip('%'))
            offensiveReboundPercent = float(points[13].text.strip('%'))
            defensiveReboundPercent = float(points[14].text.strip('%'))
            assistPercent = float(points[15].text.strip('%'))
            blockPercent = float(points[16].text.strip('%'))
            date = points[0].text

            inserts = (team, date, home, opponent, offensiveRating, defensiveRating, netRating, pace,
                        pointsPerScoringAttempt, freeThrowPercent, twoPointPercent, threePointPercent, offensiveReboundPercent,
                        defensiveReboundPercent, assistPercent, blockPercent)

            insertStats = "INSERT INTO advancedScheduleStats(team, date, home, opponent, offRtg, defRtg, netRtg, pace, ptsPerScoringAttempt, ftPercent, 2PtPercent, 3PtPercent, offRebPercent, defRebPercent, assistPercent, blockPercent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            # inserts the stats into whatever table is designated
            cursor.execute(insertStats, inserts)
            cnx.commit()
            print "Finished inserting data for: " + teamName + " vs. " + opponent

        i-=1
        j-=1

    return

def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    # whoever uses this needs to change the directory in the string
    for subdir, dirs, files in os.walk("/Users/cindygu/Sports/WSA/NCAAWomens/teamFiles/NonConference"):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')
                teamName = getTeam(soup, cursor, cnx)
                advancedScheduleStats(soup, cursor, cnx, teamName)
                print (filepath)
                # print(path_in_str)
    '''fileName = 'lakenwairau.htm'
    print fileName
    html = open(fileName).read()
    soup = BeautifulSoup(html, 'html.parser')
    teamStats(soup, cursor, cnx)
    '''
    cursor.close()
    cnx.commit()
    cnx.close()

    return



if __name__=="__main__":
    main()
