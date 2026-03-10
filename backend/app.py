from flask import Flask, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)

CORS(app)

DATEI_NAME = "notes.json"

def load_notes():
    if os.path.exists(DATEI_NAME):
        with open(DATEI_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_notes():
    with open(DATEI_NAME, "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)

notes = load_notes()

@app.route("/")
def start():
    return "Notizen Backend läuft"

@app.route("/notes", methods=["GET"])
def get_notes():
    return {"notes": notes}

@app.route("/add", methods=["POST"])
def add_note():
    data = request.json

    if not data:
        return {"msg": "keine daten"}

    note = data["note"]
    notes.append(note)
    save_notes()
    return {"msg": "Notiz gespeichert"}

@app.route("/delete/<id>", methods=["DELETE"])
def delete_note(id):
    notes.pop(int(id))
    save_notes()
    return {"msg": "Notiz gelöscht"}

@app.route("/test")
def test():
    return "API funktioniert"

app.run(host="0.0.0.0", port=3000)