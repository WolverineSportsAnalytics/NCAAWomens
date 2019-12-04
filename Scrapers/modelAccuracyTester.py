import mysql.connector
import requests
from bs4 import BeautifulSoup
from ast import literal_eval
import os
from ast import literal_eval
import csv

def getTestData(cursor,cnx):

	statement = "SELECT * from advancedScheduleStats basis join boxScoreTotalsAverages team1 on basis.team = team1.team and basis.seasonID = team1.seasonID and basis.home = team1.home join boxScoreTotalsAverages team2 on basis.opponent = team2.team and basis.seasonID = team2.seasonID where basis.home = 1 and team2.home = 0 and team1.pointsScored is not null and team2.pointsScored is not null"

	cursor.execute(statement)
	testSet = cursor.fetchall()
	listOfLists = []	
	for row in testSet:
		myList = []
		for i in [9,35,36,38,39,41,43,44,46,47,48,49,50,60,61,63,66,68,69,71,72,73,74,75]:
			q = [row[i]]
			myList.extend(q)
			
		listOfLists.extend(myList)
	# this data is not seperated into the right segments, but it is all there 
	return listOfLists

def getVariables(cursor,cnx,features):
	csvfile = open('/Users/lissjust/Desktop/testSetWinLoss.csv')
	readCSV = csv.reader(csvfile, delimiter = ',')

	statement = "SELECT * from logisticReg"
	cursor.execute(statement)
	sqlResults = cursor.fetchall()

	variablesList = []
	for row in sqlResults:
		variablesList.append(str(row[1]))

	return variablesList

def getCoefficients(cursor, cnx,features):
	csvfile = open('/Users/lissjust/Desktop/testSetWinLoss.csv')
	readCSV = csv.reader(csvfile, delimiter = ',')

	statement = "SELECT * from logisticReg"
	cursor.execute(statement)
	sqlResults = cursor.fetchall()

	variablesList = []
	for row in sqlResults:
		variablesList.append(str(row[1]))
	
	coefficients = []
	for row in sqlResults:
		coefficients.append(float(str(row[2])))
	
	return coefficients
	
def splitData(dataSet,features, coefficients):

	splitLength = len(features)
	sampleSize = len(dataSet)/splitLength

	q = 0
	for i in range(sampleSize):
		
		for dataPoint in dataSet[q:(q+splitLength)]:
			intercept = coefficients[0]
			sum = intercept
			num = 1
			for value in coefficients[1:]:
				variable = value * dataPoint
				num += 1
				sum += variable
		q += splitLength
		


def main():

    cnx = mysql.connector.connect(user="wsa",
                                  host="34.68.250.121",
                                  database="NCAAWomens",
                                  password="LeBron>MJ!")
    cursor = cnx.cursor(buffered=True)
	    
	    
    teams = ["Michigan", "Michigan St.", "Illinois", "Indiana", "Iowa", "Maryland", "Minnesota", "Nebraska", "Northwestern", "Ohio St.", "Penn St.", "Purdue", "Rutgers", "Wisconsin"]
    

    features = [9,35,36,38,39,41,43,44,46,47,48,49,50,60,61,63,66,68,69,71,72,73,74,75]
    modelTester(cursor,cnx,features)

if __name__=="__main__":
    main()