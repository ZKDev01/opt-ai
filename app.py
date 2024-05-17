import os
import textwrap 
import dotenv

import numpy as np
import pandas as pd

import google.generativeai as genai

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

dotenv.load_dotenv()
telegram_token = os.getenv("telegram_token") 
telegram_username = os.getenv("telegram_username")
geminiapi_key = os.getenv("geminiapi_key")

genai.configure(api_key=geminiapi_key)
model = genai.GenerativeModel('gemini-pro')
model_embedding = 'models/embedding-001'

original = os.getcwd() + "\\database\\doc"
dirs = os.listdir(original)

database = []
for dir in dirs:
  with open(original + '\\' + dir, encoding='utf-8') as file:
    result = file.read()
  database.append((dir, result))

def embed(title, text):
  return genai.embed_content(
    model=model_embedding,
    content=text,
    task_type="retrieval_document",
    title=title)["embedding"]

df = pd.DataFrame(database)
df.columns = ['Title', 'Text']
df['Embeddings'] = df.apply(lambda row: embed(row['Title'], row['Text']), axis=1)

df.to_json(os.getcwd() + "\\database\\database.json")
sdsd
def find_best_passage(query, dataframe):
  query_embedding = genai.embed_content(
    model=model_embedding,
    content=query,
    task_type="retrieval_query")
  dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding["embedding"])
  idx = np.argmax(dot_products)
  return dataframe.iloc[idx]['Text']

def make_prompt(query, relevant_passage: str):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = textwrap.dedent(
    """Eres un bot útil e informativo que responde preguntas utilizando texto del pasaje de referencia incluido a continuación \
    Asegúrate de responder incluyendo toda la información relevante. \
    Asegúrate de desglosar conceptos complicaados y mantener un tono amigable y conversacional \
    Si el pasaje no es relevante para la respuesta no respondas la pregunta \
    QUESTION: '{query}'
    PASSAGE: '{relevant_passage}'

    ANSWER:
    """).format(query=query, relevant_passage=escaped)

  return prompt

# commands
async def start(update: Update, context: ContextTypes):
  await update.message.reply_text("Hola, soy un bot. Está en fase de prueba")
async def help(update: Update, context: ContextTypes):
  await update.message.reply_text("Hola mucho gusto, en que puedo ayudarte?")

def handle_response(text: str, context: ContextTypes, update: Update):
  query = text.lower()
  passage = find_best_passage(query, df)
  
  prompt = make_prompt(query, passage)
  answer = model.generate_content(prompt)

  return answer.text

async def handle_message(update: Update, context: ContextTypes):
  message_type = update.message.chat.type 
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
  app = Application.builder().token(telegram_token).build() 

  app.add_handler(CommandHandler('start', start))
  app.add_handler(CommandHandler('help', help))

  app.add_handler(MessageHandler(filters.TEXT, handle_message))

  app.add_error_handler(error)
  app.run_polling(poll_interval=1, timeout=3)