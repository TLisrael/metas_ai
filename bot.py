import os 
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from crewai import Agent, Crew
from agentes import financas, coach, analista
from tarefas import tasks

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT")

crew = Crew(agents=[financas, coach, analista], tasks=tasks, verbose=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Olá! Sou uma IA que pode te ajudar a alcançar suas metas financeiras e pessoais."
    )

async def meta(update:Update, context:ContextTypes.DEFAULT_TYPE):
    result = crew.kickoff()
    await update.message.reply_text("Resultado: \n{result}".format(result=result))


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("meta", meta))

    print("Bot is running...")
    application.run_polling()