# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events


# get your api_id, api_hash, token
# from telegram as described above
api_id = '10734270'
api_hash = '8ee1087a732aabc51377dca89786bded'
token = 'bot token'
message = "Working..."

# your phone number
phone = '+989388990352'

# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session
client.connect()

@client.on(events.NewMessage())
async def my_event_handler(event):
        if event.photo!= None:
                a=await client.download_media(event.photo)
                print(a)
                await client.send_file('@Md_Gi',a)
        await client.send_message('@Md_GI',event.text)

client.start()
client.run_until_disconnected()

