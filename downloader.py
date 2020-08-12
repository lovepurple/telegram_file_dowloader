from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotoVideo

api_id = 1659305
api_hash = "3dcd4963c613d3331e5057446bee6764"
phone_number = "+8613810718824"

client = TelegramClient("session", api_id, api_hash)


async def connect():
    await client.connect()


async def check_authorized():
    me = None
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        me = await client.sign_in(phone_number, input("Enter Code:"))
    else:
        me = await client.get_me()

    # dialogs = client.iter_dialogs()         # 获取所有的对话  -1001375250801
    # async for dialog in dialogs:
    chat = await client.get_entity(-1001375250801)
    msgs = await client.get_messages(chat, 50, filter=InputMessagesFilterPhotoVideo)
    for msg in msgs:
        # await client.download_media(message=msg)
        await client.download_media(message=msg, file="G:\\"+msg.file.name)
        break


# async def trySignin():


#     client.loop.run_until_complete(trySign())

#     me = client.sign_in(phone_number, )  # input()方法接受输入


if __name__ == "__main__":
    client.loop.run_until_complete(connect())           # 异步操作
    client.loop.run_until_complete(check_authorized())
