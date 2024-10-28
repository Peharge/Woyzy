from flask import Flask, render_template, request, jsonify
import ollama
import time
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
import json

app = Flask(__name__)

models = {
    "llama3": "llama3.1", #Hir muss Chat++ hinterlegt werden
}

conversation = []


def init_db_from_jsonfile(jsonfile_path):
    if os.path.exists("knowledge.db"):
        os.remove("knowledge.db")

    conn = sqlite3.connect("knowledge.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS woyzeck (id INTEGER PRIMARY KEY, scene TEXT, content TEXT)''')

    # Lese die JSON-Datei
    with open(jsonfile_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        scenes = data['scenes']

    for scene in scenes:
        c.execute("INSERT INTO woyzeck (scene, content) VALUES (?, ?)", (scene['scene'], scene['content']))
    conn.commit()
    conn.close()


def get_relevant_passages(query, top_n=3):
    conn = sqlite3.connect("knowledge.db")
    c = conn.cursor()
    c.execute("SELECT content FROM woyzeck")
    passages = [row[0] for row in c.fetchall()]
    conn.close()

    vectorizer = TfidfVectorizer().fit_transform(passages + [query])
    vectors = vectorizer.toarray()

    cosine_similarities = cosine_similarity([vectors[-1]], vectors[:-1])
    best_match_indices = np.argsort(cosine_similarities[0])[-top_n:]
    return [passages[i] for i in best_match_indices]


def generate_response(user_message):
    relevant_passages = get_relevant_passages(user_message)
    combined_passages = "\n\n".join(relevant_passages)

    if "zusammenfassen" in user_message.lower() or "interpretieren" in user_message.lower():
        summary = summarize_passage(combined_passages)
        interpretation = ask_model_for_interpretation(combined_passages)
        return f"Zusammenfassung: {summary}\nInterpretation: {interpretation}"
    elif "erklären" in user_message.lower():
        return f"Erklärung: {combined_passages}"
    else:
        return ask_model_for_interpretation(combined_passages)


def summarize_passage(passage):
    return passage[:200] + "..."


def ask_model_for_interpretation(passage):
    prompt = f"Bitte interpretiere den folgenden Text:\n\n{passage}"
    try:
        response_stream = ollama.chat(model=models['llama3'], messages=[{'role': 'user', 'content': prompt}],
                                      stream=False)
        return response_stream['message']['content']
    except Exception as e:
        return f"Fehler beim Abrufen der Interpretation: {str(e)}"


@app.route('/')
def index():
    return render_template('index2.html', models=models)


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    model_key = request.json.get('model')
    selected_model = models.get(model_key)
    conversation.append({'role': 'user', 'content': user_message})

    custom_response = generate_response(user_message)
    conversation.append({'role': 'assistant', 'content': custom_response})
    return jsonify({'response': custom_response})


if __name__ == "__main__":
    init_db_from_jsonfile("woyzeck.json")
    app.run(debug=True)
