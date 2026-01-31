from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

async def start(update: Update, context):
    await update.message.reply_text("أهلاً 👋 البوت شغال")

async def reply(update: Update, context):
    await update.message.reply_text("وصلت رسالتك ✅")

def main():
    import os
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, reply))
    app.run_polling()

if __name__ == "__main__":
    main()
