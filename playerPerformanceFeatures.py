import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval

def getPlayersFeatures (cursor, cnx, teamID, seasonID, dateID, playerID, position, opponentTeamID):

	playerFeatures = [dateID, playerID, position, teamID, opponentTeamID, seasonID]

	getPlayerPerformance = "SELECT * from playerPerformance where teamID = ", teamID, " and dateID = ", dateID

	cursor.execute(getPlayerPerformance)\
	xx = cursor.fetchall()
	

	for x in [0, len(xx)]:
		playerFeatures.extend(xx[x]) 

	getPlayerTeamAverages = "SELECT * from teamAverages where teamID = ", teamID, " and season = ", seasonID

	cursor.execute(getPlayerTeamAverages)

	zz = cursor.fetchall()
	for z in [0, len(zz)]:
		playerFeatures.extend(zz[z])

	getOpponentTeamVsPosition = "SELECT * from teamVs", position, " where teamID = ", opponentTeamID, " and season = ", seasonID

	cursor.execute(getOpponentTeamVsPosition)
	qq = cursor.fetchall()

	for q in [0, len(qq)]:
		playerFeatures.extend(qq[q])

	getOpponentTeamAverages = "SELECT * from teamAverages where teamID = ", opponentTeamID, " and season = ", seasonID
	cursor.execute(getOpponentTeamAverages)
	tt = cursor.fetchall()

	
	playerFeatures.extend(tt)

	return playerFeatures



def getTeamFeatures(cursor, cnx, teamID, seasonID, dateID, opponentTeamID):
	teamFeatures =[dateID, teamID, opponentTeamID, seasonID]
	getTeamAverages = "SELECT * from teamAverages where teamID = ", teamID, " and seasonID = ", seasonID

	cursor.execute(getTeamAverages)
	xx = cursor.fetchall()
	teamFeatures.extend(xx)

	getOpponentTeamAverages = "SELECT * from teamAverages where teamID = ", opponentTeamID, " and season = ", seasonID, " and dateID = ", dateID, " and opponentTeamID = ", teamID
	cursor.execute(getOpponentTeamAverages)
	tt = cursor.fetchall()

	teamFeatures.extend(tt)

	return teamFeatures

def whichGames():


def main():
    
    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    
    teams = ("Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin")
    
    for team in teams:
    	
    	teamID = team 
    	for opponentTeam in teams.remove(team):
    		opponentTeamID = opponentTeam
    		seasonIDs = [1,2,3,4]
    		for season in seasonIDs:
    			selectGames = "SELECT dateID from teamPerformance where teamID = ", teamID

    			cursor.execute(selectGames)
    			games = cursor.fetchall()

    			for game in games:
    				getTeamFeatures(cursor,cnx,teamID,season,game, opponentTeamID)

    				#insertTeamFeatures = "INSERT into teamPerformanceFeatures "
    				



    

    return




if __name__=="__main__":
    main()