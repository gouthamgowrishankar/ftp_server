from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import requests


app= FastAPI()



def check_list_len():
     res = requests.get('https://ftp-sever.onrender.com')
     print(res.content)
     return res

@app.on_event('startup')
def init_data():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_list_len, 'interval', minutes=3)
    scheduler.start()

@app.get('/')
def root():
    return {'message':'ftp_server'}