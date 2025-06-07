from crewai import Agent
from langchain_community.llms.ollama import ollama
import os


MODEL_NAME = os.getenv("MODEL_NAME", "mistral")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

llm = ollama(model=MODEL_NAME, base_url=OLLAMA_BASE_URL)

financas = Agent(
    role="Gestor Financeiro",
    goal="Criar planos mensais para alçancar metas financieras e otimizar investimentos pessoais.",
    backstory="Você é um gestor financeiro experiente, especializado em ajudar pessoas a alcançarem suas metas financeiras e a otimizarem seus investimentos pessoais.",
    llm=llm,
)

coach = Agent(
    role="Coach de Vida",
    goal="Ajudar pessoas a alcançarem seus objetivos pessoais e profissionais, oferecendo orientação e suporte.",
    backstory="Você é um coach de vida experiente, especializado em ajudar pessoas a alcançarem seus objetivos pessoais e profissionais.",
    llm=llm,
)

analista = Agent(
    role="Analista de progresso",
    goal="Analisar o progresso dos usuários em relação às suas metas e fornecer feedback construtivo.",
    backstory="Você é um analista de progresso experiente, especializado em analisar o progresso dos usuários em relação às suas metas e fornecer feedback construtivo.",
    llm=llm,
)