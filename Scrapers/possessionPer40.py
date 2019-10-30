import mysql.connector
import requests
from bs4 import BeautifulSoup
import os

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

def possessionStats(soup, cursor, cnx, teamName):

    #table 56 18/19 schedule
    #table 57 17/18 schedule
    #table 58 16/17 schedule
    #table 59 15/16 schedule

    tables = soup.find_all("table")

    i = 18
    j = 19
    for table in tables[0:4]:

        print ("________________________________________________________________________________________________________________________")
        print ("Possession Stats: ", i,"/",j," season")
        rows = table.find_all("tr")
        for row in rows[10:]:
            points = row.find_all("td")
            possPerForty = float(points[2].text)
            # print(points)
            print("Poss Per 40 Min: " + str(possPerForty))
            team = teamName
            season = str(i) + "/" + str(j)

            inserts = (team, season, possPerForty)

            insertStats = "INSERT INTO teamPossessions(team, season, possPer40) VALUES(%s, %s, %s)"

            # inserts the stats into whatever table is designated
            cursor.execute(insertStats, inserts)
            cnx.commit()
            print ("Finished inserting data for: " + team + " " + season)

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
    for subdir, dirs, files in os.walk("/Users/cindygu/Sports/WSA/NCAAWomens/teamFiles"):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')
                teamName = getTeam(soup, cursor, cnx)
                possessionStats(soup, cursor, cnx, teamName)
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
