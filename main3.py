from flask import Flask, render_template, request, jsonify
import ollama
import sqlite3
import os
import json

app = Flask(__name__)

models = {
    "llama3.1": "llama3.1",
    "Chat++3": "chat++3",
    "Chat++4": "chat++4",
    "Chat++5": "chat++5",
    "Woyzy": "woyzy"
}

conversation = []

# Funktion zum Initialisieren der Datenbank aus der JSON-Datei
def init_db_from_jsonfile(jsonfile_path):
    if os.path.exists("knowledge.db"):
        os.remove("knowledge.db")

    conn = sqlite3.connect("knowledge.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS woyzeck (id INTEGER PRIMARY KEY, scene TEXT, content TEXT)''')

    with open(jsonfile_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        scenes = data['scenes']

    for scene in scenes:
        c.execute("INSERT INTO woyzeck (scene, content) VALUES (?, ?)", (scene['scene'], scene['content']))
    conn.commit()
    conn.close()

# Funktion zum Abrufen des Texts der spezifischen Szene
def get_scene_content(scene_number):
    conn = sqlite3.connect("knowledge.db")
    c = conn.cursor()
    c.execute("SELECT content FROM woyzeck WHERE scene = ?", (f"Szene {scene_number}",))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

# Hauptfunktion zur Generierung der Antwort
def generate_response(user_message):
    scene_number = extract_scene_number(user_message)

    if scene_number:
        scene_content = get_scene_content(scene_number)
        if not scene_content:
            return "Diese Szene existiert nicht oder ist leer."
    else:
        return "Bitte geben Sie eine gültige Szenennummer an, z.B. 'Szene 5'."

    # Antwort basierend auf der Anfrage des Nutzers
    if "zusammenfassen" in user_message.lower():
        summary = summarize_passage(scene_content)
        return f"Zusammenfassung der Szene {scene_number}: {summary}"
    elif "interpretieren" in user_message.lower():
        interpretation = ask_model_for_interpretation(scene_content)
        return f"Interpretation der Szene {scene_number}: {interpretation}"
    elif "erklären" in user_message.lower():
        return f"Erklärung zur Szene {scene_number}: {scene_content}"
    else:
        return ask_model_for_interpretation(scene_content)

# Funktion zur Extraktion der Szenennummer
def extract_scene_number(user_message):
    try:
        scene_number = int(user_message.lower().split("szene")[1].strip().split()[0])
        return scene_number
    except (IndexError, ValueError):
        return None

# Funktion zur Basis-Zusammenfassung der Szene
def summarize_passage(passage):
    return passage[:200] + "..." if passage else "Kein Inhalt verfügbar."

# Funktion zur Interpretation der Szene mithilfe des Modells
def ask_model_for_interpretation(passage):
    prompt = f"Bitte interpretiere den folgenden Text:\n\n{passage}"
    try:
        response_stream = ollama.chat(model=models['llama3'], messages=[{'role': 'user', 'content': prompt}], stream=False) # Hier muss das Modell 'Woyzy' eingetragen werden. Dadurch entfällt die Auswahl zwischen verschiedenen Modellen.
        return response_stream.get('message', {}).get('content', 'Keine Antwort erhalten.')
    except Exception as e:
        return f"Fehler beim Abrufen der Interpretation: {str(e)}"

# Flask-Routen
@app.route('/')
def index():
    return render_template('index5.html', models=models)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    model_key = request.json.get('model')
    selected_model = models.get(model_key)
    conversation.append({'role': 'user', 'content': user_message})

    custom_response = generate_response(user_message)
    conversation.append({'role': 'assistant', 'content': custom_response})
    return jsonify({'response': custom_response})

# Initialisierung der Datenbank
if __name__ == "__main__":
    init_db_from_jsonfile("C:/Users/julia/PycharmProjects/Woyzy/woyzeck.json") #Muss angepasst werden
    app.run(debug=True)
