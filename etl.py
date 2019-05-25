import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
        Reads a json file from the song_data folder, reads information 
        of songs and artists and saves them to songs and artists tables in 
        the database
        Arguments:
        cur: DB cursor
        filepath: path to json file
        Return: None
    """
    # open song file
    df =  pd.read_json(filepath, typ='series')

    # insert song record
    song_data = [df['song_id'],df['title'],df['artist_id'],df['year'],df['duration']]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = [df['artist_id'], df['artist_name'],df['artist_location'],
                   df['artist_latitude'],df['artist_longitude']]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
        Reads a json file from the log_data folder, reads information 
        of log and user tables in 
        the database
        Arguments:
        cur: DB cursor
        filepath: path to json file
        Return: None
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    t =pd.Series(df['ts'].unique())
     
    # insert time data records
    time_data = (t,t.dt.hour,t.dt.day,t.dt.week,t.dt.month,t.dt.year,t.dt.weekday)
    column_labels = ('start_time' ,'hour','day','week','month','year','weekday')
    time_df = pd.DataFrame({
  column_labels[0]: time_data[0].to_string(index=False).replace("\n", ",").strip().split(",")
,
  column_labels[1]: time_data[1].to_string(index=False).replace("\n", ",").strip().split(",")
,
  column_labels[2]: time_data[2].to_string(index=False).replace("\n", ",").strip().split(",")
    ,
  column_labels[3]: time_data[3].to_string(index=False).replace("\n", ",").strip().split(",")
    ,
  column_labels[4]: time_data[4].to_string(index=False).replace("\n", ",").strip().split(",")
    ,
  column_labels[5]: time_data[5].to_string(index=False).replace("\n", ",").strip().split(",")
    ,
  column_labels[6]: time_data[6].to_string(index=False).replace("\n", ",").strip().split(",")
})

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = pd.DataFrame({'user_id':list(df['userId']),
         'first_name':list(df['firstName']),
         'last_name': list(df['lastName']),
         'gender':list(df['gender']),
         'level':list(df['level'])} )

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid =  results[0],results[1]
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (index,row.ts,row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()