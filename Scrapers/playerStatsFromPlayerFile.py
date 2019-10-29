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

def playerGamesStats(soup, cursor, cnx, teamName):


    list = soup.find('ul', {"class": "list-unstyled"})
    list_items = list.findAll('li')
    player = list_items[0].text

    tables = soup.find_all("table")

    print (len(tables))

    numSeasons = (len(tables) / 7)

    if numSeasons == 4:


    	for table in tables[24:28]:
    		rows = table.find_all("tr")
    		for row in rows[1:]:
    			points = row.find_all("td")

    			date = points[0].text
    			if points[3].text == "H":
    				home = 1
    			else:
    				home = 0
    			opponent = points[4].text
    			minutes = points[5].text
    			pointsScored = points[6].text
    			fieldGoalMade = points[7].text
    			fieldGoalAttempt = points[8].text
    			if fieldGoalAttempt == "0":

    				fieldGoalPercent = -111
    			else:
    				fieldGoalPercent = float(fieldGoalMade)/float(fieldGoalAttempt)
    			threePointMade = points[10].text
    			threePointAttempt = points[11].text
    			if threePointAttempt == "0":
    				threepointPercent = -111

    			else:
    				threepointPercent = float(threePointMade)/float(threePointAttempt)
    			freeThrowMade = points[13].text
    			freeThrowAttempt = points[14].text

    			if freeThrowAttempt == "0":
    				freeThrowPercent = -111

    			else:
    				freeThrowPercent = float(freeThrowMade)/float(freeThrowAttempt)
    			offensiveRebound = points[16].text
    			defensiveRebound = points[17].text
    			totalRebound = points[18].text
    			assist = points[19].text
    			turnover = points[20].text
    			steal = points[21].text
    			block = points[22].text
    			personalFoul = points[23].text


    			#inserts = (player,date,home,opponent,minutes,pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threepointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,steal,turnover,block,personalFoul)

    			#insertStats = "INSERT into performancePlayer (player,dateOriginal,home,opponent,minutes,pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threepointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,steal,turnover,block,personalFoul) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    			#cursor.execute(insertStats, inserts)
                #cnx.commit()


    elif numSeasons == 3:


    	for table in tables[18:21]:
    		rows = table.find_all("tr")
    		for row in rows[1:]:
    			points = row.find_all("td")

    			date = points[0].text
    			if points[3].text == "H":
    				home = 1
    			else:
    				home = 0
    			opponent = points[4].text
    			minutes = points[5].text
    			pointsScored = points[6].text
    			fieldGoalMade = points[7].text
    			fieldGoalAttempt = points[8].text
    			if fieldGoalAttempt == "0":

    				fieldGoalPercent = -111
    			else:
    				fieldGoalPercent = float(fieldGoalMade)/float(fieldGoalAttempt)
    			threePointMade = points[10].text
    			threePointAttempt = points[11].text
    			if threePointAttempt == "0":
    				threepointPercent = -111

    			else:
    				threepointPercent = float(threePointMade)/float(threePointAttempt)
    			freeThrowMade = points[13].text
    			freeThrowAttempt = points[14].text

    			if freeThrowAttempt == "0":
    				freeThrowPercent = -111

    			else:
    				freeThrowPercent = float(freeThrowMade)/float(freeThrowAttempt)
    			offensiveRebound = points[16].text
    			defensiveRebound = points[17].text
    			totalRebound = points[18].text
    			assist = points[19].text
    			turnover = points[20].text
    			steal = points[21].text
    			block = points[22].text
    			personalFoul = points[23].text


    			#inserts = (player,date,home,opponent,minutes,pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threepointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,steal,turnover,block,personalFoul)

    			#insertStats = "INSERT into performancePlayer (player,dateOriginal,home,opponent,minutes,pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threepointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,steal,turnover,block,personalFoul) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    			#cursor.execute(insertStats, inserts)
                #cnx.commit()



    elif numSeasons == 2:


    	for table in tables[12:14]:
    		rows = table.find_all("tr")
    		for row in rows[1:]:
    			points = row.find_all("td")

    			date = points[0].text
    			if points[3].text == "H":
    				home = 1
    			else:
    				home = 0
    			opponent = points[4].text
    			minutes = points[5].text
    			pointsScored = points[6].text
    			fieldGoalMade = points[7].text
    			fieldGoalAttempt = points[8].text
    			if fieldGoalAttempt == "0":

    				fieldGoalPercent = -111
    			else:
    				fieldGoalPercent = float(fieldGoalMade)/float(fieldGoalAttempt)
    			threePointMade = points[10].text
    			threePointAttempt = points[11].text
    			if threePointAttempt == "0":
    				threepointPercent = -111

    			else:
    				threepointPercent = float(threePointMade)/float(threePointAttempt)
    			freeThrowMade = points[13].text
    			freeThrowAttempt = points[14].text

    			if freeThrowAttempt == "0":
    				freeThrowPercent = -111

    			else:
    				freeThrowPercent = float(freeThrowMade)/float(freeThrowAttempt)
    			offensiveRebound = points[16].text
    			defensiveRebound = points[17].text
    			totalRebound = points[18].text
    			assist = points[19].text
    			turnover = points[20].text
    			steal = points[21].text
    			block = points[22].text
    			personalFoul = points[23].text


    			#inserts = (player,date,home,opponent,minutes,pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threepointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,steal,turnover,block,personalFoul)

    			#insertStats = "INSERT into performancePlayer (player,dateOriginal,home,opponent,minutes,pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threepointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,steal,turnover,block,personalFoul) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    			#cursor.execute(insertStats, inserts)
                #cnx.commit()

    elif numSeasons == 1:


    	for table in tables[6:7]:
    		rows = table.find_all("tr")
    		for row in rows[1:]:
    			points = row.find_all("td")

    			date = points[0].text
    			if points[3].text == "H":
    				home = 1
    			else:
    				home = 0
    			opponent = points[4].text
    			minutes = points[5].text
    			pointsScored = points[6].text
    			fieldGoalMade = points[7].text
    			fieldGoalAttempt = points[8].text
    			if fieldGoalAttempt == "0":

    				fieldGoalPercent = -111
    			else:
    				fieldGoalPercent = float(fieldGoalMade)/float(fieldGoalAttempt)
    			threePointMade = points[10].text
    			threePointAttempt = points[11].text
    			if threePointAttempt == "0":
    				threepointPercent = -111

    			else:
    				threepointPercent = float(threePointMade)/float(threePointAttempt)
    			freeThrowMade = points[13].text
    			freeThrowAttempt = points[14].text

    			if freeThrowAttempt == "0":
    				freeThrowPercent = -111

    			else:
    				freeThrowPercent = float(freeThrowMade)/float(freeThrowAttempt)
    			offensiveRebound = points[16].text
    			defensiveRebound = points[17].text
    			totalRebound = points[18].text
    			assist = points[19].text
    			turnover = points[20].text
    			steal = points[21].text
    			block = points[22].text
    			personalFoul = points[23].text
                print(personalFoul)

                #inserts = (player,date,home,opponent,minutes,pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threepointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,steal,turnover,block,personalFoul)
                #insertStats = "INSERT into performancePlayer (player,dateOriginal,home,opponent,minutes,pointsScored,fieldGoalMade,fieldGoalAttempt,fieldGoalPercent,threePointMade,threePointAttempt,threepointPercent,freeThrowMade,freeThrowAttempt,freeThrowPercent,offensiveRebound,defensiveRebound,totalRebound,assist,steal,turnover,block,personalFoul) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    			#cursor.execute(insertStats, inserts)
                #cnx.commit()
    return



