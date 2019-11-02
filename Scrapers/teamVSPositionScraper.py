import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval

def teamVSPosition(cursor, cnx, teamName, seasonID, position):

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
		
	
		featureStatement = "SELECT " + feature + " from performancePlayer where position = " + position + " and opponentTeam = " + teamName + " and seasonID = " + str(seasonID)
		print featureStatement
		cursor.execute(featureStatement)

		featureStats = cursor.fetch_all()

		sumOfFeature = sum(featureStats)

		print sumOfFeature

		insertFeature = "UPDATE teamVs" + position +  " SET (" + feature + ") = "+ sumOfFeature + " where team == "+ teamName+ " and seasonID == "+ str(seasonID)
		
		cursor.execute(sumOfFeature, insertFeature)

	return




def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    
    
    
    seasonIDs = [1,2,3,4]
    for seasonID in seasonIDs:
	    positions = ["G", "F", "C"]
	    for position in positions:
		    teams = ["Michigan", "MSU", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "OSU", "Penn State", "Purdue", "Rutgers", "Wisconsin"]
		    for team in teams:
		    	
		    	
		    	
		    	statement = "INSERT into teamVs" + position+ " (team, seasonID) VALUES(%s, %s)"
		    	inserts = [team, seasonID]
		    	

		    	#cursor.execute(inserts, statements)

		    	teamVSPosition(cursor, cnx, team, seasonID, position)

	    

if __name__=="__main__":
    main()