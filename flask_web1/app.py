from flask import Flask, render_template, request,redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.update({'SECRET_KEY':'비밀'})
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app) #app에 SQLAlchemy 기능 추가한 객체, 플라스크와 SQLAlchemy 연계

app.debug = True

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     lang = db.Column(db.String(20),nullable=True)
#
#     def __repr__(self):
#         return '<User %r>' % self.username

class MyForm(FlaskForm):
    search = StringField('Search:', validators=[DataRequired()])


@app.route('/add')
def add():
    user = User()
    user.email = 'ckbaek1125@gmail.com'
    user.username = "chankoo"
    db.session.add(user)
    db.session.commit()
    return render_template('index.html')

@app.route('/insert')
def insert():
    ue = request.args.get('ue')
    uu = request.args.get('uu')
    lang = request.args.get('lang')

    user = User()
    user.email = ue
    user.username = uu
    user.lang = lang

    db.session.add(user)
    db.session.commit()
    return render_template('index.html')


@app.route('/')
def index():
    users = User.query.all()
    print(users)
    return render_template('index.html', users123 = users)

@app.route('/search', methods=['GET','POST'])
def search():
    search_term = request.form['search']

    if search_term=='문근영':
        return render_template('index.html')
    # return redirect('/search')
    return render_template('index.html')

    form = MyForm()
    if request.method == 'GET':
        if form.validate_on_submit():
            return render_template('search.html', form=form)
        return render_template('search.html', form=form)
    else:
        if form.validate_on_submit():
            return render_template('search.html', form=form)
        return render_template('search.html', form=form)

#
#
# @app.route('/search', methods=['GET','POST'])
# def search():
#     form = MyForm()
#     if request.method == 'GET':
#         if form.validate_on_submit():
#             return render_template('search.html', form=form)
#         return render_template('search.html', form=form)
#     else:
#         if form.validate_on_submit():
#             return render_template('search.html', form=form)
#         return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run()
