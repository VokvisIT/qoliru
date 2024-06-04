#@title Установка всего необходимого {display-mode:"form"}
import logging  # стандартная библиотека для логирования
from pyrogram import Client, filters  # pip install pyrogram
import pyrogram
from pyrogram.raw.types import MessageEntityTextUrl
from glob import glob
from dateutil.relativedelta import relativedelta  # pip install python-dateutil
import nest_asyncio
from pyrogram.types.messages_and_media.message import Message
from pyrogram.types.messages_and_media.message_reactions import MessageReactions
from  pyrogram.types import Reaction
import datetime
import os
import json
import asyncio
import csv
import pandas as pd
nest_asyncio.apply()

api_id = '22762367'
api_hash = '9af9f0416416e4b8d3cde1a358c4129f'


POSITIVE_EMOJIS = ['😃', '👍', '❤', '😁', '😊', '🌟', '🎉', '🥰', '😍', '🙌', '🤗', '👏', '🌞', '🌻', '💃', '🕺', '🔥', '✨',
                   '🎶', '💖', '💪', '😎', '🤩', '👌', '🥳', '😄', '👑', '🎈', '🌈', '🥇', '💯', '😻', '🙏', '💞', '🍾',
                   '👼', '💕', '🚀', '😇', '💎', '🌺', '💛', '💥', '🎵', '😋', '🍀', '🥂', '💝', '🌼', '🌸', '💘']

NEGATIVE_EMOJIS = ['😔', '👎', '💔', '😞', '😢', '😭', '😡', '😣', '😩', '😒', '🙁', '😠', '🤬', '🤯', '😓', '🤔', '😑',
                   '🤢', '👿', '👻', '💀', '🙅', '🚫', '😕', '😖', '😴', '🤦', '🙄', '😧', '😮', '😤', '🤕', '👺', '😾', '💩',
                   '👽', '🤡', '😰', '😵', '👿', '😳', '😨', '🤮', '😦', '👹']

async def get_channel_id(client, link):
    chat = await client.get_chat(link)
    channel_id = chat.id
    return str(channel_id)

async def clearify_text(msg: Message):
    text = msg.text
    text_splitted = text.split()
    text_listed = [word for word in text_splitted if word != ' ']
    return " ".join(text_listed)

async def count_positive_reactions(reactions: MessageReactions) -> int:
    count = 0
    for reaction in reactions.reactions:
        if reaction.emoji in POSITIVE_EMOJIS:
            count += reaction.count
    return count

async def count_negative_reactions(reactions: MessageReactions) -> int:
    count = 0
    for reaction in reactions.reactions:
        if reaction.emoji in NEGATIVE_EMOJIS:
            count += reaction.count
    return count

async def get_message_content(client, msg: Message, url, channel_name, chat):
    msg_url = url + '/' + str(msg.id)
    # msg_date = f"{msg.date.day}.{msg.date.month}.{msg.date.year}"
    msg_date = f"{msg.date.day}.{msg.date.month}.{msg.date.year}"
    day, month, year = msg_date.split(".")
    reordered_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    msg_date = datetime.datetime.strptime(reordered_date, "%Y-%m-%d").date()
    # msg_time = f"{msg.date.hour}:{msg.date.minute}"
    msg_time = f"{str(msg.date.hour).zfill(2)}:{str(msg.date.minute).zfill(2)}"
    msg_source = "Telegram"
    msg_reply_to_text = None
    msg_header = None
    msg_comments_count = None
    msg_rating = None
    msg_positive_reactions_count = None
    msg_negative_reactions_count = None
    msg_forwards = None
    msg_views = None
    msg_comments = None
    msg_comment_reactions = None
    msg_text_type = "Комментарий"
    msg_hashtags = None
    msg_tone = None
    msg_category = None

    if msg.text:
        text = await clearify_text(msg=msg)
        msg_text = text
    elif msg.caption:
        msg_text = msg.caption
    if msg.reply_to_message_id:
      msg_reply_to = await client.get_messages(chat_id=chat.id, message_ids=msg.reply_to_message_id)
      msg_reply_to_text = await clearify_text(msg_reply_to)
    if msg.reactions:
        msg_positive_reactions_count = await count_positive_reactions(msg.reactions)
        msg_negative_reactions_count = await count_negative_reactions(msg.reactions)
    if msg.views:
        msg_views = msg.views
        msg_text_type = "Пост"
    if msg.forwards:
        msg_forwards = msg.forwards
    if msg.reply_to_message:
        reply = msg.reply_to_message
        print(reply)
        if reply.text:
            reply_text = await clearify_text(msg=reply)
            msg_reply_text = reply_text

    message_data = [
        msg_url, msg_date, msg_time,
        msg_source, msg_header, msg_reply_to_text,
        msg_text, msg_comments_count,
        msg_rating, msg_positive_reactions_count,
        msg_negative_reactions_count,
        msg_forwards, msg_views, msg_comments,
        msg_comment_reactions, msg_text_type,
        msg_hashtags, msg_tone, msg_category
    ]
    return message_data

async def find_last_parsed_date(path):
    paths = glob(f"{path}/*/*meta.txt", recursive=True)
    oldest = datetime.datetime.strptime("1970-01-01 00:00:00+00:00", "%Y-%m-%d %H:%M:%S%z")
    temp = oldest
    for p in paths:
        with open(p, 'r') as file:
            date = datetime.datetime.strptime(file.readlines()[-1], "%Y-%m-%d %H:%M:%S%z")
            if date > oldest:
                oldest = date
    if temp == oldest:
        oldest = datetime.datetime.now() - relativedelta(months=3)
    return oldest

async def parse(client, url, limit):
    err = []
    channel_id = await get_channel_id(client, url)
    oldest = await find_last_parsed_date(channel_id)
    chat = await client.get_chat(url)
    # открываем csv файл для записи данных
    with open(f"{channel_id}.csv", "a", newline="", encoding="utf-8") as f:

        # создаем объект writer для записи данных в csv формате
        writer = csv.writer(f)

        # записываем заголовки столбцов
        writer.writerow(["URL", "Date", "Time",
                         "Source", "Header", "Reply to",
                         "Text", "Comments count", "Rating",
                         "Positive reactions count",
                         "Negative reactions count",
                         "Forwards", "Views",
                         "Comments", "Comment reactions",
                         "Text type", "Hashtags", "Tone",
                         "Category"])

        async for message in client.get_chat_history(chat.id, offset_id=0, limit=limit):
            message: Message
            try:
                # получаем данные по сообщению
                message_data = await get_message_content(client, message, url, channel_id, chat)

                # записываем данные в csv файл
                writer.writerow(message_data)

            except Exception as passing:
                err.append(passing)
                continue
    return err

#@title Парсер {display-mode:"form"}

async def main():
    logging.basicConfig(
        level=logging.INFO,
        filename='parser_log.log',
        filemode='w',
        format="%(asctime)s %(levelname)s %(message)s"
    )

    logging.info("script started")

    # url = input("Ссылка или @ канала: ")
    url = '@arkhangelsk001'  # @param {type:"string"}

    flag = False  # @param {type:"boolean"}

    limit = 1000  # @param {type:"integer"}

    logging.info(f"parsing channel {url}")

    async with Client("new", api_id, api_hash) as app:
        try:
            err = await parse(app, url, limit=limit)
            if err:
                logging.warning(str(err))
            else:
                logging.info("parsing done successfully")

        except Exception as ex:
            logging.critical(f"critical error {ex}")
            flag = False

    if flag:
        logging.info("script is done successfully")
    else:
        logging.warning("some errors occurred during script execution")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

