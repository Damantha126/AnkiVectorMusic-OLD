from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello š there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\nš“ Do you want me to play music in your Telegram groups'voice chats? Please click the \'š User Manual š\' button below to know how you can use me.\n\nš“ The Assistant must be in your group to play music in the voice chat of your group.\n\nš“ More info & commands mentioned in the [User Manual](https://telegra.ph/Anki-Vector-Music-05-07)\n\nA project by @Damantha_Jasinghe\n Join Our Group @SLTBrecLand""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "š User Manual š", url="https://telegra.ph/Anki-Vector-Music-05-07")
                  ],[
                    InlineKeyboardButton(
                        "šØāš» Updates šØāš»", url="https://t.me/ankivectorUpdates"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat šļø", url="https://t.me/AnkiSupport_Official"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**š“ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "šļø Support Group šļø", url="https://t.me/AnkiSupport_Official")
                ]
            ]
        )
   )
