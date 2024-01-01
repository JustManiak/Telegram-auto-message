from telethon import TelegramClient, events
from time import sleep
#Put your own api id and api hash
api_id =  PUT.YOUR.OWN.API.ID 
api_hash = 'API HASH GOES HERE'

client = TelegramClient('user', api_id, api_hash).start()

message = "MESSAGE GOES HERE"

# Set to store user IDs of those who have talked to the main user
already_talked_to = set()

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender_id = event.sender_id

    # Check if it's a private message and not from a group
    if event.is_private and not event.is_group:
        # Check if the user has ever sent a message
        if sender_id not in already_talked_to:
            already_talked_to.add(sender_id)

            # Send the message
            sender = await client.get_entity(sender_id)
            await client.send_message(sender, message, file="IMAGE GOES HERE(MUST BE IN YOUR PC THE IMG)")

            # Add a delay
            sleep(1)
        else:
            print("Already talked to this user before or user is in a group. Not sending the message again.")

# Function to get the set of users who have talked to the main user
async def get_already_talked_to():
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_user and not dialog.is_group:
            already_talked_to.add(dialog.entity.id)

# Run the function to get already talked to users before starting the event loop
client.loop.run_until_complete(get_already_talked_to())

# Start the event loop
client.run_until_disconnected()