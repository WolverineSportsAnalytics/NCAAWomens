import mysql.connector
import requests
from bs4 import BeautifulSoup
import os

def getTeam(soup,cursor,cnx):
    #i = 18
    # = 19

    #print "Team Info: " + str(i) + "/" + str(j) + " season"
    list = soup.find('ul', {"class": "list-unstyled"})
    # puts the list items into an array
    list_items = list.findAll('li')
    # print list_items
    teamName = list_items[0].text
    print "Team: " + teamName
    return teamName

def getSeasonOverview(soup, cursor, cnx, teamName):
    #table 0 18/19 stats
    #table 1 17/18 stats
    #table 2 16/17 stats
    #table 3 15/16 stats

    tables = soup.find_all("table")

    i = 18
    j = 19
    q = 4
    statistic = list()

    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[0:4]:
        #ptsPer100Poss is row 7
        #oppPtsPer100Poss is row 8
        #possPer40Min is row 10


        rows = table.find_all("tr")

        row7 = rows[7]
        row8 = rows[8]
        row10 = rows[10]

        perStats = (row7, row8, row10)

        for stat in perStats:
            num = stat.find_all("td")
            percentage = float(num[3].text)
            #adds each percentage into the stack
            statistic.append(percentage)

        #print team overview to test
        print "--------------------------------------------------------------------------"
        print "Team Overview: ", i,"/",j," season"

        #since this is a stack, pop in reverse order of statistics on database
        possPer40Min = statistic.pop()
        oppPtsPer100Poss = statistic.pop()
        ptsPer100Poss = statistic.pop()
        seasonID = q

        inserts = [ptsPer100Poss, oppPtsPer100Poss, possPer40Min]
        print inserts
        insertStats = "INSERT into teamAverages(ptsPer100Poss, oppPtsPer100Poss, possPer40Min) VALUES(%s, %s, %s) where seasonID = " + str(seasonID)
        i-=1
        j-=1
        q-=1

    # inserts the stats into whatever table is designated
    #cursor.execute(insertStats, inserts)
    #cnx.commit()
    print "--------------------------------------------------------------------------"
    print "Finished inserting data for: " + teamName

    return inserts

def getTeamShooting(soup, cursor, cnx, teamName):
    #table 8 18/19 stats
    #table 9 17/18 stats
    #table 10 16/17 stats
    #table 11 15/16 stats

    tables = soup.find_all("table")

    i = 18
    j = 19
    q = 4
    statistic = list() #stack
    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[8:12]:

        rows = table.find_all("tr")
        for row in rows[1:]:
            stat = row.find_all("td")
            percentage = float(stat[3].text.strip('%'))
            #adds each percentage into the stack
            statistic.append(percentage)

        #print team shooting to test
        print "--------------------------------------------------------------------------"
        print "Team shooting: ", i,"/",j," season"

        #since this is a stack, pop in reverse order of statistics on database
        percPtsFrom3 = statistic.pop()
        percPtsFrom2 = statistic.pop()
        percPtsFromFt = statistic.pop()
        ThreePtRate = statistic.pop()
        ftRate = statistic.pop()
        ptsPerPlay = statistic.pop()
        ptsPerScorAtt = statistic.pop()
        effFGPerc = statistic.pop()
        ThreePtPerc = statistic.pop()
        TwoPtPerc = statistic.pop()
        ftPerc = statistic.pop()
        fgPerc = statistic.pop()
        seasonID = q

        inserts = [percPtsFrom3, percPtsFrom2, percPtsFromFt, ThreePtRate, ftRate, ptsPerPlay, ptsPerScorAtt, effFGPerc, ThreePtPerc, TwoPtPerc, ftPerc, fgPerc]
        print inserts
        insertStats = "UPDATE teamAverages(percPtsFrom3, percPtsFrom2, percPtsFromFt, 3ptRate, ftRate, ptsPerPlay, ptsPerScorAtt, effFGPerc, 3ptPerc, 2ptPerc, ftPerc, fgPerc) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) where seasonID = " + str(seasonID)
        i-=1
        j-=1
        q-=1

    # inserts the stats into whatever table is designated
    #cursor.execute(insertStats, inserts)
    #cnx.commit()
    print "--------------------------------------------------------------------------"
    print "Finished inserting data for: " + teamName
    return inserts

