# commands.py

import responses

async def handle_message(self, message):
    user_message = str(message.content)
    channel = str(message.channel)
    

    if user_message[0] == '?':
        user_message = user_message[1:]  # Remove the '?' prefix for private messages
        await send_private_message(message, user_message)
    else:
        await send_public_message(message, user_message, self)

async def send_private_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response)
    except Exception as e:
        print(e)

async def send_public_message(message, user_message, self):
    try:
        response = responses.handle_response(user_message, self)
        await message.channel.send(response)
    except Exception as e:
        print(e)

async def print_message(self, message):
    username = str(message.author)
    user_message = str(message.content)
    message_to_send = username + " şunu dedi: " + user_message
    print(message_to_send)