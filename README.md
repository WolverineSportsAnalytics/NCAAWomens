# NCAAWomens
Data on the Michigan Women's Basketball Team
'''
Instructions for creating Excel file for presenting to the Michigan Women's Basketball Team in preparation for upcoming games:

Files that must be downloaded:
These files must be uploaded /upcomingFilesNeeded/

    1. Michigan file (team)
      - Each player file must be downloaded and put in the proper sub-folder
    2. Upcoming opponents files (team)
      - Each player file must be downloaded and put in the proper sub-folder

What we need updated from HerHoopStats.com scraping for both Michigan and Opponent team:

  1. performancePlayer table
  2. scheduleStats (team)
  3. advancedSceduleStats (team)
  4. playerAdvancedAverages table 
  5. teamAverages table
  6. playerReference
  
    To do so:
    
    1. run /Scrapers/playerStatsFromPlayerFile.py 
      - remove dupicates from performancePlayer tablel
    2. run /Scrapers/schedule_stats.py
      - remove duplicates or specify which tables to go over
    3. run /Scrapers/advanced_schedule_stats.py
      - only run on seasonID = 5 and season 5 tables
        - update statement for Michigan team
        - insert statement for Opponent team unless Michigan has played them earlier in the year
      - or simplay remove duplicates
    4. remove entries from playerAdvancedAverages where seasonID = current seasonID
      - run /Scrapers/playerAdvancedScheduleStatsFromTeamFile.py
    5. run /Scrapers/teamAveragesScraper.py
      - remove duplicates or specify seasonIDs to go over
    6. run /Scrapers/rosters.py
      - remove duplicates from playerReference table afterwards

What extrapolating we need updated after scraping data:

  1. avgAdvancedScheduleStats (team)
  2. teamVsPosition
  3. teamByPosition
  4. teamBoxScore
  
    To do so:
    
    1. MUST CREATE scraper or SQL code that does this function
    2. run /Scrapers/teamVSPositionScraper and remember to use an insert statement prior to running it for this season's teams
    3. run /Scrapers/teamByPositionScraper and remember to use an insert statement prior to running it for this season's teams
    4. MUST CREATE scraper for creating TeamBoxScore 

Excel work that must be done:

    1. Update table that contains:
      - HOME avgAdvancedScheduleStatsTable (team)
      - AWAY avgAdvancedScheduleStatsTable (team)
      - team vs. G, F, C
      - team by G, F, C

Current work that should be done:
    1. Make working master file that runs every scraper and updates all the necessary SQL missing information
    2. Determine how Google autoML works 
    3. Determine desired stats to be predicted

Managerial work that should be done:
    1. Have everyone add the WSA Linkedin to their profile for past experience
    2. Post professional headshots of current members on Linkedin
    3. Create SQL database creation project for new members
    4. Create SQL statements project for new members
    5. Create introductory R code project for creating a logistic regression algorithm
    6. Create python scraping project for new members
    7. Update Maize Pages WSA page
    8. Have ready to order t-shirt order created from Underground Printing for new members
    9. Prepare new member Google application
    10. Create WSA posterboard for Festifall and future Winterfests

