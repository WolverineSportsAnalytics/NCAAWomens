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

def getTeamShooting(soup, cursor, cnx):

    

    tables = soup.find_all("table")

    i = 18
    j = 19
    
    # you have to determine which tables contain the information you want and then only iderate through those tables
    for table in tables[56:60]:

        print "________________________________________________________________________________________________________________________"
        print "Season ____: ", i,"/",j," season"
        rows = table.find_all("tr")
        for row in rows[1:]:

            

        i-=1
        j-=1

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
    
    for subdir, dirs, files in os.walk("/Users/__________________________/Sports/WSA/NCAAWomens/teamFiles"):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')
                teamName = getTeam(soup, cursor, cnx)
                print (filepath)


                
    
    cursor.close()
    cnx.commit()
    cnx.close()

    return



if __name__=="__main__":
    main()