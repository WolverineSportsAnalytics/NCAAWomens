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

def getTeamShooting(soup, cursor, cnx, teamName):
    #table 8 18/19 stats
    #table 9 17/18 stats
    #table 10 16/17 stats
    #table 11 15/16 stats

    tables = soup.find_all("table")

    i = 15
    j = 16
    statistic = list() #stack
    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[8:12]:

        rows = table.find_all("tr")
        for row in rows[1:]:
            stat = row.find_all("td")
            percentage = float(stat[3].text.strip('%'))
            #adds each percentage into the stack
            statistic.append(percentage)

    for x in range(4):
        print "________________________________________________________________________________________________________________________"
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

        inserts = (percPtsFrom3, percPtsFrom2, percPtsFromFt, ThreePtRate, ftRate, ptsPerPlay, ptsPerScorAtt, effFGPerc, ThreePtPerc, TwoPtPerc, ftPerc, fgPerc)
        print inserts
        #insertStats = "UPDATE teamAverages(percPtsFrom3, percPtsFrom2, percPtsFromFt, 3ptRate, ftRate, ptsPerPlay, ptsPerScorAtt, effFGPerc, 3ptPerc, 2ptPerc, ftPerc, fgPerc) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        i+=1
        j+=1

    # inserts the stats into whatever table is designated
    #cursor.execute(insertStats, inserts)
    #cnx.commit()
    print "Finished inserting data for: " + teamName
    return

def getTeamRebounding(soup, cursor, cnx):



    tables = soup.find_all("table")

    i = 18
    j = 19

    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[56:60]:

        print "________________________________________________________________________________________________________________________"
        print "Season Averages: ", i,"/",j," season"
        rows = table.find_all("tr")
        for row in rows[1:]:
            print "TODO"
        i-=1
        j-=1

    return

def getTeamOther(soup, cursor, cnx):



    tables = soup.find_all("table")

    i = 18
    j = 19

    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[56:60]:

        print "________________________________________________________________________________________________________________________"
        print "Season ____: ", i,"/",j," season"
        rows = table.find_all("tr")
        for row in rows[1:]:
            print "TODO"

        i-=1
        j-=1

    return

def getTeamScoringTotals(soup, cursor, cnx):



    tables = soup.find_all("table")

    i = 18
    j = 19

    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[56:60]:

        print "________________________________________________________________________________________________________________________"
        print "Season ___: ", i,"/",j," season"
        rows = table.find_all("tr")
        for row in rows[1:]:
            print "TODO"

        i-=1
        j-=1

    return

def getTeamBonus(soup, cursor, cnx):



    tables = soup.find_all("table")

    i = 18
    j = 19

    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[56:60]:

        print "________________________________________________________________________________________________________________________"
        print "Season ____: ", i,"/",j," season"
        rows = table.find_all("tr")
        for row in rows[1:]:
            print "TODO"

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

    '''for subdir, dirs, files in os.walk("/Users/__________________________/Sports/WSA/NCAAWomens/teamFiles"):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')
                teamName = getTeam(soup, cursor, cnx)
                getTeamShooting(soup, cursor, cnx, teamName)
                print (filepath)
        '''
    file = "/Users/jonathanchuang/Desktop/WSA/NCAAWomens/teamFiles/herHoopStatsMichigan.htm"
    html = open(file).read()
    soup = BeautifulSoup(html, 'html.parser')
    teamName = getTeam(soup, cursor, cnx)
    getTeamShooting(soup, cursor, cnx, teamName)


    cursor.close()
    cnx.commit()
    cnx.close()

    return



if __name__=="__main__":
    main()
