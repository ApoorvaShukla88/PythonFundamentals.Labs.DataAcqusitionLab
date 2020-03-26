import requests
import json


def make_request(input_url, token, content) -> str:
    r = requests.get(input_url, headers={
        'token': token,
        'Content-Type': content
    })
    # print(r)
    return r.json()


def make_responce(jsonResult, fileIndex):
    jsonR = jsonResult['results']
    # print(jsonR)
    with open('/Users/amishra/DEV/PythonFundamentals.Labs.DataAcqusitionLab/location_' + str(fileIndex) + '.json',
              "w") as outfile:
        json.dump(jsonR, outfile)


# make_responce()
# file_counter = 0
#
# offset_counter = 1
# while file_counter < 39:
#     url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=' + str(offset_counter)
#
#     r = requests.get(url, headers={
#         'token': 'kiMomNqDkIjROzHmmalPEEzfuKLCmEeI',
#         'Content-Type': 'application/json'
#     })

# jsonResult = r.json()

# jsonR = jsonResult['results']
# jsonPath = '/Users/amishra/DEV/PythonFundamentals.Labs.DataAcqusitionLab/'
# with open('locations_' + str(file_counter) + '.json', "w") as outfile:
#     json.dump(jsonResult, outfile)
# file_counter = file_counter + 1
# offset_counter = offset_counter + 1000

def main():
    file_counter = 0
    offset_counter = 1
    while file_counter < 39:
        responseJson = make_request(
            'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=' + str(offset_counter),
            'kiMomNqDkIjROzHmmalPEEzfuKLCmEeI', 'application/json')

        make_responce(responseJson, file_counter)
        file_counter += 1
        offset_counter += 1000


if __name__ == "__main__":
    main()
