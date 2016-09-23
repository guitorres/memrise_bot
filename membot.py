import requests
import sqlite3
import datetime

url = 'http://www.memrise.com/api/user/get/?user_id=%d&with_leaderboard=true'

users_id = [
	11821101, #gt
	]

conn = sqlite3.connect('memrise.sqlite')
cursor = conn.cursor()
cursor.execute("create table if not exists memrise (id integer, username text, date text, points_alltime integer, points_month integer, points_week integer)")
data = datetime.datetime.now()
for id in users_id:
    request = requests.get( url%(id))
    username = request.json()['user']['username']
    leaderboard = request.json()['user']['leaderboard']
    points_alltime, points_month, points_week = leaderboard['points_alltime'], leaderboard['points_month'], leaderboard['points_week']
    cursor.execute('insert into memrise values(?, ?, ?, ? , ?, ?)', (id, username, data, points_alltime, points_month, points_week))
conn.commit()
conn.close()