import os 
import dotenv
import PIL.Image
import google.generativeai as genai

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

dotenv.load_dotenv()
telegram_token = os.getenv("telegram_token") 
telegram_username = os.getenv("telegram_username")
geminiapi_key = os.getenv("geminiapi_key")

genai.configure(api_key=geminiapi_key)
model = genai.GenerativeModel('gemini-pro')

# commands
async def start(update: Update, context: ContextTypes):
  await update.message.reply_text("Hola, soy un bot. Está en fase de prueba")
async def help(update: Update, context: ContextTypes):
  await update.message.reply_text("Hola mucho gusto, en que puedo ayudarte?")

# respuesta a los mensajes 
def handle_response(text: str, context: ContextTypes, update: Update):
  proccesed_text = text.lower()

  response = model.generate_content([proccesed_text])
  response.resolve()

  return response.text
  """
  if 'hola' in proccesed_text:
    return
  else:
    return 'No entender your language'
  """

async def handle_message(update: Update, context: ContextTypes):
  message_type = update.message.chat.type # private, group, subgroup, channel
  text = update.message.text

  if message_type == 'group':
    if text.startswith(telegram_username):
      new_text = text.replace(telegram_username, '')
      response = handle_response(new_text, context, update)
    else:
      return
  else:
    response = handle_response(text, context, update)

  await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes):
  print(context.error)
  await update.message.reply_text("Ha ocurrido un error")

if __name__ == '__main__':
  # creamos la app
  app = Application.builder().token(telegram_token).build() 

  # creamos commnads
  app.add_handler(CommandHandler('start', start))
  app.add_handler(CommandHandler('help', help))

  # creamos respuestas
  app.add_handler(MessageHandler(filters.TEXT, handle_message))

  # creamos errores
  app.add_error_handler(error)

  # iniciar bot
  app.run_polling(poll_interval=1, timeout=3)