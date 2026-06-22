from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_interview_questions(subject):

    questions = []               # Store all unique interview questions

    while len(questions) < 50:              # keep genrating question until 50 questions 

        remaining = 50 - len(questions)     # Calculate how many questions are still needed

        prompt = f"""
Generate {remaining} UNIQUE interview questions for {subject}.

Rules:
1. Questions must be interview questions only.
2. Do NOT repeat any question.
3. Return ONLY valid JSON.
4. Return a JSON array of strings.

Example:
[
    "What is Python?",
    "What is a list in Python?"
]
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",                  # Send prompt as a user message
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content.strip()         # Extract response text

        # Remove markdown if present
        result = result.replace("```json", "")          
        result = result.replace("```", "").strip()

        try:
            new_questions = json.loads(result)      # Convert JSON string to Python list

            # Add only new questions
            for q in new_questions:
                q = q.strip()                       # Remove extra spaces from question

                if q and q not in questions:        # Check for empty and duplicate questions
                    questions.append(q)             # Add only unique questions

                if len(questions) == 50:            # Stop if 50 questions are collected
                    break

        except json.JSONDecodeError:
            print("Invalid JSON received. Retrying...")     # Retry if JSON is invalid

    return {
        "subject": subject,                     # Return subject name
        "questions": questions                  # Return list of 50 interview questions
    }