
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mbti.db'
db = SQLAlchemy(app)

# Create the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    mbti_type = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the Match model
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    compatibility = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Match {self.user_id} - {self.match_id}>'

# Create the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration/', methods=['POST'])
def registration():
    username = request.form['username']
    password = request.form['password']
    mbti_type = request.form['mbti_type']

    user = User(username=username, password=password, mbti_type=mbti_type)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/login/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return redirect(url_for('profile', username=username))
    else:
        return redirect(url_for('index'))

@app.route('/profile/<username>/')
def profile(username):
    user = User.query.filter_by(username=username).first()

    matches = Match.query.filter_by(user_id=user.id).order_by(Match.compatibility.desc()).all()

    return render_template('profile.html', user=user, matches=matches)

@app.route('/matches/<username>/')
def matches(username):
    user = User.query.filter_by(username=username).first()

    matches = Match.query.filter_by(user_id=user.id).order_by(Match.compatibility.desc()).all()

    return render_template('matches.html', user=user, matches=matches)

@app.route('/chat/<username>/<match_username>/')
def chat(username, match_username):
    user = User.query.filter_by(username=username).first()
    match = User.query.filter_by(username=match_username).first()

    return render_template('chat.html', user=user, match=match)

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
