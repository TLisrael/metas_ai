from crewai import Crew
from agentes import financas, coach, analista
from tarefas import tasks

if __name__ == "__main__":
    crew = Crew(
        agents=[financas, coach, analista],
        tasks=tasks,
        verbose=True
    )
    
    print("Executando plano de metas com IA...\n")
    result = crew.kickoff()
    print("\n--- Resultado Final ---\n")
    print(result)
