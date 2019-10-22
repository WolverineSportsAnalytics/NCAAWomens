import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval

def getPlayersFeatures (cursor, cnx, teamID, seasonID, dateID, playerID, position, opponentTeamID):

	getPlayerPerformance = "SELECT * from playerPerformance where teamID = ", teamID, " and dateID = ", dateID

	cursor.execute(getPlayerPerformance)\
	xx = cursor.fetchall()
	playerFeatures = [playerID]

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

	for t in [0, len(tt)]:
		playerFeatures.extend(tt[t])






def main():
    
    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    
    teams = ("Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin")
    
    getPlayersFeatures(cursor,cnx)
        #fill in functions that want to be done for every team
    
    #playerBoxScores("Nicole MungerMichiganHerHoopsStats.htm", cursor, cnx, "Michigan", "Nicole Munger")

    

    return




if __name__=="__main__":
    main()