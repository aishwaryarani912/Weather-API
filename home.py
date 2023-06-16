from flask import Flask,render_template,request
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq
import requests
from datetime import datetime
# import pymongo
# client = pymongo.MongoClient("mongodb+srv://Aishwarya23:aish1234@cluster0.4cdxkhz.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# database_name=client['WeatherAPI']
# collection=database_name['Weather']
import mysql.connector as conn
from db_connect import *
mydb=conn.connect(host="localhost",user="root",password="aish23",database="Weather")
print(mydb)
cursor=mydb.cursor()
dataBaseName="Weather"
Weather_info="weatherinfo"
# create_db(cursor, dataBaseName)
# create_table(cursor,Weather_info)
app=Flask(__name__)
@app.route("/",methods=['POST','GET'])
def weather():
    return render_template('weather.html')
@app.route("/review",methods=['POST','GET'])
def results():
    if request.method=='POST':
        city_name=request.form['content']
        # print(city_name)
        url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=41cda69e57b7c4281022b8769bd6b4ae'
        response=requests.get(url.format(city_name)).json()
        # print(response)
        reviews=[]
        temp=response['main']['temp']
        # print(temp)
        weather=response['weather'][0]['description']
        min_temp=response['main']['temp_min']
        max_temp=response['main']['temp_max']
        datetime_1=datetime.now().strftime('%d %b %Y | %I:%M:%S %p')
        icon=response['weather'][0]['icon']

        mydict={'Temperature':temp,'Weather':weather,'Min_temp':min_temp,'Max_temp':max_temp,'Datetime':datetime_1,'Icon':icon}
        reviews.append(mydict)
        # insert_query=f"INSERT INTO {Weather_info} (Temperature,Weather,Min_temp,Max_temp,Datetime,Icon) VALUES(%(Temperature)s,%(Weather)s,%(Min_temp)s ,%(Max_temp)s,%(Datetime)s,%(Icon)s);"
        # cursor.executemany(insert_query,reviews)
        # mydb.commit()
        # collection.insert_one(mydict)
        return render_template("results.html",reviews=reviews[0:])

    else:
        return render_template('results.html')
if __name__=='__main__':
    app.run(debug='TRUE')
