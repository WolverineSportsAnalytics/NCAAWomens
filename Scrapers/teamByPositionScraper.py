import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval

def teamByPosition(cursor, cnx, teamName, seasonID, position, positionID):
	deadline = 0
	if seasonID == 1:
		deadline = 2205
	elif seasonID ==2:
		deadline = 2569
	elif seasonID ==3:
		deadline = 2933
	elif seasonID ==4:
		deadline = 3304
	elif seasonID ==5:
		deadline = 3668

	features = [
	    'pointsScored',
	    'fieldGoalMade',
	    'fieldGoalAttempt',
	    'threePointMade',
	    'threePointAttempt',
	    'freeThrowMade',
	    'freeThrowAttempt',
	    'offensiveRebound',
	    'defensiveRebound',
	    'totalRebound',
	    'assist',
	    'turnover',
	    'steal',
	    'block',
	    'personalFoul']
	gamesPlayed = bigTenGamesPlayed(cursor, cnx, teamName,seasonID)

	for feature in features:
		
	
		featureStatement = "SELECT " + feature + " from performancePlayer where positionID = '" + str(positionID) + "' and team = '" + teamName + "' and seasonID = " + str(seasonID) + " and dateID < " + str(deadline) + " and opponentTeamID is not null"
		
		#featureStatement = "SELECT pointsScored from performancePlayer where position = 'F' and opponent = 'Michigan' and seasonID = 1"
		
		cursor.execute(featureStatement)

		stats = cursor.fetchall()
		sumStat = 0
		for stat in stats:
			sumStat += stat[0]
		

		
		

		averageStat = sumStat/gamesPlayed

		insertFeature = "UPDATE teamByPosition SET " + feature + " = " + str(averageStat) + " where team = '"+ teamName+ "' and seasonID = "+ str(seasonID) +" and positionID = "+ str(positionID)
		print insertFeature
		
		cursor.execute(insertFeature)
		cnx.commit()

	return


def bigTenGamesPlayed(cursor, cnx, teamName, seasonID):

	statement = "SELECT opponent from advancedScheduleStats where opponentTeamID is not null and opponentTeamID < 15 and seasonID = " + str(seasonID) + " and team = '" + teamName + "'"

	cursor.execute(statement)
	stats = cursor.fetchall()
	
	print len(stats)
	gamesPlayed = len(stats)

	return gamesPlayed


	

def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    
    
    #i = 0
    seasonIDs = [1,2,3,4]
    for seasonID in seasonIDs:
	    positions = ["G", "F", "C"]
	    for position in positions:
		    teams = ["Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin"]
		    for team in teams:
		    	
		    	
		    	if position == "G":
		    		positionID = 1
		    	elif position == "F":
		    		positionID = 2
		    	else:
		    		positionID = 3
		    	
		    	#inserts = (team, position, positionID, seasonID)

		    	#statement = "INSERT into teamByPosition(team, position, positionID, seasonID) values(%s, %s, %s, %s)"
		    	#i += 1
		    	#print statement
		    	#cursor.execute(statement, inserts)
		    	#cnx.commit()

		    	

		    	teamByPosition(cursor, cnx, team, seasonID, position, positionID)

	    

if __name__=="__main__":
    main()