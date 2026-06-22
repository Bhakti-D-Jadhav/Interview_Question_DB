import sqlite3          # libray to work on database
import os               # used to do folder and file operations

os.makedirs("database", exist_ok=True)   #creates new folder named database if it is not exist

conn = sqlite3.connect("database/interview_questions.db")  # connect database with file
cursor = conn.cursor()          #creates cursor object to execute SQL quesries

# Creates table named questions
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    question TEXT UNIQUE,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()       # saves created table on databse

# function to insert new question in database
def insert_question(subject, question, source="LLM"):
    try:
        cursor.execute(                 # Try to insert question in database
            """
            INSERT INTO questions
            (subject, question, source)
            VALUES (?, ?, ?)
            """,
            (subject, question, source)
        )
        conn.commit()           # saves changes permanantly
        return True             # inserts question successfully

    except sqlite3.IntegrityError:          # this will execute if duplication que arive
        return False

# generate question on given topic
def get_questions(subject):

     #select question of specific subject
    cursor.execute(
        """
        SELECT question
        FROM questions
        WHERE subject = ?
        """,
        (subject,)
    )

    # uses list comprehension to return question string
    return [row[0] for row in cursor.fetchall()]