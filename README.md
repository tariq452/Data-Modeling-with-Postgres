**Purpose:**

 Build a data warehouse for analytical operations.
 to allow  Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.
 the analytics team is particularly interested in understanding what songs users are listening to. 
 
**Benefits**

 The query will be fast and simplify  
The analytics team is particularly interested in understanding what songs users are listening to. 
Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

##### Design schema

 Star schema because it's more effective for handling queries
 
Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
Dimension Tables
users - users in the app
user_id, first_name, last_name, gender, level
songs - songs in music database
song_id, title, artist_id, year, duration
artists - artists in music database
artist_id, name, location, lattitude, longitude
time - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday
 
 sample example from table songplays
 ______________________________________________________________________________________________________________________________________________________________________________________________________
songplay_id	|start_time	|user_id|  level|	song_id|artist_id	|session_id	location	                | user_agent                                                                                                          
0			|00:57.8	|73	paid|	None|	None	|954	    | Tampa-St. Petersburg-Clearwater, FL	|"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko)  Version/7.0.6 Safari/537.78.2" |
1			|01:30.8	|24	paid|	None|	None	|984	    | Lake Havasu City-Kingman, AZ		    |"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"         |
2			|04:01.8	|24	paid|	None|	None	|984	    | Lake Havasu City-Kingman, AZ			|"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"         |
3			|04:55.8	|73	paid|	None|	None	|954	    | Tampa-St. Petersburg-Clearwater, FL	|"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2" |
4			|07:13.8	|24	paid|	None|	None	|984	    | Lake Havasu City-Kingman, AZ			|"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"         |
5			|10:56.8	|24	paid|	None|	None	|984	    | Lake Havasu City-Kingman, AZ			|"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"         |
______________________________________________________________________________________________________________________________________________________________________________________________________
##### Etl
 Python
 Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
 
used Etl to read files json and insert data into tables
##### Example Query

 SELECT u.gender,count(*) FROM songplays s inner join  users u on (s.user_id=u.user_id) group by u.gender;
 
 The above query explain how many Male and Female using the application
 
 to start this project folow below step:
 
 1-run create_tables.py to cretate db and create tables.
 2-run etl.py to read json files and process data and insert into tables. 
