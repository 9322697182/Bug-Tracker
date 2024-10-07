from flask import Flask, render_template, request, redirect, url_for
from models import Bug, db_init, db_session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.db'
db_init(app)

@app.route('/')
def index():
    bugs = Bug.query.all()
    return render_template('index.html', bugs=bugs)

@app.route('/bug/new', methods=['GET', 'POST'])
def new_bug():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        new_bug = Bug(title=title, description=description, status=status)
        db_session.add(new_bug)
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('new_bug.html')

@app.route('/bug/edit/<int:id>', methods=['GET', 'POST'])
def edit_bug(id):
    bug = Bug.query.get(id)
    if request.method == 'POST':
        bug.title = request.form['title']
        bug.description = request.form['description']
        bug.status = request.form['status']
        db_session.commit()
        return redirect(url_for('index'))
    return render_template('edit_bug.html', bug=bug)

@app.route('/bug/delete/<int:id>')
def delete_bug(id):
    bug = Bug.query.get(id)
    db_session.delete(bug)
    db_session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
