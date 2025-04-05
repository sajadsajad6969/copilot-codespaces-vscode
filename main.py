from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("محصولات", callback_data='products')],
        [InlineKeyboardButton("پشتیبانی", callback_data='support')]
    ]
    update.message.reply_text('به فروشگاه من خوش آمدید!', reply_markup=InlineKeyboardMarkup(keyboard))

def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'products':
        query.message.reply_text('لیست محصولات: ...')
    elif query.data == 'support':
        query.message.reply_text('پشتیبانی: @SAJAD_HOMAEI')

updater = Updater("TOKEN", use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button_click))
updater.start_polling()
