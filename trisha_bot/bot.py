import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from config import TELEGRAM_BOT_TOKEN
from openai_api import generate_response
from memory import save_conversation, get_last_conversation

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: CallbackContext):
    """Start the bot with a flirty greeting."""
    user = update.effective_user
    await update.message.reply_text(f"Hey {user.first_name}, main Trisha hoon 😘 Chal baatein karein!")

async def chat(update: Update, context: CallbackContext):
    """Handle normal chat messages."""
    user_input = update.message.text
    user_id = update.message.chat_id

    # Recall past conversation for context
    last_response = get_last_conversation(user_id)
    context_prompt = f"Last chat: {last_response}\n" if last_response else ""

    # Generate Trisha's response
    trisha_reply = generate_response(user_id, context_prompt + user_input)

    # Save conversation to memory
    save_conversation(user_id, user_input, trisha_reply)

    await update.message.reply_text(trisha_reply)

async def reset_memory(update: Update, context: CallbackContext):
    """Clear user's chat memory."""
    user_id = update.message.chat_id
    collection.delete_many({"user_id": user_id})
    await update.message.reply_text("Maine hamari purani baatein bhool gayi! Ab sab naya rahega 💕")

def main():
    """Start the Telegram bot."""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset_memory))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Trisha is live!")
    app.run_polling()

if __name__ == "__main__":
    main()
