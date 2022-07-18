
from googleapiclient.discovery import build
import json

api_key = 'AIzaSyATNwGhUKjxZpzx0zRdhMkIFJvfEvsfG8w'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
            part='statistics',
            forUsername='schafer5'
        )

response = request.execute()
j_response = json.dumps(response, indent=2)

with open("youtube.json", "w") as f:
    f.write(j_response)

#print(response)

#print("Channel ID: {}".format(response['items'][0]['id']))
#print("No. of Subscribers: {}".format(response['items'][0]['statistics']['subscriberCount']))
