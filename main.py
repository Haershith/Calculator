import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import *


load_dotenv()

Bot = Client(
    "Calculator Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)


START_TEXT = """𝙷𝚎𝚕𝚕𝚘 {},
I ᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴄᴀʟᴄᴜʟᴀᴛᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ. \
Sᴇɴᴅ ᴍᴇ /ᴄᴀʟᴄᴜʟᴀᴛᴇ ғᴏʀ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴏʀ sᴇɴᴅ ᴀs ᴛᴇxᴛ. \
Yᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴍᴇ ɪɴ ɪɴʟɪɴᴇ..

ᗰᗩᗪᗴ ᗷY @MutyalaHarshith"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('💞 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ✨', url='https://telegram.me/MutyalaHarshith')
        ]
    ]
)

CALCULATE_TEXT = "𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒅 𝒃𝒚 @MutyalaHarshith 𝑪𝒂𝒍𝒄𝒖𝒍𝒂𝒕𝒆 :  "

CALCULATE_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Dᴇʟᴇᴛᴇ", callback_data="DEL"),
            InlineKeyboardButton("𝔸ℂ", callback_data="AC"),
            InlineKeyboardButton("(", callback_data="("),
            InlineKeyboardButton(")", callback_data=")")
        ],
        [
            InlineKeyboardButton("𝟟", callback_data="7"),
            InlineKeyboardButton("𝟠", callback_data="8"),
            InlineKeyboardButton("𝟡", callback_data="9"),
            InlineKeyboardButton("÷", callback_data="/")
        ],
        [
            InlineKeyboardButton("𝟜", callback_data="4"),
            InlineKeyboardButton("𝟝", callback_data="5"),
            InlineKeyboardButton("𝟞", callback_data="6"),
            InlineKeyboardButton("×", callback_data="*")
        ],
        [
            InlineKeyboardButton("𝟙", callback_data="1"),
            InlineKeyboardButton("𝟚", callback_data="2"),
            InlineKeyboardButton("𝟛", callback_data="3"),
            InlineKeyboardButton("-", callback_data="-"),
        ],
        [
            InlineKeyboardButton(".", callback_data="."),
            InlineKeyboardButton("𝟘", callback_data="0"),
            InlineKeyboardButton("=", callback_data="="),
            InlineKeyboardButton("+", callback_data="+"),
        ]
    ]
)

ABOUT_TEXT = """
• **BoT Name** : `MH Calculator`
• **Develoveper** : [Mutyala Harshith](https://t.me/MutyalaHarshith)
• **Support** : [MHGcHaT](https://t.me/MHGcHaT)
• **GitHub** : [MutyalaHarshith](https://GitHub.com/MutyalaHarshith)
• **Source** : [Calculator](https://GitHub.com/MutyalaHarshith/Calculator)
• **Hosted** : [Heroku](https://heroku.com)
• **Language** : `Python`
"""

HELP_TEXT = """
Your Name {},

This Is Normal Telegram Calculator BoT

U Can Use this Bot for calculate By your question

It is Clarifying Your question 

U can also use direct text like

Eg : 23×2

Any Issues By ask in : [MHGcHaT](https://t.me/MHGcHaT)
"""


@Bot.on_message(filters.command(["start"]))
async def start(_, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/236794ce4bb2213eaae1e.jpg",
        caption=START_TEXT.format(message.from_user.mention),
        reply_markup=START_BUTTONS,
        quote=True
    )

@Bot.on_message(filters.command(["about"]))
async def start(_, message):
    await message.reply_text(
        text=ABOUT_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS,
        quote=True
    )

@Bot.on_message(filters.command(["help"]))
async def start(_, message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/edb5dcfef8a8203f11ce2.jpg",
        caption=HELP_TEXT.format(message.from_user.mention),
        reply_markup=START_BUTTONS,
        quote=True
    )

@Bot.on_message(filters.private & filters.command(["mh", "calculate", "harshith"]))
async def calculate(_, message):
    await message.reply_text(
        text=CALCULATE_TEXT,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )



@Bot.on_message(filters.private & filters.text)
async def evaluate(_, message):
    try:
        data = message.text.replace("×", "*").replace("÷", "/")
        result = str(eval(data))
    except:
        return
    await message.reply_text(
        text=result,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_callback_query()
async def cb_data(_, message):
        data = message.data
        try:
            message_text = message.message.text.split("\n")[0].strip().split("=")[0].strip()
            text = '' if CALCULATE_TEXT in message_text else message_text
            if data == "=":
                text = str(eval(text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await message.message.edit_text(
                text=f"{text}\n\n{CALCULATE_TEXT}",
                disable_web_page_preview=True,
                reply_markup=CALCULATE_BUTTONS
            )
        except Exception as error:
            print(error)


@Bot.on_inline_query()
async def inline(bot, update):
    if len(update.data) == 0:
        try:
            answers = [
                InlineQueryResultArticle(
                    title="Calculator",
                    description="New calculator",
                    input_message_content=InputTextMessageContent(
                        text=CALCULATE_TEXT,
                        disable_web_page_preview=True
                    ),
                    reply_markup=CALCULATE_BUTTONS
                )
            ]
        except Exception as error:
            print(error)
    else:
        try:
            data = update.query.replace("×", "*").replace("÷", "/")
            result = str(eval(text))
            answers = [
                InlineQueryResultArticle(
                    title="Answer",
                    description=f"Result: {result}",
                    input_message_content=InputTextMessageContent(
                        text=f"{data} = {result}",
                        disable_web_page_preview=True
                    )
                )
            ]
        except:
            pass
    await update.answer(answers)


Bot.run()
