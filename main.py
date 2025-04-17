from flask import render_template, Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, BLOB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ihjournal.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Journal Table Configuration
class Journal(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    entry: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str]= mapped_column(String(800), nullable=False)
    tools: Mapped[str] = mapped_column(String(200), nullable=False)
    wquestions: Mapped[str] = mapped_column(BLOB, nullable=False)
    notes: Mapped[str] = mapped_column(BLOB)

    def __repr__(self):
        return '<Name %r>' % self.description

with app.app_context():
    db.create_all()








@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
