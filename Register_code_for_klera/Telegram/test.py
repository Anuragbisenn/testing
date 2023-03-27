from telethon import TelegramClient, events, sync

# Remember to use your own values from my.telegram.org!
api_id = 19973159
api_hash = '6cc35270be24d34d8ed5f27596987b78'
client = TelegramClient('ab123', api_id, api_hash)

@client.on(events.NewMessage(chats='@mychan910'))
async def my_event_handler(event):
    print(event.raw_text)

client.start()
client.run_until_disconnected()