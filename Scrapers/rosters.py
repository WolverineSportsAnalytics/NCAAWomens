import mysql.connector
import requests
from bs4 import BeautifulSoup

def playerRef(soup,cursor,cnx):
    i = 15
    j = 16

    print "________________________________________________________________________________________________________________________"
    print "Player Info: " + str(i) + "/" + str(j) + " season"
    list = soup.find('ul', {"class": "list-unstyled"})
    # puts the list items into an array
    list_items = list.findAll('li')
    # print list_items
    playerName = list_items[0].text
    print playerName
    team = list_items[1].text[6:]
    print team
    conference = list_items[2].text[12:]
    print conference
    league = list_items[3].text[8:]
    print league
    position = list_items[4].text[10:]
    print position
    height = list_items[5].text[8:]
    print height
    jerseyNum = list_items[6].text[15:]
    print jerseyNum
    season = str(i) + "/" + str(j)
    print season

    #finish filling in the inserts list with all the variables
    inserts = (playerName, team, season, position, height, jerseyNum)

    insertStats = "INSERT INTO playerReference (fullName, teamName, season, position, height, jerseyNumber) VALUES(%s, %s, %s, %s, %s, %s)"

    # inserts the stats into whatever table is designated
    cursor.execute(insertStats, inserts)
    cnx.commit()
    print "Finished inserting data for: " + playerName + " from " + team

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

    fileName = 'alexalfano.htm'
    print fileName
    html = open(fileName).read()
    soup = BeautifulSoup(html, 'html.parser')
    playerRef(soup, cursor, cnx)
    cursor.close()
    cnx.commit()
    cnx.close()

    return




if __name__=="__main__":
    main()
