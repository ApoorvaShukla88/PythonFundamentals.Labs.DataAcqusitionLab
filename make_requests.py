import requests
import json

file_counter = 0
offset_counter = 1
while file_counter < 39:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=' + str(offset_counter)


    r = requests.get(url, headers = {
      'token': 'kiMomNqDkIjROzHmmalPEEzfuKLCmEeI',
      'Content-Type': 'application/json'
    })
    jsonResult = r.json()

    jsonR = jsonResult['results']
    jsonPath = '/Users/amishra/DEV/PythonFundamentals.Labs.DataAcqusitionLab/'
    with open('locations_' + str(file_counter) + '.json', "w") as outfile:
        json.dump(jsonResult, outfile)
    file_counter = file_counter + 1
    offset_counter = offset_counter + 1000