def getTeamRebounding(soup, cursor, cnx, teamName):

    #table 12 18/19 stats
    #table 13 17/18 stats
    #table 14 16/17 stats
    #table 15 15/16 stats

    tables = soup.find_all("table")

    i = 18
    j = 19
    q = 4
    statistic = list() #stack
    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[12:16]:

        rows = table.find_all("tr")
        for row in rows[1:]:
            stat = row.find_all("td")
            percentage = float(stat[3].text.strip('%'))
            #adds each percentage into the stack
            statistic.append(percentage)

        #pint team rebounding to test
        print "-----------------------------------------------------------------------"
        print "Team rebounding: ", i,"/",j," season"

        #since this is a stack, pop in reverse order of statistics on database
        totRebRate = statistic.pop()
        totRebsPerGame = statistic.pop()
        defRebRate = statistic.pop()
        defRebsPerGame = statistic.pop()
        offRebRate = statistic.pop()
        offRebsPerGame = statistic.pop()
        seasonID = q

        inserts = [offRebsPerGame, offRebRate, defRebsPerGame, defRebRate, totRebsPerGame, totRebRate]
        print inserts
        insertStats = "UPDATE teamAverages(offRebsPerGame, offRebRate, defRebsPerGame, defRebRate, totRebsPerGame, totRebRate) VALUES(%s, %s, %s, %s, %s, %s) where seasonID = " + str(seasonID)
        i-=1
        j-=1
        q-=1
    # inserts the stats into whatever table is designated
    #cursor.execute(insertStats, inserts)
    #cnx.commit()
    print "-----------------------------------------------------------------------"
    print "Finished inserting data for: " + teamName
    return inserts

def getTeamOther(soup, cursor, cnx, teamName):

    #table 16 18/19 stats
    #table 17 17/18 stats
    #table 18 16/17 stats
    #table 19 15/16 stats

    tables = soup.find_all("table")

    i = 18
    j = 19
    q = 4
    statistic = list() #stack

    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[16:20]:

        rows = table.find_all("tr")
        for row in rows[1:]:
            stat = row.find_all("td")
            percentage = float(stat[3].text.strip('%'))
            #adds each percentage into the stack
            statistic.append(percentage)

        #print team other to test
        print "__________________________________________________________________________________________________"
        print "Team other: ", i,"/",j," season"

        #since this is a stack, pop in reverse order of statistics on database
        foulRate = statistic.pop()
        foulPerGame = statistic.pop()
        blkRate = statistic.pop()
        blkPerGame = statistic.pop()
        stlRate = statistic.pop()
        stlPerGame = statistic.pop()
        assistTO = statistic.pop()
        TORate = statistic.pop()
        TOPerGame = statistic.pop()
        assistedShotRate = statistic.pop()
        assistPerGame = statistic.pop()
        seasonID = q

        inserts = [assistPerGame, assistedShotRate, TOPerGame, TORate, assistTO, stlPerGame, stlRate, blkPerGame, blkRate, foulPerGame, foulRate]
        print inserts
        insertStats = "UPDATE teamAverages(assistPerGame, assistedShotRate, TOPerGame, TORate, assistTO, stlPerGame, stlRate, blkPerGame, blkRate, foulPerGame, foulRate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) where seasonID = " + str(seasonID)
        i-=1
        j-=1
        q-=1
        # inserts the stats into whatever table is designated
        #cursor.execute(insertStats, inserts)
        #cnx.commit()
        print "-----------------------------------------------------------------------"
        print "Finished inserting data for: " + teamName

    return inserts

