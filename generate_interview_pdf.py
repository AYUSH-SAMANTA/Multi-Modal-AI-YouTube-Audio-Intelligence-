from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

OUTPUT_PATH = "interview_questions_for_cv_project.pdf"

questions = [
    (
        "1. Can you walk me through this project?",
        "This project is a speech-to-text application built with FastAPI and Streamlit. The frontend allows a user to upload an audio file, and the backend processes it using OpenAI Whisper to generate a transcript. I built the full workflow from file upload to text output, which demonstrates both backend API design and frontend integration."
    ),
    (
        "2. Why did you choose FastAPI for the backend?",
        "I chose FastAPI because it is fast, lightweight, and easy to use with Python. It is ideal for handling file uploads, validation, and returning JSON responses. The API only needed to accept audio files, call the transcription model, and return the result, so FastAPI was a practical and efficient choice."
    ),
    (
        "3. Why did you use Streamlit for the frontend?",
        "Streamlit is perfect for rapid prototyping and internal tools. It allowed me to build a simple UI quickly without complex frontend setup. Since the goal was to demonstrate the transcription workflow clearly, Streamlit was an efficient and user-friendly option."
    ),
    (
        "4. What is the core workflow of the project?",
        "The user uploads an audio file through the Streamlit interface. The frontend sends that file to the FastAPI API. The backend saves it temporarily, uses Whisper for transcription, and sends the transcript back as JSON. The UI then displays the result to the user. This is a complete end-to-end AI application flow."
    ),
    (
        "5. What role does Whisper play in the project?",
        "Whisper is the core AI model used for speech recognition. It converts spoken audio into text, which is the main functionality of the project. It is useful here because it can handle common audio formats and reduces the need to build a transcription model from scratch."
    ),
    (
        "6. What technical challenge did you face and how did you resolve it?",
        "A major challenge was that Whisper depends on FFmpeg, and on Windows it failed with a missing-file error. I traced the issue to an environment dependency rather than a bug in the app logic. After installing FFmpeg and ensuring it was available on PATH, the transcription worked correctly. This taught me the importance of checking system dependencies in AI projects."
    ),
    (
        "7. How did you handle file uploads and processing?",
        "I used FastAPI's file upload support to receive the audio file. The file was saved to a temporary location, processed by the transcription model, and then removed after use. This ensures the system remains clean and avoids leaving temporary files behind."
    ),
    (
        "8. How would you improve this project in the future?",
        "I would add better validation, support for large files, progress indicators, multiple language options, and more robust deployment practices. I would also consider adding speaker detection, transcript storage, and a proper production-ready infrastructure with monitoring and logging."
    ),
    (
        "9. What are the limitations of the current project?",
        "It is a strong prototype, but it depends on local system setup such as FFmpeg and the Whisper model. It works best with short audio files and can be affected by background noise, accents, or poor audio quality. For production use, I would improve scalability, error handling, and reliability."
    ),
    (
        "10. Why is this project important for your profile?",
        "This project shows that I can connect AI, backend logic, and frontend design into a working product. It demonstrates practical Python development, working with external libraries, API design, and debugging real-world environment issues. That makes it a strong example of end-to-end software engineering."
    ),
    (
        "11. How would you deploy this project in a real environment?",
        "I would deploy the FastAPI backend in a cloud service or container environment, keep the Streamlit frontend separate, and use environment variables for configuration. I would also add logging, monitoring, and secure handling for uploaded files. This would make the app more production-ready and easier to scale."
    ),
    (
        "12. What is the biggest lesson you learned from this project?",
        "The biggest lesson was that building an AI application is not only about the model itself; it is also about integrating tools, handling dependencies, and making sure the system works end-to-end in a real environment. That requires debugging both code and infrastructure."
    ),
]

styles = getSampleStyleSheet()

heading_style = ParagraphStyle(
    "Heading1",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=18,
    leading=22,
    spaceAfter=14,
)

question_style = ParagraphStyle(
    "Question",
    parent=styles["BodyText"],
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=14,
    spaceAfter=6,
)

answer_style = ParagraphStyle(
    "Answer",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=10.5,
    leading=14,
    spaceAfter=12,
    firstLineIndent=0,
)

doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=letter,
    leftMargin=0.7 * inch,
    rightMargin=0.7 * inch,
    topMargin=0.7 * inch,
    bottomMargin=0.7 * inch,
)

story = []
story.append(Paragraph("Speech-to-Text Project: Interview Questions and Answers", heading_style))
story.append(Spacer(1, 0.2 * inch))

for question, answer in questions:
    story.append(Paragraph(question, question_style))
    story.append(Paragraph(answer, answer_style))
    story.append(Spacer(1, 0.1 * inch))

doc.build(story)
print(f"Generated PDF: {OUTPUT_PATH}")
