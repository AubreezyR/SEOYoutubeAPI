import sqlalchemy as db
import pandas as pd
from googleapiclient.discovery import build
# give values that are not id or name for error testing
# give a channel that does not exist i.e incorrect channel name


def get_channel():
    idOrName = input("type 'id' to search via id or type 'name'"
                     "to search via channel name: ")
    idOrName.lower()
    if idOrName == 'id':
        channel_id = input("please give a channel id: ")
        return channel_id
    elif idOrName == 'name':
        channel_id = input("please give a channel name: ")
        return channel_id
    else:
        print("Error incorrect input:
              "Please try again and either input 'id' or 'name'")
        channel_id = get_channel()
        return channel_id


def create_info_table(response):
    try:
        channelData = response['items'][0]['statistics']
        channelData_Dataframe = pd.DataFrame.from_dict(
          channelData,
          orient='index',
          columns=['Channel Data'])
        engine = db.create_engine('sqlite:///data_base_name.db')
        channelData_Dataframe.to_sql(
          'channelData',
          con=engine,
          if_exists='replace',
          index=True)
        query_result = engine.execute("SELECT * FROM channelData;").fetchall()
        print(pd.DataFrame(query_result))
    except KeyError:
        print("Sorry that channel is not in the youtube databse.")


channel_id = get_channel() 
api_key = "AIzaSyA_llUpUB7qysAoxM_gWqJ7XXEsSzjSveQ"
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channels().list(
        part='statistics',
        forUsername=channel_id
    )


response = request.execute()
create_info_table(response)
