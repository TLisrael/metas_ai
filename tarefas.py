from crewai import Task
from agentes import financas, coach, analista

tasks = [
    Task(description="Criar plano mensal para alcançar metas financeiras", agent=financas),
    Task(description="Gerar mensagem motivacional com base no progresso.", agent=coach),
    Task(description="Avaliar se a meta será atingida no prazo.", agent=analista),
]
