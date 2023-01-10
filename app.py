from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #default True, to use less memory

db=SQLAlchemy(app)

class Todo(db.Model): #todo table's model
    task_id=db.Column(db.Integer, primary_key=True) #assigning unique value for each task
    name=db.Column(db.String(100)) #getting the task name allowed up to 100 chars
    
@app.route('/') # home page route
def home():
    todo_list=Todo.query.all()
    return render_template('index.html', todo_list=todo_list) #rendering html and passing the data in table to that html template

@app.route('/add', methods=['POST'])
def add():
    name=request.form.get("name")
    new_task=Todo(name=name) #creating new task, task id will be uniquely generated.
    db.session.add(new_task) #adding to database
    db.session.commit()
    return redirect(url_for("home")) #returning to the home page

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    x=Todo.query.get(todo_id)
    db.session.delete(x)
    db.session.commit()
    return redirect(url_for("home")) 


if __name__=='__main__':
    app.run()