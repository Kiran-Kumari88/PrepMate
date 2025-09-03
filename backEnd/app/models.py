from datetime import datetime
from . import db

# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # store hashed passwords
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}>"


# Subject table
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Subject {self.name}>"


# Question table
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option1 = db.Column(db.String(200))
    option2 = db.Column(db.String(200))
    option3 = db.Column(db.String(200))
    option4 = db.Column(db.String(200))
    answer = db.Column(db.String(200), nullable=False)
    question_type = db.Column(db.String(20), nullable=False)  # "MCQ" or "short"

    subject = db.relationship('Subject', backref=db.backref('questions', lazy=True))

    def __repr__(self):
        return f"<Question {self.id}>"


# UserProgress table
class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    status = db.Column(db.String(20))  # "attempted", "bookmarked", "completed"
    is_correct = db.Column(db.Boolean)

    user = db.relationship('User', backref=db.backref('progress', lazy=True))
    question = db.relationship('Question', backref=db.backref('progress', lazy=True))

    def __repr__(self):
        return f"<UserProgress user:{self.user_id} question:{self.question_id}>"
