# from testing_code.llm import LLM_main

# TODO: pendiente conectar todas las cosas 

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

class DEPLOY_BOT():
  def __init__(self) -> None:
    # assistant = LLM_main(k=3)
    pass

  async def start(update: Update, context: ContextTypes):
    await update.message.reply_text("Hola, soy un asistente personal")
  async def help(update: Update, context: ContextTypes):
    await update.message.reply_text("Soy capaz de ayudarte a contestar preguntas utilizando mi base de datos predeterminada")

  def handle_response(query: str, context: ContextTypes):
    pass

def main():
  bot = DEPLOY_BOT()

if __name__ == '__main__':
  main()