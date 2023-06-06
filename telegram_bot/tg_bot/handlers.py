from telegram.ext import CommandHandler, MessageHandler
from .views import shopping_list_bp
from telegram import Filters


def register_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add", add_item))
    dp.add_handler(CommandHandler("show", show_list))
    dp.add_handler(CommandHandler("clear", clear_list))
    dp.add_handler(MessageHandler(Filters.command, unknown_command))
    dp.add_handler(MessageHandler(Filters.text, echo))


shopping_list = []


# handler for the /start command
def start(bot, update):
    user = update.message.from_user
    bot.send_message(chat_id=update.message.chat_id,
                     text=f"Hi {user.first_name}! Welcome to the Shopping List Bot. Use /add to add items to your "
                          f"list.")


# handler for the /add command
def add_item(bot, update, args):
    item = ' '.join(args)
    if item:
        shopping_list.append(item)
        bot.send_message(chat_id=update.message.chat_id, text=f"Added {item} to the shopping list.")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Please provide an item to add to the shopping list.")


# handler for the /show command
def show_list(bot, update):
    if shopping_list:
        items = '\n'.join(shopping_list)
        bot.send_message(chat_id=update.message.chat_id, text=f"Your shopping list:\n{items}")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Your shopping list is empty.")


# handler for the /clear command
def clear_list(bot, update):
    shopping_list.clear()
    bot.send_message(chat_id=update.message.chat_id, text="Shopping list cleared.")


# handler for unknown commands
def unknown_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I don't understand command.")


# handler for text messages
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Sorry, I didn't understand that.")
