import requests
import json

#Initialize Variables
nws_tornado_watch = '0'
nws_tornado_watch_headline = "None"
nws_tornado_watch_description = "None"

nws_tornado_warning = '0'
nws_tornado_warning_headline = "None"
nws_tornado_warning_description = "None"

nws_flood_warning = '0'
nws_flood_warning_headline = "None"
nws_flood_warning_description = "None"

nws_thunderstorm_warning = '0'
nws_thunderstorm_warning_headline = "None"
nws_thunderstorm_warning_description = "None"

####### TEST ZONE ########
#r = requests.get('https://api.weather.gov/alerts/active/zone/INC055')
r = requests.get('https://api.weather.gov/alerts/active/zone/REDACTED')

features = r.json()['features']

for alert in features:
    event = alert['properties']['event']
    if event == 'Tornado Watch':
        nws_tornado_watch = '1'
        nws_tornado_watch_headline = alert['properties']['headline']
        nws_tornado_watch_description = alert['properties']['description']
    if event == 'Tornado Warning':
        nws_tornado_warning = '1'
        nws_tornado_warning_headline = alert['properties']['headline']
        nws_tornado_warning_description = alert['properties']['description']
    if event == 'Severe Thunderstorm Warning':
        nws_thunderstorm_warning = '1'
        nws_thunderstorm_warning_headline = alert['properties']['headline']
        nws_thunderstorm_warning_description = alert['properties']['description']
    if event == 'Flood Warning':
        nws_flood_warning = '1'
        nws_flood_warning_headline = alert['properties']['headline']
        nws_flood_warning_description = alert['properties']['description']

nws_count = nws_tornado_watch + nws_tornado_warning + nws_thunderstorm_warning
# Format to json
nws = {'nws_tornado_watch': nws_tornado_watch, 'nws_tornado_watch_headline': nws_tornado_watch_headline, 'nws_tornado_watch_description': nws_tornado_watch_description}

print (json.dumps(nws))

#print "Tornado Watch Stats"
#print nws_tornado_watch
#print nws_tornado_watch_headline
#print nws_tornado_watch_description

#print "Tornado Warning Stats"
#print nws_tornado_warning
#print nws_tornado_warning_headline
#print nws_tornado_warning_description

#print "Severe Thunderstorm Warning Stats"
#print nws_thunderstorm_warning
#print nws_thunderstorm_warning_headline
#print nws_thunderstorm_warning_description

#print "Flood Warning Stats"
#print nws_flood_warning
#print nws_flood_warning_headline
#print nws_flood_warning_description
