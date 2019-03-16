import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime

CLIENT_ID = '22DL5L'
CLIENT_SECRET = '25b2a779b7541950db05dbd497e91346'

def get_data(client_id, client_secret):
    server = Oauth2.OAuth2Server(client_id, client_secret)
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    
    client = fitbit.Fitbit(client_id, client_secret, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

    last_week = str((datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d"))
    yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))

    # Get heart rate
    hr = get_hr(client, last_week, yesterday)

    # Get sleep
    sleep = get_sleep(client, last_week, yesterday)

    # Get calories
    calories = get_calories(client, last_week, yesterday)
    
    # Get steps
    steps = get_steps(client, last_week, yesterday)

    data = (hr, sleep, calories, steps)
    return data

def get_hr(client, start, end):
    hr_data = client.time_series('activities/heart', base_date=start, end_date=end)
    print(len(hr_data['activities-heart']))
    total = 0
    for i in range(0, 7):
        value = hr_data['activities-heart'][i]['value']['restingHeartRate']
        total += value
    return total/7


def get_sleep(client, start, end):
    sleep_data = client.time_series('sleep', base_date=start, end_date=end)
    num = len(sleep_data['sleep'])
    total = 0
    for i in range(0, num):
        value = sleep_data['sleep'][i]['minutesAsleep']
        total += value
    return total/7


def get_calories(client, start, end):
    calorie_data = client.time_series('activities/calories', base_date=start, end_date=end)
    num = len(calorie_data['activities-calories'])

    total = 0
    for i in range(0, num):
        value = calorie_data['activities-calories'][i]['value']
        total += int(value)
    return total/7


def get_steps(client, start, end):
    steps_data = client.time_series('activities/steps', base_date=start, end_date=end)
    num = len(steps_data['activities-steps'])
    total = 0
    for i in range(0, num):
        value = steps_data['activities-steps'][i]['value']
        total += int(value)
    return total/7



if __name__ == '__main__':
    get_data(CLIENT_ID, CLIENT_SECRET)