from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False)

def db_init(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# A helper function for session handling
def db_session():
    return db.session
