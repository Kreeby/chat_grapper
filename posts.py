from telethon import TelegramClient
import json


async def send_posts(n, db):
    api_id = 2954209
    api_hash = 'b48817edddfb2d9cf99132e8a1e786c3'

    group_username = 'Sickipedia'  # Group name can be found in group link (Example group link : https://t.me/c0ban_global, group name = 'c0ban_global')
    client = await TelegramClient('session_name', api_id, api_hash).start()

    # You will be asked to enter your mobile number- Enter mobile number with country code
    # Enter OTP (For OTP check Telegram inbox)

    chats = await client.get_messages(group_username, n)  # 10 number of messages to be extracted

    # Get message id, message, sender id, reply to message id, and timestamp
    message_id = []
    message = []
    sender = []
    reply_to = []
    time = []
    acc = []
    if len(chats):
        for chat in chats:
            message_id.append(chat.id)
            message.append(chat.message.replace("\n", ""))
            sender.append(chat.from_id)
            reply_to.append(chat.reply_to_msg_id)
            time.append(chat.date)

    data_set = {}
    for key, i in enumerate(message):
        data_set = {
            "message_id": message_id[key],
            "message": message[key]
        }
        acc.append(data_set)
    print(acc)
    db.posts.insert_many(acc)

    return data_set