def playerNameTrial(soup,cursor,cnx,teamName):
	list = soup.find('ul', {"class": "list-unstyled"})
	list_items = list.findAll('li')
	playerName = list_items[0].text


def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    #html = open('nicolemunger.htm').read()
    #soup = BeautifulSoup(html, 'html.parser')


    #playerGamesStats(soup, cursor, cnx, "Michigan")
    #playerNameTrial(soup,cursor,cnx,"Michigan")

<<<<<<< HEAD:Scrapers/playerStatsFromPlayerFile.py
    for subdir, dirs, files in os.walk(script):
        for file in files:
            print "made it here"
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')
                teamName = getTeam(soup, cursor, cnx)
                if teamName != "":
                    playerGamesStats(soup, cursor, cnx, teamName)
                    print (filepath)
                # print(path_in_str)




=======
    

    teams = ("Michigan", "MSU", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "OSU", "Penn State", "Purdue", "Rutgers", "Wisconsin")
    
    for team in teams:
        script = "/Users/lissjust/Documents/NCAAWomens/Player Htm Files/" + team
        print script
        for subdir, dirs, files in os.walk(script):
	        for file in files:
	            print "made it here"
	            #print os.path.join(subdir, file)
	            filepath = subdir + os.sep + file
	            if filepath.endswith(".htm"):
	                html = open(filepath).read()
	                soup = BeautifulSoup(html, 'html.parser')
	                
	                playerGamesStats(soup, cursor, cnx)
	                print (filepath)
	                # print(path_in_str)


    
>>>>>>> cc4e79df57ca30d2f663471c6840a7df0c644d74:Scrapers/playerStatsFromPlayerFile.py

        #fill in functions that want to be done for every team

    #playerBoxScores("Nicole MungerMichiganHerHoopsStats.htm", cursor, cnx, "Michigan", "Nicole Munger")


    return




if __name__=="__main__":
    main()
