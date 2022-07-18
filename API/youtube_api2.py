
from googleapiclient.discovery import build

api_key = 'AIzaSyATNwGhUKjxZpzx0zRdhMkIFJvfEvsfG8w'

youtube = build('youtube', 'v3', developerKey=api_key)

pl_request = youtube.playlists().list(
            part='contentDetails, snippet',
            channelId='UCCezIgC97PvUuR4_gbFUs5g'
        )

pl_response = pl_request.execute()

#print(pl_response) #Returns only the first 5 playlists

for item in pl_response['items']:
    print(item)
    print()
