from core.resume_parser import extract_resume_text
from core.evaluator import run_interview

if __name__ == "__main__":
    file_path = input("Drag & drop your resume PDF here: ").strip().strip('"')
    print("Resume Loaded successfully ")
    resume_text = extract_resume_text(file_path)
    run_interview(resume_text)