def getTeamScoringTotals(soup, cursor, cnx, teamName):

    #table 20 18/19 stats
    #table 21 17/18 stats
    #table 22 16/17 stats
    #table 23 15/16 stats

    tables = soup.find_all("table")

    i = 18
    j = 19
    q = 4
    statistic = list() #stack
    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[20:24]:

        rows = table.find_all("tr")
        for row in rows[1:]:
            stat = row.find_all("td")
            percentage = int(stat[3].text.replace(',', ''))
            #adds each percentage into the stack
            statistic.append(percentage)

        #pint team scoring totals to test
        print "-----------------------------------------------------------------------"
        print "Team Scoring Totals: ", i,"/",j," season"

        #since this is a stack, pop in reverse order of statistics on database
        ftTripsTOTAL = statistic.pop()
        ftAttemptTOTAL = statistic.pop()
        ftMadeTOTAL = statistic.pop()
        ThreePtAttemptTOTAL = statistic.pop()
        ThreePtMadeTOTAL = statistic.pop()
        TwoPtAttemptTOTAL = statistic.pop()
        TwoPtMadeTOTAL = statistic.pop()
        FGattemptTOTAL = statistic.pop()
        FGmadeTOTAL = statistic.pop()
        ptsTOTAL = statistic.pop()
        seasonID = q

        inserts = [ptsTOTAL, FGmadeTOTAL, FGattemptTOTAL, TwoPtMadeTOTAL, TwoPtAttemptTOTAL, ThreePtMadeTOTAL, ThreePtAttemptTOTAL, ftMadeTOTAL, ftAttemptTOTAL, ftTripsTOTAL]
        print inserts
        insertStats = "UPDATE teamAverages(ptsTOTAL, FGmadeTOTAL, FGattemptTOTAL, TwoPtMadeTOTAL, TwoPtAttemptTOTAL, ThreePtMadeTOTAL, ThreePtAttemptTOTAL, ftMadeTOTAL, ftAttemptTOTAL, ftTripsTOTAL) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) where seasonID = " + str(seasonID)
        i-=1
        j-=1
        q-=1
    # inserts the stats into whatever table is designated
    #cursor.execute(insertStats, inserts)
    #cnx.commit()
    print "-----------------------------------------------------------------------"
    print "Finished inserting data for: " + teamName
    return inserts

def getTeamBonus(soup, cursor, cnx, teamName):

    #table 24 18/19 stats
    #table 25 17/18 stats
    #table 26 16/17 stats
    #table 27 15/16 stats

    tables = soup.find_all("table")

    i = 18
    j = 19
    q = 4
    statistic = list() #stack
    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[24:28]:

        rows = table.find_all("tr")
        for row in rows[1:]:
            stat = row.find_all("td")
            percentage = int(stat[3].text.replace(',', ''))
            #adds each percentage into the stack
            statistic.append(percentage)

        #pint team other totals to test
        print "-----------------------------------------------------------------------"
        print "Team Scoring Totals: ", i,"/",j," season"

        #since this is a stack, pop in reverse order of statistics on database
        Fouls = statistic.pop()
        Blocks = statistic.pop()
        Steals = statistic.pop()
        Turnovers = statistic.pop()
        Assists = statistic.pop()
        TotalRebs = statistic.pop()
        DefRebs = statistic.pop()
        OffRebs = statistic.pop()
        Minutes = statistic.pop()
        seasonID = q

        inserts = [Minutes, OffRebs, DefRebs, TotalRebs, Assists, Turnovers, Steals, Blocks, Fouls, seasonID]
        print inserts
        insertStats = "UPDATE teamAverages(Minutes, OffRebs, DefRebs, TotalRebs, Assists, Turnovers, Steals, Blocks, Fouls, seasonID) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) where seasonID = " + str(seasonID)
        i-=1
        j-=1
        q-=1
    # inserts the stats into whatever table is designated
    #cursor.execute(insertStats, inserts)
    #cnx.commit()
    print "-----------------------------------------------------------------------"
    print "Finished inserting data for: " + teamName
    return inserts


