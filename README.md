# MockAI - Smart Interview Tool 🎙️

An AI-powered mock interview system that conducts technical interviews based on your resume, provides real-time voice interaction, and delivers detailed performance evaluations.

## 🌟 Features

- **Resume Analysis**: Automatically extracts and analyzes content from PDF resumes
- **Dynamic Question Generation**: Creates personalized interview questions based on your resume content
- **Voice Interaction**: Speaks questions aloud and captures your verbal responses
- **AI Evaluation**: Uses Ollama's Llama 3.2 model to evaluate answers with detailed feedback
- **Scoring System**: Provides numerical scores (0-10) for each answer
- **Comprehensive Reports**: Generates detailed interview summaries with overall performance metrics
- **Final Verdict**: AI-generated feedback on strengths, weaknesses, and hiring recommendations

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher (recommanded 3.10)
- [Ollama](https://ollama.ai/) installed with the `llama3.2` model
- Microphone for voice input
- Speakers/headphones for audio output

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hitesh0011/MockAI.git
   cd MockAI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and start Ollama with Llama 3.2**
   ```bash
   ollama pull llama3.2
   ollama serve
   ```

### Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Upload your resume**
   - When prompted, drag and drop your PDF resume file
   - The system will parse your resume and generate relevant questions

3. **Answer interview questions**
   - Listen to each question spoken by the AI
   - Provide your verbal answer (the system will capture your speech)
   - Receive immediate feedback and scoring

4. **Review your performance**
   - View detailed feedback for each question
   - Check your overall score and final verdict

## 📁 Project Structure

```
MockAI/
├── main.py                 # Entry point of the application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── core/
    ├── resume_parser.py   # Resume text extraction from PDFs
    ├── question_gen.py    # AI-based question generation
    ├── audio.py           # Text-to-speech and speech-to-text
    └── evaluator.py       # Answer evaluation and scoring
```

## 🛠️ Core Components

### Resume Parser
Extracts text content from PDF resumes using PyMuPDF for further processing.

### Question Generator
Leverages LangChain and Ollama to create contextually relevant interview questions based on resume content.

### Audio Handler
- **Text-to-Speech**: Uses `pyttsx3` to speak questions aloud
- **Speech-to-Text**: Uses `SpeechRecognition` to capture and transcribe verbal answers

### Evaluator
- Evaluates answers using AI with detailed feedback
- Scores answers on a 0-10 scale
- Generates comprehensive interview reports
- Provides final verdict with hiring recommendations

## 📊 Output Format

Each interview session provides:

1. **Per-Question Feedback**
   - Question asked
   - Your answer transcription
   - Numerical score (0-10)
   - Detailed feedback (strengths and areas for improvement)

2. **Overall Summary**
   - Average score across all questions
   - Final interviewer verdict
   - Recommendations for improvement

## 🔧 Technologies Used

- **AI/ML**: LangChain, Ollama (Llama 3.2)
- **PDF Processing**: PyMuPDF
- **Audio**: PyAudio, SpeechRecognition, pyttsx3
- **Core**: Python 3.x

## 📝 Example Workflow

```
1. Start the application: python main.py
2. Drag and drop your resume PDF
3. System generates 5-10 questions based on your resume
4. Listen to each question
5. Answer verbally
6. Receive immediate feedback and score
7. Review comprehensive interview report at the end
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Links

- **GitHub Repository**: [MockAI](https://github.com/hitesh0011/MockAI)
- **Ollama**: [https://ollama.ai/](https://ollama.ai/)

## 💡 Tips for Best Results

- Ensure your resume is in PDF format
- Speak clearly when answering questions
- Use a quiet environment for better speech recognition
- Review feedback carefully to improve your interview skills

## 🐛 Troubleshooting

**Issue**: Speech recognition not working
- **Solution**: Check microphone permissions and ensure PyAudio is properly installed

**Issue**: Ollama connection errors
- **Solution**: Ensure Ollama is running with `ollama serve` and the `llama3.2` model is installed

**Issue**: Resume parsing fails
- **Solution**: Ensure the resume is a valid PDF file and not password-protected

---

**Made with ❤️ for interview preparation**
