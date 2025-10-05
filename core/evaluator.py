import re
from core.audio import speak, get_answer
from core.question_gen import generate_questions
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize AI model
chat_model = ChatOllama(model="llama3.2")

def evaluate_answer(question, answer):
    """Evaluate the user's answer and give score and feedback."""
    system_prompt = """
    You are an AI interviewer evaluator.
    Evaluate the candidate's answer strictly based on:
    - Score: 0-10
    - Feedback: strengths and weaknesses
    Format response exactly like:
    Score: X/10
    Feedback: <detailed feedback>
    """

    human_prompt = f"Question: {question}\nUser Answer: {answer}"

    response = chat_model.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ])
    return response.content

def parse_score(feedback):
    """Extract numerical score from AI feedback."""
    match = re.search(r"Score:\s*(\d+)/10", feedback)
    if match:
        return int(match.group(1))
    return 0

def run_interview(resume_text=None, questions=None):
    """Run the full interview process."""
    if questions is None and resume_text:
        questions = generate_questions(resume_text)

    report = []
    scores = []

    for q in questions:
        print(f"\nQuestion: {q}")
        speak(q)
        answer = get_answer()
        if not answer:
            print("No valid answer captured. Skipping evaluation.")
            continue

        print(f"Your Answer: {answer}")
        feedback = evaluate_answer(q, answer)
        print(f"Feedback: {feedback}")

        score = parse_score(feedback)
        scores.append(score)
        report.append((q, answer, feedback, score))

    # Summary
    print("\n=== Interview Summary ===")
    for i, (q, ans, fb, sc) in enumerate(report, start=1):
        print(f"\n--- Question {i} ---")
        print(f"Q: {q}")
        print(f"A: {ans if ans else '[No Answer Given]'}")
        print(f"Score: {sc}/10")
        print(f"Feedback:\n{fb}")
        print("-" * 40)

    if scores:
        avg_score = sum(scores) / len(scores)
        print(f"\n✅ Overall Score: {avg_score:.1f}/10")

        # AI verdict summary
        verdict_prompt = f"""
        Candidate answered {len(report)} questions with an average score of {avg_score:.1f}/10.
        Provide a short final interviewer-style feedback summary (strengths, weaknesses, recommendation).
        """
        verdict = chat_model.invoke([HumanMessage(content=verdict_prompt)])
        print("\n=== Final Verdict ===")
        print(verdict.content)
