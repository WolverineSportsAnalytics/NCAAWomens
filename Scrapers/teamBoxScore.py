import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval

def firstFunction(cursor,cnx):
	seasonIDs = [1,2,3,4]
    for seasonID in seasonIDs:
        teams = ["Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin"]
        for team in teams:
            dates = "SELECT distinct dateID from performancePlayer where team = '" + str(team) +"' and seasonID = " + str(seasonID)

            cursor.execute(dates)
            dateIDs = cursor.fetchall()
            for date in dateIDs:
            	dateID = str(date)
            	dateID = dateID[1:-2]

            	statement = "INSERT into teamBoxScore (seasonID, team, dateID) values (%s, %s, %s)"
            	inserts = (seasonID, team, dateID)

            	cursor.execute(statement, inserts)
            	cnx.commit()

def secondFunction(cursor,cnx):

	seasonIDs = [1,2,3,4]
	for seasonID in seasonIDs:
        teams = ["Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin"]
        for team in teams:
        	features = ['pointsScored']
        	for f in features:
        		s1 = "SELECT disinct dateID from teamBoxScore where team = '" + str(team) + "' and seasonID = " + str(seasonID)
        		cursor.execute(s1)

        		dateIDs = cursor.fetchall()
        		for dateID in dateIDs:
        			dateID = dateID[1:-2]
        			state = "SELECT " + str(f) + " from performancePlayer where team = '" + str(team) + "' and seasonID = " + str(seasonID) + " and dateID = " + dateID

        			cursor.execute(state)
        			results = cursor.fetchall()
        			sum = 0

        			for result in in results:
        				sum += int(result.text)
        			print sum


def main():

    
    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)

    

if __name__=="__main__":
    main()