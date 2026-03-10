from flask import Flask, request

app = Flask(__name__)

notes = []

@app.route("/")
def start():
    return "Notizen Backend läuft"

@app.route("/notes", methods=["GET"])
def get_notes():
    return {"notes": notes}

@app.route("/add", methods=["POST"])
def add_note():
    data = request.json
    note = data["note"]
    notes.append(note)
    return {"msg": "Notiz gespeichert"}

@app.route("/delete/<id>", methods=["DELETE"])
def delete_note(id):
    notes.pop(int(id))
    return {"msg": "Notiz gelöscht"}

@app.route("/test")
def test():
    return "API funktioniert"

app.run(host="0.0.0.0", port=3000)