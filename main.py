from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import openai
import os

TELEGRAM_TOKEN = os.getenv("7843690543:AAEGQpWGvQE5Cw4_0_7y116Fd0K94Pp_sfM")
OPENAI_API_KEY = os.getenv("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")

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات هوش مصنوعی‌ام. هر چی خواستی بپرس.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"خطا در دریافت پاسخ از GPT: {e}"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("ربات روشنه...")
app.run_polling()
