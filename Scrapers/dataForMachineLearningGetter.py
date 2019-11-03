import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval

def createDataSetPredictPlayer(cursor, cnx):

	#performancePlayer has ___ columns
	#playerBasicAverages has ____ columns
	#playerAdvancedAverages has ____ columns
	#teamVsPosition has ___ columns
	#teamBasicAverages has ___ columns
	#teamAdvancedAverages has ___ columns

	statement1 = "SELECT * from performancePlayer inner join playerBasicAverages on ((performancePlayer.playerID = playerBasicAverages.playerID) and (performancePlayer.seasonID = playerBasicAverages.seasonID))" 

	statement2 = " inner join playerAdvancedAverages on ((performancePlayer.playerID = playerAdvancedAverages.playerID) and (performancePlayer.seasonID = playerAdvancedAverages.seasonID))"

	#statement3 = " inner join teamVsPosition on ((performancePlayer.positionID = teamVsPosition.positionID) and (performancePlayer.seasonID = teamVsPosition.seasonID) and (performancePlayer.opponentTeamID = teamVsPosition.teamID))"
	
	#statement4 = " inner join teamBasicAverages on ((performancePlayer.opponentTeamID = teamBasicAverages.teamID) and (performancePlayer.teamID = teamBasicAverages.teamID) and (performancePlayer.seasonID = teamBasicAverages.seasonID))"

	#statement5 = " inner join teamAdvancedAverages on ((performancePlayer.opponentTeamID = teamAdvancedAverages.teamID) and (performancePlayer.teamID = teamAdvancedAverages.teamID) and (performancePlayer.seasonID = teamAdvancedAverages.seasonID))"

	#statementTotal = statement1 + statement2 + statement3 + statement4 + statement5
	statementTotal = statement1 + statement2

	cursor.execute(statementTotal)

	results = cursor.fetchall()
	for row in results:
		print row.text

	return

def createDataSetPredictTeam(cursor, cnx):

	#advancedScheduleStats has ___ columns
	#teamBasicAverages has ___ columns
	#teamAdvancedAverages has ___ columns
	
	statement1 = "SELECT * from advancedScheduleStats inner join teamBasicAverages on ((advancedScheduleStats.opponentTeamID = teamBasicAverages.teamID) and (advancedScheduleStats.teamID = teamBasicAverages.opponentTeamID) and (advancedScheduleStats.seasonID = teamBasicAverages.seasonID))"

	statement2 = "inner join teamAdvancedAverages on ((advancedScheduleStats.opponentTeamID = teamAdvancedAverages.teamID) and (advancedScheduleStats.teamID = teamAdvancedAverages.opponentTeamID) and (advancedScheduleStats.seasonID = teamAdvancedAverages.seasonID))"

	statementTotal = statement1 + statement2

	cursor.execute(statementTotal)

def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    createDataSetPredictPlayer(cursor, cnx)
   

	    

if __name__=="__main__":
    main()