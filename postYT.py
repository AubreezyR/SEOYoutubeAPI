import sqlalchemy as db
from googleapiclient.discovery import build
idOrName = input("type 'id' to search via id or type 'name' to search via channel name: ")
idOrName.lower()
if idOrName == 'id':
  channel_id = input("please give a channel id: ")
elif idOrName == 'name':
  channel_id = input("please give a channel name: ")
api_key = "AIzaSyA_llUpUB7qysAoxM_gWqJ7XXEsSzjSveQ"
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channels().list(
        part='statistics',
        forUsername=channel_id
    )
response = request.execute()
print(response)
