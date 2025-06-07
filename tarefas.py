from crewai import Task
from agentes import financas, coach, analista

tasks = [

    
    Task(description="Criar plano mensal para alcançar metas financeiras", 
         expected_output="Plano mensal criado com sucesso.",
         agent=financas,),
    
    Task(description="Gerar mensagem motivacional com base no progresso.",
        expected_output="Mensagem motivacional gerada com sucesso.",
        agent=coach),
    
    Task(description="Avaliar se a meta será atingida no prazo.",
          expected_output="Análise de progresso concluída.",
          agent=analista),
]
