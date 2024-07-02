from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    company = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        gender = request.form['gender']
        company = request.form['company']
        position = request.form['position']

        new_user = User(name=name, address=address, gender=gender, company=company, position=position)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_user.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.name = request.form['name']
        user.address = request.form['address']
        user.gender = request.form['gender']
        user.company = request.form['company']
        user.position = request.form['position']

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('update_user.html', user=user)

@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
