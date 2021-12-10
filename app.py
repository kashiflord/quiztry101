from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/quiz'

db = SQLAlchemy(app)

class Contacts(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80),nullable=False)
    Email = db.Column(db.String(20),nullable=False)
    Phone_number = db.Column(db.String(12),nullable=False)
    Message = db.Column(db.String(120),nullable=False)
    



@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html') 

    
               

if __name__ == "__main__":
    app.run(debug=True)