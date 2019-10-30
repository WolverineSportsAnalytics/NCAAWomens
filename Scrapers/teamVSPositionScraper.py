import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval

def teamVSPosition(soup, cursor, cnx, teamName, seasonID, position):

	features = (
	    'pointsScored',
	    'fieldGoalMade',
	    'fieldGoalAttempt',
	    'fieldGoalPercent',
	    'threePointMade',
	    'threePointAttempt',
	    'threePointPercent',
	    'freeThrowMade',
	    'freeThrowAttempt',
	    'freeThrowPercent',
	    'offensiveRebound',
	    'defensiveRebound',
	    'totalRebound',
	    'assist',
	    'turnover',
	    'steal',
	    'block',
	    'personalFoul',
	    'playerID')
	
	for feature in features:
		featureStats = "SELECT ", feature, " from performancePlayer where position == ",position," and opponentTeam == ", teamName, " and seasonID == ", seasonID
		cursor.execute(featureStats)

		featureStats = cursor.fetch_all()

		averageOfFeature = avg(featureStats)

		print averageOfFeature

		insertFeature = "UPDATE teamVs",position, " SET (", feature, ") = ", averageOfFeature, " where team == ", teamName, " and seasonID == ", seasonID
		
		cursor.execute(averageOfFeature, insertFeature)

	return




def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    
    
    
    seasonIDs = (1,2,3,4)
    for seasonID in seasonIDs:
	    positions = ("G", "F", "C")
	    for position in positions:
		    teams = ("Michigan", "MSU", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "OSU", "Penn State", "Purdue", "Rutgers", "Wisconsin")
		    for team in teams:
		    	
		    	teamName = team
		    	fileName = "herHoopsStats" + team
		    	statement = "INSERT into teamVs", position, " (team, seasonID) VALUES(%s, %s)"
		    	inserts = (team, seasonsID)

		    	cursor.execute(inserts, statement)

		    	teamFile = open(fileName).read()
		        teamSoup = BeautifulSoup(teamFile, 'html.parser')
		    	teamVSPosition(teamSoup, cursor, cnx, teamName, seasonID, position)

	    

if __name__=="__main__":
    main()