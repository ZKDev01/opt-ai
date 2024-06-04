"""
3. Mejorar la busqueda para que no solo recolepte un solo chunk, sino un valor k que se puede escoger
4. Mejorar los prompts a como dijo el profe
5. Mejorar el query
6. Lectura de CSV y mandar tabla a ia para que:
  1. Modelo de programacion no linea
  2. Solucion de un problema relacionado con la tabla en python
"""
import os

import load_env as lenv
import pandas as pd
import google.generativeai as genai

from pymongo import MongoClient
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from llm_method import make_prompt, find_best_passage
from utils_method import load_collection

genai.configure(api_key=lenv.geminiapi_key)
model = genai.GenerativeModel(lenv.model_llm)

df = load_collection()

# COMMANDS
async def start(update: Update, context: ContextTypes):
  await update.message.reply_text("Hola, soy un bot. Está en fase de prueba")
async def help(update: Update, context: ContextTypes):
  await update.message.reply_text("Hola mucho gusto, en que puedo ayudarte?")

def handle_response(text: str, context: ContextTypes, update: Update):
  query = text.lower()
  
  passage = find_best_passage(query, df)
  
  print("CODIGO EJECUTADO HASTA EL MOMENTO HASTA AQUI?")
  print(passage)

  prompt = make_prompt(query, passage)
  answer = model.generate_content(prompt)

  print("HERE!!!!!")

  return answer.text

async def handle_message(update: Update, context: ContextTypes):
  message_type = update.message.chat.type 
  text = update.message.text

  if message_type == 'group':
    if text.startswith(lenv.telegram_username):
      new_text = text.replace(lenv.telegram_username, '')
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
  app = Application.builder().token(lenv.telegram_token).build() 

  app.add_handler(CommandHandler('start', start))
  app.add_handler(CommandHandler('help', help))

  app.add_handler(MessageHandler(filters.TEXT, handle_message))

  app.add_error_handler(error)
  app.run_polling(poll_interval=1, timeout=3)
