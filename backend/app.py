import os
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base, Note
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "notesdb")
DB_USER = os.getenv("DB_USER", "notesuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "super-secret")

@app.teardown_appcontext
def remove_session(exception=None):
    SessionLocal.remove()

@app.route("/", methods=["GET", "POST"])
def index():
    session = SessionLocal()
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if title and content:
            note = Note(title=title, content=content)
            session.add(note)
            session.commit()
            flash("Note added!", "success")
        else:
            flash("Both title and content required.", "error")
        return redirect(url_for("index"))

    notes = session.query(Note).order_by(Note.id.desc()).all()
    return render_template("index.html", notes=notes)

@app.route("/delete/<int:note_id>", methods=["POST"])
def delete(note_id):
    session = SessionLocal()
    note = session.get(Note, note_id)
    if note:
        session.delete(note)
        session.commit()
        flash("Note deleted!", "success")
    else:
        flash("Note not found.", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
