# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create ="create table if not exists songplays (songplay_id varchar primary key not null,start_time timestamp,user_id int4 references users(user_id), \
                        level varchar,song_id varchar references songs(song_id),artist_id varchar references artists(artist_id)  ,\
						session_id int4,location varchar,user_agent varchar)"

user_table_create = "create table if not exists users (user_id int4 primary key,first_name varchar,last_name varchar,gender varchar,level varchar);"

song_table_create = "create table if not exists songs (song_id varchar primary key,title varchar,artist_id varchar,year int4,duration numeric);"

artist_table_create = "create table if not exists artists (artist_id varchar primary key,name varchar,location varchar,lattitude numeric,longitude numeric);"

time_table_create ="create table if not exists time  (start_time timestamp primary key,hour int4,day int4,week int4,month int4,year int4,weekday int4);"

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (songplay_id, start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

user_table_insert = ("INSERT INTO users (user_id,first_name,last_name ,gender, level) VALUES (%s, %s, %s, %s, %s )  ON CONFLICT (user_id) DO UPDATE SET level= EXCLUDED.level ")

song_table_insert = ("INSERT INTO songs (song_id ,title ,artist_id ,year ,duration) VALUES (%s, %s, %s, %s, %s ) ON CONFLICT DO NOTHING")

artist_table_insert = ("INSERT INTO artists (artist_id,name,location,lattitude,longitude  ) VALUES (%s, %s, %s, %s, %s ) ON CONFLICT DO NOTHING")

time_table_insert = ("INSERT INTO time (start_time ,hour,day,week,month,year,weekday ) VALUES (%s, %s, %s, %s, %s, %s, %s  ) ON CONFLICT DO NOTHING")

# FIND SONGS

song_select = (" select s.song_id,s.artist_id from songs s inner join artists a on (s.artist_id=a.artist_id)  where s.title=%s and a.name=%s and s.duration=%s  ")

# QUERY LISTS

create_table_queries = [ user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create ]
drop_table_queries = [songplay_table_drop,user_table_drop, song_table_drop, artist_table_drop, time_table_drop ]