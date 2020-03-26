import unittest
import json
import make_requests_withMethod

class makeRequestTest(unittest.TestCase):

    def test_make_request(self):
        test_cases = [
            (['https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=0',
              'kiMomNqDkIjROzHmmalPEEzfuKLCmEeI' , 'application/json']),
             (['https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=',
              'kiMomNqDkIjROzHmmalPEEzfuKLmEeI' , 'application/json'], FileNotFoundError)
        ]
        for args in test_cases:
            with self.subTest(f"{args}"):
                self.assertIsNotNone((make_requests_withMethod.make_request(args[0],args[1],args[2])))
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",

                )