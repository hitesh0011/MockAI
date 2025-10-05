from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize AI model
chat_model = ChatOllama(model="llama3.2")

def generate_questions(resume_text):
    """Generate AI questions based on resume."""
    system_prompt = """
    You are an interviewer AI. 
    Ask exactly 5 interview questions based on the candidate's resume. 
    Format:
    - Q1: Introduction
    - Q2-Q3: Projects
    - Q4-Q5: CS Core (OS/DBMS/CN) - entry-level
    Only return questions, one per line, numbered Q1-Q5.
    """

    human_prompt = f"Candidate resume:\n{resume_text}\nGenerate questions accordingly."

    response = chat_model.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ])

    return [q.strip() for q in response.content.split("\n") if q.strip()]

