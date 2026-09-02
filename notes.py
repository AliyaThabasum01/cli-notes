import json

FILE = "notes.json"


def load_notes():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def add_note(text):
    notes = load_notes()
    notes.append(text)

    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)


def view_notes():
    return load_notes()
