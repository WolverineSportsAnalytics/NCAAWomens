import mysql.connector
import requests
from bs4 import BeautifulSoup
import os

def teamStats (soup,cursor,cnx):
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
