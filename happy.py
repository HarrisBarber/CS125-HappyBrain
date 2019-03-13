import json
import pprint
import subprocess
import datetime
import time
import calendar

def getTagValue(stepCode, tagName):
    obj = getAllJSON(stepCode)
    tagValue = obj[tagName]
    print(tagValue)
    return tagValue

def getAllJSON(stepCode):
    fout = subprocess.Popen(stepCode,stdout=subprocess.PIPE,shell = True)
    inFile = fout.communicate()[0]
    return json.loads("{"+inFile.decode()+"}")

def msToTime(ms):
    s = float(ms) / 1000000000.0
    return datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')

def timeToMs(yyyy, mm, dd, hour, min, sec, dec):
#    now = datetime.datetime(2015,03,10,13,0, 9, 12345)    
    now = datetime.datetime(yyyy, mm, dd, hour, min, sec, dec)
    tt = datetime.datetime.timetuple(now)
    return time.mktime(tt) * 1000000000.0

def getDataTimes(dataInput):
    points = dataInput['point']
        
    startMilliseconds = 0
    endMilliseconds = 0
    for point in points:
        if startMilliseconds < point['startTimeNanos']: 
            startMilliseconds = point['startTimeNanos']
        if endMilliseconds < point['endTimeNanos']: 
            endMilliseconds = point['endTimeNanos']
    return     (len(points), msToTime(startMilliseconds), msToTime(endMilliseconds))

def getInformationSourceList(accessToken):
    step4CodeTemplate = 'curl https://www.googleapis.com/fitness/v1/users/me/dataSources' + \
    '?access_token=<accessToken>'
    step4 = step4CodeTemplate.replace('<accessToken>',accessToken)
    allSources = getAllJSON(step4)
    dataSources = []
    for sourceList in allSources['dataSource']:
        dataSources.append(sourceList['dataStreamId'])
    return dataSources

def getUserCode(clientId, scope):
    step1CodeTemplate= 'curl -d "client_id=<clientId>' +\
    '&scope=<scope>" https://accounts.google.com/o/oauth2/device/code'
    step1= step1CodeTemplate.replace('<clientId>',clientId).replace('<scope>',scope)
    allSources = getAllJSON(step1)
    pprint.pprint(allSources)
    return allSources['device_code'], allSources['user_code'], allSources['verification_url']

def getRefreshToken(clientId, clientSecret, deviceCode):
    step2CodeTemplate = 'curl -d "client_id=<clientId>&client_secret=<clientSecret>' + \
    '&code=<deviceCode>&grant_type=http://oauth.net/grant_type/device/1.0" ' + \
    'https://accounts.google.com/o/oauth2/token'
    step2= step2CodeTemplate.replace('<clientId>',clientId) \
    .replace('<clientSecret>',clientSecret) \
    .replace('<deviceCode>',deviceCode)
    pprint.pprint(step2)
    allSources = getAllJSON(step2)
    pprint.pprint(allSources)
    return allSources['access_token'], allSources['refresh_token']

def getRefreshedAccessCode(clientId, clientSecret, refreshToken):
    step3CodeTemplate = 'curl -d "client_id=<clientId>&client_secret=<clientSecret>' + \
    '&refresh_token=<refreshToken>' + \
    '&grant_type=refresh_token" https://accounts.google.com/o/oauth2/token'
    step3 = step3CodeTemplate.replace('<clientId>',clientId) \
    .replace('<clientSecret>',clientSecret) \
    .replace('<refreshToken>',refreshToken)
    return getTagValue(step3, 'access_token')

clientId = '563118044721-quknpprbcvrgtn3djpmjual09144vmkq.apps.googleusercontent.com'
clientSecret = 'YaLeoAulyLPQbRes0webyBnp'

# set the scope of the permissions selected - for Google fit, use the following scope

scope = 'email profile+ \
https://www.googleapis.com/auth/fitness.activity.read+ \
https://www.googleapis.com/auth/fitness.activity.write+ \
https://www.googleapis.com/auth/fitness.body.read+ \
https://www.googleapis.com/auth/fitness.body.write+ \
https://www.googleapis.com/auth/fitness.location.read+ \
https://www.googleapis.com/auth/fitness.location.write'


deviceCode, userCode, verificationUrl = getUserCode(clientId, scope)
print('\n******  go  to page ' + verificationUrl + ' and enter ' + userCode + " *****\n")

accessToken, refreshToken = getRefreshToken(clientId, clientSecret, deviceCode)
accessToken = getRefreshedAccessCode(clientId, clientSecret, refreshToken)



#dataSources = getInformationSourceList(accessToken)	
#pprint.pprint(dataSources)	















