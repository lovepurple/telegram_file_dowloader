from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotoVideo
import os
from terminalutils import *
import time
from multiprocessing import Pool

api_id = 1659305
api_hash = "3dcd4963c613d3331e5057446bee6764"
phone_number = "+8613810718824"
download_folder = r"G:\TelegramDownload"

client = TelegramClient("session", api_id, api_hash)


async def connect():
    await client.connect()


# async def download_media(telethonMsg):
#     file_path = os.path.join(download_folder, telethonMsg.file.name)
#     if os.path.isfile(file_path):
#         prRed("exist file:"+file_path)
#     else:
#         prGreen("start downloading file:"+file_path +
#                 " time:"+str(time.perf_counter()))
#         await client.download_media(message=msg, file=file_path)
#         prYellow("file:"+file_path +
#                  "download finish on:" + str(time.perf_counter()))


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
    msgs = await client.get_messages(chat, 1000, filter=InputMessagesFilterPhotoVideo)

    for msg in msgs:
        file_path = os.path.join(download_folder, msg.file.name)
        if os.path.isfile(file_path):
            prRed("exist file:"+file_path)
        else:
            prGreen("start downloading file:"+file_path +
                    " time:"+str(time.perf_counter()))
            await client.download_media(message=msg, file=file_path)
            prYellow("file:"+file_path +
                     "download finish on:" + str(time.perf_counter()))

    prPurple("download finish")


if __name__ == "__main__":
    client.loop.run_until_complete(connect())           # 异步操作
    client.loop.run_until_complete(check_authorized())
