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
    auth2_client = fitbit.Fitbit(client_id, client_secret, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

    yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    today = str(datetime.datetime.now().strftime("%Y-%m-%d"))

    # Gets heart rate
    # TODO: get blood pressure, sleep, exercise
    fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday, detail_level='1sec')
    print(fit_statsHR['activities-heart-intraday']['dataset'])

    # Displays heart rate data in readable format
    time_list = []
    val_list = []
    


if __name__ == '__main__':
    get_data(CLIENT_ID, CLIENT_SECRET)