from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("សូមស្វាគមន៍មកកាន់ ExpertOsintBot!")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is online!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))
app.run_polling()

from gtts import gTTS
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import os

async def tts_km(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("សូមបញ្ចូលអត្ថបទ។ ឧទាហរណ៍: /tts_km សួស្តី​ពិភពលោក")
        return
    tts = gTTS(text=text, lang='km')
    file_path = "tts_khmer.mp3"
    tts.save(file_path)
    await update.message.reply_voice(voice=open(file_path, 'rb'))
    os.remove(file_path)

app.add_handler(CommandHandler("tts_km", tts_km))


from telegram.ext import MessageHandler, filters

async def auto_tts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text:
        tts = gTTS(text=text, lang='km')
        file_path = "auto_tts.mp3"
        tts.save(file_path)
        await update.message.reply_voice(voice=open(file_path, 'rb'))
        os.remove(file_path)

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_tts))
