from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""Dear {message.from_user.first_name}!

π I am RAJPUTBOT Music Player. 

π₯³ I can play music in your Telegram Group's Voice Chatπ

My commands - /play, /stop, /skip, /pause, /resume, which work in grp

Thanks for using .

Regrards [RAJPUTBOT](https://t.me/SARCASTICLUCKY)

π Use these buttons below to know more. π""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CREATOR π ", url="https://t.me/SarcasticLucky"
                    )
                ],
                [
                  
                    InlineKeyboardButton(
                        "π£ Channel π£", url="https://t.me/LuckyWritings"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β Close β", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**RAJPUTBOT:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΆ Search πΆ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "β Close β", callback_data="close"
                    )
                ]
            ]
        )
    )
