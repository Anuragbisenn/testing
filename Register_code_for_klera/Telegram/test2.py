from telethon import TelegramClient
from telethon.errors.rpc_errors_401 import SessionPasswordNeededError

# (1) Use your own values here
api_id = 19973159
api_hash = '6cc35270be24d34d8ed5f27596987b78'

phone = '+91 9109299363'
username = 'ab123'

# (2) Create the client and connect
client = TelegramClient(username, api_id, api_hash)
client.connect()

# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))

me = client.get_me()
print(me)