import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval
import NCAAWomens.Scraper.playerStatsFromPlayerFile.py as aaa
import NCAAWomens.Scraper.schedule_stats.py as bbb
import NCAAWomens.Scraper.advanced_schedule_stats.py as ccc
import NCAAWomens.Scraper.teamAveragesScraper.py as ddd
import NCAAWomens.Scraper.rosters.py as eee

import NCAAWomens.Scraper.teamVSPositionScraper.py as fff
import NCAAWomens.Scraper.teamByPositionScraper.py as ggg



def upcomingFilesFunctions(cursor,cnx):
	seasonIDs = [1,2,3,4,5]
    positionIDs = [1,2,3]
    positions = ["G", "F", "C"]
    teams = ["Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin"]
    teamIDs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    # insert below the spelled out numbers that corresponds to how many teams you want to go through
    numberTeams = ["One", "Two", "Three"]

    # the Michigan team file scrapers that must be ran
    script = "/Users/lissjust/Documents/NCAAWomens/upcomingFilesNeed/MichiganTeamFile"
    print script
    for subdir, dirs, files in os.walk(script):
        for file in files:
            print "made it here"
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')

                teamName = bbb.getTeam(soup,cursor,cnx)
                # this file needs to have the right tables updated and only go over 1 table for this year
                statement1 = "DELETE from scheduleStats where team = 'Michigan' and seasonID = 5"
                statement2 = "DELETE from advancedScheduleStats where team = 'Michigan' and seasonID = 5"
                statement3 = "DELETE from performancePlayer where team = 'Michigan' and seasonID = 5"
                statement4 = "DELETE from playerAdvancedAverages where team = 'Michigan' "
                bbb.scheduleStats(soup, cursor, cnx, teamName)
                # this file needs to have the right tables updated and only go over 1 table for this year
                ccc.advancedScheduleStats(soup, cursor, cnx, teamName)
                #figure out what the teamAveragesScraper has to run

    # the Michigan player file scrapers that must be ran
    script = "/Users/lissjust/Documents/NCAAWomens/upcomingFilesNeed/MichiganPlayerFiles"
    print script
    for subdir, dirs, files in os.walk(script):
        for file in files:
            print "made it here"
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            print (filepath)
            if filepath.endswith(".htm"):
                html = open(filepath).read()
                soup = BeautifulSoup(html, 'html.parser')
                
                # this file needs to be updated so that it accounts for this season being 19/20 and seasonID = 5
                eee.playerRef(soup,cursor,cnx)


                playerTeam = aaa.getTeam(soup,cursor,cnx)
                # this file needs to be updated because the insert statements are commented out
                playerGamesStats(soup,cursor,cnx,playerTeam)
                # fill in this statement with the SQL statement that would delete duplicate rows from the performancePlayer table
                statement = "__________________"
                cursor.execute(statement)            

    for numberTeam in numberTeams:
	    # the opposing team file scrapers that must be ran
	    script = "/Users/lissjust/Documents/NCAAWomens/upcomingFilesNeed/teamFiles/Team" + numberTeam + "TeamFile"
	    print script
	    for subdir, dirs, files in os.walk(script):
	        for file in files:
	            print "Accessing team" + numberTeam + " team file path"
	            #print os.path.join(subdir, file)
	            filepath = subdir + os.sep + file
	            if filepath.endswith(".htm"):
	                html = open(filepath).read()
	                soup = BeautifulSoup(html, 'html.parser')

	                teamName = "Michigan"
	                # this file needs to have the right tables updated and only go over 1 table for this year
	                bbb.scheduleStats(soup, cursor, cnx, teamName)
	                # this file needs to have the right tables updated and only go over 1 table for this year
	                ccc.advancedScheduleStats(soup, cursor, cnx, teamName)
	                #figure out what the teamAveragesScraper has to run

    for numberTeam in numberTeams:
	    # the opposing player file scrapers that must be ran
	    script = "/Users/lissjust/Documents/NCAAWomens/upcomingFilesNeed/teamFiles/Team" + numberTeam + "PlayerFiles"
	    print script
	    for subdir, dirs, files in os.walk(script):
	        for file in files:
	            print "Accessing team" + numberTeam + " player file path"
	            #print os.path.join(subdir, file)
	            filepath = subdir + os.sep + file
	            if filepath.endswith(".htm"):
	                html = open(filepath).read()
	                soup = BeautifulSoup(html, 'html.parser')
		                
		                
		            # this file needs to be updated so that it accounts for this season being 19/20 and seasonID = 5
	                eee.playerRef(soup,cursor,cnx)


	                playerTeam = aaa.getTeam(soup,cursor,cnx)
	                # this file needs to be updated because the insert statements are commented out
	                playerGamesStats(soup,cursor,cnx,playerTeam)
	                # fill in this statement with the SQL statement that would delete duplicate rows from the performancePlayer table
	                statement = "__________________"
	                cursor.execute(statement)   

def teamPositionPopulator(cursor,cnx,teams,seasonID,teamByOrTeamVS):

	positions = ["G", "F", "C"]
	for position in positions:
		    for team in teams:
		    
		    	if position == "G":
		    		positionID = 1
		    	elif position == "F":
		    		positionID = 2
		    	else:
		    		positionID = 3
		    	
		    	statement = "INSERT into " + str(teamByOrTeamVS) + " (team, position, positionID, seasonID) VALUES (%s,%s,%s,%s)"
		    	inserts = (team, position, positionID, seasonID)

		    	cursor.execute(statement,inserts)
		    	cnx.commit()


def extrapolatorFunctions(cursor,cnx,teams,seasonID):

	positions = ["G", "F", "C"]
	for position in positions:
		    for team in teams:
		    
		    	if position == "G":
		    		positionID = 1
		    	elif position == "F":
		    		positionID = 2
		    	else:
		    		positionID = 3

	    		ggg.teamByPosition(cursor,cnx,team,seasonID,position,positionID)
		    	fff.teamVSPosition(cursor,cnx,team,seasonID,position,positionID)

def sqlUpdateStatements(cursor,cnx):

	'''
	Fill this function in with any final update statements that need to be done for the database
	'''

def main():

    
    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    seasonIDs = [1,2,3,4,5]
    positionIDs = [1,2,3]
    positions = ["G", "F", "C"]
    teams = ["Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin"]
    teamIDs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    # insert below the spelled out numbers that corresponds to how many teams you want to go through
    numberTeams = ["One", "Two", "Three"]

    seasonID = 5
    upcomingTeams = ["team1", "team2", "team3"]
    
    # these only need to be ran once at the start of the season
    teamPositionPopulator(cursor,cnx,teams,seasonID,"teamVSPosition")
    teamPositionPopulator(cursor,cnx,teams,seasonID,"teamByPosition")
    
    # these will be ran every time
    upcomingFilesFunctions(cursor,cnx)
    extrapolatorFunctions(cursor,cnx,upcomingTeams,seasonID)


if __name__=="__main__":
    main()