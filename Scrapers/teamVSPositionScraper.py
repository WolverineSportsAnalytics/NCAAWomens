import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval

def teamVSPosition(cursor, cnx, teamName, seasonID, position, positionID):

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
	
	for feature in features:
		
	
		featureStatement = "SELECT " + feature + " from performancePlayer where positionID = '" + str(positionID) + "' and opponent = '" + teamName + "' and seasonID = " + str(seasonID)
		#featureStatement = "SELECT pointsScored from performancePlayer where position = 'F' and opponent = 'Michigan' and seasonID = 1"
		
		cursor.execute(featureStatement)

		stats = cursor.fetchall()
		sumStat = 0
		for stat in stats:
			sumStat += stat[0]
		

		
		

		print sumStat

		insertFeature = "UPDATE teamVsPosition SET " + feature + " = " + str(sumStat) + " where team = '"+ teamName+ "' and seasonID = "+ str(seasonID) +" and positionID = "+ str(positionID)
		print insertFeature
		
		cursor.execute(insertFeature)
		cnx.commit()

	return




def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    
    
    i = 0
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
		    	
		    	statement = "INSERT into teamVsPosition values (" + str(i) + ",'" + team + "','" + position + "'," + str(positionID) + ",0, 'nothing'," + str(seasonID) + ",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)"
		    	i += 1
		    	print statement
		    	cursor.execute(statement)
		    	cnx.commit()

		    	#cursor.execute(inserts, statements)

		    	teamVSPosition(cursor, cnx, team, seasonID, position, positionID)

	    

if __name__=="__main__":
    main()