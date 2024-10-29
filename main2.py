from flask import Flask, render_template, request, jsonify
import ollama
import time
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

models = {
    "llama3": "llama3.1",
}

conversation = []


# Funktion zum Initialisieren der Datenbank und Laden der Textdatei
def init_db_from_textfile(textfile_path):
    conn = sqlite3.connect("knowledge.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS woyzeck (id INTEGER PRIMARY KEY, content TEXT)''')

    # Datei öffnen und in Abschnitte aufteilen
    with open(textfile_path, 'r', encoding='utf-8') as f:
        text = f.read()
        # Aufteilen nach Absätzen oder anderen Kriterien (z.B. nach Doppeln Zeilenumbrüchen)
        passages = text.split('\n\n')  # Teilt bei doppelten Zeilenumbrüchen auf

    # Speichern der Abschnitte in der Datenbank
    for passage in passages:
        if passage.strip():  # Nur nicht-leere Abschnitte speichern
            c.execute("INSERT INTO woyzeck (content) VALUES (?)", (passage.strip(),))
    conn.commit()
    conn.close()


def get_relevant_passage(query):
    conn = sqlite3.connect("knowledge.db")
    c = conn.cursor()
    c.execute("SELECT content FROM woyzeck")
    passages = [row[0] for row in c.fetchall()]
    conn.close()

    # Vektorisiere die Inhalte und die Anfrage
    vectorizer = TfidfVectorizer().fit_transform(passages + [query])
    vectors = vectorizer.toarray()

    # Berechne Ähnlichkeit und finde das relevanteste Ergebnis
    cosine_similarities = cosine_similarity([vectors[-1]], vectors[:-1])
    best_match_idx = np.argmax(cosine_similarities)
    return passages[best_match_idx]


@app.route('/')
def index():
    return render_template('index2.html', models=models)


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    model_key = request.json.get('model')
    selected_model = models.get(model_key)
    conversation.append({'role': 'user', 'content': user_message})

    # Suche nach relevantem Inhalt aus der Datenbank
    relevant_passage = get_relevant_passage(user_message)
    conversation.append({'role': 'assistant', 'content': relevant_passage})  # Füge das Ergebnis der Konversation hinzu

    try:
        response_stream = ollama.chat(model=selected_model, messages=conversation, stream=True)
        response_content = ""
        for chunk in response_stream:
            content = chunk['message']['content']
            response_content += content
            time.sleep(0.05)
        conversation.append({'role': 'assistant', 'content': response_content})
        return jsonify({'response': response_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    init_db_from_textfile("woyzeck.txt")  # Initialisiert die Datenbank aus der Textdatei
    app.run(debug=True)