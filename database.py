# Import SQLite library to work with a local database
import sqlite3

# Define the database file
DATABASE_NAME = "ai_assistant.db"

# Show the absolute path of the database file
import os

print("Database location:", os.path.abspath(DATABASE_NAME))

# Create the database and the conversations table
def create_database(db_path=DATABASE_NAME):

    # Connect to the database (create the file if it does not exist)
    connection = sqlite3.connect(db_path)

    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # Create a table to store questions and answers
    # IF NOT EXISTS prevents creating the table again if it already exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    # Save the database changes
    connection.commit()

    # Close the database connection
    connection.close()


# Save one conversation (question and answer) into the database
def save_conversation(question, answer, db_path=DATABASE_NAME):

    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()

    # Insert a new conversation into the conversations table
    # The question and answer values are passed safely using placeholders (?)
    cursor.execute(
        "INSERT INTO conversations (question, answer) VALUES (?, ?)",
        (question, answer)
    )

    connection.commit()

    connection.close()


def get_conversations(db_path=DATABASE_NAME):

    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()

    # Retrieve all conversations from the database
    # Sort them by ID in descending order (newest first)
    cursor.execute("""
        SELECT id, question, answer
        FROM conversations
        ORDER BY id DESC
    """)

    # Fetch all rows returned by the SQL query
    conversations = cursor.fetchall()

    connection.close()

    # Return all retrieved conversations
    return conversations