import os
import zipfile
import wget
import shutil
from pyrogram import Client, filters
from pyrogram.types import Message


async def restart(message: Message, restart_type):
    if restart_type == "update":
        text = "1"
    else:
        text = "2"
    try:
        await os.execvp(
            "python3",
            [
                "python3",
                "./main.py",
                f"{message.chat.id}",
                f"{message.id}",
                f"{text}",
            ],
        )
    except:
        await os.execvp(
            "python",
            [
                "python",
                "./main.py",
                f"{message.chat.id}",
                f"{message.id}",
                f"{text}",
            ],
        )


# Restart
@Client.on_message(filters.command("restart", ["."]) & filters.me)
async def restart_get(client, message):
    try:
        await message.edit("**Restarting userbot...**")
        await restart(message, restart_type="restart")
    except:
        await message.edit("**An error occured...**")


# Update
@Client.on_message(filters.command('update', ["."]) & filters.me)
async def update(client, message):
    try:
        await message.edit('**Updating...**')
        link = "https://github.com/ITZ-ZAID/ZAID-USERBOT/archive/refs/heads/main.zip"
        wget.download(link, 'temp/archive.zip')

        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall("temp/")
        os.remove("temp/archive.zip")

        shutil.make_archive("temp/archive", "zip", "temp/FoxUserbot-main/")

        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall(".")
        os.remove("temp/archive.zip")

        await message.edit('**Userbot succesfully updated\nRestarting...**')
        await restart(message, restart_type="update")
    except:
        await message.edit(f"**An error occured...**")



