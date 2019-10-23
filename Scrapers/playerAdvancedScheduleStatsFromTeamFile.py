import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval


def getTeam(soup,cursor,cnx):
    i = 18
    j = 19

    print ("________________________________________________________________________________________________________________________")
    print ("Team Info: " + str(i) + "/" + str(j) + " season")
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
    q = 4

    for table in tables[52:56]:
        print ("________________________________________________________________________________________________________________________")
        print ("Player Advanced Average Stats: ", i,"/",j," season")

        rows = table.find_all("tr")
        for row in rows[1:]:
            points = row.find_all("td")
            team = teamName
            player = points[0].text
            if points[2].text != "":
                gamesPlayed = int(points[2].text)
            else:
                gamesPlayed = 0
            print("Games Played: " + str(gamesPlayed))
            if points[3].text != "":
                minutes = float(points[3].text)
            else:
                minutes = float(0)
            print ("Minutes: " + str(minutes))

            if gamesPlayed == 0 or (minutes == 0.0):
                # does not insert them into table
                print ("Player did not play in a game")
            else:
                # usage rate
                if points[4].text != "":
                    usagePercent = float(points[4].text.strip('%'))
                else:
                    usagePercent = float(0)
                print ("Usage Rate: " + str(usagePercent))

                # points per scoring attempt
                if points[5].text != "":
                    pointsPerScoringAttempt = float(points[5].text.strip('%'))
                else:
                    pointsPerScoringAttempt = float(0)
                print ("PPSA: " + str(pointsPerScoringAttempt))

                # eff field goal %
                if points[6].text != "":
                    effectiveFieldGoalPercent = float(points[6].text.strip('%'))
                else:
                    effectiveFieldGoalPercent = float(0)
                # print ("EFF FG %: " + str(effectiveFieldGoalPercent))

                # 3 point rate
                if points[7].text != "":
                    threePointRate = float(points[7].text.strip('%'))
                else:
                    threePointRate = float(0)
                # print ("3point Rate: " + str(threePointRate))

                # free throw rate
                if points[8].text != "":
                    freeThrowRate = float(points[8].text.strip('%'))
                else:
                    freeThrowRate = float(0)
                # print ("FT Rate: " + str(freeThrowRate))

                # off reb %
                if points[9].text != "":
                    offensiveReboundPercent = float(points[9].text.strip('%'))
                else:
                    offensiveReboundPercent = float(0)
                # print ("OFF Reb %: " + str(offensiveReboundPercent))

                # def reb %
                if points[10].text != "":
                    defensiveReboundPercent = float(points[10].text.strip('%'))
                else:
                    defensiveReboundPercent = float(0)
                # print ("DEF Reb %: " + str(defensiveReboundPercent))

                # total reb %
                if points[11].text != "":
                    totalReboundPercent = float(points[11].text.strip('%'))
                else:
                    totalReboundPercent = float(0)
                # print ("Total Reb %: " + str(totalReboundPercent))

                # assist %
                if points[12].text != "":
                    assistPercent = float(points[12].text.strip('%'))
                else:
                    assistPercent = float(0)
                # print ("Assist %: " + str(assistPercent))

                # TO %
                if points[13].text != "":
                    turnoverPercent = float(points[13].text.strip('%'))
                else:
                    turnoverPercent = float(0)
                # print ("TO %: " + str(turnoverPercent))


                # assist/turnover
                if points[14].text != "":
                    assistsPerTurnover = float(points[14].text.strip('%'))
                else:
                    assistsPerTurnover = float(0)
                # print ("Assists per TO: " + str(assistsPerTurnover))

                # steal %
                if points[15].text != "":
                    stealPercent = float(points[15].text.strip('%'))
                else:
                    stealPercent = float(0)
                # print ("Steal %: " + str(stealPercent))

                # block %
                if points[16].text != "":
                    blockPercent = float(points[16].text.strip('%'))
                else:
                    blockPercent = float(0)
                # print ("Block %: " + str(blockPercent))

                # PF %
                if points[17].text != "":
                    personalFoulPercent = float(points[17].text.strip('%'))
                else:
                    personalFoulPercent = float(0)
                print ("PF %: " + str(personalFoulPercent))
                season = (str(i) + "/" + str(j))
                seasonID = q

                inserts = (team,defensiveReboundPercent,seasonID,blockPercent,season,personalFoulPercent,assistsPerTurnover,stealPercent,totalReboundPercent,turnoverPercent,assistPercent,player,gamesPlayed,minutes,usagePercent,pointsPerScoringAttempt,effectiveFieldGoalPercent,threePointRate,freeThrowRate,offensiveReboundPercent)
                # print (len(inserts))

                insertStats = "INSERT INTO playerAdvancedAverages (team,defensiveReboundPercent,seasonID,blockPercent,season,personalFoulPercent,assistsPerTurnover,stealPercent,totalReboundPercent,turnoverPercent,assistPercent,player,gamesPlayed,minutes,usagePercent,pointsPerScoringAttempt,effectiveFieldGoalPercent,threePointRate,freeThrowRate,offensiveReboundPercent) VALUES(%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s)"
                # inserts the stats into whatever table is designated
                cursor.execute(insertStats, inserts)
                cnx.commit()
            print ("Finished inserting data for: " + player)

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


    for subdir, dirs, files in os.walk("/Users/cindygu/Sports/WSA/NCAAWomens/teamFiles"):
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

    cursor.close()
    cnx.commit()
    cnx.close()

    return




if __name__=="__main__":
    main()
