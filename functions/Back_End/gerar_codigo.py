import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")


def gerar_codigo(prompt_base, entrada):
    prompt = f"""
    {prompt_base}
    #Entrada:
    {entrada}
    #Código: 
        - Analise se está sendo realizado tudo o que foi solicitado no item 1.
        - Retorne somente o conteúdo do documento!"""
        
    print(prompt)
    response = generate_chat_response(prompt)
    return response.choices[0].message.content.strip()

def generate_chat_response(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Você é um especialista em desenvolvimento C# com experiência em NHibernate, arquitetura em camadas e APIs REST."},
            {"role": "user", "content": prompt + "- Não inclua blocos de código com crases (```) no inicio e no fim. Retorne apenas o conteúdo puro."}
        ],
        temperature=0.3,
        max_tokens=4096
    )
    
    return response
