from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace with your bot token
TOKEN = '7978135770:AAEggY8FsBpR7CQTkSQwu9Mm-IeN1m62VjY'
# Template links (hosted on Google Drive or Gumroad)
templates = {
    "IT Resume": "https://example.com/it-resume.docx", 
    "Marketing Resume": "https://example.com/marketing-resume.docx", 
    "Fresher Resume": "https://example.com/fresher-resume.docx" 
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(name, callback_data=name)] for name in templates]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose a resume template:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    template_name = query.data
    link = templates[template_name]
    await query.edit_message_text(text=f"🔗 Here's your {template_name}:\n{link}\n\nPay here: https://yourpaymentlink.com") 

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()