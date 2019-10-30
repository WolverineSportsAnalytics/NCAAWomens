import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval

def teamVSPosition(soup, cursor, cnx, teamName, seasonID, position):

	features = ('playerPerformanceID', 'player',
	    'team',
	    'date',
	    'dateID',
	    'dateOriginal',
	    'season',
	    'seasonID',
	    'opponent',
	    'opponentTeamID',
	    'home',
	    'minutes',
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

		insertFeature = "INSERT into teamVS",position, "(", feature, ") VALUES (%s)"
		
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

		    	teamFile = open(fileName).read()
		        teamSoup = BeautifulSoup(teamFile, 'html.parser')
		    	teamVSPosition(teamSoup, cursor, cnx, teamName, seasonID, position)
	    

if __name__=="__main__":
    main()