def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    # whoever uses this needs to change the directory in the string

    for subdir, dirs, files in os.walk("/Users/jonathanchuang/Desktop/WSA/NCAAWomens/teamFiles"):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')

                #list
                inserts = []
                #all of these variables are lists
                teamName = str(getTeam(soup, cursor, cnx))
                inserts.append(teamName)
                seasonOverview = getSeasonOverview(soup, cursor, cnx, teamName)
                for i in seasonOverview:
                    inserts.append(i)
                teamShooting = getTeamShooting(soup, cursor, cnx, teamName)
                for i in teamShooting:
                    inserts.append(i)
                teamRebounding = getTeamRebounding(soup, cursor, cnx, teamName)
                for i in teamRebounding:
                    inserts.append(i)
                teamOther = getTeamOther(soup, cursor, cnx, teamName)
                for i in teamOther:
                    inserts.append(i)
                teamScoringTotals = getTeamScoringTotals(soup, cursor, cnx, teamName)
                for i in teamScoringTotals:
                    inserts.append(i)
                teamBonus = getTeamBonus(soup, cursor, cnx, teamName)
                for i in teamBonus:
                    inserts.append(i)
                #combines all these lists into one list
                #inserts = [teamName, seasonOverview, teamShooting, teamRebounding, teamOther, teamScoringTotals, teamBonus]

                #insert = (ptsPer100Poss, oppPtsPer100Poss, possPer40Min,percPtsFrom3, percPtsFrom2, percPtsFromFt, ThreePtRate, ftRate, ptsPerPlay, ptsPerScorAtt, effFGPerc, ThreePtPerc, TwoPtPerc, ftPerc, fgPerc,offRebsPerGame, offRebRate, defRebsPerGame, defRebRate, totRebsPerGame, totRebRate,assistPerGame, assistedShotRate, TOPerGame, TORate, assistTO, stlPerGame, stlRate, blkPerGame, blkRate, foulPerGame, foulRate,ptsTOTAL, FGmadeTOTAL, FGattemptTOTAL, TwoPtMadeTOTAL, TwoPtAttemptTOTAL, ThreePtMadeTOTAL, ThreePtAttemptTOTAL, ftMadeTOTAL, ftAttemptTOTAL, ftTripsTOTAL,Minutes, OffRebs, DefRebs, TotalRebs, Assists, Turnovers, Steals, Blocks, Fouls)
                statement = "INSERT into teamAverages (team,ptsPer100Poss, oppPtsPer100Poss, possPer40Min,percPtsFrom3, percPtsFrom2, percPtsFromFt, ThreePtRate, ftRate, ptsPerPlay, ptsPerScorAtt, effFGPerc, ThreePtPerc, TwoPtPerc, ftPerc, fgPerc,offRebsPerGame, offRebRate, defRebsPerGame, defRebRate, totRebsPerGame, totRebRate,assistPerGame, assistedShotRate, TOPerGame, TORate, assistTO, stlPerGame, stlRate, blkPerGame, blkRate, foulPerGame, foulRate,ptsTOTAL, FGmadeTOTAL, FGattemptTOTAL, TwoPtMadeTOTAL, TwoPtAttemptTOTAL, ThreePtMadeTOTAL, ThreePtAttemptTOTAL, ftMadeTOTAL, ftAttemptTOTAL, ftTripsTOTAL,Minutes, OffRebs, DefRebs, TotalRebs, Assists, Turnovers, Steals, Blocks, Fouls,seasonID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(statement,inserts)
                cnx.commit()
                #print inserts

                for i in range(3): #for next 3 seasons
                    for j in range(53): #53 variables
                        inserts.pop()
                    statement = "UPDATE teamAverages (team,ptsPer100Poss, oppPtsPer100Poss, possPer40Min,percPtsFrom3, percPtsFrom2, percPtsFromFt, ThreePtRate, ftRate, ptsPerPlay, ptsPerScorAtt, effFGPerc, ThreePtPerc, TwoPtPerc, ftPerc, fgPerc,offRebsPerGame, offRebRate, defRebsPerGame, defRebRate, totRebsPerGame, totRebRate,assistPerGame, assistedShotRate, TOPerGame, TORate, assistTO, stlPerGame, stlRate, blkPerGame, blkRate, foulPerGame, foulRate,ptsTOTAL, FGmadeTOTAL, FGattemptTOTAL, TwoPtMadeTOTAL, TwoPtAttemptTOTAL, ThreePtMadeTOTAL, ThreePtAttemptTOTAL, ftMadeTOTAL, ftAttemptTOTAL, ftTripsTOTAL,Minutes, OffRebs, DefRebs, TotalRebs, Assists, Turnovers, Steals, Blocks, Fouls,seasonID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(statement,inserts)
                    cnx.commit()
                '''
    seasonIDs = [1,2,3,4]
    for seasonID in seasonIDs:
        teams = ["Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin"]
        for team in teams:

            #make the default values in database all 0s
            statement = "INSERT INTO teamAverages (team, seasonID) VALUES(%s,%s)"
            inserts = (team, seasonID)

            cursor.execute(statement, inserts)
            print statement
            cnx.commit()
            '''
            '''
            getSeasonOverview(soup, cursor, cnx, teamName)
            getTeamShooting(soup, cursor, cnx, teamName)
            getTeamRebounding(soup, cursor, cnx, teamName)
            getTeamOther(soup, cursor, cnx, teamName)
            getTeamScoringTotals(soup, cursor, cnx, teamName)
            getTeamBonus(soup, cursor, cnx, teamName)

            #cursor.close()
            #cnx.close()
            '''

    return



if __name__=="__main__":
    main()
