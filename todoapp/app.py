from flask import Flask, render_template ,redirect, request,jsonify, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
  __tablename__ = 'todo'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)
  ddate = db.Column(db.String(), nullable=True)
  completed = db.Column(db.Boolean, nullable=True, default=False)
  list_id = db.Column(db.Integer, db.ForeignKey('todolist.id'),nullable=False)

  def __repr__(self):
      return f'<Todo ID: {self.id}, description: {self.description}>'

class TodoList(db.Model):
    __tablename__= "todolist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list',lazy=True)
    
    def __init__(self, name):
        self.name = name 


@app.route('/todos/create', methods=['POST'])
def create_todo():

    error = False
    body = {}
    try:
        description = request.get_json()['description']
        date = request.get_json()['ddate']
        list_id = request.get_json()['list_id']
        todo = Todo(description=description , ddate= date)
        active_list = TodoList.query.get(list_id)
        todo.list = active_list
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
    else:
        abort(500)

@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):    
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({ 'success': True })

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        print('completed', completed)
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))

@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html',
    lists=TodoList.query.all(),
    active_list=TodoList.query.get(list_id),
    todos=Todo.query.filter_by(list_id=list_id).order_by('id').all()
    )

@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))


if __name__ == '__main__':
  app.run(debug=True)