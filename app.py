from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

DB_URL = 'postgresql://postgres:password@127.0.0.1:5432/databasename'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some_secret_key'

db = SQLAlchemy(app)

from tasksModel import TaskModel

@app.before_first_request
def create_tables():
    db.create_all()

# home route
@app.route('/', methods=['POST','GET'])
def home():
    # fetch all tasks
    tasks = TaskModel.fetch_records()

    # fetching form input data
    try:
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            createdDate = request.form['createdDate']
            startDate = request.form['createdDate']
            endDate = request.form['endDate']
            status = request.form['status']

            task = TaskModel(title=title,description=description,createdDate=createdDate,startDate=startDate,endDate=endDate,
                             status=status)
            task.create_task()
            print('success')
            return redirect(url_for('home'))
    except Exception as e:
        print(e)
    return render_template('index.html',tasks=tasks)

# edit a task
@app.route('/task/update/<int:id>', methods=['POST'])
def update(id):
    try:
        newTitle = request.form['newTitle']
        newDescription = request.form['newDescription']
        newCreatedDate = request.form['newCreatedDate']
        newStartDate = request.form['newStartDate']
        newEndDate = request.form['newEndDate']
        newStatus = request.form['newStatus']
        update = TaskModel.update_by_id(id=id,newTitle=newTitle,newDescription=newDescription,newCreatedDate=newCreatedDate,
                                        newStartDate=newStartDate,newEndDate=newEndDate,newStatus=newStatus)
        if update:
            print('record successfully updated')
            return redirect(url_for('home'))
        else:
            print('update unsuccessfull')
            return redirect(url_for('home'))
    except Exception as e:
        print(e)

# delete a task
@app.route('/task/del/<int:id>', methods=['POST'])
def delete(id):
    deleted = TaskModel.delete_by_id(id=id)
    if deleted:
        print('successfully deleted')
        return redirect(url_for('home'))
    else:
        print('record not found')
        return redirect(url_for('home'))



if __name__ == 'main':
    app.run(debug=True)