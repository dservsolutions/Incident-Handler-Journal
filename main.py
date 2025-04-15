from flask import render_template, Flask, request, url_for
from flask_sqlalchemy import SQAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ihjournal.db"
db = SQAlchemy(model_class=Base)
db.init_app(app)

# Table Configuration

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
