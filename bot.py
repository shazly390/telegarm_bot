from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7365555261:AAHiMK_gZbL4eA4ZCgUbYbWr9kBUPHgr2NQ"
ADMIN_ID = 123456789  # ضع هنا ID المشرف

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("مرحبًا! أرسل مشكلتك وسيتواصل معك المشرف.")

async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    user = update.message.chat.username or update.message.chat.first_name
    message = f"🚀 مشكلة جديدة من {user}:\n{user_message}"
    
    # إرسال المشكلة للمشرف
    await context.bot.send_message(chat_id=ADMIN_ID, text=message)
    await update.message.reply_text("تم إرسال مشكلتك للمشرف.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
